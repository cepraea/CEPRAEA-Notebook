# Prompt 02 — Propor modelo conceitual

Produza somente o corpo conceitual proposto para `02-modelo-conceitual.yaml`.

O registro semântico promovido, o manifesto de evidências e o template da etapa devem estar entre as fontes explicitamente selecionadas.

Não produza o envelope `document`. `run_id`, `notebook_id`, versão, hashes, `promoted_source_id`, timestamps, estado, aprovação e promoção pertencem ao operador.

## Tarefa

1. Identifique entidades, eventos, papéis, associações, catálogos, estados e snapshots necessários.
2. Declare identidade, temporalidade, histórico e limites de cada entidade.
3. Registre cardinalidade mínima e máxima nos dois sentidos.
4. Registre invariantes por ID.
5. Não transforme todo substantivo em entidade.
6. Não inclua tipos PostgreSQL, índices, RLS ou SQL.
7. Use somente `concept_id` e `rule_ids` existentes no registro semântico promovido.
8. Use somente `evidence_ref_ids` existentes no manifesto promovido.
9. Em `coverage`, classifique cada conceito do registro semântico como coberto ou excluído; não omita conceitos silenciosamente.

No domínio esportivo, avalie como objetos independentes partida, segmento, shoot-out, evento de pontuação, punição, posse, observação, protocolo de scout, mídia e revisão. Preserve ator, contexto, temporalidade e proveniência.

Siga exatamente os campos de `entities`, `relationships`, `domain_invariants`, `coverage` e `open_issues` do template selecionado. Retorne somente YAML válido, sem cerca Markdown, nesta raiz:

```yaml
conceptual_model:
  entities: []
  relationships: []
  domain_invariants: []
  coverage:
    required_concept_ids: []
    covered_concept_ids: []
    excluded_concept_ids: []
  open_issues: []
```
