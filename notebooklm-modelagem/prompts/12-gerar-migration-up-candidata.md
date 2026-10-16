# Prompt 12 — Gerar migration de avanço candidata

Produza somente `12-migration-up.candidate.sql`.

Use os candidatos de schema e RLS, a decisão externa do operador e as versões exatas das entradas. O operador criará a migration real com `supabase migration new <descricao>`.

## Tarefa

1. Componha DDL, índices, revogações, grants, ativação de RLS e policies em ordem segura.
2. Evite qualquer janela em que tabela exposta tenha grants de cliente sem RLS efetiva.
3. Use transação quando todas as operações forem transacionais.
4. Declare pré-condições e pós-condições verificáveis.
5. Não use `IF NOT EXISTS` para mascarar drift.
6. Não modifique objetos internos de `auth`, `storage` ou `realtime`.
7. Não fixe versão de extensão.
8. Não inclua rollback, seeds ou alegações de execução.

Na ausência de autorização externa completa, retorne somente comentários `GENERATION_BLOCKED`. Retorne apenas SQL e comentários SQL.
