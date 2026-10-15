#!/usr/bin/env python3
"""Aplica a revisão aprovada das derivações estruturais do estágio 05."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
from typing import Any

import yaml

from assemble_traceability_matrix import validate
from build_source_manifest import QuotedDumper, quote_values


CONDITIONAL_REFINEMENTS = {
    "TRACE_FK_PERIODO_SET_EQUIPE_VENCEDORA": (
        "REFINEMENT_PERIODO_SET_EQUIPE_VENCEDORA",
        "Cada período/set pode referenciar a equipe vencedora participante da mesma partida.",
    ),
    "TRACE_FK_SHOOT_OUT_EQUIPE_VENCEDORA": (
        "REFINEMENT_SHOOT_OUT_EQUIPE_VENCEDORA",
        "Cada shoot-out concluído pode referenciar a equipe vencedora participante da mesma partida.",
    ),
    "TRACE_FK_POSSE_DE_BOLA_EQUIPE": (
        "REFINEMENT_POSSE_DE_BOLA_EQUIPE_POSSUIDORA",
        "Cada posse pertence à equipe que detém a bola no contexto da partida do período/set.",
    ),
    "TRACE_FK_MIDIA_VIDEO_PARTIDA": (
        "REFINEMENT_MIDIA_VIDEO_PARTIDA",
        "Cada mídia de vídeo pode ser vinculada à partida que registra.",
    ),
    "TRACE_FK_PLACAR_JOGO_EQUIPE_VENCEDORA": (
        "REFINEMENT_PLACAR_JOGO_EQUIPE_VENCEDORA",
        "O placar consolidado pode referenciar a equipe vencedora participante da partida.",
    ),
    "TRACE_FK_EVOLUCAO_PLACAR_EVENTO_SCOUT": (
        "REFINEMENT_EVOLUCAO_PLACAR_EVENTO_SCOUT",
        "Uma alteração do placar pode ser vinculada ao evento de scout que a originou.",
    ),
    "TRACE_FK_EVOLUCAO_PLACAR_EQUIPE": (
        "REFINEMENT_EVOLUCAO_PLACAR_EQUIPE_BENEFICIADA",
        "Uma alteração do placar identifica a equipe beneficiada no contexto da partida.",
    ),
    "TRACE_UQ_PARTIDA_PAPEL_REGULAMENTAR": (
        "INV_PARTIDA_EQUIPE_PAPEL_REGULAMENTAR_UNICO",
        "Em uma partida, cada papel regulamentar de equipe ocorre no máximo uma vez.",
    ),
    "TRACE_UQ_PARTIDA_CONDICAO_MANDO": (
        "INV_PARTIDA_EQUIPE_CONDICAO_MANDO_UNICA",
        "Em uma partida, cada condição de mando ocorre no máximo uma vez.",
    ),
}

DIVERGENT_TRACE_IDS = {
    "TRACE_UQ_TRECHO_EVENTO",
    "TRACE_CHK_VIGENCIA_PARTICIPACAO",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--semantic", type=Path, required=True)
    parser.add_argument("--conceptual", type=Path, required=True)
    parser.add_argument("--logical", type=Path, required=True)
    parser.add_argument("--reviewed-at", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--review", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
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
        yaml.dump(
            quote_values(value),
            Dumper=QuotedDumper,
            sort_keys=False,
            allow_unicode=True,
            width=120,
        ),
        encoding="utf-8",
    )


def main() -> int:
    args = parse_args()
    artifact = load(args.candidate)
    manifest = load(args.manifest)
    semantic = load(args.semantic)
    conceptual = load(args.conceptual)
    logical = load(args.logical)

    unresolved = set(artifact["coverage_summary"]["unresolved_trace_ids"])
    if len(unresolved) != 79:
        raise ValueError(f"esperados 79 traços pendentes; encontrados {len(unresolved)}")
    if not set(CONDITIONAL_REFINEMENTS) <= unresolved or not DIVERGENT_TRACE_IDS <= unresolved:
        raise ValueError("conjunto esperado de condicionais ou divergentes não está presente")

    accepted_trace_ids = sorted(unresolved - set(CONDITIONAL_REFINEMENTS) - DIVERGENT_TRACE_IDS)
    accepted_foreign_keys = [item.removeprefix("TRACE_") for item in accepted_trace_ids if item.startswith("TRACE_FK_")]
    accepted_uniques = [item.removeprefix("TRACE_") for item in accepted_trace_ids if item.startswith("TRACE_UQ_")]
    accepted_checks = [item.removeprefix("TRACE_") for item in accepted_trace_ids if item.startswith("TRACE_CHK_")]
    if (len(accepted_foreign_keys), len(accepted_uniques), len(accepted_checks)) != (52, 15, 1):
        raise ValueError("classificação 52/15/1 das 68 derivações não foi preservada")

    traces = {item["id"]: item for item in artifact["traces"]}
    for trace_id in CONDITIONAL_REFINEMENTS:
        if trace_id.startswith("TRACE_FK_"):
            traces[trace_id]["relationship_ids"] = []

    removed_unique = traces.pop("TRACE_UQ_TRECHO_EVENTO")
    old_check = traces.pop("TRACE_CHK_VIGENCIA_PARTICIPACAO")
    traces["TRACE_CHK_INTERVALO_VIGENCIA_PARTICIPACAO"] = {
        **old_check,
        "id": "TRACE_CHK_INTERVALO_VIGENCIA_PARTICIPACAO",
        "relationship_ids": ["EQUIPE_PARTICIPA_COMPETICAO"],
        "attribute_ids": ["VALIDO_DESDE", "VALIDO_ATE"],
        "physical_object_ids": [
            "TABLE_PARTICIPACAO_EQUIPE_COMPETICAO",
            "CONSTRAINT_CHK_INTERVALO_VIGENCIA_PARTICIPACAO",
        ],
    }
    traces["TRACE_EXCL_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA"] = {
        **removed_unique,
        "id": "TRACE_EXCL_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA",
        "concept_ids": ["EQUIPE", "COMPETICAO"],
        "conceptual_entity_ids": ["EQUIPE", "COMPETICAO"],
        "relationship_ids": ["EQUIPE_PARTICIPA_COMPETICAO"],
        "logical_relation_ids": ["PARTICIPACAO_EQUIPE_COMPETICAO"],
        "attribute_ids": ["COMPETICAO_ID", "EQUIPE_ID", "VALIDO_DESDE", "VALIDO_ATE"],
        "physical_object_ids": [
            "TABLE_PARTICIPACAO_EQUIPE_COMPETICAO",
            "CONSTRAINT_EXCL_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA",
        ],
    }

    artifact["traces"] = list(traces.values())
    artifact["document"]["generated_at"] = args.reviewed_at
    artifact["document"]["status"] = "APROVADO"
    artifact["coverage_summary"]["unresolved_trace_ids"] = []
    artifact["open_issues"] = [
        issue for issue in artifact["open_issues"]
        if issue["id"] != "ISSUE_CONSTRAINTS_SEM_REGRA_SEMANTICA"
    ]

    review = {
        "schema_version": "1.0",
        "review_id": "STAGE_05_OPERATOR_REVIEW_001",
        "run_id": artifact["document"]["run_id"],
        "stage_id": "STAGE_05",
        "status": "APROVADO",
        "reviewed_at": args.reviewed_at,
        "base_candidate": {
            "path": str(args.candidate),
            "sha256": sha256(args.candidate),
        },
        "decision_authority": {
            "actor": "USUARIO",
            "authorization": "Registrar 68 derivações, formalizar 9 condicionais, reconciliar 2 divergentes, aprovar e promover o estágio 05.",
        },
        "summary": {
            "reviewed_total": 79,
            "accepted_structural_derivations": 68,
            "formalized_conditionals": 9,
            "reconciled_divergences": 2,
        },
        "accepted_structural_derivations": {
            "basis": "Cardinalidade, identidade e integridade referencial coerentes com o modelo lógico promovido; FKs também possuem tipos compatíveis e índice candidato.",
            "foreign_key_ids": accepted_foreign_keys,
            "unique_constraint_ids": accepted_uniques,
            "check_constraint_ids": accepted_checks,
        },
        "formalized_conditionals": [
            {
                "trace_id": trace_id,
                "constraint_id": trace_id.removeprefix("TRACE_"),
                "formalization_id": formalization_id,
                "statement": statement,
                "status": "FORMALIZADA",
                "upstream_backport_required": True,
            }
            for trace_id, (formalization_id, statement) in CONDITIONAL_REFINEMENTS.items()
        ],
        "reconciled_divergences": [
            {
                "trace_id": "TRACE_UQ_TRECHO_EVENTO",
                "decision": "REMOVER_RESTRICAO_UNIQUE",
                "reason": "A cardinalidade conceitual aprovada permite zero a muitos trechos por evento de scout.",
                "result": "Preservada a relação EVENTO_SCOUT para TRECHO_OBSERVADO em 1:N; o teste liberado foi realocado à exclusão temporal.",
                "replacement_trace_ids": ["TRACE_EXCL_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA"],
            },
            {
                "trace_id": "TRACE_CHK_VIGENCIA_PARTICIPACAO",
                "decision": "SEPARAR_VALIDACAO_DE_LINHA_E_NAO_SOBREPOSICAO",
                "reason": "CHECK valida a ordem das datas na linha, mas não impede sobreposição entre linhas no PostgreSQL.",
                "result": "Criados um CHECK de intervalo válido e uma exclusão temporal candidata para a mesma equipe e competição.",
                "replacement_trace_ids": [
                    "TRACE_CHK_INTERVALO_VIGENCIA_PARTICIPACAO",
                    "TRACE_EXCL_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA",
                ],
            },
        ],
        "diagnostic_preserved": {
            "tests_without_semantic_rule_count": len(artifact["orphan_checks"]["tests_without_rule"]),
            "reason": "A revisão do operador resolve a decisão, mas não inventa rule_ids nos artefatos semânticos já promovidos.",
        },
        "downstream_requirements": [
            {
                "requirement": "Retropropagar as 9 formalizações e as 2 reconciliações nos modelos conceitual e lógico.",
                "deadline": "ANTES_DO_STOP_GATE_FISICO",
                "status": "OBRIGATORIO",
            },
            {
                "requirement": "Implementar a não sobreposição com EXCLUDE USING gist e intervalo daterange, validando a extensão btree_gist.",
                "deadline": "ESTAGIO_FISICO_POSTGRESQL",
                "status": "PLANEJADO",
            },
        ],
    }

    validate(artifact, manifest, semantic, conceptual, logical)
    if len(artifact["traces"]) != 113 or len(artifact["open_issues"]) != 2:
        raise ValueError("contagens finais esperadas não foram preservadas")
    if len(artifact["orphan_checks"]["tests_without_rule"]) != 79:
        raise ValueError("diagnóstico de testes sem regra semântica foi alterado indevidamente")

    dump(args.output, artifact)
    dump(args.review, review)
    audit = {
        "status": "PASS",
        "review_id": review["review_id"],
        "base_candidate_sha256": sha256(args.candidate),
        "output_path": str(args.output),
        "output_sha256": sha256(args.output),
        "review_path": str(args.review),
        "review_sha256": sha256(args.review),
        "checks": {
            "reviewed_total": 79,
            "accepted_structural_derivations": len(accepted_trace_ids),
            "formalized_conditionals": len(CONDITIONAL_REFINEMENTS),
            "reconciled_divergences": len(DIVERGENT_TRACE_IDS),
            "final_traces": len(artifact["traces"]),
            "unresolved_decisions": len(artifact["coverage_summary"]["unresolved_trace_ids"]),
            "tests_without_semantic_rule": len(artifact["orphan_checks"]["tests_without_rule"]),
            "open_issues": len(artifact["open_issues"]),
        },
    }
    dump(args.audit, audit)
    print(
        "OK: 68 derivações aceitas; 9 condicionais formalizadas; "
        "2 divergências reconciliadas; 0 decisões estruturais pendentes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
