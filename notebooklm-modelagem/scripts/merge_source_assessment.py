#!/usr/bin/env python3
"""Mescla uma avaliação de chat verificada em um manifesto candidato."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

from build_source_manifest import QuotedDumper, quote_values


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Mescla enriquecimento semântico verificado.")
    parser.add_argument("manifest", type=Path)
    parser.add_argument("chat_json", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--notebook-source-id", required=True)
    parser.add_argument("--fulltext", required=True, type=Path)
    parser.add_argument("--evidence-prefix", required=True)
    parser.add_argument("--allow-partial-evidence", action="store_true")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def normalized(value: str) -> str:
    value = value.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def excerpt_fragments(excerpt: str) -> list[str]:
    ellipsis = r"\s*(?:\[\s*\.\.\.\s*\]|\(\s*\.\.\.\s*\)|\.\.\.)\s*"
    return [part.strip() for part in re.split(ellipsis, excerpt) if len(normalized(part)) >= 20]


def excerpt_is_grounded(excerpt: str, fulltext: str) -> bool:
    fragments = excerpt_fragments(excerpt)
    return bool(fragments) and all(normalized(part) in fulltext for part in fragments)


def parse_assessment_answer(answer: str) -> dict[str, Any]:
    cleaned = answer.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:yaml)?\s*", "", cleaned, count=1, flags=re.IGNORECASE)
        cleaned = re.sub(r"\s*```$", "", cleaned, count=1)
    cleaned = re.sub(r"^(\s*)`([A-Za-z_][A-Za-z0-9_]*)`(\s*:)", r"\1\2\3", cleaned, flags=re.MULTILINE)
    parsed = yaml.safe_load(cleaned)
    if not isinstance(parsed, dict):
        raise ValueError("resposta não contém um mapeamento YAML")
    return parsed


def main() -> int:
    args = parse_args()
    if args.output.exists() and not args.force:
        print(f"ERRO {args.output}: arquivo existente; use --force para sobrescrever", file=sys.stderr)
        return 1
    if not re.fullmatch(r"[A-Z][A-Z0-9_]*", args.evidence_prefix):
        print("ERRO --evidence-prefix: use UPPER_SNAKE_CASE", file=sys.stderr)
        return 1

    manifest = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))
    chat = json.loads(args.chat_json.read_text(encoding="utf-8"))
    assessment = parse_assessment_answer(chat["answer"])
    source_assessment = assessment.get("source_assessment", {})
    evidence_candidates = assessment.get("evidence_candidates", [])
    fulltext = normalized(args.fulltext.read_text(encoding="utf-8", errors="replace"))

    references = chat.get("references", [])
    foreign_reference_ids = {
        reference.get("source_id")
        for reference in references
        if reference.get("source_id") != args.notebook_source_id
    }
    if foreign_reference_ids:
        print(f"ERRO referências externas à fonte selecionada: {sorted(foreign_reference_ids)}", file=sys.stderr)
        return 1

    sources = manifest.get("sources", [])
    matches = [item for item in sources if item.get("notebook_source_id") == args.notebook_source_id]
    if len(matches) != 1:
        print(f"ERRO fonte alvo encontrada {len(matches)} vezes no manifesto", file=sys.stderr)
        return 1
    source = matches[0]

    grounded_candidates: list[dict[str, Any]] = []
    rejected_candidate_numbers: list[int] = []
    for index, candidate in enumerate(evidence_candidates, 1):
        excerpt = candidate.get("excerpt")
        if isinstance(excerpt, str) and excerpt_is_grounded(excerpt, fulltext):
            grounded_candidates.append(candidate)
        else:
            rejected_candidate_numbers.append(index)
    if rejected_candidate_numbers and not args.allow_partial_evidence:
        index = rejected_candidate_numbers[0]
        print(f"ERRO evidência {index}: excerto não localizado integralmente", file=sys.stderr)
        return 1
    if not grounded_candidates:
        print("ERRO nenhuma evidência candidata foi localizada integralmente", file=sys.stderr)
        return 1

    metadata_fields = {
        "canonical_title_proposal": "canonical_title",
        "publisher": "publisher",
        "source_revision": "source_revision",
        "publication_date": "publication_date",
        "language": "language",
        "limitations": "limitations",
    }
    for proposal_key, manifest_key in metadata_fields.items():
        value = source_assessment.get(proposal_key)
        if value is not None:
            source[manifest_key] = value

    existing_evidence_ids = {item.get("id") for item in manifest.get("evidence_refs", [])}
    new_evidence: list[dict[str, Any]] = []
    evidence_number = 0
    for candidate in grounded_candidates:
        for fragment in excerpt_fragments(candidate["excerpt"]):
            evidence_number += 1
            evidence_id = f"EVID_{args.evidence_prefix}_{evidence_number:03d}"
            if evidence_id in existing_evidence_ids:
                print(f"ERRO ID de evidência duplicado: {evidence_id}", file=sys.stderr)
                return 1
            new_evidence.append(
                {
                    "id": evidence_id,
                    "source_id": source["id"],
                    "locator": candidate.get("locator"),
                    "evidence_type": candidate.get("evidence_type"),
                    "excerpt": fragment,
                    "interpretation": candidate.get("interpretation"),
                }
            )
    manifest.setdefault("evidence_refs", []).extend(new_evidence)

    existing_issue_ids = {item.get("id") for item in manifest.get("open_issues", [])}
    for index, question in enumerate(assessment.get("open_questions", []), 1):
        issue_id = f"ISSUE_{args.evidence_prefix}_{index:03d}"
        if issue_id in existing_issue_ids:
            print(f"ERRO ID de pendência duplicado: {issue_id}", file=sys.stderr)
            return 1
        manifest.setdefault("open_issues", []).append(
            {
                "id": issue_id,
                "status": "ABERTA",
                "question": question,
                "affected_ids": [source["id"]],
                "impact": "A reconciliação semântica da fonte permanece parcial.",
                "required_evidence": "Resposta documentada com localização na fonte pertinente.",
                "owner": "OPERADOR",
            }
        )

    if rejected_candidate_numbers:
        issue_id = f"ISSUE_{args.evidence_prefix}_UNGROUNDED_EVIDENCE"
        if issue_id in existing_issue_ids:
            print(f"ERRO ID de pendência duplicado: {issue_id}", file=sys.stderr)
            return 1
        manifest.setdefault("open_issues", []).append(
            {
                "id": issue_id,
                "status": "ABERTA",
                "question": "Quais trechos contínuos sustentam os candidatos de evidência descartados?",
                "affected_ids": [source["id"]],
                "impact": "Parte do enriquecimento proposto não foi incorporada por ausência de correspondência textual integral.",
                "required_evidence": f"Reextrair os candidatos {rejected_candidate_numbers} com excertos verbatim contínuos.",
                "owner": "OPERADOR",
            }
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        yaml.dump(quote_values(manifest), Dumper=QuotedDumper, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )
    print(
        f"OK {args.output}: {len(new_evidence)} evidências verificadas; "
        f"{len(rejected_candidate_numbers)} candidatos rejeitados"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
