#!/usr/bin/env python3
"""Aplica decisões do operador ao candidato do modelo lógico."""

from __future__ import annotations

import argparse
import hashlib
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

from assemble_logical_model import validate_model
from build_source_manifest import QuotedDumper, quote_values


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--review", type=Path, required=True)
    parser.add_argument("--semantic", type=Path, required=True)
    parser.add_argument("--conceptual", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    artifact = yaml.safe_load(args.base.read_text(encoding="utf-8"))
    review = yaml.safe_load(args.review.read_text(encoding="utf-8"))
    semantic = yaml.safe_load(args.semantic.read_text(encoding="utf-8"))
    conceptual = yaml.safe_load(args.conceptual.read_text(encoding="utf-8"))
    manifest = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))
    if review["status"] != "PASS":
        raise ValueError("revisão do operador não está aprovada")

    model = {key: artifact[key] for key in ("relations", "foreign_keys", "normalization_decisions", "open_issues")}
    relation_by_id = {item["id"]: item for item in model["relations"]}
    shoot_out = relation_by_id[review["shoot_out_changes"]["relation_id"]]
    attribute_by_id = {item["id"]: item for item in shoot_out["attributes"]}
    for change in review["shoot_out_changes"]["attribute_updates"]:
        attribute = attribute_by_id[change["attribute_id"]]
        for key in ("nullable", "null_meaning", "default_semantics"):
            attribute[key] = change[key]
    shoot_out["attributes"].extend(deepcopy(review["shoot_out_changes"]["added_attributes"]))
    shoot_out["checks"].extend(deepcopy(review["shoot_out_changes"]["added_checks"]))

    existing_ids = {
        key: {item["id"] for item in model[key]}
        for key in ("relations", "foreign_keys", "normalization_decisions")
    }
    additions = {
        "relations": deepcopy(review["added_relations"]),
        "foreign_keys": deepcopy(review["added_foreign_keys"]),
        "normalization_decisions": deepcopy(review["added_normalization_decisions"]),
    }
    for key, items in additions.items():
        added_ids = [item["id"] for item in items]
        if len(added_ids) != len(set(added_ids)) or existing_ids[key] & set(added_ids):
            raise ValueError(f"IDs duplicados nas adições de {key}")
        model[key].extend(items)

    resolved_issue_ids = set(review["resolved_open_issue_ids"])
    existing_issue_ids = {item["id"] for item in model["open_issues"]}
    if not resolved_issue_ids <= existing_issue_ids:
        raise ValueError("pendência resolvida não existe no candidato-base")
    model["open_issues"] = [item for item in model["open_issues"] if item["id"] not in resolved_issue_ids]

    conceptual_entity_ids = {item["id"] for item in conceptual["entities"]}
    conceptual_relationship_ids = {item["id"] for item in conceptual["relationships"]}
    approved_logical_relationship_ids = set(review["approved_logical_relationship_ids"])
    counts = validate_model(
        model,
        conceptual_entity_ids,
        conceptual_relationship_ids,
        {item["id"] for item in semantic["rules"]},
        {item["id"] for item in manifest["evidence_refs"]},
        approved_logical_relationship_ids,
    )

    output = {"schema_version": artifact["schema_version"], "document": artifact["document"], **model}
    audit = {
        "status": "PASS",
        "inputs": {
            "base_candidate": {"path": str(args.base), "sha256": sha256(args.base)},
            "operator_review": {"path": str(args.review), "sha256": sha256(args.review)},
            "semantic_registry": {"path": str(args.semantic), "sha256": sha256(args.semantic)},
            "conceptual_model": {"path": str(args.conceptual), "sha256": sha256(args.conceptual)},
            "source_manifest": {"path": str(args.manifest), "sha256": sha256(args.manifest)},
        },
        "operator_decisions": review["operator_decisions"],
        "changes": {
            "shoot_out_attribute_updates": [item["attribute_id"] for item in review["shoot_out_changes"]["attribute_updates"]],
            "shoot_out_added_attribute_ids": [item["id"] for item in review["shoot_out_changes"]["added_attributes"]],
            "shoot_out_added_check_ids": [item["id"] for item in review["shoot_out_changes"]["added_checks"]],
            "added_relation_ids": [item["id"] for item in additions["relations"]],
            "added_foreign_key_ids": [item["id"] for item in additions["foreign_keys"]],
            "added_normalization_decision_ids": [item["id"] for item in additions["normalization_decisions"]],
            "approved_logical_relationship_ids": sorted(approved_logical_relationship_ids),
            "resolved_open_issue_ids": sorted(resolved_issue_ids),
        },
        "upstream_reconciliation": {
            "required": True,
            "target": "Próxima versão do modelo conceitual",
            "relationship_id": "EQUIPE_PARTICIPA_COMPETICAO",
        },
        "counts": counts,
    }
    args.output.write_text(
        yaml.dump(quote_values(output), Dumper=QuotedDumper, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )
    args.audit.write_text(
        yaml.dump(quote_values(audit), Dumper=QuotedDumper, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )
    print(
        f"OK {args.output}: {counts['relations']} relações, {counts['foreign_keys']} FKs, "
        f"{counts['open_issues']} pendência aberta"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
