#!/usr/bin/env bash
# check-diagnostics.sh — roda após cada escrita de arquivo pelo agente
# Recebe contexto do hook via stdin (JSON com tool_input.file_path)
set -euo pipefail

REPO="/home/davis/Gemini NotebookLM"

# Extrair o caminho do arquivo do JSON recebido via stdin
INPUT=$(cat)
FILE=$(echo "$INPUT" | python3 -c "
import json, sys
try:
    d = json.load(sys.stdin)
    path = d.get('tool_input', {}).get('file_path') or d.get('file_path', '')
    print(path)
except:
    print('')
" 2>/dev/null || echo "")

# Se não identificou arquivo, sai silenciosamente
if [ -z "$FILE" ]; then
  exit 0
fi

echo "── Diagnósticos: $FILE ───────────────────────────"

# Python: Pyright
if [[ "$FILE" == *.py ]]; then
  cd "$REPO"
  "$REPO/.venv/bin/python" -m pyright "$FILE" 2>&1 \
    | grep -E "error:|warning:" \
    | sed 's/^/  /' \
    || echo "  ✓ Sem erros Python"
fi

# Markdown: markdownlint
if [[ "$FILE" == *.md ]]; then
  npx markdownlint-cli2 "$FILE" 2>&1 \
    | grep -v "^markdownlint-cli2" \
    | sed 's/^/  /' \
    || echo "  ✓ Sem erros Markdown"
fi

# YAML: validação de sintaxe
if [[ "$FILE" == *.yaml ]] || [[ "$FILE" == *.yml ]]; then
  "$REPO/.venv/bin/python" -c "
import yaml, sys
try:
    yaml.safe_load(open('$FILE'))
    print('  ✓ YAML válido')
except yaml.YAMLError as e:
    print(f'  ✗ YAML inválido: {e}')
    sys.exit(1)
" 2>&1
fi

echo "──────────────────────────────────────────────────"
