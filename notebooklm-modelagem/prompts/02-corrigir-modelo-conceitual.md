# Prompt 02B — Corrigir o modelo conceitual rejeitado

Corrija integralmente o relatório conceitual rejeitado usando o registro semântico promovido, o manifesto promovido e o template do estágio 02.

Preserve somente conteúdo sustentado pelas fontes selecionadas. A correção está limitada à estrutura do template e aos IDs promovidos: não crie conceitos, regras ou evidências.

## Erros que devem ser removidos

- Não use `description`, `identity`, `history_policy` ou `boundaries` em entidades.
- Não use `source_entity`, `target_entity`, `semantics`, `forward_cardinality` ou `reverse_cardinality` em relacionamentos.
- Não use `description` ou `enforced_entities` em invariantes.
- Não use IDs `CPT_*`, IDs com hífen ou IDs com ponto.
- Não inclua carga de treinamento, saúde, gestão financeira, DDL, PostgreSQL ou RLS na cobertura.

## IDs permitidos

Use `concept_id` somente desta lista:

`PARTIDA`, `EQUIPE`, `ATLETA`, `GOLEIRA_POSICAO`, `PERIODO_SET`, `GOL_DE_OURO`, `SHOOT_OUT`, `GOL_SIMPLES`, `GOL_DUPLO`, `SPIN_SHOT`, `IN_FLIGHT_SHOT`, `TIRO_SEIS_METROS`, `EXCLUSAO_DISCIPLINAR`, `DESQUALIFICACAO_SEGUNDA_EXCLUSAO`, `CARTAO_AZUL_SUSPENSAO`, `POSSE_DE_BOLA`, `UNIDADE_BASICA_ATAQUE_BOU`, `FASE_TATICA`, `SISTEMA_TATICO`, `ZONA_ANALITICA_QUADRA`, `PROTOCOLO_SCOUT`, `CONFIABILIDADE_OBSERVADOR`, `EVENTO_SCOUT`, `ANALISTA_OBSERVADOR`, `TIMECODE`, `TRECHO_OBSERVADO`, `COMPETICAO`, `PAPEL_ESPORTIVO_OPERACIONAL`, `SEGMENTO_OBSERVADO`, `PLACAR_JOGO`, `ESTADO_DO_PLACAR`, `EVOLUCAO_DO_PLACAR`, `EVENTO_DE_PONTUACAO`, `PUNICAO_DISCIPLINAR`, `CONSEQUENCIA_DISCIPLINAR`, `FASE_OFENSIVA`, `FASE_DEFENSIVA`, `SISTEMA_DEFENSIVO`, `ACAO_DA_GOLEIRA`, `ACAO_OBSERVADA`, `RESULTADO_DA_ACAO`, `OBSERVACAO_DE_SCOUT`, `VERSAO_PROTOCOLO_SCOUT`, `REVISAO_DA_OBSERVACAO`, `ESTADO_DE_REVISAO`, `MIDIA_VIDEO`, `PROVENIENCIA_OBSERVACAO`.

Use `rule_ids` somente desta lista:

`RN_IHF_VIGENCIA_2026`, `RN_SGATE_0023_PONTUACAO_FHERJ_2026`, `RN_SEMANTICA_GOLEIRA`, `RN_TETO_PARTICIPANTES_SUMULA`, `RN_REJEICAO_VARIAVEIS_INFERENCIAIS`, `RN_PASSIVO_QUATRO_PASSES`, `RN_SANCAO_FINAL_15_SEGUNDOS`, `RN_PROTECAO_CABECA_GOLEIRA`, `RN_PROIBICAO_RETARDO_REPETIDO`, `RN_PRAZO_INSCRICAO_ATLETA_72H`, `RN_REGRAS_EXECUCAO_TIRO_SEIS_METROS`.

Use `evidence_ref_ids` somente quando o ID existir literalmente no manifesto promovido.

## Estrutura obrigatória

Cada entidade deve conter exatamente:

- `id`, em `UPPER_SNAKE_CASE`;
- `name`;
- `concept_id`, usando um ID permitido;
- `definition`;
- `identity_rule`;
- `temporality`: `ATEMPORAL|INSTANTANEA|INTERVALO|VERSIONADA|EVENTO`;
- `history_required`, booleano;
- `aggregate_root`, booleano;
- `rule_ids`, como lista;
- `evidence_ref_ids`, como lista.

Cada relacionamento deve conter exatamente:

- `id`, em `UPPER_SNAKE_CASE`;
- `name`;
- `from_entity_id` e `to_entity_id`, referenciando entidades declaradas;
- `meaning`;
- `cardinality.from_to.min`, `cardinality.from_to.max`, `cardinality.to_from.min` e `cardinality.to_from.max`; use inteiro para `min` e `1` ou `N` para `max`;
- `relationship_attributes`, `exclusivity_rules`, `rule_ids` e `evidence_ref_ids`, como listas;
- `temporality`.

Cada invariante deve conter exatamente:

- `id`, em `UPPER_SNAKE_CASE`;
- `statement`;
- `affected_entity_ids`, referenciando entidades declaradas;
- `rule_ids`, usando somente IDs permitidos;
- `evidence_ref_ids`, usando somente evidências existentes.

## Cobertura obrigatória

Em `coverage.required_concept_ids`, copie exatamente os 47 IDs permitidos, sem omissões ou acréscimos.

`covered_concept_ids` e `excluded_concept_ids` devem:

- conter somente IDs de `required_concept_ids`;
- ser disjuntos;
- em conjunto, classificar todos os 47 conceitos;
- considerar um conceito coberto quando ele estiver representado como entidade ou for materializado por relacionamento, atributo de relacionamento ou invariante;
- excluir somente quando houver justificativa conceitual real, registrando-a em `open_issues`.

Não transforme todo conceito em entidade apenas para aumentar a cobertura.

Retorne somente YAML válido, sem título, comentário ou cerca Markdown, nesta raiz:

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
