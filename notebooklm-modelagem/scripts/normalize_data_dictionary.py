#!/usr/bin/env python3
"""Normaliza a proposta do dicionário sem alterar a estrutura lógica promovida."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
from typing import Any

import yaml

from assemble_data_dictionary import load_report, validate_dictionary
from build_source_manifest import QuotedDumper, quote_values


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def label_for(value: Any) -> str:
    return str(value).replace("_", " ").strip().title()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", type=Path, required=True)
    parser.add_argument("--logical", type=Path, required=True)
    parser.add_argument("--semantic", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    state = yaml.safe_load(args.state.read_text(encoding="utf-8"))
    logical = yaml.safe_load(args.logical.read_text(encoding="utf-8"))
    semantic = yaml.safe_load(args.semantic.read_text(encoding="utf-8"))
    manifest = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))
    proposed = load_report(args.report)
    proposed_tables = {item["relation_id"]: item for item in proposed["tables"]}
    logical_relation_ids = {item["id"] for item in logical["relations"]}
    if set(proposed_tables) != logical_relation_ids or len(proposed_tables) != len(logical_relation_ids):
        raise ValueError("relatório não cobre exatamente as relações lógicas")

    foreign_keys_by_relation: dict[str, list[dict[str, Any]]] = {item: [] for item in logical_relation_ids}
    for foreign_key in logical["foreign_keys"]:
        foreign_keys_by_relation[foreign_key["from_relation_id"]].append(foreign_key)

    tables: list[dict[str, Any]] = []
    changed_descriptions: list[str] = []
    for relation in logical["relations"]:
        relation_id = relation["id"]
        proposed_table = proposed_tables[relation_id]
        proposed_columns = {item["attribute_id"]: item for item in proposed_table["columns"]}
        logical_attribute_ids = {item["id"] for item in relation["attributes"]}
        if set(proposed_columns) != logical_attribute_ids or len(proposed_columns) != len(logical_attribute_ids):
            raise ValueError(f"relatório não cobre exatamente os atributos de {relation_id}")

        columns = []
        for attribute in relation["attributes"]:
            proposed_column = proposed_columns[attribute["id"]]
            description = proposed_column["description"]
            if "gen_random_uuid" in description:
                description = (
                    f"Identificador de {attribute['logical_name'].lower()} no grão da relação "
                    f"{relation['logical_name']}."
                )
                changed_descriptions.append(f"{relation_id}.{attribute['id']}")
            columns.append(
                {
                    "attribute_id": attribute["id"],
                    "column_candidate": attribute["physical_name_candidate"],
                    "description": description,
                    "postgresql_type_candidate": proposed_column["postgresql_type_candidate"],
                    "nullable": attribute["nullable"],
                    "null_meaning": attribute["null_meaning"],
                    "default_candidate": attribute["default_semantics"],
                    "unit": proposed_column["unit"],
                    "format": proposed_column["format"],
                    "allowed_values": attribute["domain_values"],
                    "min_value": proposed_column["min_value"],
                    "max_value": proposed_column["max_value"],
                    "pii": proposed_column["pii"],
                    "sensitive": proposed_column["sensitive"],
                    "generated": attribute["derived"],
                    "derivation_rule_id": attribute["derivation_rule_id"],
                    "rule_ids": attribute["rule_ids"],
                    "evidence_ref_ids": attribute["evidence_ref_ids"],
                }
            )

        indexes = []
        for foreign_key in foreign_keys_by_relation[relation_id]:
            if not foreign_key["supporting_index_required"]:
                continue
            indexes.append(
                {
                    "id": f"IDX_{foreign_key['id'][3:]}",
                    "attribute_ids": foreign_key["from_attribute_ids"],
                    "purpose": "FK",
                    "rationale": (
                        f"Suporta a FK {foreign_key['id']} e as operações de junção e manutenção referencial associadas."
                    ),
                }
            )

        tables.append(
            {
                "relation_id": relation_id,
                "schema_candidate": "public",
                "table_candidate": relation["physical_name_candidate"],
                "description": proposed_table["description"],
                "grain": relation["grain"],
                "ownership_domain": state["run"]["domain_id"],
                "access_classification": proposed_table["access_classification"],
                "columns": columns,
                "primary_key_attribute_ids": relation["identity"]["attribute_ids"],
                "foreign_key_ids": [item["id"] for item in foreign_keys_by_relation[relation_id]],
                "unique_constraint_ids": [item["id"] for item in relation["unique_constraints"]],
                "check_constraint_ids": [item["id"] for item in relation["checks"]],
                "index_candidates": indexes,
                "retention_rule_ids": relation["retention_rule_ids"],
            }
        )

    catalogs = []
    for relation in logical["relations"]:
        for attribute in relation["attributes"]:
            if not attribute["domain_values"]:
                continue
            catalogs.append(
                {
                    "id": f"CAT_{relation['id']}_{attribute['id']}",
                    "name": f"Domínio de {attribute['logical_name']}",
                    "versioned": True,
                    "values": [
                        {
                            "code": value,
                            "label": label_for(value),
                            "valid_from": None,
                            "valid_to": None,
                            "evidence_ref_ids": attribute["evidence_ref_ids"],
                        }
                        for value in attribute["domain_values"]
                    ],
                }
            )

    body = {"tables": tables, "catalogs": catalogs, "open_issues": logical["open_issues"]}
    counts = validate_dictionary(
        body,
        logical,
        {item["id"] for item in semantic["rules"]},
        {item["id"] for item in manifest["evidence_refs"]},
        state["run"]["domain_id"],
    )
    stage = next(item for item in state["stages"] if item["id"] == "STAGE_04")
    artifact = {
        "schema_version": "1.1",
        "document": {
            "id": "DATA_DICTIONARY",
            "artifact_kind": "DATA_DICTIONARY",
            "title": "Dicionário de dados",
            "version": "0.1.0",
            "status": "PROPOSTO",
            "run_id": state["run"]["id"],
            "domain_id": state["run"]["domain_id"],
            "notebook_id": state["run"]["notebook_id"],
            "generated_at": None,
            "supersedes": None,
            "input_artifacts": stage["input_artifacts"],
        },
        **body,
    }
    audit = {
        "status": "PASS",
        "inputs": {
            "logical_model": {"path": str(args.logical), "sha256": sha256(args.logical)},
            "semantic_registry": {"path": str(args.semantic), "sha256": sha256(args.semantic)},
            "source_manifest": {"path": str(args.manifest), "sha256": sha256(args.manifest)},
            "notebook_correction": {"path": str(args.report), "sha256": sha256(args.report)},
        },
        "normalization": {
            "notebook_envelope_ignored": True,
            "structural_authority": "LOGICAL_MODEL_PROMOTED",
            "reused_from_notebook": [
                "TABLE_DESCRIPTION", "ACCESS_CLASSIFICATION", "COLUMN_DESCRIPTION", "POSTGRESQL_TYPE_CANDIDATE",
                "UNIT", "FORMAT", "MIN_VALUE", "MAX_VALUE", "PII", "SENSITIVE",
            ],
            "restored_from_logical_model": [
                "RELATION_AND_ATTRIBUTE_IDS", "PHYSICAL_NAMES", "GRAIN", "NULLABILITY", "NULL_MEANING", "DEFAULT",
                "ALLOWED_VALUES", "GENERATED", "DERIVATION", "RULES", "EVIDENCE", "PRIMARY_KEYS", "FOREIGN_KEYS",
                "UNIQUE_CONSTRAINTS", "CHECKS", "RETENTION",
            ],
            "generated_deterministically": ["FK_SUPPORTING_INDEXES", "CONTROLLED_DOMAIN_CATALOGS"],
            "neutralized_unsupported_description_ids": changed_descriptions,
        },
        "counts": counts,
        "validation": {
            "relation_and_attribute_coverage": "EXACT",
            "logical_constraints": "EXACT",
            "foreign_key_index_coverage": "PASS",
            "controlled_domain_catalog_coverage": "EXACT",
            "logical_references": "PASS",
        },
    }
    args.output.write_text(
        yaml.dump(quote_values(artifact), Dumper=QuotedDumper, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )
    args.audit.write_text(
        yaml.dump(quote_values(audit), Dumper=QuotedDumper, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )
    print(
        f"OK {args.output}: {counts['tables']} tabelas, {counts['columns']} colunas, "
        f"{counts['foreign_keys']} FKs, {counts['catalogs']} catálogos"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
