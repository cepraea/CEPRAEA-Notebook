# Prompt 13 — Gerar rollback candidato

Produza somente `13-rollback.candidate.sql`, separado da migration de avanço.

## Tarefa

1. Derive a reversão da migration de avanço candidata selecionada.
2. Ordene a reversão respeitando dependências.
3. Preserve dados sempre que possível.
4. Para perda inevitável, interrompa com comentário `DESTRUCTIVE_ROLLBACK_REQUIRES_APPROVAL` e descreva backup e recuperação necessários.
5. Declare pré-condições e pós-condições.
6. Não afirme que o rollback foi executado.

Na ausência da migration candidata e da decisão externa do operador, retorne somente comentários `GENERATION_BLOCKED`. Retorne apenas SQL e comentários SQL.
