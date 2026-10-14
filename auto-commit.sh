#!/usr/bin/env bash
# auto-commit.sh — Commit automático para sessões de agentes
# Fluxo: draft/agent → push → PR para main (se não existir)
set -euo pipefail

REPO="/home/davis/Gemini NotebookLM"
AGENT="${AGENT_ID:-manual}"
DRAFT_BRANCH="draft/agent"
MAIN_BRANCH="main"

cd "$REPO"

# ── 1. Nada mudou? Sai silenciosamente ─────────────────────────────────────
if git diff --quiet && git diff --staged --quiet \
   && [ -z "$(git ls-files --others --exclude-standard)" ]; then
  echo "→ Nenhuma mudança para commitar."
  exit 0
fi

# ── 2. Garantir que estamos no branch de rascunho ──────────────────────────
CURRENT_BRANCH=$(git branch --show-current 2>/dev/null || echo "")

if [ "$CURRENT_BRANCH" = "$MAIN_BRANCH" ] || [ -z "$CURRENT_BRANCH" ]; then
  git checkout -B "$DRAFT_BRANCH" 2>/dev/null || git checkout "$DRAFT_BRANCH"
  echo "→ Trocando para $DRAFT_BRANCH"
fi

# ── 3. Gate de qualidade ───────────────────────────────────────────────────
if command -v markdownlint-cli2 &>/dev/null; then
  echo "→ Validando Markdown..."
  markdownlint-cli2 "**/*.md" --fix 2>/dev/null || true
fi

# ── 4. Diff rápido antes de commitar (para auditoria no log) ──────────────
echo ""
echo "── Alterações detectadas ─────────────────────────"
git diff --stat HEAD 2>/dev/null || git diff --stat 2>/dev/null || true
echo "──────────────────────────────────────────────────"

# ── 5. Stage + Commit ─────────────────────────────────────────────────────
git add -A

TIMESTAMP=$(date '+%Y-%m-%dT%H:%M')
FILES=$(git diff --cached --name-only | wc -l | tr -d ' ')
SAMPLE=$(git diff --cached --name-only | head -3 | paste -sd ', ')

git commit -m "auto($AGENT): $TIMESTAMP — $FILES arquivo(s)

Arquivos: $SAMPLE

Co-Authored-By: $AGENT <noreply@agent>"

echo "✓ Commit: auto($AGENT) @ $TIMESTAMP"

# ── 6. Push para o remote ─────────────────────────────────────────────────
echo "→ Fazendo push para origin/$DRAFT_BRANCH..."
git push -u origin "$DRAFT_BRANCH" 2>&1

# ── 7. Abrir PR se não existir um aberto ──────────────────────────────────
if command -v gh &>/dev/null; then
  OPEN_PR=$(gh pr list --head "$DRAFT_BRANCH" --base "$MAIN_BRANCH" --json number --jq '.[0].number' 2>/dev/null || echo "")

  if [ -z "$OPEN_PR" ]; then
    echo "→ Abrindo PR draft/agent → main..."
    gh pr create \
      --title "[$AGENT] Atualizações em $TIMESTAMP" \
      --body "## Alterações automáticas do agente \`$AGENT\`

**Timestamp:** $TIMESTAMP
**Arquivos modificados:** $FILES

### Arquivos
$SAMPLE

---
> Commit automático via \`auto-commit.sh\`. Revisar antes de fazer merge em main." \
      --base "$MAIN_BRANCH" \
      --head "$DRAFT_BRANCH" \
      --draft 2>&1 || echo "⚠ PR já pode existir ou main ainda não tem commits."
  else
    echo "→ PR #$OPEN_PR já aberto — apenas atualizando com o novo push."
  fi
fi

echo ""
echo "✓ Concluído: $FILES arquivo(s) | branch: $DRAFT_BRANCH | agente: $AGENT"
