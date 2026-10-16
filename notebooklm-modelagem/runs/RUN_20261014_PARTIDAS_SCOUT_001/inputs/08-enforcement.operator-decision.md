# Decisão externa do operador — reconciliação do `STAGE_08`

```yaml
schema_version: "1.0"
decision_id: "STAGE_08_ENFORCEMENT_REVIEW"
version: "1.0.0"
run_id: "RUN_20261014_PARTIDAS_SCOUT_001"
stage_id: "STAGE_08"
status: "APROVADO"
responsible: "USER"
decided_at: "2026-10-15T16:37:34-03:00"
authorization: "Reconciliar o enforcement, retropropagar as mudanças indispensáveis e regenerar somente o schema PostgreSQL candidato."
scope:
  relation_count: 32
  add_relations: false
  add_attributes: false
  execute_sql: false
  generate_migration: false
  generate_rls: false
declarative_check_constraints:
  - id: "CHK_PARTIDA_VIGENCIA_2026"
    enforcement: "CHECK"
  - id: "CHK_NUMERO_SET_VALIDO"
    enforcement: "CHECK"
  - id: "CHK_SHOOT_OUT_COMPLETUDE"
    enforcement: "CHECK"
  - id: "CHK_ELEGIBILIDADE_RANKING_CONTEXTUAL"
    enforcement: "CHECK"
  - id: "CHK_INTERVALO_VIGENCIA_PARTICIPACAO"
    enforcement: "CHECK"
structural_invariants:
  - id: "INV_ATLETA_SEMANTICA_GOLEIRA"
    replaces: "CHK_ATLETA_SEMANTICA_GOLEIRA"
    enforcement: "SCHEMA_SHAPE_TEST"
    rationale: "GOLEIRA é valor da posição de ATLETA; não existe função defensiva de linha que permita um predicado CHECK fiel."
  - id: "INV_BOU_REJEICAO_INFERENCIAIS"
    replaces: "CHK_BOU_REJEICAO_INFERENCIAIS"
    enforcement: "SCHEMA_SHAPE_TEST"
    rationale: "A proibição é preservada pela ausência de atributos inferenciais na relação BOU."
  - id: "INV_OBSERVACAO_REJEICAO_INFERENCIAIS"
    replaces: "CHK_REJEICAO_VARIAVEIS_INFERENCIAIS"
    enforcement: "SCHEMA_SHAPE_TEST"
    rationale: "A proibição é preservada pela ausência de atributos inferenciais na observação primária."
deferred_rules:
  - id: "RN_TETO_PARTICIPANTES_SUMULA"
    former_check_id: "CHK_TETO_PARTICIPANTES_SUMULA"
    reason: "O modelo não registra o elenco de atletas e oficiais da súmula por partida."
  - id: "RN_PRAZO_INSCRICAO_ATLETA_72H"
    former_check_id: "CHK_PRAZO_INSCRICAO_72H"
    reason: "A inscrição não referencia o marco temporal específico da partida ou do prazo oficial aplicável."
  - id: "RN_PASSIVO_QUATRO_PASSES"
    former_check_id: "CHK_PASSIVO_QUATRO_PASSES"
    reason: "O modelo não registra o sinal de passivo nem a contagem de passes posteriores."
  - id: "RN_PROTECAO_CABECA_GOLEIRA"
    former_check_id: "CHK_PROTECAO_CABECA_GOLEIRA"
    reason: "O evento não registra impacto na cabeça, condição de arremessador desmarcado ou simulação."
  - id: "RN_REGRAS_EXECUCAO_TIRO_SEIS_METROS"
    former_check_id: "CHK_REGRAS_EXECUCAO_TIRO_SEIS_METROS"
    reason: "O evento não registra execução direta, tempo de execução e distância defensiva."
required_physical_outputs:
  - "Emitir ON DELETE e ON UPDATE nas 59 FKs conforme o modelo lógico."
  - "Emitir UQ_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA."
  - "Emitir EXCL_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA com EXCLUDE USING gist."
  - "Declarar CREATE EXTENSION IF NOT EXISTS btree_gist como dependência candidata não verificada."
  - "Não emitir constraints para invariantes estruturais ou regras adiadas."
  - "Não reintroduzir UQ_TRECHO_EVENTO ou CHK_VIGENCIA_PARTICIPACAO, nem em comentários."
result: "AUTHORIZED_TO_RECONCILE_AND_REGENERATE_CANDIDATE"
```
