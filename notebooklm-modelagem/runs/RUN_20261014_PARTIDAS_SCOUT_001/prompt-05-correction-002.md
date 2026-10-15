# Segunda correção do estágio 05 — Conformidade literal com o template

Gere novamente somente o corpo YAML da matriz. Preserve o domínio correto e as 11 regras da tentativa anterior, mas descarte toda a estrutura de campos produzida anteriormente.

Não traduza, adapte, qualifique ou invente IDs. Quando não localizar um ID literal nas fontes promovidas, use uma lista vazia e registre a lacuna em `open_issues` com o esquema abaixo.

## Raiz obrigatória

A saída deve começar no primeiro caractere por `phase: "PLANNED"` e possuir exatamente estas cinco chaves de raiz:

```yaml
phase: "PLANNED"
traces: []
coverage_summary: {}
orphan_checks: {}
open_issues: []
```

Não inclua título Markdown, cerca de código, texto introdutório ou comentário.

## Esqueleto literal de cada traço

Cada item de `traces` deve possuir todas e somente estas 14 chaves, com estes nomes:

```yaml
- id: "TRACE_PARTIDAS_SCOUT_001"
  evidence_ref_ids: []
  concept_ids: []
  rule_ids: []
  conceptual_entity_ids: []
  relationship_ids: []
  logical_relation_ids: []
  attribute_ids: []
  physical_object_ids: []
  permission_requirement_ids: []
  test_ids: []
  implementation_status: "CANDIDATO"
  verification_status: "NAO_EXECUTADO"
  verification_evidence_ids: []
```

É proibido usar `trace_id`, `conceptual_relation_ids`, `physical_candidate_ids` ou qualquer campo alternativo.

## Regras de referência

1. Cubra exatamente as 11 regras semânticas permitidas na correção anterior; cada regra deve aparecer pelo menos uma vez.
2. Preserve apenas referências de evidência que existam literalmente no manifesto promovido.
3. `concept_ids`, `conceptual_entity_ids` e `relationship_ids` devem usar somente IDs literais dos artefatos promovidos.
4. `logical_relation_ids` deve usar somente uma das 32 relações lógicas permitidas na correção anterior.
5. Se `attribute_ids` não estiver vazio, o traço deve possuir exatamente uma relação lógica e cada atributo deve ser um `attribute_id` literal dessa relação. Não use inglês inventado, `tabela.coluna`, nome físico ou tradução. É preferível `attribute_ids: []` a um ID inexistente.
6. `physical_object_ids` usa somente `TABLE_<RELATION_ID>` e `COLUMN_<RELATION_ID>_<ATTRIBUTE_ID>` quando a relação ou o atributo literal estiver presente no mesmo traço.
7. `permission_requirement_ids` contém somente IDs planejados em `UPPER_SNAKE_CASE`; use lista vazia quando o requisito depender do estágio 06.
8. `test_ids` usa somente `TEST_PARTIDAS_SCOUT_<NNN>` e cada teste deve estar associado a uma regra no mesmo traço.
9. Use apenas `implementation_status: "CANDIDATO"` ou `"NAO_INICIADO"`.
10. Todos os traços usam `verification_status: "NAO_EXECUTADO"` e `verification_evidence_ids: []`.

## Esqueleto literal do resumo

Use somente estes campos e calcule-os a partir dos traços:

```yaml
coverage_summary:
  source_rules_total: 11
  rules_with_logical_mapping: 0
  rules_with_physical_mapping: 0
  material_constraints_total: 0
  material_constraints_with_tests: 0
  unresolved_trace_ids: []
```

Não use `total_rules`, `covered_rules`, percentuais, `implementation_breakdown` ou `verification_breakdown`.

## Esqueleto literal de órfãos

Use exatamente estas seis chaves:

```yaml
orphan_checks:
  sources_without_use: []
  rules_without_source: []
  entities_without_rules: []
  attributes_without_definition: []
  physical_objects_without_logical_origin: []
  tests_without_rule: []
```

## Esqueleto literal de pendência

Cada pendência deve possuir todas e somente estas chaves:

```yaml
- id: "ISSUE_PARTIDAS_SCOUT_001"
  status: "ABERTA"
  question: "Questão objetiva"
  affected_ids: []
  impact: "Consequência concreta"
  required_evidence: "Fonte ou decisão necessária"
  owner: "RESPONSAVEL"
```

É proibido usar `description` ou `required_action`. Preserve a lacuna histórica de placar e shoot-out sem declarar resolução. Não reabra questões de migrations, RLS ou DDL históricos que não pertençam à matriz planejada deste domínio.
