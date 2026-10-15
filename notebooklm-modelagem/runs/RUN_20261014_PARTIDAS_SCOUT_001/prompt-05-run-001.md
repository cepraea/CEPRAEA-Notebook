# Estágio 05 — Propor matriz de rastreabilidade planejada

Produza somente o corpo proposto para `05-matriz-rastreabilidade-planejada.yaml`, com `phase: "PLANNED"`.

O manifesto, o registro semântico, o modelo conceitual, o modelo lógico, o dicionário de dados promovido e o template do estágio 05 estão entre as fontes explicitamente selecionadas. As demais fontes selecionadas são controles de formato e operação.

Não produza o envelope `document`. `run_id`, `notebook_id`, versões, hashes, `promoted_source_id`, timestamps, estado, aprovação e promoção pertencem ao operador.

## Entradas promovidas

- `SOURCE_MANIFEST` v0.1.0;
- `SEMANTIC_REGISTRY` v0.1.0;
- `CONCEPTUAL_MODEL` v0.1.1;
- `LOGICAL_MODEL` v0.1.0;
- `DATA_DICTIONARY` v0.1.0.

## Cobertura obrigatória

As entradas promovidas contêm exatamente:

- 290 referências de evidência no manifesto;
- 47 conceitos e 11 regras no registro semântico;
- 29 entidades, 47 relações e 23 invariantes no modelo conceitual;
- 32 relações e 204 atributos no modelo lógico;
- 32 tabelas candidatas e 204 colunas no dicionário de dados.

A matriz deve permitir verificar a cobertura das 11 regras e de toda restrição material identificável. Não invente referências para eliminar órfãos: registre os órfãos e as lacunas verdadeiras nas listas correspondentes e em `open_issues` quando exigirem decisão ou artefato posterior.

## Tarefa

1. Crie traços estáveis que liguem `evidence_ref_ids`, `concept_ids` e `rule_ids` aos elementos conceituais, lógicos e aos atributos correspondentes.
2. Use somente IDs existentes nas entradas promovidas para evidências, conceitos, regras, entidades, relações, relações lógicas e atributos.
3. Registre em `physical_object_ids` somente candidatos derivados inequivocamente dos nomes físicos do dicionário. Não alegue que esses objetos existem no PostgreSQL.
4. Planeje `permission_requirement_ids` somente quando a regra ou a classificação de acesso exigir controle; use IDs em `UPPER_SNAKE_CASE` que possam ser reconciliados pelo estágio 06.
5. Planeje `test_ids` para cada regra ou restrição material verificável; use `TEST_<DOMINIO>_<NNN>` sem alegar criação ou execução do teste.
6. Use `implementation_status: "CANDIDATO"` quando houver mapeamento lógico ou físico candidato e `"NAO_INICIADO"` quando ainda faltar o artefato planejado. Não use `IMPLEMENTADO`.
7. Use sempre `verification_status: "NAO_EXECUTADO"` e `verification_evidence_ids: []`. Não use `PASS` ou `FAIL`.
8. Calcule `coverage_summary` a partir dos traços emitidos. `rules_with_physical_mapping` contabiliza apenas regras com candidato físico identificado, não implementação.
9. Em `material_constraints_total`, conte regras, checks, unicidades, FKs obrigatórias e demais invariantes materiais sem duplicar a mesma restrição semântica. Explique qualquer impossibilidade de contagem em `open_issues`.
10. Execute as seis verificações de órfãos do template nos dois sentidos e liste IDs concretos, sem texto genérico.
11. Preserve a pendência histórica de placar e shoot-out como não resolvida quando ela afetar a rastreabilidade.
12. Não gere SQL, DDL, grants, RLS, policies ou resultados de teste.

## Estrutura obrigatória

Siga exatamente os campos de `phase`, `traces`, `coverage_summary`, `orphan_checks` e `open_issues` do template selecionado.

Retorne somente YAML válido, sem título, comentário ou cerca Markdown, nesta raiz:

```yaml
phase: "PLANNED"
traces: []
coverage_summary: {}
orphan_checks: {}
open_issues: []
```
