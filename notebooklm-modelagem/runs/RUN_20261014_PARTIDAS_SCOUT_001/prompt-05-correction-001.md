# Correção do estágio 05 — Limitar a matriz ao domínio promovido

Descarte integralmente a resposta anterior e gere novamente somente o corpo YAML da matriz de rastreabilidade planejada.

A resposta anterior foi rejeitada porque misturou disponibilidade, presença e treinamento; usou IDs inexistentes nas entradas promovidas; criou chaves fora do template; usou nomes físicos históricos; e adicionou um título Markdown.

## Domínio exclusivo

Trabalhe exclusivamente com `PARTIDAS_SCOUT_ANALISE_TATICA`.

Não use IDs ou termos históricos como `RN-DISP-*`, `DEC-DATA-*`, `AVAILABILITY_DECLARATION`, `FACTUAL_PRESENCE`, `CALENDAR_EVENT`, `SESSION_SEGMENT`, `PLANNED_TRAINING_LOAD`, `LOG_REL_*` ou tabelas `public.*` que não existam no dicionário promovido.

As únicas regras semânticas permitidas são:

- `RN_IHF_VIGENCIA_2026`;
- `RN_SGATE_0023_PONTUACAO_FHERJ_2026`;
- `RN_SEMANTICA_GOLEIRA`;
- `RN_TETO_PARTICIPANTES_SUMULA`;
- `RN_REJEICAO_VARIAVEIS_INFERENCIAIS`;
- `RN_PASSIVO_QUATRO_PASSES`;
- `RN_SANCAO_FINAL_15_SEGUNDOS`;
- `RN_PROTECAO_CABECA_GOLEIRA`;
- `RN_PROIBICAO_RETARDO_REPETIDO`;
- `RN_PRAZO_INSCRICAO_ATLETA_72H`;
- `RN_REGRAS_EXECUCAO_TIRO_SEIS_METROS`.

As únicas relações lógicas permitidas são:

- `COMPETICAO`, `PARTIDA`, `EQUIPE`, `ATLETA`, `PARTIDA_EQUIPE`;
- `EQUIPE_ATLETA_INSCRICAO`, `PERIODO_SET`, `SHOOT_OUT`, `POSSE_DE_BOLA`;
- `UNIDADE_BASICA_ATAQUE_BOU`, `EVENTO_SCOUT`, `OBSERVACAO_DE_SCOUT`;
- `ANALISTA_OBSERVADOR`, `PROTOCOLO_SCOUT`, `MIDIA_VIDEO`, `SEGMENTO_OBSERVADO`;
- `PLACAR_JOGO`, `ESTADO_DO_PLACAR`, `EVOLUCAO_DO_PLACAR`;
- `SISTEMA_DEFENSIVO`, `CONFIABILIDADE_OBSERVADOR`, `REVISAO_DA_OBSERVACAO`;
- `ESTADO_DE_REVISAO`, `PROVENIENCIA_OBSERVACAO`, `TRECHO_OBSERVADO`;
- `SPIN_SHOT`, `IN_FLIGHT_SHOT`, `DESQUALIFICACAO_SEGUNDA_EXCLUSAO`;
- `CARTAO_AZUL_SUSPENSAO`, `SISTEMA_TATICO`, `PAPEL_ESPORTIVO_OPERACIONAL`;
- `PARTICIPACAO_EQUIPE_COMPETICAO`.

Conceitos, entidades, relações conceituais, atributos e evidências só são permitidos quando o ID existir literalmente nos artefatos promovidos selecionados.

## Correções estruturais obrigatórias

1. Comece diretamente por `phase: "PLANNED"`. Não inclua H1, texto introdutório, comentários ou cerca Markdown.
2. Cada item de `traces` deve conter exatamente os campos do template.
3. Use a chave `relationship_ids`; a chave `conceptual_relation_ids` é proibida.
4. `orphan_checks` deve conter exatamente estas seis chaves:
   - `sources_without_use`;
   - `rules_without_source`;
   - `entities_without_rules`;
   - `attributes_without_definition`;
   - `physical_objects_without_logical_origin`;
   - `tests_without_rule`.
5. IDs de atributos são escopados por relação. Quando `attribute_ids` não estiver vazio, inclua somente uma relação em `logical_relation_ids` no mesmo traço e use os `attribute_id` literais dessa relação, sem `tabela.coluna`.
6. Para candidatos físicos, use somente IDs determinísticos:
   - tabela: `TABLE_<RELATION_ID>`;
   - coluna: `COLUMN_<RELATION_ID>_<ATTRIBUTE_ID>`.
7. Cada uma das 11 regras deve aparecer em pelo menos um traço e conservar seus `evidence_ref_ids` reais.
8. Não crie traços para preencher números. Registre ausência real em `orphan_checks` ou `open_issues`.
9. Toda restrição material testável deve possuir pelo menos um `test_id` planejado no padrão `TEST_PARTIDAS_SCOUT_<NNN>`.
10. `implementation_status` aceita nesta etapa somente `"CANDIDATO"` ou `"NAO_INICIADO"`.
11. Todos os traços devem usar `verification_status: "NAO_EXECUTADO"` e `verification_evidence_ids: []`.
12. Não afirme que DDL, policies, migrations ou testes existem ou foram executados.

## Estrutura de saída

Retorne somente YAML válido com estas cinco chaves de raiz, nesta ordem:

```yaml
phase: "PLANNED"
traces: []
coverage_summary: {}
orphan_checks: {}
open_issues: []
```
