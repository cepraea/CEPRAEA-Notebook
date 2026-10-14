#!/usr/bin/env python3
"""Valida YAML de modelagem sem aceitar chaves duplicadas ou aliases."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

import jsonschema
import yaml


PLACEHOLDER_RE = re.compile(r"(?:\bTBD\b|\bTODO\b|\.\.\.|a definir)", re.IGNORECASE)

REQUIRED_BODY_KEYS = {
    "SOURCE_MANIFEST": {"scope", "sources", "evidence_refs", "conflicts", "open_issues"},
    "SEMANTIC_REGISTRY": {"concepts", "rules", "decisions", "open_issues"},
    "CONCEPTUAL_MODEL": {"entities", "relationships", "domain_invariants", "coverage", "open_issues"},
    "LOGICAL_MODEL": {"relations", "foreign_keys", "normalization_decisions", "open_issues"},
    "DATA_DICTIONARY": {"tables", "catalogs", "open_issues"},
    "TRACEABILITY_MATRIX": {"phase", "traces", "coverage_summary", "orphan_checks", "open_issues"},
    "ACCESS_REQUIREMENTS": {"roles", "resources", "permissions", "default_policy", "open_issues"},
    "STOP_GATE_RECOMMENDATION": {"criteria", "recommendation", "recommended_scope", "open_issues"},
}


class StrictLoader(yaml.SafeLoader):
    pass


def reject_aliases(loader: StrictLoader, node: yaml.Node) -> Any:
    raise yaml.constructor.ConstructorError(None, None, "aliases YAML não são permitidos", node.start_mark)


StrictLoader.add_constructor("tag:yaml.org,2002:merge", reject_aliases)


def construct_mapping(loader: StrictLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping", node.start_mark, f"chave duplicada: {key!r}", key_node.start_mark
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Valida artefatos YAML do pacote de modelagem.")
    parser.add_argument("path", type=Path)
    parser.add_argument("--schema", type=Path)
    parser.add_argument("--allow-placeholders", action="store_true")
    return parser.parse_args()


def collect_ids(value: Any, seen: set[str], duplicates: set[str]) -> None:
    if isinstance(value, dict):
        object_id = value.get("id")
        if isinstance(object_id, str):
            if object_id in seen:
                duplicates.add(object_id)
            seen.add(object_id)
        for child in value.values():
            collect_ids(child, seen, duplicates)
    elif isinstance(value, list):
        for child in value:
            collect_ids(child, seen, duplicates)


def main() -> int:
    args = parse_args()
    text = args.path.read_text(encoding="utf-8")
    if "\t" in text:
        print(f"ERRO {args.path}: tabulação não permitida", file=sys.stderr)
        return 1
    if not args.allow_placeholders and PLACEHOLDER_RE.search(text):
        print(f"ERRO {args.path}: placeholder editorial encontrado", file=sys.stderr)
        return 1
    try:
        tokens = tuple(yaml.scan(text))
        if any(isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)) for token in tokens):
            raise ValueError("anchors e aliases YAML não são permitidos")
        data = yaml.load(text, Loader=StrictLoader)
        seen: set[str] = set()
        duplicates: set[str] = set()
        collect_ids(data, seen, duplicates)
        if duplicates:
            raise ValueError(f"IDs duplicados: {', '.join(sorted(duplicates))}")
        if args.schema:
            schema = json.loads(args.schema.read_text(encoding="utf-8"))
            jsonschema.Draft202012Validator(schema).validate(data)
        if not args.allow_placeholders and isinstance(data, dict):
            document = data.get("document")
            artifact_kind = document.get("artifact_kind") if isinstance(document, dict) else None
            required = REQUIRED_BODY_KEYS.get(artifact_kind, set())
            missing = sorted(required - data.keys())
            if missing:
                raise ValueError(f"seções obrigatórias ausentes: {', '.join(missing)}")
    except (OSError, ValueError, yaml.YAMLError, jsonschema.ValidationError) as exc:
        print(f"ERRO {args.path}: {exc}", file=sys.stderr)
        return 1
    print(f"OK {args.path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
