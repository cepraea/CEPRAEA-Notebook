#!/usr/bin/env python3
"""Monta deterministicamente o manifesto-base a partir do estado da execução."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any

import yaml


class QuotedString(str):
    pass


class QuotedDumper(yaml.SafeDumper):
    def ignore_aliases(self, _data: Any) -> bool:
        return True

    def increase_indent(self, flow: bool = False, indentless: bool = False) -> None:
        return super().increase_indent(flow, False)


def represent_string(dumper: QuotedDumper, value: QuotedString) -> yaml.ScalarNode:
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style='"')


QuotedDumper.add_representer(QuotedString, represent_string)


def quote_values(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: quote_values(child) for key, child in value.items()}
    if isinstance(value, list):
        return [quote_values(child) for child in value]
    if isinstance(value, str):
        return QuotedString(value)
    return value


def semantic_source_id(title: str, notebook_source_id: str) -> str:
    normalized = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^A-Za-z0-9]+", "_", normalized).strip("_").upper() or "SOURCE"
    suffix = hashlib.sha256(notebook_source_id.encode("utf-8")).hexdigest()[:8].upper()
    return f"SRC_{slug[:56]}_{suffix}"


def source_type(title: str) -> str:
    lowered = title.lower()
    if lowered.endswith(".pdf"):
        return "PDF"
    if lowered.endswith(".sql") or ".sql." in lowered:
        return "SQL"
    if lowered.endswith((".md", ".markdown")):
        return "MARKDOWN"
    return "OTHER"


def authority_class(role: str) -> str:
    if role == "CONTROLE":
        return "DECISAO_HUMANA"
    if role == "OPERACIONAL_PRIMARIA":
        return "OPERACIONAL_PRIMARIA"
    if role == "ARTEFATO_HISTORICO":
        return "HISTORICA"
    if role == "NORMATIVA_TRADUCAO" or role.startswith("SUPORTE_"):
        return "SUPORTE"
    if role.startswith("NORMATIVA"):
        return "AUTORITATIVA"
    return "INDETERMINADA"


def lifecycle_status(role: str) -> str:
    if role == "ARTEFATO_HISTORICO":
        return "HISTORICA"
    if role == "NORMATIVA_TRADUCAO" or role.startswith("SUPORTE_"):
        return "COMPLEMENTAR"
    return "EM_VERIFICACAO"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Monta SOURCE_MANIFEST sem delegar metadados ao modelo.")
    parser.add_argument("state", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.output.exists() and not args.force:
        print(f"ERRO {args.output}: arquivo existente; use --force para sobrescrever", file=sys.stderr)
        return 1

    state = yaml.safe_load(args.state.read_text(encoding="utf-8"))
    run = state.get("run", {})
    scope = run.get("scope", {})
    selected = state.get("selected_sources", [])
    required_run = ("id", "domain_id", "notebook_id")
    missing_run = [key for key in required_run if not run.get(key)]
    if missing_run:
        print(f"ERRO {args.state}: campos run ausentes: {', '.join(missing_run)}", file=sys.stderr)
        return 1
    if not scope.get("reference_date") or not scope.get("included") or not scope.get("excluded"):
        print(f"ERRO {args.state}: run.scope incompleto", file=sys.stderr)
        return 1
    if not selected:
        print(f"ERRO {args.state}: selected_sources vazio", file=sys.stderr)
        return 1

    sources: list[dict[str, Any]] = []
    semantic_ids: list[str] = []
    notebook_ids: list[str] = []
    for item in selected:
        notebook_source_id = item["source_id"]
        title = item["title"]
        role = item["role"]
        source_id = semantic_source_id(title, notebook_source_id)
        semantic_ids.append(source_id)
        notebook_ids.append(notebook_source_id)
        sources.append(
            {
                "id": source_id,
                "canonical_title": title,
                "notebook_source_id": notebook_source_id,
                "drive_file_id": None,
                "source_type": source_type(title),
                "publisher": None,
                "source_revision": None,
                "publication_date": None,
                "retrieved_at": None,
                "content_sha256": item.get("content_sha256"),
                "language": None,
                "authority_class": authority_class(role),
                "lifecycle_status": lifecycle_status(role),
                "notebook_status": item["readiness"],
                "valid_from": None,
                "valid_to": None,
                "supersedes_source_id": None,
                "duplicate_of_source_id": None,
                "supported_domain_ids": [run["domain_id"]],
                "limitations": [],
            }
        )

    if len(notebook_ids) != len(set(notebook_ids)):
        print(f"ERRO {args.state}: source_id duplicado em selected_sources", file=sys.stderr)
        return 1
    if len(semantic_ids) != len(set(semantic_ids)):
        print(f"ERRO {args.state}: colisão de IDs semânticos", file=sys.stderr)
        return 1

    artifact = {
        "schema_version": "1.1",
        "document": {
            "id": "SOURCE_MANIFEST",
            "artifact_kind": "SOURCE_MANIFEST",
            "title": "Manifesto de fontes",
            "version": "0.1.0",
            "status": "PROPOSTO",
            "run_id": run["id"],
            "domain_id": run["domain_id"],
            "notebook_id": run["notebook_id"],
            "generated_at": None,
            "supersedes": None,
            "input_artifacts": [],
        },
        "scope": {
            "included": scope["included"],
            "excluded": scope["excluded"],
            "reference_date": scope["reference_date"],
        },
        "sources": sources,
        "evidence_refs": [],
        "precedence_rules": [],
        "conflicts": [],
        "open_issues": [
            {
                "id": "ISSUE_SOURCE_METADATA_ENRICHMENT",
                "status": "ABERTA",
                "question": "Quais metadados documentais podem ser comprovados em cada fonte?",
                "affected_ids": semantic_ids.copy(),
                "impact": "Editora, revisão, datas, idioma, tipo nativo e limitações permanecem incompletos.",
                "required_evidence": "Metadados observáveis da fonte e análise individual rastreada.",
                "owner": "OPERADOR",
            },
            {
                "id": "ISSUE_SOURCE_SEMANTIC_RECONCILIATION",
                "status": "ABERTA",
                "question": "Quais evidências, precedências e conflitos são demonstrados pelas fontes selecionadas?",
                "affected_ids": semantic_ids.copy(),
                "impact": "O manifesto-base ainda não pode ser aprovado ou promovido.",
                "required_evidence": "Enriquecimento semântico fundamentado e revisado pelo operador.",
                "owner": "OPERADOR",
            },
        ],
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        yaml.dump(quote_values(artifact), Dumper=QuotedDumper, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )
    print(f"OK {args.output}: {len(sources)} fontes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
