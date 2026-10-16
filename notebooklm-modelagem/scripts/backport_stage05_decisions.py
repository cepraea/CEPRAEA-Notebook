#!/usr/bin/env python3
"""Retropropaga as 9 formalizações e 2 reconciliações do STAGE_05."""

from __future__ import annotations

import argparse
import hashlib
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

from assemble_conceptual_model import validate as validate_conceptual
from assemble_logical_model import validate_model
from build_source_manifest import QuotedDumper, quote_values


TRACEABILITY_SHA256 = "3e36cfb319571923d213c8527eda511bd6cba0f193e75dfbb795b94e839e66d1"
TRACEABILITY_SOURCE_ID = "5b4b8ee3-c08d-40b5-bc0d-705f68f2e0dd"

RELATIONSHIPS = [
    {
        "id": "PERIODO_SET_VENCIDO_POR_EQUIPE",
        "name": "Período Set vencido por Equipe",
        "from_entity_id": "PERIODO_SET",
        "to_entity_id": "EQUIPE",
        "meaning": "Identifica opcionalmente a equipe vencedora do período/set entre as participantes da mesma partida.",
        "cardinality": {"from_to": {"min": 0, "max": 1}, "to_from": {"min": 0, "max": "N"}},
        "relationship_attributes": [],
        "temporality": "EVENTO",
        "exclusivity_rules": ["A equipe vencedora, quando informada, deve participar da mesma partida do período/set."],
        "rule_ids": [],
        "evidence_ref_ids": ["EVID_IHF_RULES_2026_EN_002"],
    },
    {
        "id": "SHOOT_OUT_VENCIDO_POR_EQUIPE",
        "name": "Shoot-out vencido por Equipe",
        "from_entity_id": "SHOOT_OUT",
        "to_entity_id": "EQUIPE",
        "meaning": "Identifica opcionalmente a equipe vencedora quando o shoot-out estiver concluído.",
        "cardinality": {"from_to": {"min": 0, "max": 1}, "to_from": {"min": 0, "max": "N"}},
        "relationship_attributes": [],
        "temporality": "EVENTO",
        "exclusivity_rules": ["A equipe vencedora, quando informada, deve participar da partida do shoot-out."],
        "rule_ids": [],
        "evidence_ref_ids": ["EVID_IHF_RULES_2026_EN_004"],
    },
    {
        "id": "POSSE_DE_BOLA_DETIDA_POR_EQUIPE",
        "name": "Posse de Bola detida por Equipe",
        "from_entity_id": "POSSE_DE_BOLA",
        "to_entity_id": "EQUIPE",
        "meaning": "Identifica a equipe que detém a bola no contexto da partida do período/set.",
        "cardinality": {"from_to": {"min": 1, "max": 1}, "to_from": {"min": 0, "max": "N"}},
        "relationship_attributes": [],
        "temporality": "INTERVALO",
        "exclusivity_rules": ["A equipe possuidora deve participar da partida à qual pertence o período/set."],
        "rule_ids": [],
        "evidence_ref_ids": ["EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"],
    },
    {
        "id": "MIDIA_VIDEO_REGISTRA_PARTIDA",
        "name": "Mídia de Vídeo registra Partida",
        "from_entity_id": "MIDIA_VIDEO",
        "to_entity_id": "PARTIDA",
        "meaning": "Vincula opcionalmente a mídia de vídeo à partida que ela registra.",
        "cardinality": {"from_to": {"min": 0, "max": 1}, "to_from": {"min": 0, "max": "N"}},
        "relationship_attributes": [],
        "temporality": "ATEMPORAL",
        "exclusivity_rules": [],
        "rule_ids": [],
        "evidence_ref_ids": ["EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"],
    },
    {
        "id": "PLACAR_JOGO_INDICA_EQUIPE_VENCEDORA",
        "name": "Placar do Jogo indica Equipe vencedora",
        "from_entity_id": "PLACAR_JOGO",
        "to_entity_id": "EQUIPE",
        "meaning": "Identifica opcionalmente a equipe vencedora no placar consolidado concluído.",
        "cardinality": {"from_to": {"min": 0, "max": 1}, "to_from": {"min": 0, "max": "N"}},
        "relationship_attributes": [],
        "temporality": "SNAPSHOT",
        "exclusivity_rules": ["A equipe vencedora, quando informada, deve participar da partida do placar."],
        "rule_ids": [],
        "evidence_ref_ids": ["EVID_IHF_RULES_2026_EN_002"],
    },
    {
        "id": "EVOLUCAO_PLACAR_ORIGINADA_POR_EVENTO_SCOUT",
        "name": "Evolução do Placar originada por Evento Scout",
        "from_entity_id": "EVOLUCAO_DO_PLACAR",
        "to_entity_id": "EVENTO_SCOUT",
        "meaning": "Vincula opcionalmente a alteração do placar ao evento de scout que a originou.",
        "cardinality": {"from_to": {"min": 0, "max": 1}, "to_from": {"min": 0, "max": "N"}},
        "relationship_attributes": [],
        "temporality": "EVENTO",
        "exclusivity_rules": ["O evento vinculado deve pertencer à mesma partida da alteração do placar."],
        "rule_ids": [],
        "evidence_ref_ids": ["EVID_IHF_RULES_2026_EN_006"],
    },
    {
        "id": "EVOLUCAO_PLACAR_BENEFICIA_EQUIPE",
        "name": "Evolução do Placar beneficia Equipe",
        "from_entity_id": "EVOLUCAO_DO_PLACAR",
        "to_entity_id": "EQUIPE",
        "meaning": "Identifica a equipe beneficiada por cada alteração do placar.",
        "cardinality": {"from_to": {"min": 1, "max": 1}, "to_from": {"min": 0, "max": "N"}},
        "relationship_attributes": [],
        "temporality": "EVENTO",
        "exclusivity_rules": ["A equipe beneficiada deve participar da partida da alteração do placar."],
        "rule_ids": [],
        "evidence_ref_ids": ["EVID_IHF_RULES_2026_EN_006"],
    },
]

