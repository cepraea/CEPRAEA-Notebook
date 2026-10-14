# Prompt 11 — Gerar testes pgTAP candidatos

Produza somente `11-testes-pgtap.candidate.sql` para o escopo autorizado externamente.

## Tarefa

1. Gere testes estruturais, positivos, negativos, temporais e de RLS.
2. Vincule cada teste a regra, permissão ou invariante.
3. Teste constraints pelo comportamento, não apenas pelo nome.
4. Cubra banco vazio e estado anterior quando aplicável.
5. Cubra fatos esportivos exigidos pelo modelo aprovado.
6. Teste `anon`, `authenticated`, usuário sem papel, acesso próprio e cruzado.
7. Inclua plano coerente com as assertions e rollback da transação de teste.
8. Não declare `PASS` antes da execução.

Na ausência da decisão externa do operador, retorne somente comentários `GENERATION_BLOCKED`. Retorne apenas SQL pgTAP e comentários SQL.
