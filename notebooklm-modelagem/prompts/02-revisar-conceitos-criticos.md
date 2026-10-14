# Prompt 02C — Revisar conceitos críticos do modelo conceitual

Revise somente os dez conceitos abaixo, atualmente excluídos como objetos conceituais independentes no candidato do estágio 02:

`SEGMENTO_OBSERVADO`, `PLACAR_JOGO`, `ESTADO_DO_PLACAR`, `EVOLUCAO_DO_PLACAR`, `SISTEMA_DEFENSIVO`, `CONFIABILIDADE_OBSERVADOR`, `REVISAO_DA_OBSERVACAO`, `ESTADO_DE_REVISAO`, `PROVENIENCIA_OBSERVACAO`, `TRECHO_OBSERVADO`.

Cada um deve passar a ser representado como entidade, evento, estado ou snapshot próprio, preservando identidade, temporalidade, ator, contexto e proveniência quando sustentados pelas evidências.

Use como fontes o candidato conceitual atual, o registro semântico promovido, o manifesto promovido e o template do estágio 02.

## Limites obrigatórios

- Não altere nem repita as 13 entidades existentes: `COMPETICAO`, `PARTIDA`, `EQUIPE`, `ATLETA`, `PERIODO_SET`, `SHOOT_OUT`, `POSSE_DE_BOLA`, `UNIDADE_BASICA_ATAQUE_BOU`, `EVENTO_SCOUT`, `OBSERVACAO_DE_SCOUT`, `ANALISTA_OBSERVADOR`, `PROTOCOLO_SCOUT`, `MIDIA_VIDEO`.
- Crie exatamente uma entidade para cada um dos dez conceitos críticos, usando o próprio `concept_id` como `id` da entidade.
- Não crie novos conceitos, regras, evidências ou IDs de fonte.
- Relacionamentos podem usar como extremidades somente as 13 entidades existentes e as 10 novas entidades.
- Use `rule_ids` somente quando existirem literalmente no registro semântico promovido.
- Use `evidence_ref_ids` somente quando existirem literalmente no manifesto promovido.
- Não produza envelope `document`, SQL, tabelas, colunas, índices ou políticas de acesso.

## Estrutura das entidades

Cada item de `entities` deve conter exatamente:

- `id`;
- `name`;
- `concept_id`;
- `definition`;
- `identity_rule`;
- `temporality`: `ATEMPORAL|INSTANTANEA|INTERVALO|VERSIONADA|EVENTO`;
- `history_required`, booleano;
- `aggregate_root`, booleano;
- `rule_ids`, como lista;
- `evidence_ref_ids`, como lista.

## Estrutura dos relacionamentos

Cada item de `relationships` deve conter exatamente:

- `id`, em `UPPER_SNAKE_CASE`;
- `name`;
- `from_entity_id` e `to_entity_id`;
- `meaning`;
- `cardinality.from_to.min` e `cardinality.to_from.min`, usando apenas `0` ou `1`;
- `cardinality.from_to.max` e `cardinality.to_from.max`, usando apenas `1` ou `N`;
- `relationship_attributes`, `exclusivity_rules`, `rule_ids` e `evidence_ref_ids`, como listas;
- `temporality`.

## Estrutura dos invariantes

Cada item de `domain_invariants` deve conter exatamente:

- `id`, em `UPPER_SNAKE_CASE`;
- `statement`;
- `affected_entity_ids`;
- `rule_ids`;
- `evidence_ref_ids`.

Crie invariantes somente quando necessários para preservar identidade, temporalidade ou exclusividade das novas entidades.

## Atualização da cobertura

Em `coverage_updates`:

- `promote_to_covered_concept_ids` deve conter exatamente os dez conceitos críticos;
- `remove_open_issue_ids` deve conter exatamente os dez IDs `ISSUE_COVERAGE_<CONCEPT_ID>` correspondentes;
- `remaining_open_issues` deve conter apenas novas pendências materiais introduzidas pela revisão; use lista vazia quando não houver.

Retorne somente YAML válido, sem título, comentário ou cerca Markdown, nesta raiz:

```yaml
conceptual_model_revision:
  entities: []
  relationships: []
  domain_invariants: []
  coverage_updates:
    promote_to_covered_concept_ids: []
    remove_open_issue_ids: []
    remaining_open_issues: []
```
