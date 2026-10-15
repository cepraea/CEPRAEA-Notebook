#!/usr/bin/env python3
"""Aplica as quatro decisões aprovadas sobre o candidato do estágio 06."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
from typing import Any

import yaml

from assemble_access_requirements import validate
from build_source_manifest import QuotedDumper, quote_values


REVIEW_PERMISSION_IDS = {"PERM_029", "PERM_031", "PERM_032", "PERM_033"}
GOVERNANCE_CONDITIONS = [
    "ATRIBUICAO_NAO_AUTODECLARADA",
    "ATRIBUICAO_AUDITAVEL_COM_VIGENCIA",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--semantic", type=Path, required=True)
    parser.add_argument("--logical", type=Path, required=True)
    parser.add_argument("--dictionary", type=Path, required=True)
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


def ordered_unique(values: list[str]) -> list[str]:
    return list(dict.fromkeys(values))


def dump(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.dump(
            quote_values(value), Dumper=QuotedDumper, sort_keys=False,
            allow_unicode=True, width=120,
        ),
        encoding="utf-8",
    )


def main() -> int:
    args = parse_args()
    artifact = load(args.candidate)
    manifest = load(args.manifest)
    semantic = load(args.semantic)
    logical = load(args.logical)
    dictionary = load(args.dictionary)

    role_ids = {item["id"] for item in artifact["roles"]}
    if role_ids != {
        "ROLE_ADMIN_DADOS", "ROLE_TREINADOR", "ROLE_ANALISTA_SCOUT",
        "ROLE_ATLETA", "ROLE_PUBLICO_LEITOR",
    }:
        raise ValueError("conjunto-base de papéis inesperado")
    permission_ids = {item["id"] for item in artifact["permissions"]}
    if not REVIEW_PERMISSION_IDS <= permission_ids or "PERM_047" not in permission_ids:
        raise ValueError("permissões necessárias à revisão não foram encontradas")

    artifact["roles"] = [item for item in artifact["roles"] if item["id"] != "ROLE_ATLETA"]
    artifact["roles"].append({
        "id": "ROLE_REVISOR_SCOUT",
        "name": "Revisor de scout",
        "description": "Responsável por revisar observações de partidas às quais foi atribuído, sem revisar o próprio registro.",
        "authentication_required": True,
        "assignment_scope": "MATCH",
        "authorization_claim_source": "DATABASE_MEMBERSHIP",
        "evidence_ref_ids": [],
    })

    permissions = []
    for permission in artifact["permissions"]:
        if permission["id"] == "PERM_047":
            continue
        item = dict(permission)
        item["conditions"] = list(permission["conditions"])
        if item["id"] in REVIEW_PERMISSION_IDS:
            item["role_id"] = "ROLE_REVISOR_SCOUT"
            item["row_scope"] = "Somente linhas vinculadas às partidas atribuídas ao revisor por associação vigente no banco."
            item["conditions"] = ["ATRIBUICAO_DE_REVISAO_VIGENTE_NO_BANCO"]
            if item["resource_id"] in {"RES_REVISAO_DA_OBSERVACAO", "RES_ESTADO_DE_REVISAO"}:
                item["conditions"].append("REVISOR_DIFERENTE_DO_ANALISTA_ORIGINAL")
        if item["role_id"] != "ROLE_PUBLICO_LEITOR":
            item["conditions"] = ordered_unique(item["conditions"] + GOVERNANCE_CONDITIONS)
        permissions.append(item)
    artifact["permissions"] = permissions

    for resource in artifact["resources"]:
        resource["exposed_via_data_api"] = resource["classification"] == "PUBLICO"

    artifact["open_issues"] = []

    review = {
        "schema_version": "1.0",
        "review_id": "STAGE_06_OPERATOR_REVIEW_001",
        "run_id": artifact["document"]["run_id"],
        "stage_id": "STAGE_06",
        "status": "APROVADO",
        "reviewed_at": args.reviewed_at,
        "base_candidate": {
            "path": str(args.candidate),
            "sha256": sha256(args.candidate),
        },
        "decision_authority": {
            "actor": "USUARIO",
            "authorization": "Revisar as quatro decisões e, depois, aprovar e promover o estágio 06.",
        },
        "decisions": [
            {
                "decision_id": "DEC_ACCESS_001_DEFERIR_AUTOCONSULTA_ATLETA",
                "status": "ACEITA",
                "decision": "Excluir ROLE_ATLETA e PERM_047 do escopo aprovado até existir vínculo confiável entre conta e ATLETA.",
                "rationale": "O modelo promovido não possui associação de identidade capaz de garantir isolamento SELF.",
                "affected_ids": ["ROLE_ATLETA", "PERM_047", "ATLETA"],
            },
            {
                "decision_id": "DEC_ACCESS_002_GOVERNANCA_MEMBROS_BANCO",
                "status": "ACEITA",
                "decision": "Autorizações dependem de associação no banco, com vigência, auditoria e proibição de autoatribuição.",
                "rationale": "Metadados controláveis pelo cliente não constituem fonte confiável de autorização.",
                "affected_ids": [
                    "ROLE_ADMIN_DADOS", "ROLE_TREINADOR", "ROLE_ANALISTA_SCOUT", "ROLE_REVISOR_SCOUT",
                ],
            },
            {
                "decision_id": "DEC_ACCESS_003_SEPARAR_REVISOR_ANALISTA",
                "status": "ACEITA",
                "decision": "Criar ROLE_REVISOR_SCOUT e impedir que o autor da observação revise o próprio registro.",
                "rationale": "A separação preserva independência e confiabilidade da observação.",
                "affected_ids": sorted(REVIEW_PERMISSION_IDS | {"ROLE_REVISOR_SCOUT"}),
            },
            {
                "decision_id": "DEC_ACCESS_004_DATA_API_PUBLICA_APENAS",
                "status": "ACEITA",
                "decision": "Expor diretamente pela Data API somente os nove recursos classificados como PUBLICO.",
                "rationale": "Fechar recursos internos e restritos reduz a superfície de ataque até existir necessidade de cliente demonstrada.",
                "affected_ids": [
                    item["id"] for item in artifact["resources"] if item["classification"] != "PUBLICO"
                ],
            },
        ],
        "result": {
            "roles": len(artifact["roles"]),
            "resources": len(artifact["resources"]),
            "permissions": len(artifact["permissions"]),
            "positive_tests": sum(len(item["positive_test_ids"]) for item in artifact["permissions"]),
            "negative_tests": sum(len(item["negative_test_ids"]) for item in artifact["permissions"]),
            "data_api_exposed_resources": sum(item["exposed_via_data_api"] for item in artifact["resources"]),
            "data_api_closed_resources": sum(not item["exposed_via_data_api"] for item in artifact["resources"]),
            "open_issues": len(artifact["open_issues"]),
        },
        "downstream_requirements": [
            {
                "requirement": "Modelar vínculo único, revogável e auditável entre identidade autenticada e ATLETA antes de reintroduzir autoconsulta.",
                "deadline": "ANTES_DE_PERMISSAO_SELF_ATLETA",
                "status": "OBRIGATORIO",
            },
            {
                "requirement": "Modelar atribuições de papel e escopo com início, fim, responsável e trilha de auditoria.",
                "deadline": "ANTES_DA_IMPLEMENTACAO_RBAC_RLS",
                "status": "OBRIGATORIO",
            },
            {
                "requirement": "Implementar e testar a regra revisor diferente do analista original.",
                "deadline": "ANTES_DA_IMPLEMENTACAO_DA_REVISAO",
                "status": "OBRIGATORIO",
            },
            {
                "requirement": "Criar índices nas colunas usadas pelos escopos RLS e validar os planos das consultas.",
                "deadline": "ESTAGIO_FISICO_POSTGRESQL",
                "status": "PLANEJADO",
            },
            {
                "requirement": "Qualquer futura exposição de recurso INTERNO ou RESTRITO pela Data API exige revisão explícita deste artefato.",
                "deadline": "ANTES_DE_NOVA_EXPOSICAO_DATA_API",
                "status": "OBRIGATORIO",
            },
        ],
    }

    validate(artifact, manifest, semantic, logical, dictionary)
    final_role_ids = {item["id"] for item in artifact["roles"]}
    if final_role_ids != {
        "ROLE_ADMIN_DADOS", "ROLE_TREINADOR", "ROLE_ANALISTA_SCOUT",
        "ROLE_REVISOR_SCOUT", "ROLE_PUBLICO_LEITOR",
    }:
        raise ValueError("conjunto final de papéis divergente")
    if len(artifact["permissions"]) != 55 or artifact["open_issues"]:
        raise ValueError("contagem final de permissões ou pendências divergente")
    if sum(item["exposed_via_data_api"] for item in artifact["resources"]) != 9:
        raise ValueError("exposição final da Data API divergente")
    if any(item["role_id"] == "ROLE_ATLETA" for item in artifact["permissions"]):
        raise ValueError("permissão de atleta permaneceu no escopo aprovado")
    for permission in artifact["permissions"]:
        if permission["id"] in REVIEW_PERMISSION_IDS:
            if permission["role_id"] != "ROLE_REVISOR_SCOUT":
                raise ValueError(f"permissão de revisão não transferida: {permission['id']}")
        if permission["role_id"] != "ROLE_PUBLICO_LEITOR":
            if not set(GOVERNANCE_CONDITIONS) <= set(permission["conditions"]):
                raise ValueError(f"governança de atribuição ausente: {permission['id']}")

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
        "checks": review["result"],
    }
    dump(args.audit, audit)
    print(
        "OK: 4 decisões aplicadas; 5 papéis; 32 recursos; 55 permissões; "
        "9 recursos expostos; 23 fechados; 0 pendências"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
