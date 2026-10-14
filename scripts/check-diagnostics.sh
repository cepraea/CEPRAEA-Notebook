#!/usr/bin/env bash
# check-diagnostics.sh — roda após cada escrita de arquivo pelo agente
# Output vai para o contexto do agente como feedback de erro
set -euo pipefail

FILE="${TOOL_OUTPUT_FILE:-}"   # arquivo que acabou de ser escrito (injetado pelo hook)
REPO="/home/davis/Gemini NotebookLM"

echo "── Diagnósticos pós-escrita ──────────────────────"

# Python: Pyright
if [[ "$FILE" == *.py ]]; then
  echo "[Python/Pyright]"
  cd "$REPO"
  .venv/bin/python -m pyright "$FILE" 2>&1 | grep -E "error|warning|information" || echo "✓ Sem erros"
fi

# Markdown: markdownlint
if [[ "$FILE" == *.md ]]; then
  echo "[Markdown/markdownlint]"
  cd "$REPO"
  npx markdownlint-cli2 "$FILE" 2>&1 || true
fi

# YAML: validação básica
if [[ "$FILE" == *.yaml ]] || [[ "$FILE" == *.yml ]]; then
  echo "[YAML]"
  .venv/bin/python -c "import yaml, sys; yaml.safe_load(open('$FILE'))" 2>&1 \
    && echo "✓ YAML válido" || echo "✗ YAML inválido"
fi

echo "──────────────────────────────────────────────────"
