#!/usr/bin/env python3
"""Monta o candidato do estágio 06 a partir da proposta válida em cobertura."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
from typing import Any

import yaml

from build_source_manifest import QuotedDumper, quote_values


ROLE_FIELDS = {
    "id", "name", "description", "authentication_required", "assignment_scope",
    "authorization_claim_source", "evidence_ref_ids",
}
RESOURCE_FIELDS = {
    "id", "resource_kind", "logical_relation_ids", "classification",
    "exposed_via_data_api", "owner_rule", "view_security_mode",
}
PERMISSION_FIELDS = {
    "id", "role_id", "resource_id", "operation", "effect", "grant_required",
    "row_scope", "column_scope", "conditions", "rule_ids", "evidence_ref_ids",
    "negative_test_ids", "positive_test_ids",
}
ISSUE_FIELDS = {
    "id", "status", "question", "affected_ids", "impact", "required_evidence", "owner",
}

ROLE_MAP = {
    "ROLE_ADMIN": "ROLE_ADMIN_DADOS",
    "ROLE_ANALISTA_OBSERVADOR": "ROLE_ANALISTA_SCOUT",
}

ROLE_NORMALIZATION = {
    "ROLE_ADMIN_DADOS": {
        "name": "Administrador de dados",
        "description": "Responsável pela governança dos dados e pela administração controlada de cadastros e acessos.",
        "authentication_required": True,
        "assignment_scope": "GLOBAL",
        "authorization_claim_source": "DATABASE_MEMBERSHIP",
    },
    "ROLE_TREINADOR": {
        "name": "Treinador e comissão técnica",
        "description": "Responsável técnico por dados esportivos das equipes, competições e partidas sob sua atribuição.",
        "authentication_required": True,
        "assignment_scope": "TEAM",
        "authorization_claim_source": "DATABASE_MEMBERSHIP",
    },
    "ROLE_ANALISTA_SCOUT": {
        "name": "Analista de scout",
        "description": "Responsável por coletar, codificar e revisar observações das partidas que lhe foram atribuídas.",
        "authentication_required": True,
        "assignment_scope": "MATCH",
        "authorization_claim_source": "DATABASE_MEMBERSHIP",
    },
    "ROLE_ATLETA": {
        "name": "Atleta",
        "description": "Atleta com proposta de consulta ao próprio cadastro esportivo, condicionada a vínculo de identidade confiável.",
        "authentication_required": True,
        "assignment_scope": "SELF",
        "authorization_claim_source": "DATABASE_MEMBERSHIP",
    },
    "ROLE_PUBLICO_LEITOR": {
        "name": "Leitor público",
        "description": "Acesso anônimo somente à leitura explicitamente permitida para recursos classificados como públicos.",
        "authentication_required": False,
        "assignment_scope": "GLOBAL",
        "authorization_claim_source": "NONE",
    },
}

ROLE_EVIDENCE = {
    "ROLE_ADMIN_DADOS": [],
    "ROLE_TREINADOR": [],
    "ROLE_ANALISTA_SCOUT": ["EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"],
    "ROLE_ATLETA": [],
    "ROLE_PUBLICO_LEITOR": ["EVID_SOURCE_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919_004"],
}

ROW_SCOPE_BY_ROLE = {
    "ROLE_ADMIN_DADOS": "Todas as linhas, somente enquanto houver atribuição administrativa vigente no banco.",
    "ROLE_TREINADOR": "Somente linhas vinculadas às equipes, competições e partidas atribuídas ao papel por associação vigente no banco.",
    "ROLE_ANALISTA_SCOUT": "Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.",
    "ROLE_ATLETA": "Somente a linha da própria atleta, após existir vínculo confiável entre identidade autenticada e atleta.",
    "ROLE_PUBLICO_LEITOR": "Somente linhas do recurso cuja publicação para leitura pública tenha sido autorizada.",
}

CONDITIONS_BY_ROLE = {
    "ROLE_ADMIN_DADOS": ["ATRIBUICAO_ADMINISTRATIVA_VIGENTE_NO_BANCO"],
    "ROLE_TREINADOR": ["VINCULO_DE_EQUIPE_VIGENTE_NO_BANCO"],
    "ROLE_ANALISTA_SCOUT": ["ATRIBUICAO_DE_PARTIDA_VIGENTE_NO_BANCO"],
    "ROLE_ATLETA": ["VINCULO_IDENTIDADE_ATLETA_PENDENTE_DE_DECISAO"],
    "ROLE_PUBLICO_LEITOR": ["PUBLICACAO_EXPLICITA_DO_RECURSO"],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", type=Path, required=True)
    parser.add_argument("--proposal", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--semantic", type=Path, required=True)
    parser.add_argument("--conceptual", type=Path, required=True)
    parser.add_argument("--logical", type=Path, required=True)
    parser.add_argument("--dictionary", type=Path, required=True)
    parser.add_argument("--traceability", type=Path, required=True)
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


def stage(state: dict[str, Any], stage_id: str) -> dict[str, Any]:
    return next(item for item in state["stages"] if item["id"] == stage_id)


def dump(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.dump(
            quote_values(value), Dumper=QuotedDumper, sort_keys=False,
            allow_unicode=True, width=120,
        ),
        encoding="utf-8",
    )


def build(args: argparse.Namespace) -> tuple[dict[str, Any], dict[str, int]]:
    state = load(args.state)
    proposal = load(args.proposal)
    manifest = load(args.manifest)
    semantic = load(args.semantic)
    conceptual = load(args.conceptual)
    logical = load(args.logical)
    dictionary = load(args.dictionary)
    traceability = load(args.traceability)

    if set(proposal) != {"roles", "resources", "permissions", "default_policy", "open_issues"}:
        raise ValueError("raízes inesperadas na proposta aceita")

    evidence_ids = {item["id"] for item in manifest["evidence_refs"]}
    rule_ids = {item["id"] for item in semantic["rules"]}
    relation_ids = {item["id"] for item in logical["relations"]}
    class_by_relation = {
        item["relation_id"]: item["access_classification"] for item in dictionary["tables"]
    }
    attributes_by_relation = {
        item["id"]: [attribute["id"] for attribute in item["attributes"]]
        for item in logical["relations"]
    }

    proposed_relations = {
        relation_id
        for resource in proposal["resources"]
        for relation_id in resource["logical_relation_ids"]
    }
    if proposed_relations != relation_ids or len(proposal["resources"]) != len(relation_ids) != 32:
        raise ValueError("a proposta aceita não cobre exatamente as 32 relações promovidas")
    for resource in proposal["resources"]:
        relation_id = resource["logical_relation_ids"][0]
        if resource["classification"] != class_by_relation[relation_id]:
            raise ValueError(f"classificação divergente em {relation_id}")

    roles = [
        {
            "id": role_id,
            **fields,
            "evidence_ref_ids": [item for item in ROLE_EVIDENCE[role_id] if item in evidence_ids],
        }
        for role_id, fields in ROLE_NORMALIZATION.items()
    ]

    resources = []
    relation_by_resource: dict[str, str] = {}
    for proposed in proposal["resources"]:
        relation_id = proposed["logical_relation_ids"][0]
        classification = class_by_relation[relation_id]
        if classification == "PUBLICO":
            owner_rule = "Leitura pública somente por permissão explícita; mutações exigem papel autorizado e escopo atribuído no banco."
        elif classification == "INTERNO":
            owner_rule = "Acesso limitado às equipes, competições ou partidas associadas ao papel por vínculo vigente no banco."
        else:
            owner_rule = "Acesso mínimo por finalidade, escopo atribuído e colunas necessárias; nenhuma leitura pública."
        resource = {
            "id": proposed["id"],
            "resource_kind": "TABLE",
            "logical_relation_ids": [relation_id],
            "classification": classification,
            "exposed_via_data_api": proposed["exposed_via_data_api"] if classification != "RESTRITO" else False,
            "owner_rule": owner_rule,
            "view_security_mode": "NOT_APPLICABLE",
        }
        resources.append(resource)
        relation_by_resource[resource["id"]] = relation_id

    permissions = []
    for proposed in proposal["permissions"]:
        role_id = ROLE_MAP.get(proposed["role_id"], proposed["role_id"])
        resource_id = proposed["resource_id"]
        relation_id = relation_by_resource[resource_id]
        column_scope = list(proposed["column_scope"])
        if class_by_relation[relation_id] == "RESTRITO":
            column_scope = attributes_by_relation[relation_id]
            if role_id == "ROLE_ATLETA" and relation_id == "ATLETA":
                column_scope = ["ID", "NOME_COMPLETO", "NOME_CAMISA", "POSICAO_PRINCIPAL"]
        permissions.append({
            "id": proposed["id"],
            "role_id": role_id,
            "resource_id": resource_id,
            "operation": proposed["operation"],
            "effect": "ALLOW",
            "grant_required": True,
            "row_scope": ROW_SCOPE_BY_ROLE[role_id],
            "column_scope": column_scope,
            "conditions": CONDITIONS_BY_ROLE[role_id],
            "rule_ids": [item for item in proposed["rule_ids"] if item in rule_ids],
            "evidence_ref_ids": [item for item in proposed["evidence_ref_ids"] if item in evidence_ids],
            "negative_test_ids": list(proposed["negative_test_ids"]),
            "positive_test_ids": list(proposed["positive_test_ids"]),
        })

    issues = [
        {
            "id": "ISSUE_VINCULO_IDENTIDADE_ATLETA",
            "status": "BLOQUEANTE",
            "question": "Qual relação confiável vinculará a identidade autenticada ao registro ATLETA para aplicar o escopo SELF?",
            "affected_ids": ["ROLE_ATLETA", "ATLETA", "PERM_047"],
            "impact": "A permissão de autoconsulta da atleta não pode ser implementada com isolamento seguro sem esse vínculo.",
            "required_evidence": "Decisão de arquitetura e modelo promovido para identidade e associação de conta.",
            "owner": "OPERADOR",
        },
        {
            "id": "ISSUE_GOVERNANCA_ATRIBUICAO_PAPEIS",
            "status": "ABERTA",
            "question": "Quem pode atribuir, revogar e auditar cada papel e seu escopo temporal?",
            "affected_ids": [item["id"] for item in roles],
            "impact": "Sem governança de atribuição, DATABASE_MEMBERSHIP não define um processo autorizativo completo.",
            "required_evidence": "Decisão aprovada de administração de papéis, segregação de funções e trilha de auditoria.",
            "owner": "OPERADOR",
        },
        {
            "id": "ISSUE_SEPARACAO_ANALISTA_REVISOR",
            "status": "ABERTA",
            "question": "A revisão de scout deve exigir pessoa diferente daquela que registrou a observação?",
            "affected_ids": ["ROLE_ANALISTA_SCOUT", "REVISAO_DA_OBSERVACAO", "ESTADO_DE_REVISAO"],
            "impact": "A resposta define se haverá papel revisor separado e impedimento de autorrevisão.",
            "required_evidence": "Decisão metodológica sobre independência da revisão e confiabilidade da observação.",
            "owner": "OPERADOR",
        },
        {
            "id": "ISSUE_EXPOSICAO_DATA_API_NAO_PUBLICA",
            "status": "ABERTA",
            "question": "Quais recursos INTERNO realmente precisam de acesso direto pela Data API?",
            "affected_ids": [item["id"] for item in resources if item["classification"] == "INTERNO"],
            "impact": "Exposição desnecessária aumenta a superfície de ataque mesmo quando grants e escopo de linha são planejados.",
            "required_evidence": "Inventário de fluxos do aplicativo e decisão de exposição por recurso.",
            "owner": "OPERADOR",
        },
    ]

    input_paths = [
        args.manifest, args.semantic, args.conceptual, args.logical, args.dictionary, args.traceability,
    ]
    input_stage_ids = ["STAGE_00", "STAGE_01", "STAGE_02", "STAGE_03", "STAGE_04", "STAGE_05"]
    input_documents = [manifest, semantic, conceptual, logical, dictionary, traceability]
    artifact = {
        "schema_version": "1.1",
        "document": {
            "id": "ACCESS_REQUIREMENTS",
            "artifact_kind": "ACCESS_REQUIREMENTS",
            "title": "Requisitos de acesso e matriz de permissões",
            "version": "0.1.0",
            "status": "PROPOSTO",
            "run_id": state["run"]["id"],
            "domain_id": state["run"]["domain_id"],
            "notebook_id": state["run"]["notebook_id"],
            "generated_at": None,
            "supersedes": None,
            "input_artifacts": [
                {
                    "document_id": document["document"]["id"],
                    "version": document["document"]["version"],
                    "sha256": sha256(path),
                    "promoted_source_id": stage(state, stage_id)["promotion"]["promoted_source_id"],
                }
                for stage_id, document, path in zip(input_stage_ids, input_documents, input_paths, strict=True)
            ],
        },
        "roles": roles,
        "resources": resources,
        "permissions": permissions,
        "default_policy": {
            "anonymous": "DENY",
            "authenticated_without_role": "DENY",
            "cross_tenant": "DENY",
            "privileged_service_role": "SERVER_ONLY",
            "client_authorization_from_user_metadata": "DENY",
        },
        "open_issues": issues,
    }
    counts = {
        "roles": len(roles),
        "resources": len(resources),
        "permissions": len(permissions),
        "positive_tests": sum(len(item["positive_test_ids"]) for item in permissions),
        "negative_tests": sum(len(item["negative_test_ids"]) for item in permissions),
        "open_issues": len(issues),
    }
    return artifact, counts


def validate(artifact: dict[str, Any], manifest: dict[str, Any], semantic: dict[str, Any], logical: dict[str, Any], dictionary: dict[str, Any]) -> None:
    evidence_ids = {item["id"] for item in manifest["evidence_refs"]}
    rule_ids = {item["id"] for item in semantic["rules"]}
    relation_ids = {item["id"] for item in logical["relations"]}
    class_by_relation = {item["relation_id"]: item["access_classification"] for item in dictionary["tables"]}
    roles = {item["id"] for item in artifact["roles"]}
    resources = {item["id"] for item in artifact["resources"]}

    if any(set(item) != ROLE_FIELDS for item in artifact["roles"]):
        raise ValueError("campos de papel divergentes")
    if any(not set(item["evidence_ref_ids"]) <= evidence_ids for item in artifact["roles"]):
        raise ValueError("evidência inválida em papel")
    if any(set(item) != RESOURCE_FIELDS for item in artifact["resources"]):
        raise ValueError("campos de recurso divergentes")
    if any(set(item) != PERMISSION_FIELDS for item in artifact["permissions"]):
        raise ValueError("campos de permissão divergentes")
    if any(set(item) != ISSUE_FIELDS for item in artifact["open_issues"]):
        raise ValueError("campos de pendência divergentes")
    if len(roles) != len(artifact["roles"]) or len(resources) != len(artifact["resources"]):
        raise ValueError("IDs de papel ou recurso duplicados")

    covered_relations: list[str] = []
    for resource in artifact["resources"]:
        if resource["resource_kind"] != "TABLE" or resource["view_security_mode"] != "NOT_APPLICABLE":
            raise ValueError(f"tipo de recurso inválido em {resource['id']}")
        if len(resource["logical_relation_ids"]) != 1:
            raise ValueError(f"recurso sem relação lógica única: {resource['id']}")
        relation_id = resource["logical_relation_ids"][0]
        covered_relations.append(relation_id)
        if relation_id not in relation_ids or resource["classification"] != class_by_relation[relation_id]:
            raise ValueError(f"relação ou classificação inválida em {resource['id']}")
    if set(covered_relations) != relation_ids or len(covered_relations) != len(relation_ids):
        raise ValueError("cobertura de relações divergente")

    tests: list[str] = []
    allowed_operations = {"SELECT", "INSERT", "UPDATE", "DELETE", "EXECUTE"}
    for permission in artifact["permissions"]:
        if permission["role_id"] not in roles or permission["resource_id"] not in resources:
            raise ValueError(f"referência interna inválida em {permission['id']}")
        if permission["operation"] not in allowed_operations or permission["effect"] != "ALLOW":
            raise ValueError(f"operação ou efeito inválido em {permission['id']}")
        if not permission["positive_test_ids"] or not permission["negative_test_ids"]:
            raise ValueError(f"testes ausentes em {permission['id']}")
        if not set(permission["rule_ids"]) <= rule_ids or not set(permission["evidence_ref_ids"]) <= evidence_ids:
            raise ValueError(f"regra ou evidência inválida em {permission['id']}")
        if any(token in permission["row_scope"].lower() for token in ("auth.", "jwt", "user_metadata", "current_user")):
            raise ValueError(f"escopo dependente de plataforma em {permission['id']}")
        tests.extend(permission["positive_test_ids"] + permission["negative_test_ids"])
    if len(tests) != len(set(tests)):
        raise ValueError("IDs de teste duplicados")
    if resources != {item["resource_id"] for item in artifact["permissions"] if item["effect"] == "ALLOW"}:
        raise ValueError("há recurso sem permissão ALLOW explícita")
    if set(artifact["default_policy"]) != {
        "anonymous", "authenticated_without_role", "cross_tenant",
        "privileged_service_role", "client_authorization_from_user_metadata",
    } or any(value not in {"DENY", "SERVER_ONLY"} for value in artifact["default_policy"].values()):
        raise ValueError("política padrão divergente")


def main() -> int:
    args = parse_args()
    artifact, counts = build(args)
    manifest = load(args.manifest)
    semantic = load(args.semantic)
    logical = load(args.logical)
    dictionary = load(args.dictionary)
    validate(artifact, manifest, semantic, logical, dictionary)
    dump(args.output, artifact)
    audit = {
        "status": "PASS",
        "accepted_proposal_path": str(args.proposal),
        "accepted_proposal_sha256": sha256(args.proposal),
        "normalization": (
            "RESOURCE_COVERAGE_AND_EVIDENCE_ACCEPTED; TEMPLATE_FIELDS_REBUILT; "
            "HISTORICAL_RELATIONS_DISCARDED; PLATFORM_SPECIFIC_ROW_SCOPES_REPLACED; "
            "UNKNOWN_RULE_IDS_REMOVED; DEFAULT_DENY_RESTORED; HUMAN_DECISIONS_EXPOSED"
        ),
        "output_path": str(args.output),
        "output_sha256": sha256(args.output),
        "counts": counts,
    }
    dump(args.audit, audit)
    print(f"OK {args.output}: {counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
