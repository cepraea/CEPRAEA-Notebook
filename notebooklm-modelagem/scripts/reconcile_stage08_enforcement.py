#!/usr/bin/env python3
"""Reconcilia a responsabilidade de enforcement exposta pelo STAGE_08."""

from __future__ import annotations

import argparse
import hashlib
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

from assemble_data_dictionary import validate_dictionary
from assemble_logical_model import validate_model
from build_source_manifest import QuotedDumper, quote_values


DIRECT_CHECK_IDS = {
    "CHK_PARTIDA_VIGENCIA_2026",
    "CHK_NUMERO_SET_VALIDO",
    "CHK_SHOOT_OUT_COMPLETUDE",
    "CHK_ELEGIBILIDADE_RANKING_CONTEXTUAL",
    "CHK_INTERVALO_VIGENCIA_PARTICIPACAO",
}

STRUCTURAL_INVARIANTS = {
    "CHK_ATLETA_SEMANTICA_GOLEIRA": {
        "trace_id": "TRACE_INV_ATLETA_SEMANTICA_GOLEIRA",
        "decision": "A posição GOLEIRA permanece valor do domínio posicional de ATLETA; não criar entidade ou função isolada.",
        "affected_relation_ids": ["ATLETA"],
    },
    "CHK_BOU_REJEICAO_INFERENCIAIS": {
        "trace_id": "TRACE_INV_BOU_REJEICAO_INFERENCIAIS",
        "decision": "A relação BOU contém somente variáveis observáveis; a ausência de campos inferenciais é verificada pela forma do schema.",
        "affected_relation_ids": ["UNIDADE_BASICA_ATAQUE_BOU"],
    },
    "CHK_REJEICAO_VARIAVEIS_INFERENCIAIS": {
        "trace_id": "TRACE_INV_OBSERVACAO_REJEICAO_INFERENCIAIS",
        "decision": "A observação primária contém somente fatos observáveis; a ausência de campos inferenciais é verificada pela forma do schema.",
        "affected_relation_ids": ["OBSERVACAO_DE_SCOUT"],
    },
}

DEFERRED_RULES = {
    "CHK_TETO_PARTICIPANTES_SUMULA": {
        "trace_id": "TRACE_RULE_TETO_PARTICIPANTES_SUMULA_DEFERRED",
        "issue_id": "ISSUE_ENFORCEMENT_TETO_PARTICIPANTES_SUMULA",
        "question": "Como representar atletas e oficiais relacionados na súmula de uma partida para aplicar os limites de 10 e 4 por equipe?",
        "affected_ids": ["PARTIDA_EQUIPE", "PARTIDA", "EQUIPE"],
        "impact": "O teto regulamentar não pode ser validado fielmente no schema físico atual.",
        "required_evidence": "Extensão aprovada do modelo com o elenco da súmula por partida e a categoria do participante.",
    },
    "CHK_PRAZO_INSCRICAO_72H": {
        "trace_id": "TRACE_RULE_PRAZO_INSCRICAO_72H_DEFERRED",
        "issue_id": "ISSUE_ENFORCEMENT_PRAZO_INSCRICAO_72H",
        "question": "Qual partida ou prazo oficial deve ser associado a cada inscrição para validar a antecedência mínima de 72 horas?",
        "affected_ids": ["EQUIPE_ATLETA_INSCRICAO", "PARTIDA"],
        "impact": "A inscrição referencia a competição, mas não contém o marco temporal específico exigido pela regra.",
        "required_evidence": "Decisão de modelagem que vincule a inscrição ao prazo oficial aplicável ou à partida correspondente.",
    },
    "CHK_PASSIVO_QUATRO_PASSES": {
        "trace_id": "TRACE_RULE_PASSIVO_QUATRO_PASSES_DEFERRED",
        "issue_id": "ISSUE_ENFORCEMENT_PASSIVO_QUATRO_PASSES",
        "question": "Como registrar o sinal de jogo passivo e a contagem de passes posteriores dentro da posse?",
        "affected_ids": ["POSSE_DE_BOLA", "EVENTO_SCOUT"],
        "impact": "Sem o sinal e a contagem observada, o limite de quatro passes não possui operandos físicos.",
        "required_evidence": "Extensão aprovada do protocolo e do modelo para sinal de passivo e passes subsequentes.",
    },
    "CHK_PROTECAO_CABECA_GOLEIRA": {
        "trace_id": "TRACE_RULE_PROTECAO_CABECA_GOLEIRA_DEFERRED",
        "issue_id": "ISSUE_ENFORCEMENT_PROTECAO_CABECA_GOLEIRA",
        "question": "Como registrar impacto na cabeça, condição de arremessador desmarcado e eventual simulação da goleira?",
        "affected_ids": ["EVENTO_SCOUT", "ATLETA"],
        "impact": "Os fatos condicionantes da sanção não existem como atributos ou eventos no modelo atual.",
        "required_evidence": "Extensão aprovada do evento de scout e do protocolo observacional com os fatos condicionantes.",
    },
    "CHK_REGRAS_EXECUCAO_TIRO_SEIS_METROS": {
        "trace_id": "TRACE_RULE_EXECUCAO_TIRO_SEIS_METROS_DEFERRED",
        "issue_id": "ISSUE_ENFORCEMENT_EXECUCAO_TIRO_SEIS_METROS",
        "question": "Como registrar execução direta, tempo de execução e distância defensiva do tiro de seis metros?",
        "affected_ids": ["EVENTO_SCOUT"],
        "impact": "A classificação do evento como tiro de seis metros não prova as três condições de execução.",
        "required_evidence": "Extensão aprovada do evento de scout ou evento especializado com os três fatos observáveis.",
    },
}

