#!/usr/bin/env python3
"""Versiona o modelo conceitual com a relação equipe-competição aprovada."""

from __future__ import annotations

import argparse
import hashlib
from copy import deepcopy
from pathlib import Path

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


def main() -> int:
    args = parse_args()
    artifact = yaml.safe_load(args.base.read_text(encoding="utf-8"))
    review = yaml.safe_load(args.review.read_text(encoding="utf-8"))
    semantic = yaml.safe_load(args.semantic.read_text(encoding="utf-8"))
    manifest = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))

    if review["status"] != "PASS":
        raise ValueError("reconciliação do ranking não está aprovada")
    if artifact["document"]["version"] != "0.1.0":
        raise ValueError("versão-base conceitual inesperada")

    relationship = deepcopy(review["relationship"])
    invariant = deepcopy(review["invariant"])
    relationship_ids = {item["id"] for item in artifact["relationships"]}
    invariant_ids = {item["id"] for item in artifact["domain_invariants"]}
    if relationship["id"] in relationship_ids or invariant["id"] in invariant_ids:
        raise ValueError("reconciliação já aplicada ao modelo conceitual")

    artifact["document"]["version"] = "0.1.1"
    artifact["document"]["supersedes"] = "CONCEPTUAL_MODEL@0.1.0"
    artifact["relationships"].append(relationship)
    artifact["domain_invariants"].append(invariant)

    validate(
        artifact,
        {item["id"] for item in semantic["concepts"]},
        {item["id"] for item in semantic["rules"]},
        {item["id"] for item in manifest["evidence_refs"]},
    )

    audit = {
        "status": "PASS",
        "inputs": {
            "base_candidate": {"path": str(args.base), "sha256": sha256(args.base)},
            "ranking_reconciliation": {"path": str(args.review), "sha256": sha256(args.review)},
            "semantic_registry": {"path": str(args.semantic), "sha256": sha256(args.semantic)},
            "source_manifest": {"path": str(args.manifest), "sha256": sha256(args.manifest)},
        },
        "operator_decision": review["operator_decision"],
        "changes": {
            "version": "0.1.1",
            "supersedes": "CONCEPTUAL_MODEL@0.1.0",
            "added_relationship_id": relationship["id"],
            "added_invariant_id": invariant["id"],
            "entities_changed": False,
            "coverage_changed": False,
            "open_issues_changed": False,
        },
        "counts": {
            "entities": len(artifact["entities"]),
            "relationships": len(artifact["relationships"]),
            "domain_invariants": len(artifact["domain_invariants"]),
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
        f"{len(artifact['relationships'])} relacionamentos, "
        f"{len(artifact['domain_invariants'])} invariantes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
