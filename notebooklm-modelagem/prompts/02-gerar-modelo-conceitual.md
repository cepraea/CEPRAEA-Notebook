# Prompt 02 — Gerar modelo conceitual

Produza somente `02-modelo-conceitual.yaml` para o domínio e o `run_id` informados.

Use o registro semântico promovido e as evidências necessárias, todos explicitamente selecionados. Registre a entrada em `document.input_artifacts`.

## Tarefa

1. Identifique entidades, eventos, papéis, associações, catálogos, estados e snapshots necessários.
2. Declare identidade, temporalidade, histórico e limites de cada entidade.
3. Registre cardinalidade mínima e máxima nos dois sentidos.
4. Registre invariantes por ID.
5. Não transforme todo substantivo em entidade.
6. Não inclua tipos PostgreSQL, índices, RLS ou SQL.

No domínio esportivo, avalie como objetos independentes partida, segmento, shoot-out, evento de pontuação, punição, posse, observação, protocolo de scout, mídia e revisão. Preserve ator, contexto, temporalidade e proveniência.

Retorne somente YAML válido conforme `02-modelo-conceitual.template.yaml`, sem cerca Markdown.
