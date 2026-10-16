# Prompt 10 — Gerar seeds simulados candidatos

Produza somente `10-seeds-simulados.candidate.sql` para o escopo autorizado externamente.

## Tarefa

1. Use apenas dados artificiais identificados como simulados.
2. Cubra casos válidos, limites, ausência, histórico e relações relevantes.
3. Inclua cenários esportivos necessários sem reproduzir dados pessoais reais.
4. Use IDs determinísticos apenas para repetibilidade.
5. Não contorne constraints ou RLS.
6. Limite a limpeza ao conjunto simulado.

Na ausência da decisão externa do operador, retorne somente comentários `GENERATION_BLOCKED`. Retorne apenas SQL e comentários SQL.