ISSUE_FIELDS = {"id", "status", "question", "affected_ids", "impact", "required_evidence", "owner"}
TRACE_FIELDS = {
    "id", "evidence_ref_ids", "concept_ids", "rule_ids", "conceptual_entity_ids", "relationship_ids",
    "logical_relation_ids", "attribute_ids", "physical_object_ids", "permission_requirement_ids", "test_ids",
    "implementation_status", "verification_status", "verification_evidence_ids",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=("logical", "dictionary", "traceability"), required=True)
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--wrapper-output", type=Path, required=True)
    parser.add_argument("--generated-at", required=True)
    parser.add_argument("--decision-source-id", required=True)
    parser.add_argument("--decision-sha256", required=True)
    parser.add_argument("--logical", type=Path)
    parser.add_argument("--logical-source-id")
    parser.add_argument("--dictionary", type=Path)
    parser.add_argument("--dictionary-source-id")
    parser.add_argument("--semantic", type=Path)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--conceptual", type=Path)
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


def decision_input(args: argparse.Namespace) -> dict[str, str]:
    return {
        "document_id": "STAGE_08_ENFORCEMENT_REVIEW",
        "version": "1.0.0",
        "sha256": args.decision_sha256,
        "promoted_source_id": args.decision_source_id,
    }


def deferred_issues() -> list[dict[str, Any]]:
    return [
        {
            "id": spec["issue_id"],
            "status": "ABERTA",
            "question": spec["question"],
            "affected_ids": spec["affected_ids"],
            "impact": spec["impact"],
            "required_evidence": spec["required_evidence"],
            "owner": "MODELISTA",
        }
        for spec in DEFERRED_RULES.values()
    ]


