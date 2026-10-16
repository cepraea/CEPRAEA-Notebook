#!/usr/bin/env python3
"""Valida o schema candidato do STAGE_08 sem executar DDL."""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path
from typing import Any

import yaml

from build_source_manifest import QuotedDumper, quote_values


FORBIDDEN_IDS = ("UQ_TRECHO_EVENTO", "CHK_VIGENCIA_PARTICIPACAO")
DIRECT_CHECK_IDS = {
    "CHK_PARTIDA_VIGENCIA_2026",
    "CHK_NUMERO_SET_VALIDO",
    "CHK_SHOOT_OUT_COMPLETUDE",
    "CHK_ELEGIBILIDADE_RANKING_CONTEXTUAL",
    "CHK_INTERVALO_VIGENCIA_PARTICIPACAO",
}
FALSE_CHECK_IDS = {
    "CHK_ATLETA_SEMANTICA_GOLEIRA",
    "CHK_TETO_PARTICIPANTES_SUMULA",
    "CHK_PRAZO_INSCRICAO_72H",
    "CHK_PASSIVO_QUATRO_PASSES",
    "CHK_BOU_REJEICAO_INFERENCIAIS",
    "CHK_PROTECAO_CABECA_GOLEIRA",
    "CHK_REGRAS_EXECUCAO_TIRO_SEIS_METROS",
    "CHK_REJEICAO_VARIAVEIS_INFERENCIAIS",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sql", type=Path, required=True)
    parser.add_argument("--logical", type=Path, required=True)
    parser.add_argument("--dictionary", type=Path, required=True)
    parser.add_argument("--artifact-id", required=True)
    parser.add_argument("--validated-at", required=True)
    parser.add_argument("--audit", type=Path, required=True)
    return parser.parse_args()


def load(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"YAML inválido: {path}")
    return value


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized_action(value: str) -> str:
    return {"SET_NULL": "SET NULL", "NO_ACTION": "NO ACTION"}.get(value, value)


def expected_default(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return "TRUE" if value else "FALSE"
    if isinstance(value, (int, float)):
        return str(value)
    return f"'{value}'"


def main() -> int:
    args = parse_args()
    text = args.sql.read_text(encoding="utf-8")
    logical = load(args.logical)
    dictionary = load(args.dictionary)
    findings: list[dict[str, Any]] = []

    def reject(finding_id: str, evidence: Any) -> None:
        findings.append({"id": finding_id, "evidence": evidence})

    if not text.startswith("--") or re.search(r"^#", text, re.MULTILINE) or "```" in text:
        reject("FORMAT_NOT_SQL_ONLY", "A saída deve começar com comentário SQL e não conter Markdown.")
    for forbidden_id in FORBIDDEN_IDS:
        if forbidden_id.lower() in text.lower():
            reject("LEGACY_ID_REINTRODUCED", forbidden_id)
    for false_check_id in FALSE_CHECK_IDS:
        if re.search(rf"CONSTRAINT\s+{re.escape(false_check_id)}\b", text, re.IGNORECASE):
            reject("FALSE_CHECK_EMITTED", false_check_id)
    if not re.search(r"CREATE\s+EXTENSION\s+IF\s+NOT\s+EXISTS\s+btree_gist\s*;", text, re.IGNORECASE):
        reject("BTREE_GIST_DEPENDENCY_MISSING", "CREATE EXTENSION IF NOT EXISTS btree_gist")
    if re.search(r"CREATE\s+SCHEMA\s+(?:IF\s+NOT\s+EXISTS\s+)?public\b", text, re.IGNORECASE):
        reject("PUBLIC_SCHEMA_CREATION_FORBIDDEN", "public")
    if not re.search(r"CREATE\s+SCHEMA\s+private\s*;", text, re.IGNORECASE):
        reject("PRIVATE_SCHEMA_MISSING", "private")

    table_pattern = re.compile(
        r"CREATE\s+TABLE\s+(public|private)\.(\w+)\s*\(\n(.*?)\n\);", re.IGNORECASE | re.DOTALL
    )
    table_blocks = {(match.group(1).lower(), match.group(2).lower()): match.group(3) for match in table_pattern.finditer(text)}
    expected_tables = {
        (("public" if table["access_classification"] == "PUBLICO" else "private"), table["table_candidate"]): table
        for table in dictionary["tables"]
    }
    if set(table_blocks) != set(expected_tables):
        reject(
            "TABLE_OR_SCHEMA_COVERAGE_MISMATCH",
            {
                "missing": [f"{schema}.{table}" for schema, table in sorted(set(expected_tables) - set(table_blocks))],
                "unexpected": [f"{schema}.{table}" for schema, table in sorted(set(table_blocks) - set(expected_tables))],
            },
        )

    column_errors: list[dict[str, Any]] = []
    covered_columns = 0
    for key, table in expected_tables.items():
        body = table_blocks.get(key)
        if body is None:
            continue
        for column in table["columns"]:
            pattern = re.compile(
                rf"^\s*{re.escape(column['column_candidate'])}\s+(.+?)\s+(NOT NULL|NULL)(?:\s+DEFAULT\s+([^,]+))?[,]?$",
                re.IGNORECASE | re.MULTILINE,
            )
            match = pattern.search(body)
            if match is None:
                column_errors.append({"column": f"{key[0]}.{key[1]}.{column['column_candidate']}", "error": "MISSING"})
                continue
            covered_columns += 1
            actual_type = " ".join(match.group(1).lower().split())
            expected_type = " ".join(column["postgresql_type_candidate"].lower().split())
            actual_nullable = match.group(2).upper() == "NULL"
            actual_default = match.group(3).strip().upper() if match.group(3) else None
            default = expected_default(column["default_candidate"])
            expected_default_sql = default.upper() if default else None
            if actual_type != expected_type or actual_nullable != column["nullable"] or actual_default != expected_default_sql:
                column_errors.append(
                    {
                        "column": f"{key[0]}.{key[1]}.{column['column_candidate']}",
                        "expected": {"type": expected_type, "nullable": column["nullable"], "default": expected_default_sql},
                        "actual": {"type": actual_type, "nullable": actual_nullable, "default": actual_default},
                    }
                )
    if column_errors:
        reject("COLUMN_CONFORMANCE_MISMATCH", column_errors)

    primary_key_errors = []
    logical_relation_by_id = {item["id"]: item for item in logical["relations"]}
    for key, table in expected_tables.items():
        body = table_blocks.get(key)
        if body is None:
            continue
        relation = logical_relation_by_id[table["relation_id"]]
        attribute_names = {
            attribute["id"]: attribute["physical_name_candidate"] for attribute in relation["attributes"]
        }
        expected_columns = [attribute_names[item] for item in relation["identity"]["attribute_ids"]]
        match = re.search(r"CONSTRAINT\s+\w+\s+PRIMARY\s+KEY\s*\(([^)]+)\)", body, re.IGNORECASE)
        actual_columns = [item.strip().lower() for item in match.group(1).split(",")] if match else None
        if actual_columns != expected_columns:
            primary_key_errors.append(
                {"relation_id": table["relation_id"], "expected": expected_columns, "actual": actual_columns}
            )
    if primary_key_errors:
        reject("PRIMARY_KEY_CONFORMANCE_MISMATCH", primary_key_errors)

    expected_uniques = {
        unique["id"]: unique["attribute_ids"]
        for relation in logical["relations"]
        for unique in relation["unique_constraints"]
    }
    found_uniques = {
        match.group(1).upper(): [item.strip().lower() for item in match.group(2).split(",")]
        for match in re.finditer(r"CONSTRAINT\s+(\w+)\s+UNIQUE\s*\(([^)]+)\)", text, re.IGNORECASE)
    }
    logical_physical_names = {
        relation["id"]: {attribute["id"]: attribute["physical_name_candidate"] for attribute in relation["attributes"]}
        for relation in logical["relations"]
    }
    expected_unique_columns = {}
    for relation in logical["relations"]:
        for unique in relation["unique_constraints"]:
            expected_unique_columns[unique["id"]] = [logical_physical_names[relation["id"]][item] for item in unique["attribute_ids"]]
    if found_uniques != expected_unique_columns:
        reject(
            "UNIQUE_CONFORMANCE_MISMATCH",
            {
                "missing_or_changed": sorted(
                    item for item, columns in expected_unique_columns.items() if found_uniques.get(item) != columns
                ),
                "unexpected": sorted(set(found_uniques) - set(expected_unique_columns)),
            },
        )

    alter_blocks = list(re.finditer(r"ALTER\s+TABLE\s+(public|private)\.(\w+)\s+(.*?);", text, re.IGNORECASE | re.DOTALL))
    fk_pattern = re.compile(
        r"ADD\s+CONSTRAINT\s+(\w+)\s+FOREIGN\s+KEY\s*\(([^)]+)\)\s+REFERENCES\s+"
        r"(public|private)\.(\w+)\s*\(([^)]+)\)\s+ON\s+DELETE\s+(NO ACTION|SET NULL|CASCADE|RESTRICT)\s+"
        r"ON\s+UPDATE\s+(NO ACTION|CASCADE|RESTRICT)",
        re.IGNORECASE,
    )
    found_fks: dict[str, dict[str, Any]] = {}
    for block in alter_blocks:
        source = (block.group(1).lower(), block.group(2).lower())
        for match in fk_pattern.finditer(block.group(3)):
            found_fks[match.group(1).upper()] = {
                "source": source,
                "source_columns": [item.strip().lower() for item in match.group(2).split(",")],
                "target": (match.group(3).lower(), match.group(4).lower()),
                "target_columns": [item.strip().lower() for item in match.group(5).split(",")],
                "on_delete": match.group(6).upper(),
                "on_update": match.group(7).upper(),
            }
    table_by_relation = {item["relation_id"]: item for item in dictionary["tables"]}
    relation_by_id = {item["id"]: item for item in logical["relations"]}
    fk_errors = []
    for foreign_key in logical["foreign_keys"]:
        source_table = table_by_relation[foreign_key["from_relation_id"]]
        target_table = table_by_relation[foreign_key["to_relation_id"]]
        source_schema = "public" if source_table["access_classification"] == "PUBLICO" else "private"
        target_schema = "public" if target_table["access_classification"] == "PUBLICO" else "private"
        source_names = logical_physical_names[foreign_key["from_relation_id"]]
        target_names = logical_physical_names[foreign_key["to_relation_id"]]
        expected = {
            "source": (source_schema, source_table["table_candidate"]),
            "source_columns": [source_names[item] for item in foreign_key["from_attribute_ids"]],
            "target": (target_schema, target_table["table_candidate"]),
            "target_columns": [target_names[item] for item in foreign_key["to_attribute_ids"]],
            "on_delete": normalized_action(foreign_key["on_delete_semantics"]),
            "on_update": normalized_action(foreign_key["on_update_semantics"]),
        }
        actual = found_fks.get(foreign_key["id"])
        if actual != expected:
            fk_errors.append({"foreign_key_id": foreign_key["id"], "expected": expected, "actual": actual})
    if fk_errors or set(found_fks) != {item["id"] for item in logical["foreign_keys"]}:
        reject(
            "FOREIGN_KEY_CONFORMANCE_MISMATCH",
            {"errors": fk_errors, "unexpected": sorted(set(found_fks) - {item["id"] for item in logical["foreign_keys"]})},
        )

    missing_checks = sorted(
        check_id for check_id in DIRECT_CHECK_IDS
        if not re.search(rf"CONSTRAINT\s+{re.escape(check_id)}\s+CHECK\b", text, re.IGNORECASE)
    )
    if missing_checks:
        reject("DIRECT_CHECKS_MISSING", missing_checks)
    normalized_sql = " ".join(text.lower().split())
    required_check_semantics = {
        "CHK_PARTIDA_VIGENCIA_2026": "data_hora_inicio is null or data_hora_inicio >=",
        "CHK_NUMERO_SET_VALIDO": "numero_set in (1, 2)",
        "CHK_SHOOT_OUT_COMPLETUDE": "status_completude = 'completo' and pontos_equipe_a is not null and pontos_equipe_b is not null",
        "CHK_ELEGIBILIDADE_RANKING_CONTEXTUAL": "status_elegibilidade_ranking <> 'inelegivel_por_decisao_coletiva' or (motivo_decisao is not null",
        "CHK_INTERVALO_VIGENCIA_PARTICIPACAO": "valido_ate is null or valido_ate > valido_desde",
    }
    semantic_errors = [
        check_id for check_id, fragment in required_check_semantics.items() if fragment not in normalized_sql
    ]
    if semantic_errors or "decisao_ref is not null" not in normalized_sql:
        reject("DIRECT_CHECK_SEMANTICS_MISMATCH", semantic_errors or ["CHK_ELEGIBILIDADE_RANKING_CONTEXTUAL"])
    if not re.search(
        r"ADD\s+CONSTRAINT\s+excl_participacao_equipe_competicao_vigencia\s+EXCLUDE\s+USING\s+gist",
        text,
        re.IGNORECASE | re.DOTALL,
    ):
        reject("TEMPORAL_EXCLUSION_MISSING", "EXCL_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA")

    explicit_indexes = len(re.findall(r"^CREATE\s+INDEX\b", text, re.IGNORECASE | re.MULTILINE))
    covered_indexes = len(re.findall(r"Omitido \(coberto", text, re.IGNORECASE))
    if (explicit_indexes, covered_indexes) != (50, 9):
        reject("FK_INDEX_COVERAGE_MISMATCH", {"explicit": explicit_indexes, "covered": covered_indexes})

    if re.search(r"\b(?:DROP|TRUNCATE|GRANT|REVOKE)\b|ENABLE\s+ROW\s+LEVEL\s+SECURITY|CREATE\s+POLICY", text, re.IGNORECASE):
        reject("FORBIDDEN_DDL_PRESENT", "DROP/TRUNCATE/GRANT/REVOKE/RLS/POLICY")

    public_tables = sum(schema == "public" for schema, _ in table_blocks)
    private_tables = sum(schema == "private" for schema, _ in table_blocks)
    audit = {
        "status": "PASS" if not findings else "REJECTED",
        "stage_id": "STAGE_08",
        "artifact_id": args.artifact_id,
        "sql_path": str(args.sql),
        "sql_sha256": file_sha256(args.sql),
        "validated_at": args.validated_at,
        "input_artifacts": {
            "logical_model": {"version": logical["document"]["version"], "sha256": file_sha256(args.logical)},
            "data_dictionary": {"version": dictionary["document"]["version"], "sha256": file_sha256(args.dictionary)},
        },
        "coverage": {
            "tables": len(table_blocks),
            "public_tables": public_tables,
            "private_tables": private_tables,
            "expected_columns": sum(len(item["columns"]) for item in dictionary["tables"]),
            "covered_columns": covered_columns,
            "primary_keys": len(expected_tables) - len(primary_key_errors),
            "foreign_keys": len(found_fks),
            "unique_constraints": len(found_uniques),
            "direct_checks": len(DIRECT_CHECK_IDS) - len(missing_checks),
            "direct_check_semantics": len(DIRECT_CHECK_IDS) - len(semantic_errors),
            "explicit_fk_indexes": explicit_indexes,
            "fk_indexes_covered_by_pk_or_unique_prefix": covered_indexes,
            "temporal_exclusion": not any(item["id"] == "TEMPORAL_EXCLUSION_MISSING" for item in findings),
        },
        "findings": findings,
        "execution": "NOT_PERFORMED",
    }
    args.audit.write_text(
        yaml.dump(quote_values(audit), Dumper=QuotedDumper, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )
    print(f"{audit['status']} {args.sql}: findings={len(findings)}")
    return 0 if not findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
