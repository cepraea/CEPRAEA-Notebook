#!/usr/bin/env python3
"""Executa chat de uma etapa com fontes explícitas e preserva o JSON retornado."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Executa uma etapa via NotebookLM chat.")
    parser.add_argument("--notebook", required=True)
    parser.add_argument("--prompt", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--source", action="append", required=True)
    parser.add_argument("--conversation-id")
    parser.add_argument("--timeout", type=int, default=240)
    args = parser.parse_args()

    if len(args.source) != len(set(args.source)):
        print("ERRO fontes duplicadas", file=sys.stderr)
        return 1

    command = [
        "notebooklm",
        "ask",
        "--notebook",
        args.notebook,
        "--prompt-file",
        str(args.prompt),
        "--timeout",
        str(args.timeout),
        "--json",
    ]
    if args.conversation_id:
        command.extend(("--conversation-id", args.conversation_id))
    for source_id in args.source:
        command.extend(("--source", source_id))

    result = subprocess.run(
        command,
        text=True,
        capture_output=True,
        timeout=args.timeout + 60,
        check=False,
    )
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()[-2000:]
        print(f"ERRO NotebookLM ({result.returncode}): {detail}", file=sys.stderr)
        return 1

    response = json.loads(result.stdout)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(response, ensure_ascii=False, indent=2) + "\n"
    args.output.write_text(serialized, encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "sha256": hashlib.sha256(serialized.encode("utf-8")).hexdigest(),
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
