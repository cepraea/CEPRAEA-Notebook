#!/usr/bin/env python3
"""Monta e valida o candidato SEMANTIC_REGISTRY a partir de saídas preservadas."""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path
from typing import Any

import yaml


CONCEPT_FIELDS = {
    "id", "preferred_term", "canonical_name", "classification", "definition",
    "valid_context", "invalid_context", "inclusions", "exclusions", "synonyms",
    "related_concept_ids", "allowed_values", "temporality", "privacy_classification",
    "status", "evidence_ref_ids",
}
RULE_FIELDS = {
    "id", "name", "rule_type", "subject_ids", "statement", "conditions", "exceptions",
    "valid_from", "valid_to", "valid_context", "invalid_context", "implementation_targets",
    "verification_test_ids", "status", "evidence_ref_ids",
}
DECISION_FIELDS = {
    "id", "question", "alternatives", "selected_alternative", "rationale", "affected_ids",
    "risk", "status", "evidence_ref_ids",
}
CONCEPT_LIST_FIELDS = {
    "valid_context", "invalid_context", "inclusions", "exclusions", "synonyms",
    "related_concept_ids", "allowed_values", "evidence_ref_ids",
}
RULE_LIST_FIELDS = {
    "subject_ids", "conditions", "exceptions", "valid_context", "invalid_context",
    "implementation_targets", "verification_test_ids", "evidence_ref_ids",
}
CONCEPT_TYPES = {
    "PARTIDA": "ENTITY",
    "EQUIPE": "ENTITY",
    "ATLETA": "ENTITY",
    "GOLEIRA_POSICAO": "ROLE",
    "PERIODO_SET": "EVENT",
    "GOL_DE_OURO": "RULE",
    "SHOOT_OUT": "EVENT",
    "GOL_SIMPLES": "EVENT",
    "GOL_DUPLO": "EVENT",
    "SPIN_SHOT": "CATALOG",
    "IN_FLIGHT_SHOT": "CATALOG",
    "TIRO_SEIS_METROS": "EVENT",
    "EXCLUSAO_DISCIPLINAR": "EVENT",
    "DESQUALIFICACAO_SEGUNDA_EXCLUSAO": "EVENT",
    "CARTAO_AZUL_SUSPENSAO": "EVENT",
    "POSSE_DE_BOLA": "EVENT",
    "UNIDADE_BASICA_ATAQUE_BOU": "EVENT",
    "FASE_TATICA": "CATALOG",
    "SISTEMA_TATICO": "CATALOG",
    "ZONA_ANALITICA_QUADRA": "CATALOG",
    "PROTOCOLO_SCOUT": "CATALOG",
    "CONFIABILIDADE_OBSERVADOR": "INDICATOR",
    "EVENTO_SCOUT": "EVENT",
    "ANALISTA_OBSERVADOR": "ROLE",
    "TIMECODE": "VALUE_OBJECT",
    "TRECHO_OBSERVADO": "VALUE_OBJECT",
}
PRIVACY_MAP = {"DADO_PESSOAL": "PESSOAL", "USO_INTERNO": "INTERNO"}
BASE_RULE_TYPES = {
    "RN_IHF_VIGENCIA_2026": "TEMPORAL",
    "RN_SGATE_0023_PONTUACAO_FHERJ_2026": "CALCULATION",
}
ALLOWED_CONCEPT_TYPES = {
    "ENTITY", "ATTRIBUTE", "EVENT", "ROLE", "ASSOCIATION", "VALUE_OBJECT", "STATE",
    "CATALOG", "RULE", "INDICATOR", "SNAPSHOT",
}
ALLOWED_RULE_TYPES = {
    "DEFINITION", "OBLIGATION", "PROHIBITION", "PERMISSION", "CONDITION", "EXCEPTION",
    "CLASSIFICATION", "CALCULATION", "TEMPORAL",
}
ALLOWED_PRIVACY = {"PUBLICO", "INTERNO", "PESSOAL", "SENSIVEL", "RESTRITO"}
ID_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")
REQUIRED_COVERAGE = {
    "partida": ["PARTIDA"],
    "competicao": ["COMPETICAO"],
    "equipe": ["EQUIPE"],
    "atleta": ["ATLETA"],
    "papel": ["PAPEL_ESPORTIVO_OPERACIONAL"],
    "periodo_set": ["PERIODO_SET"],
    "segmento_observado": ["SEGMENTO_OBSERVADO", "TRECHO_OBSERVADO"],
    "gol_de_ouro": ["GOL_DE_OURO"],
    "shoot_out": ["SHOOT_OUT"],
    "placar": ["PLACAR_JOGO", "ESTADO_DO_PLACAR", "EVOLUCAO_DO_PLACAR", "EVENTO_DE_PONTUACAO"],
    "pontuacao": ["GOL_SIMPLES", "GOL_DUPLO", "SPIN_SHOT", "IN_FLIGHT_SHOT", "TIRO_SEIS_METROS"],
    "disciplina": ["PUNICAO_DISCIPLINAR", "EXCLUSAO_DISCIPLINAR", "CONSEQUENCIA_DISCIPLINAR"],
    "posse_e_fases": ["POSSE_DE_BOLA", "FASE_OFENSIVA", "FASE_DEFENSIVA", "SISTEMA_DEFENSIVO"],
    "observacao_tatica": ["ACAO_DA_GOLEIRA", "ZONA_ANALITICA_QUADRA", "ACAO_OBSERVADA", "RESULTADO_DA_ACAO"],
    "scout": ["EVENTO_SCOUT", "OBSERVACAO_DE_SCOUT", "PROTOCOLO_SCOUT", "VERSAO_PROTOCOLO_SCOUT"],
    "qualidade_observacao": [
        "ANALISTA_OBSERVADOR", "REVISAO_DA_OBSERVACAO", "ESTADO_DE_REVISAO", "CONFIABILIDADE_OBSERVADOR",
    ],
    "midia": ["MIDIA_VIDEO", "TIMECODE", "TRECHO_OBSERVADO"],
    "proveniencia": ["PROVENIENCIA_OBSERVACAO"],
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def listify(value: Any) -> list[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def body(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data["semantic_registry"]


def evidence_ids(manifest: dict[str, Any]) -> set[str]:
    return {item["id"] for item in manifest["evidence_refs"]}


def normalize_base_concepts(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    normalized = []
    for source in items:
        item = dict(source)
        item["classification"] = CONCEPT_TYPES[item["id"]]
        item["privacy_classification"] = PRIVACY_MAP.get(
            item["privacy_classification"], item["privacy_classification"]
        )
        for field in CONCEPT_LIST_FIELDS:
            item[field] = listify(item[field])
        normalized.append(item)
    return normalized


def normalize_base_rules(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_id = {item["id"]: item for item in items}
    normalized = []
    for rule_id, rule_type in BASE_RULE_TYPES.items():
        item = dict(by_id[rule_id])
        item["rule_type"] = rule_type
        for field in RULE_LIST_FIELDS:
            item[field] = listify(item[field])
        normalized.append(item)
    return normalized


def validate(artifact: dict[str, Any], known_evidence: set[str]) -> None:
    concepts = artifact["concepts"]
    rules = artifact["rules"]
    decisions = artifact["decisions"]
    all_items = concepts + rules + decisions + artifact["open_issues"]
    ids = [item["id"] for item in all_items]
    if len(ids) != len(set(ids)):
        raise ValueError("IDs duplicados no candidato")
    if any(not ID_RE.fullmatch(item_id) for item_id in ids):
        raise ValueError("ID fora de UPPER_SNAKE_CASE")

    for item in concepts:
        if set(item) != CONCEPT_FIELDS:
            raise ValueError(f"campos inválidos no conceito {item['id']}")
        if item["classification"] not in ALLOWED_CONCEPT_TYPES:
            raise ValueError(f"classification inválida em {item['id']}")
        if item["privacy_classification"] not in ALLOWED_PRIVACY:
            raise ValueError(f"privacy_classification inválida em {item['id']}")
        if item["status"] != "PROPOSTO":
            raise ValueError(f"status inválido em {item['id']}")
        if any(not isinstance(item[field], list) for field in CONCEPT_LIST_FIELDS):
            raise ValueError(f"campo-lista inválido em {item['id']}")

    for item in rules:
        if set(item) != RULE_FIELDS:
            raise ValueError(f"campos inválidos na regra {item['id']}")
        if item["rule_type"] not in ALLOWED_RULE_TYPES:
            raise ValueError(f"rule_type inválido em {item['id']}")
        if item["status"] != "PROPOSTO":
            raise ValueError(f"status inválido em {item['id']}")
        if any(not isinstance(item[field], list) for field in RULE_LIST_FIELDS):
            raise ValueError(f"campo-lista inválido em {item['id']}")

    for item in decisions:
        if set(item) != DECISION_FIELDS or item["status"] != "EM_REVISAO":
            raise ValueError(f"decisão inválida: {item['id']}")
        if item["selected_alternative"] is not None:
            raise ValueError(f"decisão indevidamente selecionada: {item['id']}")

    concept_ids = {item["id"] for item in concepts}
    semantic_ids = concept_ids | {item["id"] for item in rules}
    for topic, required_ids in REQUIRED_COVERAGE.items():
        if not set(required_ids) <= concept_ids:
            raise ValueError(f"cobertura incompleta em {topic}")
    if any(not item["temporality"] for item in concepts):
        raise ValueError("conceito sem temporalidade declarada")
    for item in concepts:
        if not set(item["related_concept_ids"]) <= concept_ids:
            raise ValueError(f"conceito relacionado inexistente em {item['id']}")
    for item in rules:
        if not set(item["subject_ids"]) <= concept_ids:
            raise ValueError(f"subject_id inexistente em {item['id']}")
    for item in decisions:
        if not set(item["affected_ids"]) <= semantic_ids:
            raise ValueError(f"affected_id inexistente em {item['id']}")

    for item in all_items:
        refs = item.get("evidence_ref_ids", [])
        if not isinstance(refs, list) or not set(refs) <= known_evidence:
            raise ValueError(f"evidência inexistente em {item['id']}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--supplement", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    state = yaml.safe_load(args.state.read_text(encoding="utf-8"))
    manifest = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))
    base = body(args.base)
    supplement = body(args.supplement)
    stage = next(item for item in state["stages"] if item["id"] == "STAGE_01")

    concepts = normalize_base_concepts(base["concepts"]) + supplement["concepts"]
    rules = normalize_base_rules(base["rules"]) + supplement["rules"]
    artifact = {
        "schema_version": "1.1",
        "document": {
            "id": "SEMANTIC_REGISTRY",
            "artifact_kind": "SEMANTIC_REGISTRY",
            "title": "Registro semântico e catálogo de regras",
            "version": "0.1.0",
            "status": "PROPOSTO",
            "run_id": state["run"]["id"],
            "domain_id": state["run"]["domain_id"],
            "notebook_id": state["run"]["notebook_id"],
            "generated_at": None,
            "supersedes": None,
            "input_artifacts": stage["input_artifacts"],
        },
        "concepts": concepts,
        "rules": rules,
        "decisions": base["decisions"],
        "open_issues": [
            item for item in supplement["open_issues"]
            if item["id"] == "ISSUE_LACUNA_PLACAR_SHOOTOUT_E_ETAPAS"
        ],
    }
    validate(artifact, evidence_ids(manifest))

    selected_base_rule_ids = set(BASE_RULE_TYPES)
    audit = {
        "status": "PASS",
        "inputs": {
            "manifest": {"path": str(args.manifest), "sha256": sha256(args.manifest)},
            "base": {"path": str(args.base), "sha256": sha256(args.base)},
            "supplement": {"path": str(args.supplement), "sha256": sha256(args.supplement)},
        },
        "normalization": {
            "concept_classification_by_id": CONCEPT_TYPES,
            "privacy_value_map": PRIVACY_MAP,
            "base_rule_type_by_id": BASE_RULE_TYPES,
            "scalar_fields_converted_to_single_item_lists": sorted(CONCEPT_LIST_FIELDS | RULE_LIST_FIELDS),
        },
        "selection": {
            "included_base_rule_ids": sorted(selected_base_rule_ids),
            "omitted_base_rule_ids": sorted({item["id"] for item in base["rules"]} - selected_base_rule_ids),
            "included_supplement_rule_ids": [item["id"] for item in supplement["rules"]],
            "omitted_open_issue_ids": sorted(
                {item["id"] for item in base["open_issues"] + supplement["open_issues"]}
                - {"ISSUE_LACUNA_PLACAR_SHOOTOUT_E_ETAPAS"}
            ),
        },
        "counts": {
            "concepts": len(concepts),
            "rules": len(rules),
            "decisions": len(artifact["decisions"]),
            "open_issues": len(artifact["open_issues"]),
        },
        "coverage": {
            "status": "PASS",
            "required_topics": REQUIRED_COVERAGE,
            "temporality_declared_for_all_concepts": True,
        },
    }
    args.output.write_text(yaml.safe_dump(artifact, sort_keys=False, allow_unicode=True, width=120), encoding="utf-8")
    args.audit.write_text(yaml.safe_dump(audit, sort_keys=False, allow_unicode=True, width=120), encoding="utf-8")
    print(f"OK {args.output}: {len(concepts)} conceitos, {len(rules)} regras")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
