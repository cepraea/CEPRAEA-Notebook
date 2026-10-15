# Estágio 03 — Propor corpo do modelo lógico relacional

Produza somente o corpo lógico proposto para `03-modelo-logico.yaml`.

O registro semântico promovido, o modelo conceitual promovido e o template do estágio 03 estão entre as fontes explicitamente selecionadas. As demais fontes selecionadas são controles de formato e operação.

Não produza o envelope `document`. `run_id`, `notebook_id`, versão, hashes, `promoted_source_id`, timestamps, estado, aprovação e promoção pertencem ao operador.

## Tarefa

1. Transforme todas as 29 entidades do modelo conceitual promovido em relações lógicas, admitindo relações associativas adicionais somente quando necessárias para materializar relacionamentos N:N ou fatos com atributos próprios.
2. Declare para cada relação o grão, a identidade, as chaves candidatas, os atributos, a nulabilidade e a estratégia de histórico.
3. Materialize os 46 relacionamentos conceituais por FK, relação associativa ou restrição rastreável. Não invente IDs de entidades ou relacionamentos conceituais.
4. Modele vínculos temporais, histórico, correções, versões e snapshots explicitamente.
5. Registre FKs, semântica de exclusão e atualização e necessidade de índice de suporte.
6. Registre decisões de normalização e trade-offs.
7. Não gere DDL, tipos físicos específicos do PostgreSQL, índices físicos, grants, RLS ou policies.
8. Não comprima informação multivalorada em texto ou JSON sem decisão de normalização rastreada.
9. Sets, shoot-out, placar, técnicas de arremesso, punições, posses, sistemas táticos, papéis operacionais, observações, revisões e proveniência devem permanecer fatos ou relações próprios; não os agregue como colunas de `PARTIDA`.

## Estrutura obrigatória

Siga exatamente os campos de `relations`, `foreign_keys`, `normalization_decisions` e `open_issues` do template selecionado.

Em cada relação:

- `conceptual_entity_ids` referencia somente entidades existentes no modelo conceitual promovido;
- `identity.attribute_ids`, chaves e constraints referenciam atributos declarados na própria relação;
- `candidate_keys` é uma lista de objetos com `id` e `attribute_ids`;
- `unique_constraints` é uma lista de objetos com `id` e `attribute_ids`;
- `checks` é uma lista de objetos com `id`, `expression_semantics` e `rule_ids`;
- `rule_ids` e `derivation_rule_id` usam somente regras existentes no registro semântico promovido;
- `evidence_ref_ids` usa somente evidências já referenciadas pelos artefatos promovidos selecionados;
- valores desconhecidos são representados por `null` e pendência rastreável, nunca por `TBD`, `TODO`, reticências ou “a definir”.

Em cada FK:

- os atributos de origem e destino devem existir nas relações indicadas;
- `relationship_id` referencia exatamente um dos 46 relacionamentos do modelo conceitual promovido;
- uma associação N:N com contexto próprio deve possuir relação associativa e duas FKs, ambas rastreadas ao mesmo relacionamento conceitual quando aplicável.

Cada item de `open_issues` deve usar exatamente os campos `id`, `status`, `question`, `affected_ids`, `impact`, `required_evidence` e `owner` definidos no contrato.

Retorne somente YAML válido, sem título, comentário ou cerca Markdown, nesta raiz:

```yaml
logical_model:
  relations: []
  foreign_keys: []
  normalization_decisions: []
  open_issues: []
```
