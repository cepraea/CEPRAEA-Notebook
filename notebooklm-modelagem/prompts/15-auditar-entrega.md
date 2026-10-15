# Prompt 15 — Auditar a entrega

Produza somente `15-relatorio-validacao.md` para um domínio.

Use artefatos promovidos, decisão do operador, migration real, matriz `AS_BUILT` e evidências reais de execução e testes. Não trate texto gerado pelo NotebookLM como prova de execução.

## Tarefa

1. Identifique versões, hashes e estados dos artefatos.
2. Verifique consistência entre semântica, modelos, dicionário, migration e RLS.
3. Verifique órfãos e divergências na matriz `AS_BUILT`.
4. Compare resultados observados com critérios preexistentes.
5. Separe proposta, aprovação, implementação, execução, teste e homologação.
6. Liste desvios, riscos residuais e escopo não verificado.
7. Conclua por domínio, nunca para todo o corpus.

O documento deve conter exatamente um H1, resumo executivo, escopo e versões, evidências, resultados, divergências, riscos, conclusão e aprovações pendentes. Sem logs ou códigos de saída, registre `NÃO EXECUTADO`, nunca `PASS`.

Retorne somente Markdown. O relatório começa como `PROPOSTO`.
