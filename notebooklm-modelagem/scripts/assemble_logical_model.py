#!/usr/bin/env python3
"""Monta e valida o candidato lógico a partir do relatório do NotebookLM."""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path
from typing import Any

import yaml

from build_source_manifest import QuotedDumper, quote_values


RELATION_FIELDS = {
    "id", "logical_name", "physical_name_candidate", "conceptual_entity_ids", "purpose", "grain",
    "identity", "attributes", "candidate_keys", "unique_constraints", "checks", "history_strategy",
    "retention_rule_ids",
}
ATTRIBUTE_FIELDS = {
    "id", "logical_name", "physical_name_candidate", "semantic_type", "nullable", "null_meaning",
    "multivalued", "derived", "derivation_rule_id", "default_semantics", "domain_values", "rule_ids",
    "evidence_ref_ids",
}
FOREIGN_KEY_FIELDS = {
    "id", "from_relation_id", "from_attribute_ids", "to_relation_id", "to_attribute_ids", "required",
    "on_delete_semantics", "on_update_semantics", "relationship_id", "supporting_index_required", "rule_ids",
}
NORMALIZATION_FIELDS = {"id", "affected_relation_ids", "decision", "rationale", "accepted_tradeoffs"}
ISSUE_FIELDS = {"id", "status", "question", "affected_ids", "impact", "required_evidence", "owner"}
HISTORY_STRATEGIES = {"NONE", "VALID_TIME", "SYSTEM_TIME", "BITEMPORAL", "APPEND_ONLY", "VERSIONED_ROW"}
ISSUE_STATUSES = {"ABERTA", "BLOQUEANTE", "RESOLVIDA", "NAO_APLICAVEL"}
ID_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")
PHYSICAL_NAME_RE = re.compile(r"^[a-z][a-z0-9_]*$")
PLACEHOLDER_RE = re.compile(r"(?i)\b(TBD|TODO|a definir)\b|\.\.\.")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_report(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    marker = "logical_model:"
    if marker not in text:
        raise ValueError("raiz logical_model ausente no relatório")
    body = marker + text.split(marker, 1)[1]
    if PLACEHOLDER_RE.search(body):
        raise ValueError("placeholder proibido no relatório")
    data = yaml.safe_load(body)
    if set(data) != {"logical_model"}:
        raise ValueError("raiz inesperada no relatório")
    return data["logical_model"]


def normalize_absorbed_concept(model: dict[str, Any], conceptual_entity_ids: set[str]) -> dict[str, str]:
    athlete = next(item for item in model["relations"] if item["id"] == "ATLETA")
    before = athlete["conceptual_entity_ids"]
    if before != ["ATLETA", "GOLEIRA_POSICAO"] or "GOLEIRA_POSICAO" in conceptual_entity_ids:
        raise ValueError("representação inesperada de GOLEIRA_POSICAO em ATLETA")
    athlete["conceptual_entity_ids"] = ["ATLETA"]
    return {"relation_id": "ATLETA", "removed_non_entity_concept_id": "GOLEIRA_POSICAO"}


def validate_model(
    model: dict[str, Any],
    conceptual_entity_ids: set[str],
    conceptual_relationship_ids: set[str],
    rule_ids: set[str],
    evidence_ids: set[str],
) -> dict[str, int]:
    if set(model) != {"relations", "foreign_keys", "normalization_decisions", "open_issues"}:
        raise ValueError("seções lógicas inválidas")

    relations = model["relations"]
    foreign_keys = model["foreign_keys"]
    decisions = model["normalization_decisions"]
    issues = model["open_issues"]
    all_ids = [item["id"] for collection in (relations, foreign_keys, decisions, issues) for item in collection]
    if len(all_ids) != len(set(all_ids)) or any(not ID_RE.fullmatch(item_id) for item_id in all_ids):
        raise ValueError("IDs duplicados ou fora de UPPER_SNAKE_CASE")

    relation_by_id = {item["id"]: item for item in relations}
    covered_entities: set[str] = set()
    used_rules: set[str] = set()
    used_evidence: set[str] = set()

    for relation in relations:
        if set(relation) != RELATION_FIELDS:
            raise ValueError(f"campos inválidos na relação {relation['id']}")
        if not PHYSICAL_NAME_RE.fullmatch(relation["physical_name_candidate"]):
            raise ValueError(f"nome físico inválido em {relation['id']}")
        if set(relation["identity"]) != {"strategy", "attribute_ids"}:
            raise ValueError(f"identidade inválida em {relation['id']}")
        if relation["identity"]["strategy"] not in {"NATURAL", "SURROGATE", "COMPOSITE"}:
            raise ValueError(f"estratégia de identidade inválida em {relation['id']}")
        if relation["history_strategy"] not in HISTORY_STRATEGIES:
            raise ValueError(f"histórico inválido em {relation['id']}")
        if not set(relation["conceptual_entity_ids"]) <= conceptual_entity_ids:
            raise ValueError(f"entidade conceitual desconhecida em {relation['id']}")
        covered_entities.update(relation["conceptual_entity_ids"])

        attribute_ids = [item["id"] for item in relation["attributes"]]
        physical_names = [item["physical_name_candidate"] for item in relation["attributes"]]
        if len(attribute_ids) != len(set(attribute_ids)) or len(physical_names) != len(set(physical_names)):
            raise ValueError(f"atributos duplicados em {relation['id']}")
        attribute_id_set = set(attribute_ids)
        if not set(relation["identity"]["attribute_ids"]) <= attribute_id_set:
            raise ValueError(f"identidade referencia atributo ausente em {relation['id']}")

        for attribute in relation["attributes"]:
            if set(attribute) != ATTRIBUTE_FIELDS:
                raise ValueError(f"campos inválidos em {relation['id']}.{attribute['id']}")
            if not ID_RE.fullmatch(attribute["id"]) or not PHYSICAL_NAME_RE.fullmatch(attribute["physical_name_candidate"]):
                raise ValueError(f"identificador inválido em {relation['id']}.{attribute['id']}")
            if not isinstance(attribute["nullable"], bool) or not isinstance(attribute["multivalued"], bool) or not isinstance(attribute["derived"], bool):
                raise ValueError(f"booleano inválido em {relation['id']}.{attribute['id']}")
            if attribute["nullable"] == (attribute["null_meaning"] is None):
                raise ValueError(f"semântica de nulidade inconsistente em {relation['id']}.{attribute['id']}")
            if attribute["derived"] != (attribute["derivation_rule_id"] is not None):
                raise ValueError(f"derivação inconsistente em {relation['id']}.{attribute['id']}")
            used_rules.update(attribute["rule_ids"])
            if attribute["derivation_rule_id"]:
                used_rules.add(attribute["derivation_rule_id"])
            used_evidence.update(attribute["evidence_ref_ids"])

        for group in ("candidate_keys", "unique_constraints"):
            for constraint in relation[group]:
                if set(constraint) != {"id", "attribute_ids"} or not set(constraint["attribute_ids"]) <= attribute_id_set:
                    raise ValueError(f"{group} inválida em {relation['id']}")
        for check in relation["checks"]:
            if set(check) != {"id", "expression_semantics", "rule_ids"}:
                raise ValueError(f"check inválido em {relation['id']}")
            used_rules.update(check["rule_ids"])
        used_rules.update(relation["retention_rule_ids"])

    if covered_entities != conceptual_entity_ids:
        raise ValueError("relações não cobrem exatamente as entidades conceituais")

    covered_relationships: set[str] = set()
    for foreign_key in foreign_keys:
        if set(foreign_key) != FOREIGN_KEY_FIELDS:
            raise ValueError(f"campos inválidos na FK {foreign_key['id']}")
        source = relation_by_id.get(foreign_key["from_relation_id"])
        target = relation_by_id.get(foreign_key["to_relation_id"])
        if source is None or target is None:
            raise ValueError(f"relação ausente na FK {foreign_key['id']}")
        source_attributes = {item["id"]: item for item in source["attributes"]}
        target_attributes = {item["id"]: item for item in target["attributes"]}
        if not set(foreign_key["from_attribute_ids"]) <= set(source_attributes):
            raise ValueError(f"atributo de origem ausente na FK {foreign_key['id']}")
        if not set(foreign_key["to_attribute_ids"]) <= set(target_attributes):
            raise ValueError(f"atributo de destino ausente na FK {foreign_key['id']}")
        if len(foreign_key["from_attribute_ids"]) != len(foreign_key["to_attribute_ids"]):
            raise ValueError(f"aridade inválida na FK {foreign_key['id']}")
        nullable = [source_attributes[item]["nullable"] for item in foreign_key["from_attribute_ids"]]
        if foreign_key["required"] and any(nullable):
            raise ValueError(f"FK obrigatória usa atributo anulável em {foreign_key['id']}")
        if not foreign_key["required"] and not any(nullable):
            raise ValueError(f"FK opcional usa somente atributos não anuláveis em {foreign_key['id']}")
        if foreign_key["on_delete_semantics"] == "SET_NULL" and not all(nullable):
            raise ValueError(f"SET_NULL usa atributo não anulável em {foreign_key['id']}")
        if foreign_key["on_delete_semantics"] not in {"RESTRICT", "CASCADE", "SET_NULL", "NO_ACTION"}:
            raise ValueError(f"ON DELETE inválido em {foreign_key['id']}")
        if foreign_key["on_update_semantics"] not in {"RESTRICT", "CASCADE", "NO_ACTION"}:
            raise ValueError(f"ON UPDATE inválido em {foreign_key['id']}")
        if foreign_key["relationship_id"] not in conceptual_relationship_ids:
            raise ValueError(f"relacionamento conceitual inválido na FK {foreign_key['id']}")
        covered_relationships.add(foreign_key["relationship_id"])
        used_rules.update(foreign_key["rule_ids"])

    if covered_relationships != conceptual_relationship_ids:
        raise ValueError("FKs não cobrem exatamente os relacionamentos conceituais")
    if used_rules - rule_ids:
        raise ValueError(f"regras desconhecidas: {sorted(used_rules - rule_ids)}")
    if used_evidence - evidence_ids:
        raise ValueError(f"evidências desconhecidas: {sorted(used_evidence - evidence_ids)}")

    for decision in decisions:
        if set(decision) != NORMALIZATION_FIELDS or not set(decision["affected_relation_ids"]) <= set(relation_by_id):
            raise ValueError(f"decisão de normalização inválida: {decision.get('id')}")
    for issue in issues:
        if set(issue) != ISSUE_FIELDS or issue["status"] not in ISSUE_STATUSES:
            raise ValueError(f"pendência inválida: {issue.get('id')}")

    return {
        "relations": len(relations),
        "foreign_keys": len(foreign_keys),
        "normalization_decisions": len(decisions),
        "open_issues": len(issues),
        "covered_conceptual_entities": len(covered_entities),
        "covered_conceptual_relationships": len(covered_relationships),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", type=Path, required=True)
    parser.add_argument("--semantic", type=Path, required=True)
    parser.add_argument("--conceptual", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    state = yaml.safe_load(args.state.read_text(encoding="utf-8"))
    semantic = yaml.safe_load(args.semantic.read_text(encoding="utf-8"))
    conceptual = yaml.safe_load(args.conceptual.read_text(encoding="utf-8"))
    manifest = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))
    stage = next(item for item in state["stages"] if item["id"] == "STAGE_03")
    model = load_report(args.report)

    conceptual_entity_ids = {item["id"] for item in conceptual["entities"]}
    conceptual_relationship_ids = {item["id"] for item in conceptual["relationships"]}
    normalization = normalize_absorbed_concept(model, conceptual_entity_ids)
    counts = validate_model(
        model,
        conceptual_entity_ids,
        conceptual_relationship_ids,
        {item["id"] for item in semantic["rules"]},
        {item["id"] for item in manifest["evidence_refs"]},
    )

    artifact = {
        "schema_version": "1.1",
        "document": {
            "id": "LOGICAL_MODEL",
            "artifact_kind": "LOGICAL_MODEL",
            "title": "Modelo lógico relacional",
            "version": "0.1.0",
            "status": "PROPOSTO",
            "run_id": state["run"]["id"],
            "domain_id": state["run"]["domain_id"],
            "notebook_id": state["run"]["notebook_id"],
            "generated_at": None,
            "supersedes": None,
            "input_artifacts": stage["input_artifacts"],
        },
        **model,
    }
    audit = {
        "status": "PASS",
        "inputs": {
            "notebook_report": {"path": str(args.report), "sha256": sha256(args.report)},
            "semantic_registry": {"path": str(args.semantic), "sha256": sha256(args.semantic)},
            "conceptual_model": {"path": str(args.conceptual), "sha256": sha256(args.conceptual)},
            "source_manifest": {"path": str(args.manifest), "sha256": sha256(args.manifest)},
        },
        "normalization": {
            "removed_markdown_heading": True,
            "absorbed_concept_reference": normalization,
            "semantic_content_added": False,
        },
        "coverage": {
            "conceptual_entities": f"{counts['covered_conceptual_entities']}/{len(conceptual_entity_ids)}",
            "conceptual_relationships": f"{counts['covered_conceptual_relationships']}/{len(conceptual_relationship_ids)}",
        },
        "validator_compatibility": {
            "generic_validate_yaml": "NOT_APPLICABLE",
            "reason": "IDs de atributos são locais à relação; o validador genérico exige unicidade global para toda chave id.",
            "specialized_validation": "PASS",
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
        f"OK {args.output}: {counts['relations']} relações, {counts['foreign_keys']} FKs, "
        f"{counts['covered_conceptual_relationships']} relacionamentos cobertos"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
