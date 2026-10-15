# Estágio 07 — Recomendar o STOP GATE físico

Produza somente o corpo proposto para `07-stop-gate-PARTIDAS_SCOUT_ANALISE_TATICA.yaml`.

As fontes selecionadas explicitamente contêm as versões promovidas dos estágios 00 a 06 e o template do estágio 07. Avalie exclusivamente esse conjunto. Não recupere nem use artefatos históricos, fontes avulsas do caderno ou conhecimento externo.

Não produza o envelope `document`. `run_id`, `notebook_id`, versões, hashes, `promoted_source_id`, timestamps, estado, aprovação e promoção pertencem ao operador.

## Entradas promovidas obrigatórias

- `SOURCE_MANIFEST` v0.1.0;
- `SEMANTIC_REGISTRY` v0.1.0;
- `CONCEPTUAL_MODEL` v0.1.1;
- `LOGICAL_MODEL` v0.1.0;
- `DATA_DICTIONARY` v0.1.0;
- `TRACEABILITY_MATRIX` v0.1.0;
- `ACCESS_REQUIREMENTS` v0.1.0.

## Regra de decisão

1. Avalie cada critério do template como `PASS`, `FAIL`, `BLOCKED` ou `NAO_APLICAVEL`.
2. Todo `PASS` deve apontar para IDs existentes nas entradas promovidas. Não invente IDs de evidência.
3. Uma obrigação com prazo `ANTES_DO_STOP_GATE_FISICO` ainda não cumprida bloqueia o critério afetado e impede `READY` e `READY_WITH_RESTRICTIONS`.
4. `READY_WITH_RESTRICTIONS` só é válido quando os elementos excluídos são independentes e o restante do escopo satisfaz todos os pré-requisitos.
5. Lacunas factuais históricas devem ser isoladas do modelo estrutural quando não impedirem a criação do schema, mas devem excluir a carga ou afirmação dos dados afetados.
6. Uma pendência registrada em artefato anterior pode ser considerada superada somente se um artefato promovido posterior trouxer evidência inequívoca de resolução.
7. O escopo físico recomendado deve ser uma lista objetiva de estruturas autorizáveis. Se a recomendação for `BLOCKED`, deixe `recommended_scope` vazio e registre em `excluded_scope` o escopo ainda não autorizável.
8. Não gere SQL e não autorize o avanço. A recomendação permanece `PROPOSTO` até decisão humana.

## Pontos que exigem confronto explícito

- A revisão do estágio 05 registrou 68 derivações aceitas, 9 condicionais formalizadas e 2 divergências reconciliadas.
- Verifique o requisito de retropropagar as 9 formalizações e as 2 reconciliações aos modelos conceitual e lógico antes do `STOP GATE` físico.
- O estágio 06 resolveu a pendência de requisitos de acesso do estágio 05; trate a matriz como imutável e use o artefato promovido posterior como evidência da resolução.
- A autoconsulta do atleta está excluída até existir vínculo confiável de identidade.
- A implementação de RBAC/RLS exige atribuição de papéis auditável, com vigência e sem autoatribuição.
- A revisão de scout exige papel distinto e proibição de autorrevisão.
- Somente os nove recursos `PUBLICO` podem ser candidatos à Data API nesta versão; os outros 23 permanecem fechados.
- A lacuna de placares históricos detalhados de shoot-out e etapas não deve ser preenchida por inferência.

## Estrutura obrigatória

Siga exatamente os campos de `criteria`, `recommendation`, `recommended_scope`, `excluded_scope`, `restrictions`, `required_human_decisions` e `open_issues` do template selecionado.

Retorne somente YAML válido, sem título, comentário ou cerca Markdown, nesta raiz:

```yaml
criteria: []
recommendation: "READY|READY_WITH_RESTRICTIONS|BLOCKED"
recommended_scope: []
excluded_scope: []
restrictions: []
required_human_decisions: []
open_issues: []
```