def build_logical(args: argparse.Namespace) -> tuple[dict[str, Any], dict[str, Any]]:
    if not all((args.semantic, args.manifest, args.conceptual)):
        raise ValueError("logical exige semantic, manifest e conceptual")
    artifact = deepcopy(load(args.base))
    removed: list[str] = []
    for relation in artifact["relations"]:
        kept = []
        for check in relation["checks"]:
            if check["id"] in DIRECT_CHECK_IDS:
                kept.append(check)
            else:
                removed.append(check["id"])
        relation["checks"] = kept

    expected_removed = set(STRUCTURAL_INVARIANTS) | set(DEFERRED_RULES)
    if set(removed) != expected_removed:
        raise ValueError(f"checks removidos inesperados: {sorted(set(removed) ^ expected_removed)}")

    artifact["normalization_decisions"].extend(
        [
            {
                "id": "NORM_DECISION_011",
                "affected_relation_ids": ["ATLETA", "UNIDADE_BASICA_ATAQUE_BOU", "OBSERVACAO_DE_SCOUT"],
                "decision": "Tratar semântica de goleira e rejeição de variáveis inferenciais como invariantes estruturais, não como CHECKs de linha.",
                "rationale": "As relações atuais preservam essas regras pela forma do schema; não existem operandos de linha capazes de expressá-las como predicados SQL.",
                "accepted_tradeoffs": ["A verificação será feita por teste de forma do schema e revisão do contrato, não por CHECK em cada linha."],
            },
            {
                "id": "NORM_DECISION_012",
                "affected_relation_ids": sorted({item for spec in DEFERRED_RULES.values() for item in spec["affected_ids"]}),
                "decision": "Adiar cinco regras de negócio que dependem de fatos ainda ausentes nas 32 relações autorizadas.",
                "rationale": "Criar CHECKs sem operandos físicos produziria falsa garantia de integridade; ampliar relações ou atributos excederia o escopo físico autorizado.",
                "accepted_tradeoffs": ["Essas regras permanecem abertas e fora do schema candidato até uma extensão explícita do modelo."],
            },
            {
                "id": "NORM_DECISION_013",
                "affected_relation_ids": [
                    "PARTIDA", "PERIODO_SET", "SHOOT_OUT", "PARTICIPACAO_EQUIPE_COMPETICAO"
                ],
                "decision": "Limitar os CHECKs físicos do escopo atual aos cinco predicados integralmente expressáveis pelos atributos existentes.",
                "rationale": "Vigência da partida, número do set, completude do shoot-out, elegibilidade contextual e ordem do intervalo possuem operandos locais suficientes.",
                "accepted_tradeoffs": ["Regras entre linhas continuam em UNIQUE ou EXCLUDE; regras sem fatos próprios permanecem adiadas."],
            },
        ]
    )
    existing_issue_ids = {item["id"] for item in artifact["open_issues"]}
    for issue in deferred_issues():
        if issue["id"] not in existing_issue_ids:
            artifact["open_issues"].append(issue)

    artifact["document"].update(
        {
            "version": "0.1.2",
            "status": "APROVADO",
            "generated_at": args.generated_at,
            "supersedes": "LOGICAL_MODEL@0.1.1",
            "input_artifacts": artifact["document"]["input_artifacts"] + [decision_input(args)],
        }
    )
    relation_ids = [item["id"] for item in artifact["relations"]]
    if len(relation_ids) != 32 or len(relation_ids) != len(set(relation_ids)):
        raise ValueError("cobertura ou identidade das relações foi alterada")
    if sum(len(item["attributes"]) for item in artifact["relations"]) != 204:
        raise ValueError("cobertura de atributos foi alterada")
    if len(artifact["foreign_keys"]) != 59:
        raise ValueError("cobertura de FKs foi alterada")
    resulting_checks = {check["id"] for relation in artifact["relations"] for check in relation["checks"]}
    if resulting_checks != DIRECT_CHECK_IDS:
        raise ValueError("conjunto de CHECKs declarativos divergente")
    if any(set(issue) != ISSUE_FIELDS for issue in artifact["open_issues"]):
        raise ValueError("estrutura de pendência inválida")
    semantic = load(args.semantic)
    manifest = load(args.manifest)
    conceptual = load(args.conceptual)
    validate_model(
        {key: artifact[key] for key in ("relations", "foreign_keys", "normalization_decisions", "open_issues")},
        {item["id"] for item in conceptual["entities"]},
        {item["id"] for item in conceptual["relationships"]},
        {item["id"] for item in semantic["rules"]},
        {item["id"] for item in manifest["evidence_refs"]},
    )
    audit = {
        "status": "PASS",
        "phase": "LOGICAL_MODEL_ENFORCEMENT_RECONCILIATION",
        "base": {"path": str(args.base), "sha256": sha256(args.base)},
        "decision_source_id": args.decision_source_id,
        "result": {
            "relations": len(artifact["relations"]),
            "attributes": sum(len(item["attributes"]) for item in artifact["relations"]),
            "foreign_keys": len(artifact["foreign_keys"]),
            "sql_check_candidates": len(DIRECT_CHECK_IDS),
            "structural_invariants": len(STRUCTURAL_INVARIANTS),
            "deferred_rules": len(DEFERRED_RULES),
        },
        "removed_false_check_ids": sorted(removed),
        "scope_expanded": False,
        "validation": "PASS",
    }
    return artifact, audit


