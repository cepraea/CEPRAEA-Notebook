# Prompt 03 — Gerar modelo lógico

Produza somente `03-modelo-logico.yaml` para o domínio e o `run_id` informados.

Use apenas o registro semântico e o modelo conceitual promovidos selecionados pelo operador. Registre todas as entradas em `document.input_artifacts`.

## Tarefa

1. Transforme entidades e associações em relações lógicas.
2. Declare o grão, identidade, chaves candidatas, atributos e nulabilidade.
3. Modele N:N, vínculos temporais, histórico, correções e versões explicitamente.
4. Registre FKs, semântica de exclusão e atualização e necessidade de índice de suporte.
5. Registre decisões de normalização e trade-offs.
6. Não gere DDL ou policies.

Não comprima informação multivalorada em texto ou JSON sem decisão rastreada. Sets, shoot-out, placar, punições, posses, observações e revisões não podem ser apenas colunas da partida.

Retorne somente YAML válido conforme `03-modelo-logico.template.yaml`, sem cerca Markdown.
