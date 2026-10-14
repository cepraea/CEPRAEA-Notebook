# Prompt 06 — Gerar requisitos de acesso

Produza somente `06-requisitos-acesso.yaml` para o domínio e o `run_id` informados.

Use papéis, recursos, dados e regras dos artefatos promovidos selecionados. Registre as entradas em `document.input_artifacts`.

## Tarefa

1. Defina papéis, origem confiável da autorização e escopo de atribuição.
2. Classifique recursos, titularidade e exposição pela Data API.
3. Mapeie operações, grants necessários, escopo de linha e coluna.
4. Aplique negação padrão a anônimo, usuário sem papel e acesso cruzado.
5. Não use metadados controláveis pelo usuário como fonte de autorização.
6. Exija `SECURITY INVOKER` para views expostas quando aplicável.
7. Vincule permissões a regras e testes positivos e negativos.
8. Não gere SQL nem alegue teste de policy.

Retorne somente YAML válido conforme `06-requisitos-acesso.template.yaml`, sem cerca Markdown.
