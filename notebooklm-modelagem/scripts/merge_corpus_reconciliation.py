#!/usr/bin/env python3
"""Aplica ao manifesto somente decisões de reconciliação revisadas pelo operador."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from build_source_manifest import QuotedDumper, quote_values


def main() -> int:
    parser = argparse.ArgumentParser(description="Mescla a revisão do corpus no manifesto candidato.")
    parser.add_argument("manifest", type=Path)
    parser.add_argument("review", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    if args.output.exists() and not args.force:
        print(f"ERRO {args.output}: arquivo existente; use --force para sobrescrever", file=sys.stderr)
        return 1

    manifest = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))
    review = yaml.safe_load(args.review.read_text(encoding="utf-8"))
    source_ids = {item["id"] for item in manifest["sources"]}
    evidence_ids = {item["id"] for item in manifest["evidence_refs"]}
    issue_ids = {item["id"] for item in manifest["open_issues"]}

    precedence = review.get("precedence_rules", [])
    conflicts = review.get("conflicts", [])
    resolved_issue_ids = set(review.get("resolved_open_issue_ids", []))
    for item in precedence:
        referenced_sources = {
            item["higher_authority_source_id"],
            item["lower_authority_source_id"],
        }
        if not referenced_sources <= source_ids or not set(item["evidence_ref_ids"]) <= evidence_ids:
            print(f"ERRO referências inválidas em {item['id']}", file=sys.stderr)
            return 1
    for item in conflicts:
        if not set(item["source_ids"]) <= source_ids or not set(item["evidence_ref_ids"]) <= evidence_ids:
            print(f"ERRO referências inválidas em {item['id']}", file=sys.stderr)
            return 1
    already_resolved_ids = resolved_issue_ids - issue_ids

    manifest["precedence_rules"] = precedence
    manifest["conflicts"] = conflicts
    manifest["open_issues"] = [
        item for item in manifest["open_issues"] if item["id"] not in resolved_issue_ids
    ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        yaml.dump(quote_values(manifest), Dumper=QuotedDumper, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )
    closed_now = resolved_issue_ids & issue_ids
    print(
        f"OK {args.output}: precedências={len(precedence)}; conflitos={len(conflicts)}; "
        f"pendências_encerradas_agora={len(closed_now)}; pendências_já_ausentes={len(already_resolved_ids)}; "
        f"pendências_abertas={len(manifest['open_issues'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
