#!/usr/bin/env python3
"""Executa enriquecimento isolado e recuperável de fontes em lotes curtos."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import yaml


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Enriquece fontes individualmente via NotebookLM chat.")
    parser.add_argument("--state", required=True, type=Path)
    parser.add_argument("--candidate", required=True, type=Path)
    parser.add_argument("--prompt", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--ledger", required=True, type=Path)
    parser.add_argument("--schema", required=True, type=Path)
    parser.add_argument("--limit", type=int, default=3)
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def run_command(command: list[str], timeout: int) -> str:
    result = subprocess.run(command, text=True, capture_output=True, timeout=timeout, check=False)
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()[-1000:]
        raise RuntimeError(f"comando falhou ({result.returncode}): {detail}")
    return result.stdout


def save_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def now() -> str:
    return datetime.now(ZoneInfo("America/Sao_Paulo")).isoformat(timespec="seconds")


def main() -> int:
    args = parse_args()
    if args.limit < 1:
        print("ERRO --limit deve ser positivo", file=sys.stderr)
        return 1

    state = yaml.safe_load(args.state.read_text(encoding="utf-8"))
    manifest = yaml.safe_load(args.candidate.read_text(encoding="utf-8"))
    notebook_id = state["run"]["notebook_id"]
    stage = next(item for item in state["stages"] if item["id"] == "STAGE_00")
    already_verified = set(stage["operator_assembly"]["semantic_enrichment"].get("verified_source_ids", []))

    if args.ledger.exists():
        ledger = json.loads(args.ledger.read_text(encoding="utf-8"))
    else:
        ledger = {"schema_version": "1.0", "run_id": state["run"]["id"], "records": []}
    already_verified.update(
        record["notebook_source_id"] for record in ledger["records"] if record.get("status") == "VERIFIED_CANDIDATE"
    )

    manifest_by_notebook_id = {item["notebook_source_id"]: item for item in manifest["sources"]}
    pending = [
        item
        for item in state["selected_sources"]
        if item["role"] != "CONTROLE" and item["source_id"] not in already_verified
    ][: args.limit]
    if not pending:
        print("OK nenhuma fonte documental pendente")
        return 0

    merge_script = Path(__file__).with_name("merge_source_assessment.py")
    validate_script = Path(__file__).with_name("validate_yaml.py")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    for position, selected in enumerate(pending, 1):
        source_id = selected["source_id"]
        title = selected["title"]
        semantic_source = manifest_by_notebook_id[source_id]
        evidence_prefix = semantic_source["id"].removeprefix("SRC_")
        if not evidence_prefix[0].isalpha():
            evidence_prefix = f"SOURCE_{evidence_prefix}"
        response_path = args.output_dir / f"{source_id}.chat.json"
        fulltext_path = Path("/tmp") / f"notebooklm-enrichment-{source_id}.txt"
        next_candidate = args.candidate.with_name(args.candidate.name + ".next")
        record: dict[str, Any] = {
            "notebook_source_id": source_id,
            "semantic_source_id": semantic_source["id"],
            "title": title,
            "started_at": now(),
            "status": "STARTED",
        }
        ledger["records"].append(record)
        save_json(args.ledger, ledger)
        print(f"START {position}/{len(pending)} {source_id} {title}", flush=True)

        try:
            answer_text = run_command(
                [
                    "notebooklm",
                    "ask",
                    "--new",
                    "--yes",
                    "--notebook",
                    notebook_id,
                    "--source",
                    source_id,
                    "--prompt-file",
                    str(args.prompt),
                    "--timeout",
                    "180",
                    "--json",
                ],
                timeout=240,
            )
            answer = json.loads(answer_text)
            save_json(response_path, answer)
            record.update(
                {
                    "conversation_id": answer.get("conversation_id"),
                    "turn_id": answer.get("turn_key", {}).get("turn_id"),
                    "response_path": str(response_path),
                    "response_sha256": sha256(response_path),
                    "api_reference_count": len(answer.get("references", [])),
                    "status": "CHAT_SAVED",
                }
            )
            save_json(args.ledger, ledger)
            print(f"CHAT_SAVED {source_id}", flush=True)

            fulltext_result = json.loads(
                run_command(
                    [
                        "notebooklm",
                        "source",
                        "fulltext",
                        source_id,
                        "--notebook",
                        notebook_id,
                        "--format",
                        "text",
                        "--output",
                        str(fulltext_path),
                        "--force",
                        "--json",
                    ],
                    timeout=120,
                )
            )
            evidence_before = len(yaml.safe_load(args.candidate.read_text(encoding="utf-8"))["evidence_refs"])
            run_command(
                [
                    sys.executable,
                    str(merge_script),
                    str(args.candidate),
                    str(response_path),
                    str(next_candidate),
                    "--notebook-source-id",
                    source_id,
                    "--fulltext",
                    str(fulltext_path),
                    "--evidence-prefix",
                    evidence_prefix,
                    "--allow-partial-evidence",
                    "--force",
                ],
                timeout=60,
            )
            run_command(
                [
                    sys.executable,
                    str(validate_script),
                    "--schema",
                    str(args.schema),
                    "--state",
                    str(args.state),
                    str(next_candidate),
                ],
                timeout=60,
            )
            evidence_after = len(yaml.safe_load(next_candidate.read_text(encoding="utf-8"))["evidence_refs"])
            os.replace(next_candidate, args.candidate)
            record.update(
                {
                    "status": "VERIFIED_CANDIDATE",
                    "completed_at": now(),
                    "fulltext_bytes": fulltext_result.get("bytes"),
                    "evidence_added": evidence_after - evidence_before,
                    "candidate_sha256": sha256(args.candidate),
                }
            )
            save_json(args.ledger, ledger)
            print(
                f"VERIFIED {source_id} evidence_added={record['evidence_added']} candidate={record['candidate_sha256']}",
                flush=True,
            )
        except Exception as exc:
            record.update({"status": "FAILED", "completed_at": now(), "error": str(exc)})
            save_json(args.ledger, ledger)
            if next_candidate.exists():
                next_candidate.unlink()
            print(f"FAILED {source_id}: {exc}", file=sys.stderr, flush=True)
            return 1
        finally:
            if fulltext_path.exists():
                fulltext_path.unlink()

    print(f"OK lote concluído: {len(pending)} fontes", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
