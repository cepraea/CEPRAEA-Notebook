# Prompt 14 — Reconciliar rastreabilidade AS BUILT

Produza somente `14-matriz-rastreabilidade-as-built.yaml` com `phase: AS_BUILT`.

Use a matriz planejada, a migration real, os testes reais e as evidências de execução selecionadas pelo operador. Não use candidato SQL como prova de implementação.

## Tarefa

1. Substitua objetos físicos candidatos pelos objetos realmente implementados.
2. Registre `IMPLEMENTADO` somente quando a migration real os contiver.
3. Registre `PASS` ou `FAIL` somente com resultado observável de execução.
4. Atualize contagens e órfãos.
5. Preserve divergências entre o planejado e o implementado.
6. Não homologue a entrega.

Retorne somente YAML válido conforme `05-matriz-rastreabilidade.template.yaml`, sem cerca Markdown.
