#!/usr/bin/env python3
"""Deriva JSON determinístico de um YAML canônico."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml


def main() -> int:
    parser = argparse.ArgumentParser(description="Converte YAML canônico em JSON derivado.")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    data = yaml.safe_load(args.input.read_text(encoding="utf-8"))
    rendered = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    args.output.write_text(rendered, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