INVARIANTS = [
    {
        "id": "INV_PARTIDA_EQUIPE_PAPEL_REGULAMENTAR_UNICO",
        "statement": "Em uma partida, cada papel regulamentar de equipe ocorre no máximo uma vez.",
        "affected_entity_ids": ["PARTIDA", "EQUIPE"],
        "rule_ids": [],
        "evidence_ref_ids": [],
    },
    {
        "id": "INV_PARTIDA_EQUIPE_CONDICAO_MANDO_UNICA",
        "statement": "Em uma partida, cada condição de mando ocorre no máximo uma vez.",
        "affected_entity_ids": ["PARTIDA", "EQUIPE"],
        "rule_ids": [],
        "evidence_ref_ids": [],
    },
    {
        "id": "INV_EVENTO_SCOUT_MULTIPLOS_TRECHOS",
        "statement": "Um evento de scout pode possuir zero a muitos trechos observados; não existe unicidade por evento.",
        "affected_entity_ids": ["EVENTO_SCOUT", "TRECHO_OBSERVADO"],
        "rule_ids": [],
        "evidence_ref_ids": ["EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"],
    },
    {
        "id": "INV_INTERVALO_VIGENCIA_PARTICIPACAO_VALIDO",
        "statement": "Em cada participação, o fim da vigência deve ser nulo ou posterior ao início da vigência.",
        "affected_entity_ids": ["EQUIPE", "COMPETICAO"],
        "rule_ids": [],
        "evidence_ref_ids": [],
    },
    {
        "id": "INV_NAO_SOBREPOSICAO_VIGENCIA_PARTICIPACAO",
        "statement": "Intervalos de vigência da mesma equipe na mesma competição não podem se sobrepor.",
        "affected_entity_ids": ["EQUIPE", "COMPETICAO"],
        "rule_ids": [],
        "evidence_ref_ids": [],
    },
]

