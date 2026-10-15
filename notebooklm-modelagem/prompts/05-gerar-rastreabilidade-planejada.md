# Prompt 05 — Gerar rastreabilidade planejada

Produza somente `05-matriz-rastreabilidade-planejada.yaml` com `phase: PLANNED`.

Use manifesto, registro semântico, modelos conceitual e lógico e dicionário promovidos, todos selecionados explicitamente. Registre as entradas em `document.input_artifacts`.

## Tarefa

1. Ligue `evidence_ref_ids` a conceitos e regras.
2. Ligue regras a entidades, relações, atributos, permissões e testes planejados.
3. Registre objetos físicos apenas como candidatos identificados.
4. Separe `implementation_status` de `verification_status`.
5. Detecte órfãos nos dois sentidos.
6. Não marque implementação ou teste como concluído.

Retorne somente YAML válido conforme `05-matriz-rastreabilidade.template.yaml`, sem cerca Markdown.
