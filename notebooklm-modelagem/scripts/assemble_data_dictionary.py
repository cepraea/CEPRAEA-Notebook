#!/usr/bin/env python3
"""Monta e valida o DATA_DICTIONARY a partir do relatório do NotebookLM."""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path
from typing import Any

import yaml

from build_source_manifest import QuotedDumper, quote_values


TABLE_FIELDS = {
    "relation_id", "schema_candidate", "table_candidate", "description", "grain", "ownership_domain",
    "access_classification", "columns", "primary_key_attribute_ids", "foreign_key_ids",
    "unique_constraint_ids", "check_constraint_ids", "index_candidates", "retention_rule_ids",
}
COLUMN_FIELDS = {
    "attribute_id", "column_candidate", "description", "postgresql_type_candidate", "nullable", "null_meaning",
    "default_candidate", "unit", "format", "allowed_values", "min_value", "max_value", "pii", "sensitive",
    "generated", "derivation_rule_id", "rule_ids", "evidence_ref_ids",
}
INDEX_FIELDS = {"id", "attribute_ids", "purpose", "rationale"}
CATALOG_FIELDS = {"id", "name", "versioned", "values"}
CATALOG_VALUE_FIELDS = {"code", "label", "valid_from", "valid_to", "evidence_ref_ids"}
ISSUE_FIELDS = {"id", "status", "question", "affected_ids", "impact", "required_evidence", "owner"}
ACCESS_CLASSES = {"PUBLICO", "INTERNO", "PESSOAL", "SENSIVEL", "RESTRITO"}
INDEX_PURPOSES = {"FK", "QUERY", "UNIQUENESS", "RLS"}
ISSUE_STATUSES = {"ABERTA", "BLOQUEANTE", "RESOLVIDA", "NAO_APLICAVEL"}
PLACEHOLDER_RE = re.compile(r"(?:\b(?i:TBD)\b|\bTODO\b|\.\.\.|(?i:a definir))")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_report(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    marker = "data_dictionary:"
    if marker not in text:
        raise ValueError("raiz data_dictionary ausente no relatório")
    body = marker + text.split(marker, 1)[1]
    if PLACEHOLDER_RE.search(body):
        raise ValueError("placeholder proibido no relatório")
    data = yaml.safe_load(body)
    if set(data) != {"data_dictionary"}:
        raise ValueError("raiz inesperada no relatório")
    return data["data_dictionary"]


def validate_dictionary(
    body: dict[str, Any], logical: dict[str, Any], rule_ids: set[str], evidence_ids: set[str], domain_id: str
) -> dict[str, int]:
    if set(body) != {"tables", "catalogs", "open_issues"}:
        raise ValueError("seções inválidas no dicionário")

    logical_relations = {item["id"]: item for item in logical["relations"]}
    tables = body["tables"]
    if len(tables) != len(logical_relations):
        raise ValueError("quantidade de tabelas diverge do modelo lógico")
    table_by_id = {item["relation_id"]: item for item in tables}
    if len(table_by_id) != len(tables) or set(table_by_id) != set(logical_relations):
        raise ValueError("cobertura de relation_id não é exata")

    foreign_keys_by_relation: dict[str, list[dict[str, Any]]] = {item: [] for item in logical_relations}
    for foreign_key in logical["foreign_keys"]:
        foreign_keys_by_relation[foreign_key["from_relation_id"]].append(foreign_key)

    index_ids: set[str] = set()
    total_columns = 0
    total_indexes = 0
    for relation_id, logical_relation in logical_relations.items():
        table = table_by_id[relation_id]
        if set(table) != TABLE_FIELDS:
            raise ValueError(f"campos inválidos na tabela {relation_id}: {sorted(set(table) ^ TABLE_FIELDS)}")
        if table["schema_candidate"] != "public":
            raise ValueError(f"schema candidato inesperado em {relation_id}")
        if table["table_candidate"] != logical_relation["physical_name_candidate"]:
            raise ValueError(f"nome físico divergente em {relation_id}")
        if table["grain"] != logical_relation["grain"] or table["ownership_domain"] != domain_id:
            raise ValueError(f"grão ou domínio divergente em {relation_id}")
        if table["access_classification"] not in ACCESS_CLASSES or not table["description"]:
            raise ValueError(f"classificação ou descrição inválida em {relation_id}")

        logical_attributes = {item["id"]: item for item in logical_relation["attributes"]}
        columns = table["columns"]
        column_by_id = {item["attribute_id"]: item for item in columns}
        if len(column_by_id) != len(columns) or set(column_by_id) != set(logical_attributes):
            raise ValueError(f"cobertura de atributos divergente em {relation_id}")
        total_columns += len(columns)

        for attribute_id, logical_attribute in logical_attributes.items():
            column = column_by_id[attribute_id]
            if set(column) != COLUMN_FIELDS:
                raise ValueError(
                    f"campos inválidos em {relation_id}.{attribute_id}: {sorted(set(column) ^ COLUMN_FIELDS)}"
                )
            if column["column_candidate"] != logical_attribute["physical_name_candidate"]:
                raise ValueError(f"nome físico divergente em {relation_id}.{attribute_id}")
            if column["nullable"] != logical_attribute["nullable"]:
                raise ValueError(f"nulabilidade divergente em {relation_id}.{attribute_id}")
            if column["null_meaning"] != logical_attribute["null_meaning"]:
                raise ValueError(f"semântica de nulo divergente em {relation_id}.{attribute_id}")
            if column["default_candidate"] != logical_attribute["default_semantics"]:
                raise ValueError(f"default divergente em {relation_id}.{attribute_id}")
            if column["allowed_values"] != logical_attribute["domain_values"]:
                raise ValueError(f"valores permitidos divergentes em {relation_id}.{attribute_id}")
            if column["generated"] != logical_attribute["derived"]:
                raise ValueError(f"derivação divergente em {relation_id}.{attribute_id}")
            if column["derivation_rule_id"] != logical_attribute["derivation_rule_id"]:
                raise ValueError(f"regra de derivação divergente em {relation_id}.{attribute_id}")
            if column["rule_ids"] != logical_attribute["rule_ids"]:
                raise ValueError(f"regras divergentes em {relation_id}.{attribute_id}")
            if column["evidence_ref_ids"] != logical_attribute["evidence_ref_ids"]:
                raise ValueError(f"evidências divergentes em {relation_id}.{attribute_id}")
            if not column["description"] or not column["postgresql_type_candidate"]:
                raise ValueError(f"descrição ou tipo ausente em {relation_id}.{attribute_id}")
            if "jsonb" in column["postgresql_type_candidate"].lower():
                raise ValueError(f"jsonb proibido em {relation_id}.{attribute_id}")
            for field in ("nullable", "pii", "sensitive", "generated"):
                if not isinstance(column[field], bool):
                    raise ValueError(f"booleano inválido em {relation_id}.{attribute_id}.{field}")

        expected_fk_ids = {item["id"] for item in foreign_keys_by_relation[relation_id]}
        expected_unique_ids = {item["id"] for item in logical_relation["unique_constraints"]}
        expected_check_ids = {item["id"] for item in logical_relation["checks"]}
        if table["primary_key_attribute_ids"] != logical_relation["identity"]["attribute_ids"]:
            raise ValueError(f"PK divergente em {relation_id}")
        if set(table["foreign_key_ids"]) != expected_fk_ids or len(table["foreign_key_ids"]) != len(expected_fk_ids):
            raise ValueError(f"FKs divergentes em {relation_id}")
        if set(table["unique_constraint_ids"]) != expected_unique_ids or len(table["unique_constraint_ids"]) != len(expected_unique_ids):
            raise ValueError(f"unicidades divergentes em {relation_id}")
        if set(table["check_constraint_ids"]) != expected_check_ids or len(table["check_constraint_ids"]) != len(expected_check_ids):
            raise ValueError(f"checks divergentes em {relation_id}")
        if table["retention_rule_ids"] != logical_relation["retention_rule_ids"]:
            raise ValueError(f"retenção divergente em {relation_id}")

        for index in table["index_candidates"]:
            if set(index) != INDEX_FIELDS or index["purpose"] not in INDEX_PURPOSES:
                raise ValueError(f"índice inválido em {relation_id}")
            if index["id"] in index_ids or not set(index["attribute_ids"]) <= set(logical_attributes):
                raise ValueError(f"ID ou atributos inválidos no índice {index['id']}")
            if not index["rationale"]:
                raise ValueError(f"justificativa ausente no índice {index['id']}")
            index_ids.add(index["id"])
        total_indexes += len(table["index_candidates"])
        for foreign_key in foreign_keys_by_relation[relation_id]:
            if not foreign_key["supporting_index_required"]:
                continue
            matches = [
                item for item in table["index_candidates"]
                if item["purpose"] == "FK"
                and item["attribute_ids"] == foreign_key["from_attribute_ids"]
                and foreign_key["id"] in item["rationale"]
            ]
            if not matches:
                raise ValueError(f"índice de suporte ausente para {foreign_key['id']}")

    allowed_catalog_sets = {
        tuple(attribute["domain_values"])
        for relation in logical["relations"]
        for attribute in relation["attributes"]
        if attribute["domain_values"]
    }
    catalog_sets: set[tuple[Any, ...]] = set()
    catalog_ids: set[str] = set()
    for catalog in body["catalogs"]:
        if set(catalog) != CATALOG_FIELDS or catalog["id"] in catalog_ids or catalog["versioned"] is not True:
            raise ValueError(f"catálogo inválido: {catalog.get('id')}")
        codes = tuple(item["code"] for item in catalog["values"])
        if len(codes) != len(set(codes)) or codes not in allowed_catalog_sets:
            raise ValueError(f"valores inventados ou catálogo não rastreável: {catalog['id']}")
        for value in catalog["values"]:
            if set(value) != CATALOG_VALUE_FIELDS or not set(value["evidence_ref_ids"]) <= evidence_ids:
                raise ValueError(f"valor inválido no catálogo {catalog['id']}")
        catalog_ids.add(catalog["id"])
        catalog_sets.add(codes)
    if catalog_sets != allowed_catalog_sets:
        raise ValueError("catálogos não cobrem exatamente os domínios controlados do modelo lógico")

    issue_ids: set[str] = set()
    for issue in body["open_issues"]:
        if set(issue) != ISSUE_FIELDS or issue["id"] in issue_ids or issue["status"] not in ISSUE_STATUSES:
            raise ValueError(f"pendência inválida: {issue.get('id')}")
        issue_ids.add(issue["id"])
    logical_issue_ids = {item["id"] for item in logical["open_issues"]}
    if not logical_issue_ids <= issue_ids:
        raise ValueError("pendência do modelo lógico não foi preservada")

    used_rules = {
        rule_id for table in tables for column in table["columns"] for rule_id in column["rule_ids"]
    }
    used_rules.update(
        column["derivation_rule_id"]
        for table in tables
        for column in table["columns"]
        if column["derivation_rule_id"]
    )
    used_evidence = {
        evidence_id for table in tables for column in table["columns"] for evidence_id in column["evidence_ref_ids"]
    }
    used_evidence.update(
        evidence_id for catalog in body["catalogs"] for value in catalog["values"] for evidence_id in value["evidence_ref_ids"]
    )
    if used_rules - rule_ids or used_evidence - evidence_ids:
        raise ValueError("regra ou evidência desconhecida no dicionário")

    return {
        "tables": len(tables),
        "columns": total_columns,
        "foreign_keys": sum(len(item["foreign_key_ids"]) for item in tables),
        "unique_constraints": sum(len(item["unique_constraint_ids"]) for item in tables),
        "checks": sum(len(item["check_constraint_ids"]) for item in tables),
        "index_candidates": total_indexes,
        "catalogs": len(body["catalogs"]),
        "open_issues": len(body["open_issues"]),
    }


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
    body = load_report(args.report)
    stage = next(item for item in state["stages"] if item["id"] == "STAGE_04")
    counts = validate_dictionary(
        body,
        logical,
        {item["id"] for item in semantic["rules"]},
        {item["id"] for item in manifest["evidence_refs"]},
        state["run"]["domain_id"],
    )
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
            "notebook_report": {"path": str(args.report), "sha256": sha256(args.report)},
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
