#!/usr/bin/env python3
"""Aplica a revisão humana de acesso e tipos ao dicionário candidato."""

from __future__ import annotations

import argparse
import hashlib
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

from assemble_data_dictionary import validate_dictionary
from build_source_manifest import QuotedDumper, quote_values


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def distributions(artifact: dict[str, Any]) -> dict[str, dict[str, int] | int]:
    return {
        "access_classification": dict(Counter(item["access_classification"] for item in artifact["tables"])),
        "postgresql_types": dict(
            Counter(column["postgresql_type_candidate"] for table in artifact["tables"] for column in table["columns"])
        ),
        "pii_columns": sum(column["pii"] for table in artifact["tables"] for column in table["columns"]),
        "sensitive_columns": sum(
            column["sensitive"] for table in artifact["tables"] for column in table["columns"]
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--review", type=Path, required=True)
    parser.add_argument("--logical", type=Path, required=True)
    parser.add_argument("--semantic", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    artifact = yaml.safe_load(args.base.read_text(encoding="utf-8"))
    review = yaml.safe_load(args.review.read_text(encoding="utf-8"))
    logical = yaml.safe_load(args.logical.read_text(encoding="utf-8"))
    semantic = yaml.safe_load(args.semantic.read_text(encoding="utf-8"))
    manifest = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))
    if review["status"] != "PASS":
        raise ValueError("revisão do operador não está aprovada")

    before = distributions(artifact)
    table_by_id = {item["relation_id"]: item for item in artifact["tables"]}

    type_changes: Counter[tuple[str, str]] = Counter()
    replacement_by_type = {item["from"]: item["to"] for item in review["type_replacements"]}
    accepted_types = {item["type"] for item in review["accepted_types"]}
    for table in artifact["tables"]:
        for column in table["columns"]:
            current = column["postgresql_type_candidate"]
            replacement = replacement_by_type.get(current)
            if replacement:
                column["postgresql_type_candidate"] = replacement
                type_changes[(current, replacement)] += 1
            elif current not in accepted_types:
                raise ValueError(f"tipo não revisado: {current}")

    access_changes = []
    for change in review["access_overrides"]:
        table = table_by_id[change["relation_id"]]
        if table["access_classification"] != change["from"]:
            raise ValueError(f"classificação-base inesperada em {change['relation_id']}")
        table["access_classification"] = change["to"]
        access_changes.append(change)

    pii_changes = []
    for change in review["pii_additions"]:
        table = table_by_id[change["relation_id"]]
        column = next(item for item in table["columns"] if item["attribute_id"] == change["attribute_id"])
        if column["pii"] is not False:
            raise ValueError(f"PII já classificado em {change['relation_id']}.{change['attribute_id']}")
        column["pii"] = True
        pii_changes.append(change)

    if review["sensitive_changes"]:
        raise ValueError("alterações sensitive não previstas nesta revisão")

    counts = validate_dictionary(
        {key: artifact[key] for key in ("tables", "catalogs", "open_issues")},
        logical,
        {item["id"] for item in semantic["rules"]},
        {item["id"] for item in manifest["evidence_refs"]},
        artifact["document"]["domain_id"],
    )
    after = distributions(artifact)
    audit = {
        "status": "PASS",
        "inputs": {
            "base_candidate": {"path": str(args.base), "sha256": sha256(args.base)},
            "operator_review": {"path": str(args.review), "sha256": sha256(args.review)},
            "logical_model": {"path": str(args.logical), "sha256": sha256(args.logical)},
            "semantic_registry": {"path": str(args.semantic), "sha256": sha256(args.semantic)},
            "source_manifest": {"path": str(args.manifest), "sha256": sha256(args.manifest)},
        },
        "changes": {
            "type_replacements": [
                {"from": old, "to": new, "columns": count}
                for (old, new), count in sorted(type_changes.items())
            ],
            "access_overrides": access_changes,
            "pii_additions": pii_changes,
            "sensitive_changes": [],
        },
        "distributions": {"before": before, "after": after},
        "counts": counts,
        "validation": {
            "specialized_dictionary_validation": "PASS",
            "logical_structure_changed": False,
            "logical_traceability_changed": False,
            "foreign_key_index_coverage": "PASS",
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
        f"OK {args.output}: tipos={after['postgresql_types']}, "
        f"acesso={after['access_classification']}, PII={after['pii_columns']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
