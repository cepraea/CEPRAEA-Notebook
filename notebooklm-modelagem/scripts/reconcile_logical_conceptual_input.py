#!/usr/bin/env python3
"""Reconcilia o candidato lógico com uma nova versão conceitual promovida."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import yaml

from assemble_logical_model import validate_model
from build_source_manifest import QuotedDumper, quote_values


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--semantic", type=Path, required=True)
    parser.add_argument("--conceptual", type=Path, required=True)
    parser.add_argument("--conceptual-source-id", required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    artifact = yaml.safe_load(args.base.read_text(encoding="utf-8"))
    semantic = yaml.safe_load(args.semantic.read_text(encoding="utf-8"))
    conceptual = yaml.safe_load(args.conceptual.read_text(encoding="utf-8"))
    manifest = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))

    if conceptual["document"]["version"] != "0.1.1":
        raise ValueError("versão conceitual promovida inesperada")

    conceptual_input = next(
        item for item in artifact["document"]["input_artifacts"] if item["document_id"] == "CONCEPTUAL_MODEL"
    )
    previous_conceptual_input = dict(conceptual_input)
    conceptual_input.update(
        {
            "version": conceptual["document"]["version"],
            "sha256": sha256(args.conceptual),
            "promoted_source_id": args.conceptual_source_id,
        }
    )

    reconciliation_note = (
        "A relação EQUIPE_PARTICIPA_COMPETICAO é um refinamento lógico aprovado que deverá ser reconciliado "
        "no próximo versionamento conceitual."
    )
    decision = next(item for item in artifact["normalization_decisions"] if item["id"] == "NORM_DECISION_006")
    if reconciliation_note not in decision["accepted_tradeoffs"]:
        raise ValueError("nota de reconciliação conceitual pendente não encontrada")
    decision["accepted_tradeoffs"].remove(reconciliation_note)

    model = {key: artifact[key] for key in ("relations", "foreign_keys", "normalization_decisions", "open_issues")}
    counts = validate_model(
        model,
        {item["id"] for item in conceptual["entities"]},
        {item["id"] for item in conceptual["relationships"]},
        {item["id"] for item in semantic["rules"]},
        {item["id"] for item in manifest["evidence_refs"]},
    )

    audit = {
        "status": "PASS",
        "inputs": {
            "base_candidate": {"path": str(args.base), "sha256": sha256(args.base)},
            "semantic_registry": {"path": str(args.semantic), "sha256": sha256(args.semantic)},
            "conceptual_model": {
                "path": str(args.conceptual),
                "version": conceptual["document"]["version"],
                "sha256": sha256(args.conceptual),
                "promoted_source_id": args.conceptual_source_id,
            },
            "source_manifest": {"path": str(args.manifest), "sha256": sha256(args.manifest)},
        },
        "changes": {
            "previous_conceptual_input": previous_conceptual_input,
            "current_conceptual_input": conceptual_input,
            "removed_pending_reconciliation_note": True,
            "logical_structure_changed": False,
            "approved_logical_relationship_ids": [],
        },
        "upstream_reconciliation": {
            "required": False,
            "relationship_id": "EQUIPE_PARTICIPA_COMPETICAO",
            "resolved_in_conceptual_version": "0.1.1",
        },
        "counts": counts,
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
        f"OK {args.output}: {counts['covered_conceptual_relationships']} relacionamentos conceituais, "
        f"{counts['approved_logical_relationships']} refinamentos lógicos"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