def build_dictionary(args: argparse.Namespace) -> tuple[dict[str, Any], dict[str, Any]]:
    if not all((args.logical, args.logical_source_id, args.semantic, args.manifest)):
        raise ValueError("dictionary exige logical, logical-source-id, semantic e manifest")
    artifact = deepcopy(load(args.base))
    logical = load(args.logical)
    logical_relations = {item["id"]: item for item in logical["relations"]}
    for table in artifact["tables"]:
        relation = logical_relations[table["relation_id"]]
        table["unique_constraint_ids"] = [item["id"] for item in relation["unique_constraints"]]
        table["check_constraint_ids"] = [item["id"] for item in relation["checks"]]
    artifact["open_issues"] = deepcopy(logical["open_issues"])
    artifact["document"].update(
        {
            "version": "0.1.1",
            "status": "APROVADO",
            "generated_at": args.generated_at,
            "supersedes": "DATA_DICTIONARY@0.1.0",
            "input_artifacts": [
                artifact["document"]["input_artifacts"][0],
                {
                    "document_id": "LOGICAL_MODEL",
                    "version": logical["document"]["version"],
                    "sha256": sha256(args.logical),
                    "promoted_source_id": args.logical_source_id,
                },
                decision_input(args),
            ],
        }
    )
    semantic = load(args.semantic)
    manifest = load(args.manifest)
    counts = validate_dictionary(
        {key: artifact[key] for key in ("tables", "catalogs", "open_issues")},
        logical,
        {item["id"] for item in semantic["rules"]},
        {item["id"] for item in manifest["evidence_refs"]},
        artifact["document"]["domain_id"],
    )
    audit = {
        "status": "PASS",
        "phase": "DATA_DICTIONARY_ENFORCEMENT_RECONCILIATION",
        "base": {"path": str(args.base), "sha256": sha256(args.base)},
        "logical": {"path": str(args.logical), "sha256": sha256(args.logical), "source_id": args.logical_source_id},
        "result": counts,
        "preserved": ["32 tabelas", "204 colunas", "tipos PostgreSQL", "classificações de acesso", "59 índices de FK"],
        "changed": ["unique_constraint_ids", "check_constraint_ids", "open_issues", "linhagem documental"],
        "validation": "PASS",
    }
    return artifact, audit


def validate_traceability(artifact: dict[str, Any], logical: dict[str, Any]) -> None:
    relation_ids = {item["id"] for item in logical["relations"]}
    trace_ids: set[str] = set()
    for trace in artifact["traces"]:
        if set(trace) != TRACE_FIELDS or trace["id"] in trace_ids:
            raise ValueError(f"traço inválido: {trace.get('id')}")
        trace_ids.add(trace["id"])
        if not set(trace["logical_relation_ids"]) <= relation_ids:
            raise ValueError(f"relação lógica inválida em {trace['id']}")
        if trace["implementation_status"] not in {
            "NAO_INICIADO", "CANDIDATO", "IMPLEMENTADO", "BLOQUEADO", "NAO_APLICAVEL"
        }:
            raise ValueError(f"status de implementação inválido em {trace['id']}")
        if trace["verification_status"] not in {
            "NAO_EXECUTADO", "PASS", "FAIL", "BLOQUEADO", "NAO_APLICAVEL"
        }:
            raise ValueError(f"status de verificação inválido em {trace['id']}")
    if len(artifact["traces"]) != len(trace_ids):
        raise ValueError("IDs de traço duplicados")
    for issue in artifact["open_issues"]:
        if set(issue) != ISSUE_FIELDS:
            raise ValueError(f"pendência inválida: {issue.get('id')}")


