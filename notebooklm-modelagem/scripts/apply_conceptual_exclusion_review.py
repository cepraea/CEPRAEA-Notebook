#!/usr/bin/env python3
"""Aplica ao modelo conceitual a decisão do operador sobre exclusões remanescentes."""

from __future__ import annotations

import argparse
import hashlib
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

from assemble_conceptual_model import validate
from build_source_manifest import QuotedDumper, quote_values


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--review", type=Path, required=True)
    parser.add_argument("--semantic", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    return parser.parse_args()


def ensure_unique(existing: list[dict[str, Any]], additions: list[dict[str, Any]], label: str) -> None:
    existing_ids = {item["id"] for item in existing}
    addition_ids = [item["id"] for item in additions]
    if len(addition_ids) != len(set(addition_ids)):
        raise ValueError(f"IDs duplicados nas adições de {label}")
    overlap = existing_ids & set(addition_ids)
    if overlap:
        raise ValueError(f"IDs de {label} já existentes: {sorted(overlap)}")


def main() -> int:
    args = parse_args()
    artifact = yaml.safe_load(args.base.read_text(encoding="utf-8"))
    review = yaml.safe_load(args.review.read_text(encoding="utf-8"))
    semantic = yaml.safe_load(args.semantic.read_text(encoding="utf-8"))
    manifest = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))

    if review["status"] != "PASS":
        raise ValueError("a revisão das exclusões não está aprovada")

    reviewed_ids = set(review["reviewed_concept_ids"])
    decision_ids = {item["concept_id"] for item in review["decisions"]}
    entity_ids = {item["concept_id"] for item in review["entities"]}
    promoted_ids = set(review["coverage_updates"]["promote_to_covered_concept_ids"])
    expected_issues = {f"ISSUE_COVERAGE_{concept_id}" for concept_id in reviewed_ids}
    removed_issues = set(review["coverage_updates"]["remove_open_issue_ids"])
    if not reviewed_ids or not (reviewed_ids == decision_ids == entity_ids == promoted_ids):
        raise ValueError("conceitos revisados, decididos, materializados e promovidos divergem")
    if removed_issues != expected_issues:
        raise ValueError("questões removidas não correspondem exatamente às exclusões revisadas")
    if reviewed_ids != set(artifact["coverage"]["excluded_concept_ids"]):
        raise ValueError("a revisão não cobre exatamente as exclusões remanescentes")

    additions = {
        "entities": deepcopy(review["entities"]),
        "relationships": deepcopy(review["relationships"]),
        "domain_invariants": deepcopy(review["domain_invariants"]),
    }
    for key, items in additions.items():
        ensure_unique(artifact[key], items, key)
        artifact[key].extend(items)

    coverage = artifact["coverage"]
    coverage["covered_concept_ids"].extend(
        concept_id for concept_id in review["reviewed_concept_ids"] if concept_id not in coverage["covered_concept_ids"]
    )
    coverage["excluded_concept_ids"] = []
    artifact["open_issues"] = [
        item for item in artifact["open_issues"] if item["id"] not in removed_issues
    ]

    concept_ids = {item["id"] for item in semantic["concepts"]}
    rule_ids = {item["id"] for item in semantic["rules"]}
    evidence_ids = {item["id"] for item in manifest["evidence_refs"]}
    validate(artifact, concept_ids, rule_ids, evidence_ids)

    audit = {
        "status": "PASS",
        "inputs": {
            "base_candidate": {"path": str(args.base), "sha256": sha256(args.base)},
            "exclusion_review": {"path": str(args.review), "sha256": sha256(args.review)},
            "semantic_registry": {"path": str(args.semantic), "sha256": sha256(args.semantic)},
            "source_manifest": {"path": str(args.manifest), "sha256": sha256(args.manifest)},
        },
        "decisions": review["decisions"],
        "changes": {
            "added_entity_ids": [item["id"] for item in additions["entities"]],
            "added_relationship_ids": [item["id"] for item in additions["relationships"]],
            "added_invariant_ids": [item["id"] for item in additions["domain_invariants"]],
            "removed_open_issue_ids": sorted(removed_issues),
        },
        "counts": {
            "entities": len(artifact["entities"]),
            "relationships": len(artifact["relationships"]),
            "domain_invariants": len(artifact["domain_invariants"]),
            "covered_concept_ids": len(coverage["covered_concept_ids"]),
            "excluded_concept_ids": len(coverage["excluded_concept_ids"]),
            "open_issues": len(artifact["open_issues"]),
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
        f"OK {args.output}: {len(artifact['entities'])} entidades, "
        f"{len(coverage['covered_concept_ids'])} conceitos cobertos, nenhuma exclusão"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
