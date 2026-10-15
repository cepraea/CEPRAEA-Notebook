#!/usr/bin/env python3
"""Executa e preserva a reconciliação cruzada do corpus verificado."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import yaml


def main() -> int:
    parser = argparse.ArgumentParser(description="Reconcilia fontes documentais via NotebookLM chat.")
    parser.add_argument("--state", required=True, type=Path)
    parser.add_argument("--prompt", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--conversation-id")
    parser.add_argument("--manifest-only", action="store_true")
    args = parser.parse_args()

    state = yaml.safe_load(args.state.read_text(encoding="utf-8"))
    notebook_id = state["run"]["notebook_id"]
    stage = next(item for item in state["stages"] if item["id"] == "STAGE_00")
    enrichment = stage["operator_assembly"]["semantic_enrichment"]
    work_source_id = enrichment["reconciliation_input"]["notebook_source_id"]
    if args.manifest_only:
        source_ids = [work_source_id]
    else:
        source_ids = [
            item["source_id"] for item in state["selected_sources"] if item["role"] != "CONTROLE"
        ]
        source_ids.append(work_source_id)
        if len(source_ids) != 27 or len(set(source_ids)) != 27:
            print("ERRO esperadas 26 fontes documentais e uma fonte de trabalho distintas", file=sys.stderr)
            return 1

    command = [
        "notebooklm",
        "ask",
        "--notebook",
        notebook_id,
        "--prompt-file",
        str(args.prompt),
        "--timeout",
        "240",
        "--json",
    ]
    if args.conversation_id:
        command.extend(("--conversation-id", args.conversation_id))
    else:
        command.extend(("--new", "--yes"))
    for source_id in source_ids:
        command.extend(("--source", source_id))

    result = subprocess.run(command, text=True, capture_output=True, timeout=300, check=False)
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()[-2000:]
        print(f"ERRO NotebookLM ({result.returncode}): {detail}", file=sys.stderr)
        return 1

    response = json.loads(result.stdout)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(response, ensure_ascii=False, indent=2) + "\n"
    args.output.write_text(serialized, encoding="utf-8")
    digest = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
    print(
        json.dumps(
            {
                "output": str(args.output),
                "sha256": digest,
                "conversation_id": response.get("conversation_id"),
                "turn_id": response.get("turn_key", {}).get("turn_id"),
                "reference_count": len(response.get("references", [])),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
