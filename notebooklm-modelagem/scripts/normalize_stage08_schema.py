#!/usr/bin/env python3
"""Aplica correções determinísticas e limitadas ao schema STAGE_08 report-002."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import yaml

from build_source_manifest import QuotedDumper, quote_values


EXPECTED_BASE_SHA256 = "4e134a0886048cd2fac18f0cde23066f82e0122afbd457e3b78f0b3a7efc2acc"

REPLACEMENTS = {
    "CREATE TABLE public.atleta (": "CREATE TABLE private.atleta (",
    "REFERENCES public.atleta (id)": "REFERENCES private.atleta (id)",
    "ON DELETE NO ACTION ON UPDATE CASCADE;": "ON DELETE RESTRICT ON UPDATE CASCADE;",
    "fk_inscricao_equipe FOREIGN KEY (equipe_id) REFERENCES public.equipe (id) ON DELETE RESTRICT ON UPDATE CASCADE":
        "fk_inscricao_equipe FOREIGN KEY (equipe_id) REFERENCES public.equipe (id) ON DELETE CASCADE ON UPDATE CASCADE",
    "fk_periodo_set_equipe_vencedora FOREIGN KEY (equipe_vencedora_id) REFERENCES public.equipe (id) ON DELETE SET NULL ON UPDATE CASCADE":
        "fk_periodo_set_equipe_vencedora FOREIGN KEY (equipe_vencedora_id) REFERENCES public.equipe (id) ON DELETE RESTRICT ON UPDATE CASCADE",
    "fk_shoot_out_equipe_vencedora FOREIGN KEY (equipe_vencedora_id) REFERENCES public.equipe (id) ON DELETE SET NULL ON UPDATE CASCADE":
        "fk_shoot_out_equipe_vencedora FOREIGN KEY (equipe_vencedora_id) REFERENCES public.equipe (id) ON DELETE RESTRICT ON UPDATE CASCADE",
    "fk_evento_scout_atleta_exec FOREIGN KEY (atleta_executor_id) REFERENCES private.atleta (id) ON DELETE SET NULL ON UPDATE CASCADE":
        "fk_evento_scout_atleta_exec FOREIGN KEY (atleta_executor_id) REFERENCES private.atleta (id) ON DELETE RESTRICT ON UPDATE CASCADE",
    "fk_evento_scout_atleta_alvo FOREIGN KEY (atleta_alvo_id) REFERENCES private.atleta (id) ON DELETE SET NULL ON UPDATE CASCADE":
        "fk_evento_scout_atleta_alvo FOREIGN KEY (atleta_alvo_id) REFERENCES private.atleta (id) ON DELETE RESTRICT ON UPDATE CASCADE",
    "fk_segmento_observado_midia FOREIGN KEY (midia_video_id) REFERENCES private.midia_video (id) ON DELETE CASCADE ON UPDATE CASCADE":
        "fk_segmento_observado_midia FOREIGN KEY (midia_video_id) REFERENCES private.midia_video (id) ON DELETE RESTRICT ON UPDATE CASCADE",
    "fk_placar_jogo_equipe_vencedora FOREIGN KEY (equipe_vencedora_id) REFERENCES public.equipe (id) ON DELETE SET NULL ON UPDATE CASCADE":
        "fk_placar_jogo_equipe_vencedora FOREIGN KEY (equipe_vencedora_id) REFERENCES public.equipe (id) ON DELETE RESTRICT ON UPDATE CASCADE",
    "fk_trecho_observado_midia FOREIGN KEY (midia_video_id) REFERENCES private.midia_video (id) ON DELETE CASCADE ON UPDATE CASCADE":
        "fk_trecho_observado_midia FOREIGN KEY (midia_video_id) REFERENCES private.midia_video (id) ON DELETE RESTRICT ON UPDATE CASCADE",
    "fk_cartao_azul_atleta FOREIGN KEY (atleta_id) REFERENCES private.atleta (id) ON DELETE SET NULL ON UPDATE CASCADE":
        "fk_cartao_azul_atleta FOREIGN KEY (atleta_id) REFERENCES private.atleta (id) ON DELETE RESTRICT ON UPDATE CASCADE",
    "fk_cartao_azul_papel_operacional FOREIGN KEY (papel_operacional_id) REFERENCES private.papel_esportivo_operacional (id) ON DELETE SET NULL ON UPDATE CASCADE":
        "fk_cartao_azul_papel_operacional FOREIGN KEY (papel_operacional_id) REFERENCES private.papel_esportivo_operacional (id) ON DELETE RESTRICT ON UPDATE CASCADE",
    "fk_participacao_equipe_competicao_competicao FOREIGN KEY (competicao_id) REFERENCES public.competicao (id) ON DELETE CASCADE ON UPDATE CASCADE":
        "fk_participacao_equipe_competicao_competicao FOREIGN KEY (competicao_id) REFERENCES public.competicao (id) ON DELETE RESTRICT ON UPDATE CASCADE",
    "CONSTRAINT uq_segmento_ordem UNIQUE (partida_id, midia_video_id, ordem_intervalo)":
        "CONSTRAINT uq_segmento_ordem UNIQUE (partida_id, ordem_intervalo)",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--normalized-at", required=True)
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    args = parse_args()
    if sha256(args.base) != EXPECTED_BASE_SHA256:
        raise ValueError("base divergente do report-002 auditado")
    text = args.base.read_text(encoding="utf-8")
    h1 = "# Guia de Estruturação e Instruções DDL para `08-schema-postgresql.candidate.sql`\n\n"
    if not text.startswith(h1):
        raise ValueError("H1 esperado ausente")
    text = text.removeprefix(h1)

    old_distribution = (
        "-- especifica 10 tabelas no schema public (competicao, partida, equipe, atleta, partida_equipe,\n"
        "-- periodo_set, shoot_out, placar_jogo, estado_do_placar, evolucao_do_placar) e 22 tabelas no\n"
        "-- schema private, totalizando exatamente 32 relações físicas."
    )
    new_distribution = (
        "-- especifica 9 tabelas no schema public (competicao, partida, equipe, partida_equipe, periodo_set,\n"
        "-- shoot_out, placar_jogo, estado_do_placar, evolucao_do_placar) e 23 tabelas no schema private,\n"
        "-- totalizando exatamente 32 relações físicas."
    )
    if text.count(old_distribution) != 1:
        raise ValueError("comentário de distribuição esperado ausente ou duplicado")
    text = text.replace(old_distribution, new_distribution)

    changes = ["REMOVE_MARKDOWN_H1", "FIX_SCHEMA_DISTRIBUTION_COMMENT"]
    for old, new in REPLACEMENTS.items():
        expected_count = 5 if old == "REFERENCES public.atleta (id)" else 1
        actual_count = text.count(old)
        if actual_count != expected_count:
            raise ValueError(f"substituição insegura: esperado {expected_count}, encontrado {actual_count}: {old}")
        text = text.replace(old, new)
        changes.append(old.split(" ", 1)[0])

    args.output.write_text(text, encoding="utf-8")
    audit = {
        "status": "PASS",
        "stage_id": "STAGE_08",
        "operation": "DETERMINISTIC_OPERATOR_NORMALIZATION",
        "normalized_at": args.normalized_at,
        "base": {"path": str(args.base), "sha256": sha256(args.base)},
        "output": {"path": str(args.output), "sha256": sha256(args.output)},
        "changes": changes,
        "semantic_scope_changed": False,
        "relations_added": 0,
        "columns_added": 0,
        "sql_executed": False,
    }
    args.audit.write_text(
        yaml.dump(quote_values(audit), Dumper=QuotedDumper, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )
    print(f"OK {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
