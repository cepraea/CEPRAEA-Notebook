#!/usr/bin/env python3
"""Mescla a revisão dos conceitos críticos no candidato do modelo conceitual."""

from __future__ import annotations

import argparse
import hashlib
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

from assemble_conceptual_model import validate
from build_source_manifest import QuotedDumper, quote_values


TARGET_CONCEPT_IDS = {
    "SEGMENTO_OBSERVADO",
    "PLACAR_JOGO",
    "ESTADO_DO_PLACAR",
    "EVOLUCAO_DO_PLACAR",
    "SISTEMA_DEFENSIVO",
    "CONFIABILIDADE_OBSERVADOR",
    "REVISAO_DA_OBSERVACAO",
    "ESTADO_DE_REVISAO",
    "PROVENIENCIA_OBSERVACAO",
    "TRECHO_OBSERVADO",
}
LEGACY_RULE_IDS = {"DEC-001", "REG-IHF-003", "TAX-001", "CON-006"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_revision(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if "```yaml\n" in text:
        text = text.split("```yaml\n", 1)[1].rsplit("\n```", 1)[0]
    return yaml.safe_load(text)["conceptual_model_revision"]


def normalize_rule_ids(items: list[dict[str, Any]], allowed_rule_ids: set[str]) -> set[str]:
    removed: set[str] = set()
    for item in items:
        unknown = set(item["rule_ids"]) - allowed_rule_ids
        if not unknown <= LEGACY_RULE_IDS:
            raise ValueError(f"regra desconhecida não prevista em {item['id']}: {sorted(unknown)}")
        removed |= unknown
        item["rule_ids"] = [rule_id for rule_id in item["rule_ids"] if rule_id in allowed_rule_ids]
    return removed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--revision", type=Path, required=True)
    parser.add_argument("--semantic", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    base = yaml.safe_load(args.base.read_text(encoding="utf-8"))
    revision = load_revision(args.revision)
    semantic = yaml.safe_load(args.semantic.read_text(encoding="utf-8"))
    manifest = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))
    concept_ids = {item["id"] for item in semantic["concepts"]}
    rule_ids = {item["id"] for item in semantic["rules"]}
    evidence_ids = {item["id"] for item in manifest["evidence_refs"]}

    entities = deepcopy(revision["entities"])
    relationships = deepcopy(revision["relationships"])
    invariants = deepcopy(revision["domain_invariants"])
    if {item["id"] for item in entities} != TARGET_CONCEPT_IDS:
        raise ValueError("a revisão não contém exatamente as dez entidades críticas")
    if any(item["id"] != item["concept_id"] for item in entities):
        raise ValueError("id e concept_id divergem na revisão")

    updates = revision["coverage_updates"]
    expected_issue_ids = {f"ISSUE_COVERAGE_{concept_id}" for concept_id in TARGET_CONCEPT_IDS}
    if set(updates["promote_to_covered_concept_ids"]) != TARGET_CONCEPT_IDS:
        raise ValueError("promote_to_covered_concept_ids divergente")
    if set(updates["remove_open_issue_ids"]) != expected_issue_ids:
        raise ValueError("remove_open_issue_ids divergente")
    if updates["remaining_open_issues"]:
        raise ValueError("a revisão introduziu pendências novas")

    removed_rules = set()
    for collection in (entities, relationships, invariants):
        removed_rules |= normalize_rule_ids(collection, rule_ids)
    if removed_rules != LEGACY_RULE_IDS:
        raise ValueError(f"conjunto inesperado de regras legadas: {sorted(removed_rules)}")

    placar = next(item for item in entities if item["id"] == "PLACAR_JOGO")
    if placar["temporality"] != "SNAPSHOT":
        raise ValueError("temporalidade original inesperada para PLACAR_JOGO")
    placar["temporality"] = "VERSIONADA"

    artifact = deepcopy(base)
    artifact["entities"].extend(entities)
    artifact["relationships"].extend(relationships)
    artifact["domain_invariants"].extend(invariants)
    coverage = artifact["coverage"]
    coverage["covered_concept_ids"] = [
        *coverage["covered_concept_ids"],
        *[concept_id for concept_id in updates["promote_to_covered_concept_ids"] if concept_id not in coverage["covered_concept_ids"]],
    ]
    coverage["excluded_concept_ids"] = [
        concept_id for concept_id in coverage["excluded_concept_ids"] if concept_id not in TARGET_CONCEPT_IDS
    ]
    artifact["open_issues"] = [
        issue for issue in artifact["open_issues"] if issue["id"] not in expected_issue_ids
    ]
    validate(artifact, concept_ids, rule_ids, evidence_ids)

    audit = {
        "status": "PASS",
        "inputs": {
            "base_candidate": {"path": str(args.base), "sha256": sha256(args.base)},
            "critical_review": {"path": str(args.revision), "sha256": sha256(args.revision)},
            "semantic_registry": {"path": str(args.semantic), "sha256": sha256(args.semantic)},
            "source_manifest": {"path": str(args.manifest), "sha256": sha256(args.manifest)},
        },
        "changes": {
            "added_entity_ids": sorted(TARGET_CONCEPT_IDS),
            "added_relationship_ids": [item["id"] for item in relationships],
            "added_invariant_ids": [item["id"] for item in invariants],
            "removed_open_issue_ids": sorted(expected_issue_ids),
            "removed_legacy_rule_ids": sorted(removed_rules),
            "temporality_normalization": {"PLACAR_JOGO": {"from": "SNAPSHOT", "to": "VERSIONADA"}},
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
        f"{len(coverage['covered_concept_ids'])} conceitos cobertos"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
