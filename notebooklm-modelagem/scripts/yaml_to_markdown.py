#!/usr/bin/env python3
"""Agrupa YAML canônico em uma fonte Markdown aceita pelo NotebookLM."""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Converte um ou mais YAML em uma fonte Markdown.")
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    sections = ["# Fontes YAML consolidadas", ""]
    for path in args.inputs:
        if path.suffix.lower() not in {".yaml", ".yml"}:
            parser.error(f"extensão YAML esperada: {path}")
        content = path.read_text(encoding="utf-8").rstrip()
        sections.extend((f"## Arquivo: `{path.as_posix()}`", "", "```yaml", content, "```", ""))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(sections), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
