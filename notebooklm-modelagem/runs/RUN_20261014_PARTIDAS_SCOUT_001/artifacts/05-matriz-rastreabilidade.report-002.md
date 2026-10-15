phase: "PLANNED"
traces:
  - trace_id: "TRACE_PARTIDAS_SCOUT_001"
    rule_ids:
      - "RN_IHF_VIGENCIA_2026"
    evidence_ref_ids:
      - "EVID_IHF_RULES_2026_EN_001"
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_001"
    logical_relation_ids:
      - "COMPETICAO"
    attribute_ids:
      - "valid_from"
    relationship_ids: []
    physical_candidate_ids:
      - "TABLE_COMPETICAO"
      - "COLUMN_COMPETICAO_VALID_FROM"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_001"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - trace_id: "TRACE_PARTIDAS_SCOUT_002"
    rule_ids:
      - "RN_SGATE_0023_PONTUACAO_FHERJ_2026"
    evidence_ref_ids:
      - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_006"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_027"
    logical_relation_ids:
      - "COMPETICAO"
    attribute_ids:
      - "scoring_table"
    relationship_ids: []
    physical_candidate_ids:
      - "TABLE_COMPETICAO"
      - "COLUMN_COMPETICAO_SCORING_TABLE"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_002"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - trace_id: "TRACE_PARTIDAS_SCOUT_003"
    rule_ids:
      - "RN_SEMANTICA_GOLEIRA"
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_004"
      - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_007"
    logical_relation_ids:
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    attribute_ids:
      - "position_name"
      - "function_name"
    relationship_ids: []
    physical_candidate_ids:
      - "TABLE_PAPEL_ESPORTIVO_OPERACIONAL"
      - "COLUMN_PAPEL_ESPORTIVO_OPERACIONAL_POSITION_NAME"
      - "COLUMN_PAPEL_ESPORTIVO_OPERACIONAL_FUNCTION_NAME"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_003"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - trace_id: "TRACE_PARTIDAS_SCOUT_004"
    rule_ids:
      - "RN_TETO_PARTICIPANTES_SUMULA"
    evidence_ref_ids:
      - "EVID_IHF_RULES_2026_EN_005"
      - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_007"
    logical_relation_ids:
      - "PARTIDA_EQUIPE"
    attribute_ids:
      - "max_athletes"
      - "max_officials"
    relationship_ids: []
    physical_candidate_ids:
      - "TABLE_PARTIDA_EQUIPE"
      - "COLUMN_PARTIDA_EQUIPE_MAX_ATHLETES"
      - "COLUMN_PARTIDA_EQUIPE_MAX_OFFICIALS"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_004"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - trace_id: "TRACE_PARTIDAS_SCOUT_005"
    rule_ids:
      - "RN_REJEICAO_VARIAVEIS_INFERENCIAIS"
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
    logical_relation_ids:
      - "OBSERVACAO_DE_SCOUT"
    attribute_ids:
      - "is_inferential_rejected"
    relationship_ids: []
    physical_candidate_ids:
      - "TABLE_OBSERVACAO_DE_SCOUT"
      - "COLUMN_OBSERVACAO_DE_SCOUT_IS_INFERENTIAL_REJECTED"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_005"
    implementation_status: "NAO_INICIADO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - trace_id: "TRACE_PARTIDAS_SCOUT_006"
    rule_ids:
      - "RN_PASSIVO_QUATRO_PASSES"
    evidence_ref_ids:
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_004"
    logical_relation_ids:
      - "POSSE_DE_BOLA"
    attribute_ids:
      - "passes_after_forewarning"
    relationship_ids: []
    physical_candidate_ids:
      - "TABLE_POSSE_DE_BOLA"
      - "COLUMN_POSSE_DE_BOLA_PASSES_AFTER_FOREWARNING"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_006"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - trace_id: "TRACE_PARTIDAS_SCOUT_007"
    rule_ids:
      - "RN_SANCAO_FINAL_15_SEGUNDOS"
    evidence_ref_ids:
      - "EVID_IHF_RULES_2026_EN_012"
      - "EVID_IHF_RULES_2026_EN_013"
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_005"
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_006"
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_007"
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_008"
    logical_relation_ids:
      - "EVENTO_SCOUT"
    attribute_ids:
      - "is_last_15_seconds"
      - "disqualification_granted"
    relationship_ids: []
    physical_candidate_ids:
      - "TABLE_EVENTO_SCOUT"
      - "COLUMN_EVENTO_SCOUT_IS_LAST_15_SECONDS"
      - "COLUMN_EVENTO_SCOUT_DISQUALIFICATION_GRANTED"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_007"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - trace_id: "TRACE_PARTIDAS_SCOUT_008"
    rule_ids:
      - "RN_PROTECAO_CABECA_GOLEIRA"
    evidence_ref_ids:
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_009"
    logical_relation_ids:
      - "EVENTO_SCOUT"
    attribute_ids:
      - "head_strike_suspension"
    relationship_ids: []
    physical_candidate_ids:
      - "TABLE_EVENTO_SCOUT"
      - "COLUMN_EVENTO_SCOUT_HEAD_STRIKE_SUSPENSION"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_008"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - trace_id: "TRACE_PARTIDAS_SCOUT_009"
    rule_ids:
      - "RN_PROIBICAO_RETARDO_REPETIDO"
    evidence_ref_ids:
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_003"
    logical_relation_ids:
      - "POSSE_DE_BOLA"
    attribute_ids:
      - "repeated_delay_count"
    relationship_ids: []
    physical_candidate_ids:
      - "TABLE_POSSE_DE_BOLA"
      - "COLUMN_POSSE_DE_BOLA_REPEATED_DELAY_COUNT"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_009"
    implementation_status: "NAO_INICIADO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - trace_id: "TRACE_PARTIDAS_SCOUT_010"
    rule_ids:
      - "RN_PRAZO_INSCRICAO_ATLETA_72H"
    evidence_ref_ids:
      - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_004"
    logical_relation_ids:
      - "EQUIPE_ATLETA_INSCRICAO"
    attribute_ids:
      - "registration_lead_hours"
    relationship_ids: []
    physical_candidate_ids:
      - "TABLE_EQUIPE_ATLETA_INSCRICAO"
      - "COLUMN_EQUIPE_ATLETA_INSCRICAO_REGISTRATION_LEAD_HOURS"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_010"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - trace_id: "TRACE_PARTIDAS_SCOUT_011"
    rule_ids:
      - "RN_REGRAS_EXECUCAO_TIRO_SEIS_METROS"
    evidence_ref_ids:
      - "EVID_IHF_RULES_2026_EN_011"
      - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_008"
      - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_009"
      - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_010"
      - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_011"
      - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_012"
    logical_relation_ids:
      - "EVENTO_SCOUT"
    attribute_ids:
      - "six_metre_throw_execution_time"
    relationship_ids: []
    physical_candidate_ids:
      - "TABLE_EVENTO_SCOUT"
      - "COLUMN_EVENTO_SCOUT_SIX_METRE_THROW_EXECUTION_TIME"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_011"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
