# Prompt 08 — Gerar schema PostgreSQL candidato

Produza somente `08-schema-postgresql.candidate.sql`.

As fontes selecionadas devem incluir a recomendação do gate e a decisão externa do operador com `operator_decision`, responsável, instante, evidência e escopo autorizado. Na ausência desses dados, retorne apenas comentários `GENERATION_BLOCKED` com os campos faltantes.

## Tarefa

1. Derive DDL somente do modelo lógico e do dicionário autorizados.
2. Declare schemas, tipos, tabelas, PKs, FKs, `NOT NULL`, `UNIQUE` e `CHECK`.
3. Preserve temporalidade, histórico, proveniência e correções.
4. Crie índices de suporte para FKs e índices justificados para consultas ou RLS.
5. Use funções ou triggers apenas quando constraints declarativas forem insuficientes.
6. Não inclua policies, dados reais, secrets ou alegações de execução.
7. Não use `IF NOT EXISTS` para ocultar divergência estrutural.

Este arquivo é candidato de composição e não deve ser aplicado isoladamente em schema exposto. Retorne somente SQL e comentários SQL com o cabeçalho exigido no contrato.
