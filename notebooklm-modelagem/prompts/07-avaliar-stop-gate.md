# Prompt 07 — Recomendar o STOP GATE físico

Produza somente `07-stop-gate-<dominio>.yaml` para um domínio e `run_id`.

Use as versões promovidas do manifesto, registro semântico, modelos, dicionário, rastreabilidade planejada e requisitos de acesso, todas selecionadas explicitamente.

## Tarefa

1. Avalie cada critério como `PASS`, `FAIL`, `BLOCKED` ou `NAO_APLICAVEL`.
2. Exija evidência identificável para cada `PASS`.
3. Isole lacunas externas ao domínio.
4. Emita `READY`, `READY_WITH_RESTRICTIONS` ou `BLOCKED`.
5. Liste escopo recomendado, exclusões, restrições e decisões humanas necessárias.
6. Não gere SQL e não autorize o avanço.

`READY_WITH_RESTRICTIONS` só admite elementos independentes e explicitamente listados. O resultado é recomendação `PROPOSTO`; a decisão vinculante pertence ao operador e ao responsável humano.

Retorne somente YAML válido conforme `07-stop-gate.template.yaml`, sem cerca Markdown.