coverage_summary:
  total_rules: 11
  covered_rules: 11
  total_traces: 11
  rules_coverage_percentage: 100.0
  implementation_breakdown:
    CANDIDATO: 9
    NAO_INICIADO: 2
  verification_breakdown:
    NAO_EXECUTADO: 11
orphan_checks:
  sources_without_use:
    - "SRC_CTRL_FLUXO_MODELAGEM_ACF6AFA2AAB0_C17B2843"
    - "SRC_CTRL_INSTRUCOES_NOTEBOOK_A6EDE74B1BAA_63B2FA9E"
    - "SRC_CTRL_CONTRATO_ARTEFATOS_DB2D64DA9680_5CDE0B19"
    - "SRC_00_MANIFESTO_FONTES_TEMPLATE_8F26F1D8"
    - "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    - "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    - "SRC_REGULAMENTO_CBHB_2026_PDF_818BCC8B"
    - "SRC_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC"
    - "SRC_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56"
    - "SRC_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2"
    - "SRC_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A"
    - "SRC_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94"
    - "SRC_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E"
    - "SRC_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0"
    - "SRC_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533"
    - "SRC_04B_MODELO_LOGICO_MD_FFCFA1B3"
    - "SRC_04C_DICIONARIO_DE_DADOS_MD_6B0D9716"
    - "SRC_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB"
    - "SRC_05_SCHEMA_POSTGRESQL_SQL_B7F68C42"
    - "SRC_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E"
    - "SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919"
  rules_without_source: []
  entities_without_rules:
    - "PARTIDA"
    - "EQUIPE"
    - "ATLETA"
    - "PERIODO_SET"
    - "SHOOT_OUT"
    - "UNIDADE_BASICA_ATAQUE_BOU"
    - "ANALISTA_OBSERVADOR"
    - "PROTOCOLO_SCOUT"
    - "MIDIA_VIDEO"
    - "SEGMENTO_OBSERVADO"
    - "PLACAR_JOGO"
    - "ESTADO_DO_PLACAR"
    - "EVOLUCAO_DO_PLACAR"
    - "SISTEMA_DEFENSIVO"
    - "CONFIABILIDADE_OBSERVADOR"
    - "REVISAO_DA_OBSERVACAO"
    - "ESTADO_DE_REVISAO"
    - "PROVENIENCIA_OBSERVACAO"
    - "TRECHO_OBSERVADO"
    - "SPIN_SHOT"
    - "IN_FLIGHT_SHOT"
    - "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
    - "CARTAO_AZUL_SUSPENSAO"
    - "SISTEMA_TATICO"
    - "PARTICIPACAO_EQUIPE_COMPETICAO"
  attributes_without_definition: []
  physical_objects_without_logical_origin: []
  tests_without_rule: []
