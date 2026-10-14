# Prompt 00 — Reconciliar fontes

Produza somente `00-manifesto-fontes.yaml` para o domínio e o `run_id` informados pelo operador.

Use apenas as fontes selecionadas nesta solicitação. Siga `Fluxo_Modelagem.md`, `INSTRUCOES_NOTEBOOK.md`, `CONTRATO_ARTEFATOS.md` e `00-manifesto-fontes.template.yaml` quando estiverem entre as fontes selecionadas.

## Tarefa

1. Registre o `notebook_source_id` real de cada fonte selecionada.
2. Classifique autoridade, vigência, escopo, revisão e limitações.
3. Detecte duplicidades, substituições e material histórico.
4. Crie `evidence_refs` com IDs únicos e localizadores precisos.
5. Registre precedências demonstráveis e conflitos não resolvidos.
6. Não promova uma fonte por nome, pasta ou rótulo editorial.
7. Não faça modelagem conceitual, lógica ou física.

Use `null` quando revisão, hash ou data de obtenção não estiverem disponíveis nas fontes. Não invente metadados do operador.

Retorne somente YAML válido, sem cerca Markdown. O documento começa como `PROPOSTO`.
