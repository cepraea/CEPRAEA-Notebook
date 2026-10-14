#!/usr/bin/env python3
"""Monta e valida o candidato CONCEPTUAL_MODEL a partir da correção do NotebookLM."""

from __future__ import annotations

import argparse
import hashlib
import re
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

from build_source_manifest import QuotedDumper, quote_values


ENTITY_FIELDS = {
    "id", "name", "concept_id", "definition", "identity_rule", "temporality",
    "history_required", "aggregate_root", "rule_ids", "evidence_ref_ids",
}
RELATIONSHIP_FIELDS = {
    "id", "name", "from_entity_id", "to_entity_id", "meaning", "cardinality",
    "relationship_attributes", "temporality", "exclusivity_rules", "rule_ids",
    "evidence_ref_ids",
}
INVARIANT_FIELDS = {"id", "statement", "affected_entity_ids", "rule_ids", "evidence_ref_ids"}
ISSUE_FIELDS = {"id", "status", "question", "affected_ids", "impact", "required_evidence", "owner"}
TEMPORALITIES = {"ATEMPORAL", "INSTANTANEA", "INTERVALO", "VERSIONADA", "EVENTO"}
ID_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")

CARDINALITY_NORMALIZATIONS = {
    "PARTIDA_DISPUTADA_POR_EQUIPE": {
        "expected": {"min": 2, "max": 2},
        "replacement": {"min": 1, "max": "N"},
        "constraint": "Cada partida deve relacionar exatamente duas equipes.",
    },
    "EQUIPE_INSCREVE_ATLETA": {
        "expected": {"min": 6, "max": "N"},
        "replacement": {"min": 1, "max": "N"},
        "constraint": "No contexto da partida, a equipe deve possuir no mínimo seis atletas inscritos para iniciar o jogo.",
    },
    "PARTIDA_POSSUI_PERIODO_SET": {
        "expected": {"min": 2, "max": 2},
        "replacement": {"min": 1, "max": "N"},
        "constraint": "Cada partida regulamentar deve possuir exatamente dois períodos ou sets.",
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize_cardinalities(relationships: list[dict[str, Any]]) -> list[dict[str, Any]]:
    normalized = deepcopy(relationships)
    by_id = {item["id"]: item for item in normalized}
    for relationship_id, change in CARDINALITY_NORMALIZATIONS.items():
        item = by_id[relationship_id]
        actual = item["cardinality"]["from_to"]
        if actual != change["expected"]:
            raise ValueError(f"cardinalidade inesperada em {relationship_id}: {actual}")
        item["cardinality"]["from_to"] = change["replacement"]
        item["exclusivity_rules"] = [*item["exclusivity_rules"], change["constraint"]]
    return normalized


def normalize_open_issues(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    normalized = []
    for item in items:
        if set(item) != {"concept_id", "justification"}:
            raise ValueError(f"questão de cobertura inesperada: {item}")
        concept_id = item["concept_id"]
        normalized.append(
            {
                "id": f"ISSUE_COVERAGE_{concept_id}",
                "status": "ABERTA",
                "question": f"A exclusão de {concept_id} como entidade conceitual independente deve ser mantida?",
                "affected_ids": [concept_id],
                "impact": (
                    f"{concept_id} permanece representado apenas como atributo, projeção, regra ou aspecto "
                    "de outra entidade até validação."
                ),
                "required_evidence": item["justification"],
                "owner": "OPERADOR",
            }
        )
    return normalized


def validate(
    artifact: dict[str, Any], concept_ids: set[str], rule_ids: set[str], evidence_ids: set[str]
) -> None:
    entities = artifact["entities"]
    relationships = artifact["relationships"]
    invariants = artifact["domain_invariants"]
    issues = artifact["open_issues"]
    entity_ids = {item["id"] for item in entities}

    ids = [item["id"] for collection in (entities, relationships, invariants, issues) for item in collection]
    if len(ids) != len(set(ids)) or any(not ID_RE.fullmatch(item_id) for item_id in ids):
        raise ValueError("IDs duplicados ou fora de UPPER_SNAKE_CASE")

    for item in entities:
        if set(item) != ENTITY_FIELDS:
            raise ValueError(f"campos inválidos na entidade {item['id']}")
        if item["concept_id"] not in concept_ids:
            raise ValueError(f"concept_id inexistente em {item['id']}")
        if item["temporality"] not in TEMPORALITIES:
            raise ValueError(f"temporalidade inválida em {item['id']}")
        if not isinstance(item["history_required"], bool) or not isinstance(item["aggregate_root"], bool):
            raise ValueError(f"booleano inválido em {item['id']}")
        if not set(item["rule_ids"]) <= rule_ids or not set(item["evidence_ref_ids"]) <= evidence_ids:
            raise ValueError(f"referência inválida em {item['id']}")

    for item in relationships:
        if set(item) != RELATIONSHIP_FIELDS:
            raise ValueError(f"campos inválidos no relacionamento {item['id']}")
        if {item["from_entity_id"], item["to_entity_id"]} - entity_ids:
            raise ValueError(f"extremidade inexistente em {item['id']}")
        for direction in ("from_to", "to_from"):
            cardinality = item["cardinality"].get(direction)
            if not isinstance(cardinality, dict) or set(cardinality) != {"min", "max"}:
                raise ValueError(f"cardinalidade inválida em {item['id']}")
            if cardinality["min"] not in {0, 1} or cardinality["max"] not in {1, "N"}:
                raise ValueError(f"limite cardinal inválido em {item['id']}")
        if not set(item["rule_ids"]) <= rule_ids or not set(item["evidence_ref_ids"]) <= evidence_ids:
            raise ValueError(f"referência inválida em {item['id']}")
        for field in ("relationship_attributes", "exclusivity_rules", "rule_ids", "evidence_ref_ids"):
            if not isinstance(item[field], list):
                raise ValueError(f"campo-lista inválido em {item['id']}")

    for item in invariants:
        if set(item) != INVARIANT_FIELDS:
            raise ValueError(f"campos inválidos no invariante {item['id']}")
        if not set(item["affected_entity_ids"]) <= entity_ids:
            raise ValueError(f"entidade inexistente em {item['id']}")
        if not set(item["rule_ids"]) <= rule_ids or not set(item["evidence_ref_ids"]) <= evidence_ids:
            raise ValueError(f"referência inválida em {item['id']}")

    for item in issues:
        if set(item) != ISSUE_FIELDS or item["status"] not in {"ABERTA", "BLOQUEANTE", "RESOLVIDA", "NAO_APLICAVEL"}:
            raise ValueError(f"questão aberta inválida: {item.get('id')}")
        if not set(item["affected_ids"]) <= concept_ids:
            raise ValueError(f"questão referencia conceito inexistente: {item['id']}")

    coverage = artifact["coverage"]
    if set(coverage) != {"required_concept_ids", "covered_concept_ids", "excluded_concept_ids"}:
        raise ValueError("campos inválidos em coverage")
    required = coverage["required_concept_ids"]
    covered = coverage["covered_concept_ids"]
    excluded = coverage["excluded_concept_ids"]
    if any(len(values) != len(set(values)) for values in (required, covered, excluded)):
        raise ValueError("IDs duplicados em coverage")
    if set(required) != concept_ids:
        raise ValueError("required_concept_ids diverge do registro semântico")
    if set(covered) & set(excluded) or set(covered) | set(excluded) != concept_ids:
        raise ValueError("covered_concept_ids e excluded_concept_ids não formam partição exata")
    issue_concepts = {affected for issue in issues for affected in issue["affected_ids"]}
    if issue_concepts != set(excluded):
        raise ValueError("questões abertas não justificam exatamente os conceitos excluídos")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", type=Path, required=True)
    parser.add_argument("--semantic", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--correction", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    state = yaml.safe_load(args.state.read_text(encoding="utf-8"))
    semantic = yaml.safe_load(args.semantic.read_text(encoding="utf-8"))
    manifest = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))
    correction = yaml.safe_load(args.correction.read_text(encoding="utf-8"))["conceptual_model"]
    stage = next(item for item in state["stages"] if item["id"] == "STAGE_02")
    concept_ids = {item["id"] for item in semantic["concepts"]}
    rule_ids = {item["id"] for item in semantic["rules"]}
    evidence_ids = {item["id"] for item in manifest["evidence_refs"]}

    artifact = {
        "schema_version": "1.1",
        "document": {
            "id": "CONCEPTUAL_MODEL",
            "artifact_kind": "CONCEPTUAL_MODEL",
            "title": "Modelo conceitual",
            "version": "0.1.0",
            "status": "PROPOSTO",
            "run_id": state["run"]["id"],
            "domain_id": state["run"]["domain_id"],
            "notebook_id": state["run"]["notebook_id"],
            "generated_at": None,
            "supersedes": None,
            "input_artifacts": stage["input_artifacts"],
        },
        "entities": correction["entities"],
        "relationships": normalize_cardinalities(correction["relationships"]),
        "domain_invariants": correction["domain_invariants"],
        "coverage": correction["coverage"],
        "open_issues": normalize_open_issues(correction["open_issues"]),
    }
    validate(artifact, concept_ids, rule_ids, evidence_ids)

    audit = {
        "status": "PASS",
        "inputs": {
            "semantic_registry": {"path": str(args.semantic), "sha256": sha256(args.semantic)},
            "source_manifest": {"path": str(args.manifest), "sha256": sha256(args.manifest)},
            "notebook_correction": {"path": str(args.correction), "sha256": sha256(args.correction)},
        },
        "normalization": {
            "cardinality": CARDINALITY_NORMALIZATIONS,
            "open_issues": "16 justificativas de exclusão convertidas para o contrato de pendências.",
            "semantic_content_added": False,
        },
        "counts": {
            "entities": len(artifact["entities"]),
            "relationships": len(artifact["relationships"]),
            "domain_invariants": len(artifact["domain_invariants"]),
            "open_issues": len(artifact["open_issues"]),
            "required_concept_ids": len(artifact["coverage"]["required_concept_ids"]),
            "covered_concept_ids": len(artifact["coverage"]["covered_concept_ids"]),
            "excluded_concept_ids": len(artifact["coverage"]["excluded_concept_ids"]),
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
        f"{len(artifact['relationships'])} relacionamentos, {len(artifact['domain_invariants'])} invariantes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