open_issues:
  - id: "ISSUE_FHERJ_SCORING_POSITIONS_8_PLUS"
    status: "ABERTA"
    description: "A regra de pontuação de etapa do Circuito FHERJ 2026 (SGATE-0023 / DEC-DATA-042) cobre apenas as posições de 1ª a 7ª colocada, retornando INDETERMINATE para a 8ª posição em diante devido ao estado desatualizado (STALE_FOR_SCORING) do Artigo 25º armazenado."
    affected_ids:
      - "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
      - "SRC_04A_MODELO_CONCEITUAL_MD_D7C900D7"
    impact: "Incapacidade de calcular deterministicamente a pontuação de ranking para equipes classificadas abaixo da 7ª colocação no campeonato estadual."
    required_action: "Obter a versão atualizada da tabela de pontuação oficial da FHERJ junto à federação para complementar o mapeamento de posições de 8ª em diante."
  - id: "ISSUE_MIGRATION_EXECUTION_STATUS"
    status: "ABERTA"
    description: "A versão de migração 20261013000001 do banco de dados encontra-se descrita em arquivo SQL de migração, porém não há confirmação se foi efetivamente executada em ambiente de produção/staging."
    affected_ids:
      - "SRC_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E"
    impact: "Incerteza sobre a vigência real das tabelas físicas no banco de dados operacional."
    required_action: "Realizar auditoria no banco de dados e obter log de confirmação de execução da migração emitido pelo operador."
  - id: "ISSUE_RLS_POLICIES_MISSING_DECLARATION"
    status: "ABERTA"
    description: "Diversas tabelas do domínio (ex.: matches, match_appearances, possessions, bous, tactical_events) possuem a flag de RLS ativada na Seção 1 do documento de segurança, porém carecem de declarações explícitas de comandos CREATE POLICY."
    affected_ids:
      - "SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919"
    impact: "Bloqueio ou acesso indevido às tabelas afetadas caso o RLS esteja ativo sem políticas explícitas parametrizadas."
    required_action: "Elaborar e aprovar o script complementar de DDL contendo os comandos CREATE POLICY para as tabelas omitidas."
  - id: "ISSUE_IHF_2026_YELLOW_HIGHLIGHT_EXTRACTION"
    status: "ABERTA"
    description: "A extração de texto em formato plano das Regras da IHF 2026 em inglês não preserva as cores de destaque em amarelo da nota oficial, impedindo a verificação puramente textual de todas as disposições que entram em vigor estritamente em 1º de julho de 2026."
    affected_ids:
      - "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    impact: "Risco de ambiguidade na definição exata das datas de início de vigência de regras específicas."
    required_action: "Reconciliar manualmente os trechos com a edição visual do PDF original da IHF e com o comunicado oficial de atualizações (SRC_ATUALIZACOES_IHF_2026_MD_02D99F75)."