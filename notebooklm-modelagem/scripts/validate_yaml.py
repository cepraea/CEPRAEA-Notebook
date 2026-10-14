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


PLACEHOLDER_RE = re.compile(r"(?:\b(?i:TBD)\b|\bTODO\b|\.\.\.|(?i:a definir))")

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


def reject_aliases(_loader: StrictLoader, node: yaml.Node) -> Any:
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
    parser.add_argument("--state", type=Path, help="Confere as fontes contra selected_sources do estado da execução.")
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
            required = REQUIRED_BODY_KEYS.get(artifact_kind, set()) if isinstance(artifact_kind, str) else set()
            missing = sorted(required - data.keys())
            if missing:
                raise ValueError(f"seções obrigatórias ausentes: {', '.join(missing)}")
            if args.state and artifact_kind == "SOURCE_MANIFEST":
                state = yaml.load(args.state.read_text(encoding="utf-8"), Loader=StrictLoader)
                selected = state.get("selected_sources", []) if isinstance(state, dict) else []
                sources = data.get("sources", [])
                expected_ids = [item.get("source_id") for item in selected if isinstance(item, dict)]
                actual_ids = [item.get("notebook_source_id") for item in sources if isinstance(item, dict)]
                if len(expected_ids) != len(set(expected_ids)):
                    raise ValueError("selected_sources contém source_id duplicado")
                if len(actual_ids) != len(set(actual_ids)):
                    raise ValueError("sources contém notebook_source_id duplicado")
                missing_ids = set(expected_ids) - set(actual_ids)
                unexpected_ids = set(actual_ids) - set(expected_ids)
                if missing_ids or unexpected_ids or len(expected_ids) != len(actual_ids):
                    matched = len(set(expected_ids) & set(actual_ids))
                    raise ValueError(
                        "cobertura de fontes divergente: "
                        f"correspondentes={matched}/{len(expected_ids)}, "
                        f"ausentes={len(missing_ids)}, inesperadas={len(unexpected_ids)}"
                    )
            if artifact_kind == "SOURCE_MANIFEST":
                source_ids = {item.get("id") for item in data.get("sources", []) if isinstance(item, dict)}
                evidence_ids = {
                    item.get("id") for item in data.get("evidence_refs", []) if isinstance(item, dict)
                }
                for evidence in data.get("evidence_refs", []):
                    if evidence.get("source_id") not in source_ids:
                        raise ValueError(f"evidência referencia fonte inexistente: {evidence.get('id')}")
                for rule in data.get("precedence_rules", []):
                    referenced_sources = {
                        rule.get("higher_authority_source_id"),
                        rule.get("lower_authority_source_id"),
                    }
                    if not referenced_sources <= source_ids:
                        raise ValueError(f"precedência referencia fonte inexistente: {rule.get('id')}")
                    if not set(rule.get("evidence_ref_ids", [])) <= evidence_ids:
                        raise ValueError(f"precedência referencia evidência inexistente: {rule.get('id')}")
                for conflict in data.get("conflicts", []):
                    if not set(conflict.get("source_ids", [])) <= source_ids:
                        raise ValueError(f"conflito referencia fonte inexistente: {conflict.get('id')}")
                    if not set(conflict.get("evidence_ref_ids", [])) <= evidence_ids:
                        raise ValueError(f"conflito referencia evidência inexistente: {conflict.get('id')}")
    except (OSError, ValueError, yaml.YAMLError, jsonschema.ValidationError) as exc:
        print(f"ERRO {args.path}: {exc}", file=sys.stderr)
        return 1
    print(f"OK {args.path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