FK_RELATIONSHIP_UPDATES = {
    "FK_PERIODO_SET_EQUIPE_VENCEDORA": "PERIODO_SET_VENCIDO_POR_EQUIPE",
    "FK_SHOOT_OUT_EQUIPE_VENCEDORA": "SHOOT_OUT_VENCIDO_POR_EQUIPE",
    "FK_POSSE_DE_BOLA_EQUIPE": "POSSE_DE_BOLA_DETIDA_POR_EQUIPE",
    "FK_MIDIA_VIDEO_PARTIDA": "MIDIA_VIDEO_REGISTRA_PARTIDA",
    "FK_PLACAR_JOGO_EQUIPE_VENCEDORA": "PLACAR_JOGO_INDICA_EQUIPE_VENCEDORA",
    "FK_EVOLUCAO_PLACAR_EVENTO_SCOUT": "EVOLUCAO_PLACAR_ORIGINADA_POR_EVENTO_SCOUT",
    "FK_EVOLUCAO_PLACAR_EQUIPE": "EVOLUCAO_PLACAR_BENEFICIA_EQUIPE",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--conceptual-base", type=Path, required=True)
    parser.add_argument("--logical-base", type=Path, required=True)
    parser.add_argument("--semantic", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--traceability", type=Path, required=True)
    parser.add_argument("--review", type=Path, required=True)
    parser.add_argument("--generated-at", required=True)
    parser.add_argument("--conceptual-output", type=Path, required=True)
    parser.add_argument("--conceptual-audit", type=Path, required=True)
    parser.add_argument("--conceptual-source-id")
    parser.add_argument("--logical-output", type=Path)
    parser.add_argument("--logical-audit", type=Path)
    return parser.parse_args()


def load(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"YAML inválido: {path}")
    return value


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.dump(quote_values(value), Dumper=QuotedDumper, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )


def build_conceptual(args: argparse.Namespace, semantic: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any]:
    conceptual = deepcopy(load(args.conceptual_base))
    conceptual["document"].update(
        {
            "version": "0.1.2",
            "generated_at": args.generated_at,
            "supersedes": "CONCEPTUAL_MODEL@0.1.1",
            "input_artifacts": [
                conceptual["document"]["input_artifacts"][0],
                {
                    "document_id": "TRACEABILITY_MATRIX",
                    "version": "0.1.0",
                    "sha256": TRACEABILITY_SHA256,
                    "promoted_source_id": TRACEABILITY_SOURCE_ID,
                },
            ],
        }
    )
    existing_relationship_ids = {item["id"] for item in conceptual["relationships"]}
    existing_invariant_ids = {item["id"] for item in conceptual["domain_invariants"]}
    if existing_relationship_ids & {item["id"] for item in RELATIONSHIPS}:
        raise ValueError("relacionamento de backport já existe no modelo-base")
    if existing_invariant_ids & {item["id"] for item in INVARIANTS}:
        raise ValueError("invariante de backport já existe no modelo-base")
    conceptual["relationships"].extend(deepcopy(RELATIONSHIPS))
    conceptual["domain_invariants"].extend(deepcopy(INVARIANTS))

    relationships = {item["id"]: item for item in conceptual["relationships"]}
    partida_equipe = relationships["PARTIDA_DISPUTADA_POR_EQUIPE"]
    partida_equipe["relationship_attributes"] = ["papel_regulamentar", "condicao_mando"]
    partida_equipe["exclusivity_rules"].extend(
        [
            "Em uma partida, cada papel regulamentar de equipe ocorre no máximo uma vez.",
            "Em uma partida, cada condição de mando ocorre no máximo uma vez.",
        ]
    )
    participacao = relationships["EQUIPE_PARTICIPA_COMPETICAO"]
    participacao["exclusivity_rules"].extend(
        [
            "O fim da vigência deve ser nulo ou posterior ao início da vigência.",
            "Intervalos da mesma equipe na mesma competição não podem se sobrepor.",
        ]
    )

    validate_conceptual(
        conceptual,
        {item["id"] for item in semantic["concepts"]},
        {item["id"] for item in semantic["rules"]},
        {item["id"] for item in manifest["evidence_refs"]},
    )
    return conceptual


def build_logical(
    args: argparse.Namespace,
    conceptual: dict[str, Any],
    semantic: dict[str, Any],
    manifest: dict[str, Any],
) -> dict[str, Any]:
    if not args.conceptual_source_id or not args.logical_output or not args.logical_audit:
        raise ValueError("geração lógica exige source ID e caminhos de saída")
    logical = deepcopy(load(args.logical_base))
    logical["document"].update(
        {
            "version": "0.1.1",
            "generated_at": args.generated_at,
            "supersedes": "LOGICAL_MODEL@0.1.0",
            "input_artifacts": [
                logical["document"]["input_artifacts"][0],
                {
                    "document_id": "CONCEPTUAL_MODEL",
                    "version": "0.1.2",
                    "sha256": sha256(args.conceptual_output),
                    "promoted_source_id": args.conceptual_source_id,
                },
                {
                    "document_id": "TRACEABILITY_MATRIX",
                    "version": "0.1.0",
                    "sha256": TRACEABILITY_SHA256,
                    "promoted_source_id": TRACEABILITY_SOURCE_ID,
                },
            ],
        }
    )

    foreign_keys = {item["id"]: item for item in logical["foreign_keys"]}
    for foreign_key_id, relationship_id in FK_RELATIONSHIP_UPDATES.items():
        foreign_keys[foreign_key_id]["relationship_id"] = relationship_id

    relations = {item["id"]: item for item in logical["relations"]}
    trecho = relations["TRECHO_OBSERVADO"]
    trecho["unique_constraints"] = [
        item for item in trecho["unique_constraints"] if item["id"] != "UQ_TRECHO_EVENTO"
    ]
    participacao = relations["PARTICIPACAO_EQUIPE_COMPETICAO"]
    old_checks = [item for item in participacao["checks"] if item["id"] == "CHK_VIGENCIA_PARTICIPACAO"]
    if len(old_checks) != 1:
        raise ValueError("CHK_VIGENCIA_PARTICIPACAO ausente ou duplicado")
    participacao["checks"] = [
        item for item in participacao["checks"] if item["id"] != "CHK_VIGENCIA_PARTICIPACAO"
    ]
    participacao["checks"].append(
        {
            "id": "CHK_INTERVALO_VIGENCIA_PARTICIPACAO",
            "expression_semantics": "VALIDO_ATE deve ser nulo ou posterior a VALIDO_DESDE na mesma linha.",
            "rule_ids": [],
        }
    )
    logical["normalization_decisions"].extend(
        [
            {
                "id": "NORM_DECISION_007",
                "affected_relation_ids": [
                    "PERIODO_SET",
                    "SHOOT_OUT",
                    "POSSE_DE_BOLA",
                    "MIDIA_VIDEO",
                    "PLACAR_JOGO",
                    "EVOLUCAO_DO_PLACAR",
                    "EQUIPE",
                    "EVENTO_SCOUT",
                ],
                "decision": "Vincular sete FKs condicionais a relacionamentos conceituais específicos, preservando ator e contexto da partida.",
                "rationale": "Relacionamentos genéricos não expressavam o papel semântico de equipe vencedora, equipe possuidora, mídia da partida, evento originador e equipe beneficiada.",
                "accepted_tradeoffs": ["A integridade de pertencimento à mesma partida exigirá validação física compatível com o contexto relacional."],
            },
            {
                "id": "NORM_DECISION_008",
                "affected_relation_ids": ["PARTIDA_EQUIPE"],
                "decision": "Preservar unicidade de papel regulamentar e condição de mando no contexto de cada partida.",
                "rationale": "As duas restrições representam identidade contextual da participação de equipe na partida.",
                "accepted_tradeoffs": ["Papéis ou condições adicionais exigem revisão explícita dos respectivos domínios."],
            },
            {
                "id": "NORM_DECISION_009",
                "affected_relation_ids": ["EVENTO_SCOUT", "TRECHO_OBSERVADO"],
                "decision": "Remover UQ_TRECHO_EVENTO e preservar cardinalidade de zero a muitos trechos por evento de scout.",
                "rationale": "Um mesmo evento pode exigir múltiplos recortes audiovisuais sem duplicar o evento observado.",
                "accepted_tradeoffs": ["Consultas devem ordenar e agrupar os trechos do evento explicitamente."],
            },
            {
                "id": "NORM_DECISION_010",
                "affected_relation_ids": ["PARTICIPACAO_EQUIPE_COMPETICAO"],
                "decision": "Separar a validade interna do intervalo da regra de não sobreposição entre linhas.",
                "rationale": "CHECK valida uma linha; a não sobreposição temporal requer restrição relacional própria no PostgreSQL.",
                "accepted_tradeoffs": ["A etapa física deverá validar btree_gist antes de propor EXCLUDE USING gist."],
            },
        ]
    )

    validate_model(
        {key: logical[key] for key in ("relations", "foreign_keys", "normalization_decisions", "open_issues")},
        {item["id"] for item in conceptual["entities"]},
        {item["id"] for item in conceptual["relationships"]},
        {item["id"] for item in semantic["rules"]},
        {item["id"] for item in manifest["evidence_refs"]},
    )
    return logical


def main() -> int:
    args = parse_args()
    semantic = load(args.semantic)
    manifest = load(args.manifest)
    traceability = load(args.traceability)
    review = load(args.review)
    if sha256(args.traceability) != TRACEABILITY_SHA256 or traceability["document"]["version"] != "0.1.0":
        raise ValueError("matriz de rastreabilidade divergente da versão aprovada")
    if review.get("summary") != {
        "reviewed_total": 79,
        "accepted_structural_derivations": 68,
        "formalized_conditionals": 9,
        "reconciled_divergences": 2,
    }:
        raise ValueError("revisão do STAGE_05 divergente")

    conceptual = build_conceptual(args, semantic, manifest)
    dump(args.conceptual_output, conceptual)
    conceptual_audit = {
        "status": "PASS",
        "source_review_id": review["review_id"],
        "base_path": str(args.conceptual_base),
        "base_sha256": sha256(args.conceptual_base),
        "output_path": str(args.conceptual_output),
        "output_sha256": sha256(args.conceptual_output),
        "version": "0.1.2",
        "added_relationship_ids": [item["id"] for item in RELATIONSHIPS],
        "added_invariant_ids": [item["id"] for item in INVARIANTS],
        "formalizations_backported": 9,
        "reconciliations_backported": 2,
    }
    dump(args.conceptual_audit, conceptual_audit)

    if args.conceptual_source_id:
        logical = build_logical(args, conceptual, semantic, manifest)
        dump(args.logical_output, logical)
        logical_audit = {
            "status": "PASS",
            "source_review_id": review["review_id"],
            "base_path": str(args.logical_base),
            "base_sha256": sha256(args.logical_base),
            "conceptual_path": str(args.conceptual_output),
            "conceptual_sha256": sha256(args.conceptual_output),
            "conceptual_promoted_source_id": args.conceptual_source_id,
            "output_path": str(args.logical_output),
            "output_sha256": sha256(args.logical_output),
            "version": "0.1.1",
            "updated_foreign_key_ids": sorted(FK_RELATIONSHIP_UPDATES),
            "removed_unique_constraint_ids": ["UQ_TRECHO_EVENTO"],
            "replaced_check_constraint_ids": {
                "removed": "CHK_VIGENCIA_PARTICIPACAO",
                "added": "CHK_INTERVALO_VIGENCIA_PARTICIPACAO",
            },
            "added_normalization_decision_ids": [
                "NORM_DECISION_007",
                "NORM_DECISION_008",
                "NORM_DECISION_009",
                "NORM_DECISION_010",
            ],
            "formalizations_backported": 9,
            "reconciliations_backported": 2,
        }
        dump(args.logical_audit, logical_audit)
        print(f"OK {args.conceptual_output} e {args.logical_output}: 11 decisões retropropagadas")
    else:
        print(f"OK {args.conceptual_output}: modelo conceitual pronto para promoção")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
