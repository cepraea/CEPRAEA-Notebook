# Estágio 07 — Reavaliar o STOP GATE após retropropagação

Produza somente o corpo proposto para `07-stop-gate-PARTIDAS_SCOUT_ANALISE_TATICA.yaml`.

Avalie exclusivamente as fontes selecionadas: os artefatos promovidos 00 e 01, as novas versões promovidas 02 e 03, os artefatos promovidos 04 a 06 e o template do estágio 07. Não use fontes históricas avulsas do caderno.

Não produza o envelope `document`. `run_id`, `notebook_id`, hashes, IDs promovidos, timestamps, aprovação e promoção pertencem ao operador.

## Entradas promovidas

- `SOURCE_MANIFEST` v0.1.0;
- `SEMANTIC_REGISTRY` v0.1.0;
- `CONCEPTUAL_MODEL` v0.1.2, que substitui v0.1.1;
- `LOGICAL_MODEL` v0.1.1, que substitui v0.1.0;
- `DATA_DICTIONARY` v0.1.0;
- `TRACEABILITY_MATRIX` v0.1.0;
- `ACCESS_REQUIREMENTS` v0.1.0.

## Reconciliação concluída

As novas versões conceitual e lógica retropropagam as 9 formalizações e as 2 reconciliações do estágio 05:

- sete relacionamentos conceituais específicos para as FKs condicionais;
- unicidade contextual de papel regulamentar e condição de mando;
- cardinalidade de zero a muitos trechos por evento, com remoção de `UQ_TRECHO_EVENTO`;
- separação entre `CHK_INTERVALO_VIGENCIA_PARTICIPACAO` e a não sobreposição candidata `EXCL_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA`.

Não mantenha o bloqueio anterior se as novas fontes comprovarem esses pontos.

## Regra de decisão

1. Avalie exatamente os sete critérios `GATE_*` do template.
2. Todo `PASS` deve possuir referência identificável existente nas fontes selecionadas.
3. Emita `READY_WITH_RESTRICTIONS` somente quando cada limitação for independente, explícita e não comprometer o restante do escopo.
4. O dicionário v0.1.0 antecede a reconciliação e ainda pode citar `UQ_TRECHO_EVENTO` e `CHK_VIGENCIA_PARTICIPACAO`. Compare-o com o modelo lógico v0.1.1 e a matriz promovida. Não trate esses IDs antigos como implementáveis; determine se a divergência está isolada o bastante para restrição ou se bloqueia o gate.
5. A lacuna de placares históricos restringe a carga dos fatos afetados; não preencha lacunas por inferência.
6. A autoconsulta do atleta permanece excluída até existir vínculo confiável de identidade.
7. Atribuição de papéis exige vigência, auditoria, responsável e proibição de autoatribuição.
8. Revisão de scout exige revisor distinto do analista original.
9. Somente os nove recursos `PUBLICO` podem ser candidatos à Data API; os 23 recursos `INTERNO` ou `RESTRITO` permanecem fechados.
10. Não gere SQL e não autorize o avanço. A decisão vinculante pertence ao responsável humano.

Retorne somente YAML válido, sem título, comentário ou cerca Markdown, nesta raiz exata:

```yaml
criteria: []
recommendation: "READY|READY_WITH_RESTRICTIONS|BLOCKED"
recommended_scope: []
excluded_scope: []
restrictions: []
required_human_decisions: []
open_issues: []
```
