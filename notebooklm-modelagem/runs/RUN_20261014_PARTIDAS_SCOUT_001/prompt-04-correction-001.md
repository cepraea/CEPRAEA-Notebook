# Estágio 04 — Corrigir o dicionário de dados para o contrato canônico

Produza somente o corpo corrigido para `04-dicionario-dados.yaml`.

Use o modelo lógico promovido como autoridade estrutural. Use o relatório anterior do estágio 04 somente para reaproveitar descrições, tipos candidatos, classificações de acesso, semânticas de ausência e catálogos que sejam compatíveis com o modelo lógico. O template do estágio 04 é a autoridade para nomes e campos da saída.

Não produza o envelope `document`. Campos operacionais pertencem ao operador.

## Falhas que devem ser corrigidas

O relatório anterior cobriu as 32 relações e os 204 atributos, mas foi reprovado porque:

- renomeou campos do template;
- renomeou 23 IDs de FK;
- declarou 24 unicidades, incluindo 6 não existentes, quando o modelo lógico contém exatamente 18;
- não apresentou todos os metadados obrigatórios das colunas;
- usou uma estrutura de catálogos diferente do template;
- adicionou um título Markdown antes do YAML.

## Regras estruturais obrigatórias

1. Retorne exatamente a raiz `data_dictionary` com `tables`, `catalogs` e `open_issues`.
2. Produza exatamente 32 tabelas e 204 colunas, sem adicionar, remover, renomear, fundir ou dividir relações e atributos do modelo lógico.
3. Em cada tabela, use exatamente estes campos:
   - `relation_id`
   - `schema_candidate`
   - `table_candidate`
   - `description`
   - `grain`
   - `ownership_domain`
   - `access_classification`
   - `columns`
   - `primary_key_attribute_ids`
   - `foreign_key_ids`
   - `unique_constraint_ids`
   - `check_constraint_ids`
   - `index_candidates`
   - `retention_rule_ids`
4. Em cada coluna, use exatamente estes campos:
   - `attribute_id`
   - `column_candidate`
   - `description`
   - `postgresql_type_candidate`
   - `nullable`
   - `null_meaning`
   - `default_candidate`
   - `unit`
   - `format`
   - `allowed_values`
   - `min_value`
   - `max_value`
   - `pii`
   - `sensitive`
   - `generated`
   - `derivation_rule_id`
   - `rule_ids`
   - `evidence_ref_ids`
5. `attribute_id` é único somente no escopo de sua relação. Repetições como `ID`, `PARTIDA_ID` e `EQUIPE_ID` entre tabelas são válidas.
6. Preserve exatamente os 59 IDs de FK, os 18 IDs de `unique_constraints` e os 13 IDs de checks existentes no modelo lógico. Não crie nem renomeie constraints.
7. `primary_key_attribute_ids` deve corresponder a `identity.attribute_ids` da relação lógica.
8. Para cada FK com `supporting_index_required: true`, crie um índice de suporte com os campos exatos `id`, `attribute_ids`, `purpose` e `rationale`. Use `purpose: "FK"` e preserve os IDs das FKs na justificativa.
9. Índices adicionais exigem padrão de consulta, unicidade ou RLS demonstrado e justificativa específica.
10. Preserve `nullable`, `null_meaning`, `derived`, `derivation_rule_id`, `rule_ids`, `evidence_ref_ids`, `domain_values` e `retention_rule_ids` do modelo lógico. `generated` corresponde a `derived`; `allowed_values` corresponde a `domain_values`.
11. Escreva uma definição operacional específica em `description` para cada uma das 204 colunas. Não use apenas o nome lógico como definição.
12. Use `null` para `unit`, `format`, limites e default quando as fontes não sustentarem valor mais específico. Não invente precisão, unidade, padrão, limite ou default.
13. Classifique `pii` e `sensitive` conservadoramente com base no significado da coluna e nas fontes. Quando a classificação depender de decisão humana ausente, registre pendência rastreável em vez de presumir que o dado é público.
14. Não use `jsonb`, não gere SQL e não converta catálogos em enums PostgreSQL.
15. Em `catalogs`, use exatamente `id`, `name`, `versioned` e `values`; cada valor usa exatamente `code`, `label`, `valid_from`, `valid_to` e `evidence_ref_ids`. Não invente códigos além dos `domain_values` do modelo lógico.
16. Preserve `ISSUE_LACUNA_PLACAR_SHOOTOUT_E_ETAPAS` como pendência aberta. Qualquer nova pendência deve usar exatamente os campos do contrato e apontar uma decisão ou evidência realmente ausente.

Retorne somente YAML válido, sem título, explicação, comentário ou cerca Markdown, nesta raiz:

```yaml
data_dictionary:
  tables: []
  catalogs: []
  open_issues: []
```