def build_traceability(args: argparse.Namespace) -> tuple[dict[str, Any], dict[str, Any]]:
    if not all((args.logical, args.logical_source_id, args.dictionary, args.dictionary_source_id)):
        raise ValueError("traceability exige logical/dictionary e seus source IDs")
    artifact = deepcopy(load(args.base))
    logical = load(args.logical)
    dictionary = load(args.dictionary)
    traces = {item["id"]: item for item in artifact["traces"]}

    for old_check_id, spec in STRUCTURAL_INVARIANTS.items():
        old_trace = traces.pop(f"TRACE_{old_check_id}")
        old_trace.update(
            {
                "id": spec["trace_id"],
                "physical_object_ids": [f"TABLE_{old_trace['logical_relation_ids'][0]}"],
                "implementation_status": "CANDIDATO",
                "verification_status": "NAO_EXECUTADO",
            }
        )
        traces[old_trace["id"]] = old_trace

    for old_check_id, spec in DEFERRED_RULES.items():
        old_trace = traces.pop(f"TRACE_{old_check_id}")
        old_trace.update(
            {
                "id": spec["trace_id"],
                "physical_object_ids": [],
                "test_ids": [],
                "implementation_status": "NAO_APLICAVEL",
                "verification_status": "NAO_APLICAVEL",
            }
        )
        traces[old_trace["id"]] = old_trace

    artifact["traces"] = list(traces.values())
    artifact["open_issues"] = [
        issue for issue in artifact["open_issues"]
        if issue["id"] not in {"ISSUE_REQUISITOS_ACESSO_STAGE_06", *(item["issue_id"] for item in DEFERRED_RULES.values())}
    ]
    artifact["open_issues"].extend(deepcopy(logical["open_issues"]))
    deduped_issues = []
    seen_issues: set[str] = set()
    for issue in artifact["open_issues"]:
        if issue["id"] not in seen_issues:
            deduped_issues.append(issue)
            seen_issues.add(issue["id"])
    artifact["open_issues"] = deduped_issues

    artifact["coverage_summary"].update(
        {
            "material_constraints_total": 93,
            "material_constraints_with_tests": 93,
            "unresolved_trace_ids": [],
        }
    )
    old_inputs = {item["document_id"]: item for item in artifact["document"]["input_artifacts"]}
    artifact["document"].update(
        {
            "version": "0.1.1",
            "status": "APROVADO",
            "generated_at": args.generated_at,
            "supersedes": "TRACEABILITY_MATRIX@0.1.0",
            "input_artifacts": [
                old_inputs["SOURCE_MANIFEST"],
                old_inputs["SEMANTIC_REGISTRY"],
                old_inputs["CONCEPTUAL_MODEL"],
                {
                    "document_id": "LOGICAL_MODEL",
                    "version": logical["document"]["version"],
                    "sha256": sha256(args.logical),
                    "promoted_source_id": args.logical_source_id,
                },
                {
                    "document_id": "DATA_DICTIONARY",
                    "version": dictionary["document"]["version"],
                    "sha256": sha256(args.dictionary),
                    "promoted_source_id": args.dictionary_source_id,
                },
                decision_input(args),
            ],
        }
    )
    validate_traceability(artifact, logical)
    if any(f"CONSTRAINT_{item}" in trace["physical_object_ids"] for item in STRUCTURAL_INVARIANTS for trace in artifact["traces"]):
        raise ValueError("invariante estrutural ainda aparece como constraint")
    if any(f"CONSTRAINT_{item}" in trace["physical_object_ids"] for item in DEFERRED_RULES for trace in artifact["traces"]):
        raise ValueError("regra adiada ainda aparece como constraint")
    audit = {
        "status": "PASS",
        "phase": "TRACEABILITY_ENFORCEMENT_RECONCILIATION",
        "base": {"path": str(args.base), "sha256": sha256(args.base)},
        "logical": {"path": str(args.logical), "sha256": sha256(args.logical), "source_id": args.logical_source_id},
        "dictionary": {"path": str(args.dictionary), "sha256": sha256(args.dictionary), "source_id": args.dictionary_source_id},
        "result": {
            "traces": len(artifact["traces"]),
            "direct_sql_checks": len(DIRECT_CHECK_IDS),
            "structural_invariants": len(STRUCTURAL_INVARIANTS),
            "deferred_rules": len(DEFERRED_RULES),
            "open_issues": len(artifact["open_issues"]),
        },
        "false_physical_constraints_removed": sorted(set(STRUCTURAL_INVARIANTS) | set(DEFERRED_RULES)),
        "validation": "PASS",
    }
    return artifact, audit


def main() -> int:
    args = parse_args()
    builders = {
        "logical": build_logical,
        "dictionary": build_dictionary,
        "traceability": build_traceability,
    }
    artifact, audit = builders[args.phase](args)
    dump(args.output, artifact)
    dump(args.audit, audit)
    args.wrapper_output.parent.mkdir(parents=True, exist_ok=True)
    args.wrapper_output.write_text(
        f"# Artefato promovido — {artifact['document']['id']} v{artifact['document']['version']}\n\n"
        f"## Arquivo: `{args.output}`\n\n"
        "```yaml\n"
        + args.output.read_text(encoding="utf-8")
        + "```\n",
        encoding="utf-8",
    )
    print(f"OK {args.phase}: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
