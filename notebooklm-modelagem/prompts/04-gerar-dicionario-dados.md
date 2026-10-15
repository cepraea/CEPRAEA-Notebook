# Prompt 04 — Gerar dicionário de dados

Produza somente `04-dicionario-dados.yaml` para o domínio e o `run_id` informados.

Use o registro semântico e o modelo lógico promovidos selecionados pelo operador. Registre as entradas em `document.input_artifacts`.

## Tarefa

1. Documente todas as relações e atributos lógicos, sem adicionar outros.
2. Defina descrição, grão, tipo PostgreSQL candidato, nulabilidade, ausência, unidade, formato, valores e limites.
3. Diferencie desconhecido, não observado, não aplicável, não informado, protegido e ausência factual.
4. Registre classificação de acesso, chaves, unicidade, checks, FKs e retenção.
5. Proponha índice para cada FK e para padrões de consulta ou RLS demonstrados; justifique cada um.
6. Registre catálogos versionados sem inventar enums fechados.
7. Não gere SQL.

Retorne somente YAML válido conforme `04-dicionario-dados.template.yaml`, sem cerca Markdown.
