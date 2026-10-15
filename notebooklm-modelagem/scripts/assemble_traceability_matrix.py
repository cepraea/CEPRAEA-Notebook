#!/usr/bin/env python3
"""Monta a matriz PLANNED usando apenas IDs dos artefatos promovidos."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
from typing import Any

import yaml

from build_source_manifest import QuotedDumper, quote_values


TRACE_FIELDS = {
    "id", "evidence_ref_ids", "concept_ids", "rule_ids", "conceptual_entity_ids",
    "relationship_ids", "logical_relation_ids", "attribute_ids", "physical_object_ids",
    "permission_requirement_ids", "test_ids", "implementation_status", "verification_status",
    "verification_evidence_ids",
}
ISSUE_FIELDS = {"id", "status", "question", "affected_ids", "impact", "required_evidence", "owner"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", type=Path, required=True)
    parser.add_argument("--proposal", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--semantic", type=Path, required=True)
    parser.add_argument("--conceptual", type=Path, required=True)
    parser.add_argument("--logical", type=Path, required=True)
    parser.add_argument("--dictionary", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    return parser.parse_args()


def load(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"YAML inválido: {path}")
    return value


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ordered_unique(values: list[str]) -> list[str]:
    return list(dict.fromkeys(values))


def stage(state: dict[str, Any], stage_id: str) -> dict[str, Any]:
    return next(item for item in state["stages"] if item["id"] == stage_id)


def proposal_rule_coverage(
    proposal: dict[str, Any], allowed_rules: set[str], allowed_evidence: set[str]
) -> set[str]:
    if set(proposal) != {"phase", "traces", "coverage_summary", "orphan_checks", "open_issues"}:
        raise ValueError("raízes inesperadas na proposta do NotebookLM")
    if proposal["phase"] != "PLANNED":
        raise ValueError("fase da proposta não é PLANNED")
    covered: set[str] = set()
    for trace in proposal["traces"]:
        rule_ids = set(trace.get("rule_ids", []))
        evidence_ids = set(trace.get("evidence_ref_ids", []))
        if not rule_ids <= allowed_rules or not evidence_ids <= allowed_evidence:
            raise ValueError("proposta contém regra ou evidência externa às entradas promovidas")
        covered.update(rule_ids)
    if covered != allowed_rules:
        raise ValueError("proposta não cobre exatamente as regras promovidas")
    return covered


def evidence_for_attributes(relation: dict[str, Any], attribute_ids: list[str]) -> list[str]:
    wanted = set(attribute_ids)
    values: list[str] = []
    for attribute in relation["attributes"]:
        if attribute["id"] in wanted:
            values.extend(attribute.get("evidence_ref_ids", []))
    return ordered_unique(values)


def relation_context(
    relation: dict[str, Any], concepts: set[str]
) -> tuple[list[str], list[str]]:
    entity_ids = relation.get("conceptual_entity_ids", [])
    return [item for item in entity_ids if item in concepts], list(entity_ids)


def build_artifact(
    state: dict[str, Any], manifest: dict[str, Any], semantic: dict[str, Any],
    conceptual: dict[str, Any], logical: dict[str, Any], dictionary: dict[str, Any],
    input_hashes: list[str],
) -> tuple[dict[str, Any], dict[str, int]]:
    rules = {item["id"]: item for item in semantic["rules"]}
    concepts = {item["id"] for item in semantic["concepts"]}
    entities = {item["id"]: item for item in conceptual["entities"]}
    relationships = conceptual["relationships"]
    relations = {item["id"]: item for item in logical["relations"]}
    tables = {item["relation_id"]: item for item in dictionary["tables"]}
    evidence = {item["id"]: item for item in manifest["evidence_refs"]}

    traces: list[dict[str, Any]] = []
    rule_trace_ids: dict[str, list[str]] = {rule_id: [] for rule_id in rules}

    for rule_id, rule in rules.items():
        subject_ids = [item for item in rule.get("subject_ids", []) if item in concepts]
        entity_ids = [
            entity_id for entity_id, entity in entities.items()
            if entity_id in subject_ids or entity.get("concept_id") in subject_ids or rule_id in entity.get("rule_ids", [])
        ]
        relationship_ids = [
            item["id"] for item in relationships if rule_id in item.get("rule_ids", [])
        ]
        matches: list[tuple[str, list[str]]] = []
        for relation_id, relation in relations.items():
            attribute_ids = [
                item["id"] for item in relation["attributes"]
                if rule_id in item.get("rule_ids", []) or item.get("derivation_rule_id") == rule_id
            ]
            has_check = any(rule_id in item.get("rule_ids", []) for item in relation.get("checks", []))
            if attribute_ids or has_check or rule_id in relation.get("retention_rule_ids", []):
                matches.append((relation_id, attribute_ids))
        if not matches:
            matches = [("", [])]

        for relation_id, attribute_ids in matches:
            trace_id = f"TRACE_{rule_id}_{relation_id or 'SEM_MAPEAMENTO'}"
            physical_ids: list[str] = []
            logical_ids: list[str] = []
            if relation_id:
                logical_ids = [relation_id]
                physical_ids.append(f"TABLE_{relation_id}")
                physical_ids.extend(f"COLUMN_{relation_id}_{item}" for item in attribute_ids)
            trace = {
                "id": trace_id,
                "evidence_ref_ids": list(rule.get("evidence_ref_ids", [])),
                "concept_ids": subject_ids,
                "rule_ids": [rule_id],
                "conceptual_entity_ids": entity_ids,
                "relationship_ids": relationship_ids,
                "logical_relation_ids": logical_ids,
                "attribute_ids": attribute_ids,
                "physical_object_ids": physical_ids,
                "permission_requirement_ids": [],
                "test_ids": list(rule.get("verification_test_ids", [])),
                "implementation_status": "CANDIDATO" if relation_id else "NAO_INICIADO",
                "verification_status": "NAO_EXECUTADO",
                "verification_evidence_ids": [],
            }
            traces.append(trace)
            rule_trace_ids[rule_id].append(trace_id)

    constraint_test_number = 1
    constraint_trace_ids: list[str] = []
    tests_without_rule: list[str] = []

    def add_constraint_trace(
        constraint_id: str, relation_id: str, attribute_ids: list[str], rule_ids: list[str],
        relationship_ids: list[str], evidence_ids: list[str]
    ) -> None:
        nonlocal constraint_test_number
        relation = relations[relation_id]
        concept_ids, entity_ids = relation_context(relation, concepts)
        test_id = f"TEST_PARTIDAS_SCOUT_{constraint_test_number:03d}"
        constraint_test_number += 1
        trace_id = f"TRACE_{constraint_id}"
        trace = {
            "id": trace_id,
            "evidence_ref_ids": ordered_unique(evidence_ids),
            "concept_ids": concept_ids,
            "rule_ids": list(rule_ids),
            "conceptual_entity_ids": entity_ids,
            "relationship_ids": list(relationship_ids),
            "logical_relation_ids": [relation_id],
            "attribute_ids": list(attribute_ids),
            "physical_object_ids": [f"TABLE_{relation_id}", f"CONSTRAINT_{constraint_id}"],
            "permission_requirement_ids": [],
            "test_ids": [test_id],
            "implementation_status": "CANDIDATO",
            "verification_status": "NAO_EXECUTADO",
            "verification_evidence_ids": [],
        }
        traces.append(trace)
        constraint_trace_ids.append(trace_id)
        if not rule_ids:
            tests_without_rule.append(test_id)

    for foreign_key in logical["foreign_keys"]:
        relation_id = foreign_key["from_relation_id"]
        attribute_ids = foreign_key["from_attribute_ids"]
        add_constraint_trace(
            foreign_key["id"], relation_id, attribute_ids, foreign_key.get("rule_ids", []),
            [foreign_key["relationship_id"]], evidence_for_attributes(relations[relation_id], attribute_ids),
        )

    for relation_id, relation in relations.items():
        for unique in relation.get("unique_constraints", []):
            attribute_ids = unique["attribute_ids"]
            add_constraint_trace(
                unique["id"], relation_id, attribute_ids, unique.get("rule_ids", []), [],
                evidence_for_attributes(relation, attribute_ids),
            )
        for check in relation.get("checks", []):
            rule_ids = check.get("rule_ids", [])
            evidence_ids: list[str] = []
            for rule_id in rule_ids:
                evidence_ids.extend(rules[rule_id].get("evidence_ref_ids", []))
            add_constraint_trace(check["id"], relation_id, [], rule_ids, [], evidence_ids)

    used_evidence = {item for trace in traces for item in trace["evidence_ref_ids"]}
    used_source_ids = {evidence[item]["source_id"] for item in used_evidence}
    source_ids = [item["id"] for item in manifest["sources"]]
    rules_without_source = [item for item, rule in rules.items() if not rule.get("evidence_ref_ids")]
    entities_without_rules = [item for item, entity in entities.items() if not entity.get("rule_ids")]
    unresolved = [item for ids in rule_trace_ids.values() for item in ids if not next(t for t in traces if t["id"] == item)["logical_relation_ids"]]
    unresolved.extend(trace["id"] for trace in traces if trace["test_ids"] and not trace["rule_ids"])

    access_pending = [
        relation_id for relation_id, table in tables.items()
        if table["access_classification"] in {"INTERNO", "RESTRITO", "PESSOAL", "SENSIVEL"}
    ]
    issues = [dict(item) for item in dictionary["open_issues"]]
    issues.append({
        "id": "ISSUE_REQUISITOS_ACESSO_STAGE_06",
        "status": "ABERTA",
        "question": "Quais IDs de requisitos de permissão serão aprovados para as relações não públicas?",
        "affected_ids": access_pending,
        "impact": "permission_requirement_ids permanece vazio até a geração e aprovação do estágio 06.",
        "required_evidence": "Artefato ACCESS_REQUIREMENTS promovido no estágio 06.",
        "owner": "OPERADOR",
    })
    constraints_without_rules = [
        trace["id"].removeprefix("TRACE_") for trace in traces
        if trace["id"] in constraint_trace_ids and not trace["rule_ids"]
    ]
    if constraints_without_rules:
        issues.append({
            "id": "ISSUE_CONSTRAINTS_SEM_REGRA_SEMANTICA",
            "status": "ABERTA",
            "question": "Quais regras semânticas justificam as restrições lógicas que hoje possuem apenas origem estrutural?",
            "affected_ids": constraints_without_rules,
            "impact": "Os testes dessas restrições permanecem identificados em tests_without_rule.",
            "required_evidence": "Regra ou decisão promovida que fundamente cada restrição estrutural afetada.",
            "owner": "OPERADOR",
        })

    input_stage_ids = ["STAGE_00", "STAGE_01", "STAGE_02", "STAGE_03", "STAGE_04"]
    artifact = {
        "schema_version": "1.1",
        "document": {
            "id": "TRACEABILITY_MATRIX",
            "artifact_kind": "TRACEABILITY_MATRIX",
            "title": "Matriz de rastreabilidade planejada",
            "version": "0.1.0",
            "status": "PROPOSTO",
            "run_id": state["run"]["id"],
            "domain_id": state["run"]["domain_id"],
            "notebook_id": state["run"]["notebook_id"],
            "generated_at": None,
            "supersedes": None,
            "input_artifacts": [
                {
                    "document_id": artifact_doc["document"]["id"],
                    "version": artifact_doc["document"]["version"],
                    "sha256": artifact_hash,
                    "promoted_source_id": stage(state, stage_id)["promotion"]["promoted_source_id"],
                }
                for stage_id, artifact_doc, artifact_hash in zip(
                    input_stage_ids, [manifest, semantic, conceptual, logical, dictionary], input_hashes, strict=True
                )
            ],
        },
        "phase": "PLANNED",
        "traces": traces,
        "coverage_summary": {
            "source_rules_total": len(rules),
            "rules_with_logical_mapping": sum(any(t["logical_relation_ids"] for t in traces if rule_id in t["rule_ids"]) for rule_id in rules),
            "rules_with_physical_mapping": sum(any(t["physical_object_ids"] for t in traces if rule_id in t["rule_ids"]) for rule_id in rules),
            "material_constraints_total": len(rules) + len(constraint_trace_ids),
            "material_constraints_with_tests": len(rules) + len(constraint_trace_ids),
            "unresolved_trace_ids": ordered_unique(unresolved),
        },
        "orphan_checks": {
            "sources_without_use": [item for item in source_ids if item not in used_source_ids],
            "rules_without_source": rules_without_source,
            "entities_without_rules": entities_without_rules,
            "attributes_without_definition": [],
            "physical_objects_without_logical_origin": [],
            "tests_without_rule": tests_without_rule,
        },
        "open_issues": issues,
    }
    counts = {
        "traces": len(traces),
        "rule_traces": len(traces) - len(constraint_trace_ids),
        "constraint_traces": len(constraint_trace_ids),
        "unresolved_traces": len(artifact["coverage_summary"]["unresolved_trace_ids"]),
        "tests_without_rule": len(tests_without_rule),
        "open_issues": len(issues),
    }
    return artifact, counts


def validate(artifact: dict[str, Any], manifest: dict[str, Any], semantic: dict[str, Any], conceptual: dict[str, Any], logical: dict[str, Any]) -> None:
    evidence = {item["id"] for item in manifest["evidence_refs"]}
    concepts = {item["id"] for item in semantic["concepts"]}
    rules = {item["id"] for item in semantic["rules"]}
    entities = {item["id"] for item in conceptual["entities"]}
    relationships = {item["id"] for item in conceptual["relationships"]}
    relations = {item["id"]: item for item in logical["relations"]}
    trace_ids: set[str] = set()
    for trace in artifact["traces"]:
        if set(trace) != TRACE_FIELDS or trace["id"] in trace_ids:
            raise ValueError(f"campos ou ID inválido no traço {trace.get('id')}")
        trace_ids.add(trace["id"])
        if not set(trace["evidence_ref_ids"]) <= evidence or not set(trace["concept_ids"]) <= concepts:
            raise ValueError(f"evidência ou conceito inválido em {trace['id']}")
        if not set(trace["rule_ids"]) <= rules or not set(trace["conceptual_entity_ids"]) <= entities:
            raise ValueError(f"regra ou entidade inválida em {trace['id']}")
        if not set(trace["relationship_ids"]) <= relationships or not set(trace["logical_relation_ids"]) <= set(relations):
            raise ValueError(f"relação inválida em {trace['id']}")
        if trace["attribute_ids"]:
            if len(trace["logical_relation_ids"]) != 1:
                raise ValueError(f"atributo sem escopo único em {trace['id']}")
            relation = relations[trace["logical_relation_ids"][0]]
            allowed_attributes = {item["id"] for item in relation["attributes"]}
            if not set(trace["attribute_ids"]) <= allowed_attributes:
                raise ValueError(f"atributo inválido em {trace['id']}")
        if trace["implementation_status"] not in {"CANDIDATO", "NAO_INICIADO"}:
            raise ValueError(f"implementação indevida em {trace['id']}")
        if trace["verification_status"] != "NAO_EXECUTADO" or trace["verification_evidence_ids"]:
            raise ValueError(f"verificação indevida em {trace['id']}")
    if set(artifact["coverage_summary"]) != {
        "source_rules_total", "rules_with_logical_mapping", "rules_with_physical_mapping",
        "material_constraints_total", "material_constraints_with_tests", "unresolved_trace_ids",
    }:
        raise ValueError("resumo de cobertura divergente")
    if set(artifact["orphan_checks"]) != {
        "sources_without_use", "rules_without_source", "entities_without_rules",
        "attributes_without_definition", "physical_objects_without_logical_origin", "tests_without_rule",
    }:
        raise ValueError("verificação de órfãos divergente")
    for issue in artifact["open_issues"]:
        if set(issue) != ISSUE_FIELDS:
            raise ValueError(f"campos inválidos na pendência {issue.get('id')}")


def main() -> int:
    args = parse_args()
    state = load(args.state)
    proposal = load(args.proposal)
    manifest = load(args.manifest)
    semantic = load(args.semantic)
    conceptual = load(args.conceptual)
    logical = load(args.logical)
    dictionary = load(args.dictionary)
    covered = proposal_rule_coverage(
        proposal,
        {item["id"] for item in semantic["rules"]},
        {item["id"] for item in manifest["evidence_refs"]},
    )
    artifact, counts = build_artifact(
        state, manifest, semantic, conceptual, logical, dictionary,
        [sha256(args.manifest), sha256(args.semantic), sha256(args.conceptual), sha256(args.logical), sha256(args.dictionary)],
    )
    validate(artifact, manifest, semantic, conceptual, logical)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        yaml.dump(quote_values(artifact), Dumper=QuotedDumper, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )
    audit = {
        "status": "PASS",
        "proposal_path": str(args.proposal),
        "proposal_sha256": sha256(args.proposal),
        "accepted_proposal_evidence": {
            "covered_rule_ids": sorted(covered),
            "normalization": "RULE_AND_EVIDENCE_COVERAGE_ACCEPTED; STRUCTURE_AND_REFERENCES_REBUILT_FROM_PROMOTED_ARTIFACTS",
        },
        "output_path": str(args.output),
        "output_sha256": sha256(args.output),
        "counts": counts,
    }
    args.audit.write_text(
        yaml.dump(quote_values(audit), Dumper=QuotedDumper, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )
    print(f"OK {args.output}: {counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
