# Prompt 00 — Enriquecer uma fonte

Analise somente a fonte documental selecionada pelo operador. Os documentos de controle selecionados servem apenas para orientar a análise.

Não produza o manifesto final. Identidade da fonte, UUID do NotebookLM, `run_id`, hashes, estados e aprovação pertencem ao operador.

## Tarefa

1. Proponha título canônico, editora ou responsável, revisão, data, idioma, tipo documental e limitações somente quando demonstráveis.
2. Classifique autoridade e vigência com justificativa localizada.
3. Extraia evidências relevantes ao domínio com página, regra, seção, aba, célula ou timecode.
   - Cada `excerpt` deve ser uma transcrição literal, contínua e verificável.
   - Não use `...`, `(...)`, `[...]` nem una passagens descontínuas; crie candidatos separados.
4. Sinalize indícios de tradução, duplicidade, substituição ou material histórico sem concluir além da evidência.
5. Não faça modelagem conceitual, lógica ou física.

Use `null` quando um valor não estiver demonstrado. Não invente identificadores ou metadados operacionais.

Retorne somente YAML válido, sem cerca Markdown, nesta estrutura:

```yaml
source_assessment:
  canonical_title_proposal: null
  publisher: null
  source_revision: null
  publication_date: null
  language: null
  source_type: null
  authority_class_proposal: null
  lifecycle_status_proposal: null
  classification_rationale: null
  limitations: []
evidence_candidates:
  - locator: null
    evidence_type: "FATO|REGRA|DECISAO|DERIVACAO|SUPORTE"
    excerpt: null
    interpretation: null
reconciliation_signals: []
open_questions: []
```
