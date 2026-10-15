# Matriz de Rastreabilidade Planejada - CEPRAEA Beach Handball Pro

phase: "PLANNED"
traces:
  - id: "TRC_DISPONIBILIDADE_DECLARADA_CORE"
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_006"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_003"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_004"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_005"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_006"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_007"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_008"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_009"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_010"
    concept_ids:
      - "CON_DECLARACAO_DISPONIBILIDADE"
    rule_ids:
      - "RN-DISP-001"
      - "RN-DISP-002"
      - "RN-DISP-003"
      - "RN-DISP-004"
      - "RN-DISP-005"
      - "RN-DISP-006"
      - "RN-DISP-007"
      - "RN-DISP-008"
    conceptual_entity_ids:
      - "AVAILABILITY_DECLARATION"
    conceptual_relation_ids:
      - "REL_ATHLETE_AVAILABILITY"
    logical_relation_ids:
      - "LOG_REL_ATHLETE_AVAILABILITY"
    attribute_ids:
      - "availability_declarations.status"
      - "availability_declarations.event_id"
      - "availability_declarations.athlete_id"
      - "availability_declarations.updated_at"
    physical_object_ids:
      - "public.availability_declarations"
      - "public.availability_declarations.status"
      - "public.availability_declarations.event_id"
      - "public.availability_declarations.athlete_id"
      - "public.availability_declarations.updated_at"
    permission_requirement_ids:
      - "PERM_DECLARAR_DISPONIBILIDADE_ATHLETE"
    test_ids:
      - "TEST_DISPONIBILIDADE_001"
      - "TEST_DISPONIBILIDADE_002"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRC_DISPONIBILIDADE_GOVERNANCA_E_LIFECYCLE"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_011"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_012"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_013"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_014"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_015"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_016"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_017"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_018"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_019"
    concept_ids:
      - "CON_DECLARACAO_DISPONIBILIDADE"
      - "CON_ISOLAMENTO_DISPONIBILIDADE_PRESENCA"
    rule_ids:
      - "RN-DISP-009"
      - "RN-DISP-010"
      - "RN-DISP-011"
      - "RN-DISP-012"
      - "RN-DISP-013"
      - "RN-DISP-014"
      - "RN-DISP-015"
      - "RN-DISP-016"
      - "RN-DISP-017"
    conceptual_entity_ids:
      - "AVAILABILITY_DECLARATION"
      - "CALENDAR_EVENT"
    conceptual_relation_ids:
      - "REL_EVENT_AVAILABILITY_POLICY"
    logical_relation_ids:
      - "LOG_REL_EVENT_AVAILABILITY_POLICY"
    attribute_ids:
      - "calendar_events.accepts_availability"
      - "calendar_events.event_date"
      - "availability_declarations.status"
    physical_object_ids:
      - "public.calendar_events"
      - "public.calendar_events.accepts_availability"
      - "public.calendar_events.event_date"
      - "public.availability_declarations"
    permission_requirement_ids:
      - "PERM_DECLARAR_DISPONIBILIDADE_ATHLETE"
    test_ids:
      - "TEST_DISPONIBILIDADE_003"
      - "TEST_DISPONIBILIDADE_004"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRC_PRESENCA_FATUAL"
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_003"
      - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_006"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_020"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_021"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_022"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_023"
    concept_ids:
      - "CON_PRESENCA_FATUAL"
      - "CON_PROPOSTA_PRESENCA"
    rule_ids:
      - "DEC-DATA-045.1"
      - "DEC-DATA-045.2"
      - "DEC-DATA-045.3"
      - "DEC-DATA-045.4"
    conceptual_entity_ids:
      - "FACTUAL_PRESENCE"
      - "PRESENCE_PROPOSAL"
    conceptual_relation_ids:
      - "REL_TRAINER_CONFIRMATION"
    logical_relation_ids:
      - "LOG_REL_PROPOSAL_TO_FACTUAL"
    attribute_ids:
      - "factual_presences.confirmed_by"
      - "factual_presences.confirmed_at"
      - "factual_presences.athlete_id"
      - "presence_proposals.status"
    physical_object_ids:
      - "public.factual_presences"
      - "public.factual_presences.confirmed_by"
      - "public.factual_presences.confirmed_at"
      - "public.presence_proposals"
      - "public.presence_proposals.status"
    permission_requirement_ids:
      - "PERM_CONFIRMAR_PRESENCA_TREINADOR"
    test_ids:
      - "TEST_PRESENCA_001"
      - "TEST_PRESENCA_002"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRC_CONVOCACAO_SUMULA"
    evidence_ref_ids:
      - "EVID_IHF_RULES_2026_EN_005"
      - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_007"
      - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_007"
      - "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_004"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_024"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_025"
      - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_007"
      - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_008"
      - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_010"
      - "EVID_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB_003"
    concept_ids:
      - "CON_CONVOCACAO"
      - "CON_ESCALACAO_SUMULA"
      - "CON_PARTICIPACAO_EFETIVA"
    rule_ids:
      - "REG-IHF-001"
      - "REG-IHF-002"
    conceptual_entity_ids:
      - "CONVOCATION"
      - "MATCH_APPEARANCE"
    conceptual_relation_ids:
      - "REL_CONVOCATION_ATHLETES"
    logical_relation_ids:
      - "LOG_REL_CONVOCATION_MATCH"
    attribute_ids:
      - "convocations.max_match_athletes"
      - "match_appearances.participation_status"
    physical_object_ids:
      - "public.convocations"
      - "public.convocation_athletes"
      - "public.match_appearances"
      - "public.convocations.max_match_athletes"
      - "public.match_appearances.participation_status"
    permission_requirement_ids:
      - "PERM_SUBMIT_CONVOCATION_COACH"
    test_ids:
      - "TEST_CONVOCACAO_001"
      - "TEST_IHF_001"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRC_ESTRUTURA_PARTIDA_E_PONTUACAO"
    evidence_ref_ids:
      - "EVID_IHF_RULES_2026_EN_002"
      - "EVID_IHF_RULES_2026_EN_003"
      - "EVID_IHF_RULES_2026_EN_004"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_026"
      - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_009"
    concept_ids:
      - "CON_PARTIDA"
      - "CON_SET_PARTIDA"
      - "CON_SHOOTOUT"
    rule_ids:
      - "REG-IHF-003"
    conceptual_entity_ids:
      - "MATCH"
      - "MATCH_SEGMENT"
    conceptual_relation_ids:
      - "REL_MATCH_SEGMENTS"
    logical_relation_ids:
      - "LOG_REL_MATCH_SEGMENTS"
    attribute_ids:
      - "matches.sets_won_cepraea"
      - "matches.sets_won_opponent"
      - "matches.cepraea_victory"
    physical_object_ids:
      - "public.matches"
      - "public.matches.sets_won_cepraea"
      - "public.matches.sets_won_opponent"
      - "public.matches.cepraea_victory"
    permission_requirement_ids:
      - "PERM_RECORD_MATCH_RESULT"
    test_ids:
      - "TEST_PARTIDA_001"
      - "TEST_IHF_003"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRC_PONTUACAO_RANKING_FHERJ_2026"
    evidence_ref_ids:
      - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_006"
      - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_008"
      - "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_005"
      - "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_008"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_027"
    concept_ids:
      - "CON_RANKING_ETAPA"
      - "CON_INELEGIBILIDADE_EXCECAO"
    rule_ids:
      - "SGATE-0023"
      - "SGATE-0024"
      - "DEC-DATA-042"
    conceptual_entity_ids:
      - "CARIOCA_2026_SCORING_RULE"
      - "FINAL_RANKING_ELIGIBILITY"
    conceptual_relation_ids:
      - "REL_COMPETITION_RANKING"
    logical_relation_ids:
      - "LOG_REL_COMPETITION_RANKING"
    attribute_ids:
      - "carioca_2026_scoring_rule.position"
      - "carioca_2026_scoring_rule.points"
      - "final_ranking_eligibility.eligibility"
    physical_object_ids:
      - "public.carioca_2026_scoring_rules"
      - "public.carioca_2026_scoring_rules.position"
      - "public.carioca_2026_scoring_rules.points"
    permission_requirement_ids: []
    test_ids:
      - "TEST_FHERJ_SCORING_001"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRC_FINALIZACAO_VALORACAO_GOLS"
    evidence_ref_ids:
      - "EVID_IHF_RULES_2026_EN_006"
      - "EVID_IHF_RULES_2026_EN_007"
      - "EVID_IHF_RULES_2026_EN_008"
      - "EVID_IHF_RULES_2026_EN_014"
      - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_009"
      - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_010"
      - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_011"
      - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_005"
      - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_006"
    concept_ids:
      - "CON_GOL_DUPLO"
      - "CON_SPIN_SHOT"
      - "CON_IN_FLIGHT"
    rule_ids: []
    conceptual_entity_ids:
      - "FINALIZATION"
      - "TACTICAL_EVENT"
    conceptual_relation_ids:
      - "REL_FINALIZATION_EVENT"
    logical_relation_ids:
      - "LOG_REL_FINALIZATION_EVENT"
    attribute_ids:
      - "finalizations.goal_value"
      - "finalizations.technique_type"
    physical_object_ids:
      - "public.finalizations"
      - "public.finalizations.goal_value"
      - "public.finalizations.technique_type"
    permission_requirement_ids: []
    test_ids:
      - "TEST_IHF_GOL_001"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRC_SCOUT_UNIDADE_BOU_E_POSSE"
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_004"
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_005"
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_006"
      - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_001"
    concept_ids:
      - "CON_POSSE_DE_BOLA"
      - "CON_BASIC_ATTACK_UNIT"
      - "CON_FAIXA_LATERAL_QUADRA"
    rule_ids:
      - "UNT-003"
      - "UNT-004"
      - "TAX-001"
      - "TAX-006"
    conceptual_entity_ids:
      - "POSSESSION"
      - "BOU"
      - "TACTICAL_EVENT"
    conceptual_relation_ids:
      - "REL_POSSESSION_BOU"
      - "REL_BOU_TACTICAL_EVENTS"
    logical_relation_ids:
      - "LOG_REL_POSSESSION_BOU"
      - "LOG_REL_BOU_TACTICAL_EVENTS"
    attribute_ids:
      - "possessions.id"
      - "bous.id"
      - "bous.offensive_phase"
      - "tactical_events.court_zone"
    physical_object_ids:
      - "public.possessions"
      - "public.bous"
      - "public.tactical_events"
      - "public.bous.offensive_phase"
      - "public.tactical_events.court_zone"
    permission_requirement_ids:
      - "PERM_REGISTRAR_SCOUT_OBSERVADOR"
    test_ids:
      - "TEST_SCOUT_BOU_001"
      - "TEST_SCOUT_POSSESSION_001"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRC_SCOUT_ACOES_GOLEIRA"
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_004"
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_008"
      - "EVID_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0_003"
      - "EVID_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_005"
    concept_ids:
      - "CON_ACAO_GOLEIRA"
      - "CON_TAXA_DEFESA_GOLEIRA"
    rule_ids:
      - "IND-016"
    conceptual_entity_ids:
      - "GOALKEEPER_ACTION"
      - "ATHLETE"
    conceptual_relation_ids:
      - "REL_ATHLETE_GOALKEEPER_ACTIONS"
    logical_relation_ids:
      - "LOG_REL_ATHLETE_GOALKEEPER_ACTIONS"
    attribute_ids:
      - "goalkeeper_actions.id"
      - "goalkeeper_actions.athlete_id"
      - "goalkeeper_actions.save_result"
      - "goalkeeper_actions.defense_stage"
    physical_object_ids:
      - "public.goalkeeper_actions"
      - "public.goalkeeper_actions.athlete_id"
      - "public.goalkeeper_actions.save_result"
    permission_requirement_ids:
      - "PERM_REGISTRAR_SCOUT_OBSERVADOR"
    test_ids:
      - "TEST_GOALKEEPER_001"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRC_SCOUT_QUALIFICACAO_OBSERVADOR"
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_002"
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
    concept_ids:
      - "CON_QUALIFICACAO_OBSERVADOR"
      - "CON_CONFIABILIDADE_SCOUT"
    rule_ids:
      - "CON-006"
    conceptual_entity_ids:
      - "OBSERVER_QUALIFICATION"
    conceptual_relation_ids:
      - "REL_OBSERVER_QUALIFICATION_STATUS"
    logical_relation_ids:
      - "LOG_REL_OBSERVER_QUALIFICATION_STATUS"
    attribute_ids:
      - "observer_qualifications.status"
      - "observer_qualifications.score"
    physical_object_ids:
      - "public.observer_qualifications"
      - "public.observer_qualifications.status"
    permission_requirement_ids:
      - "PERM_AUTORIZAR_OBSERVADOR_SCOUT"
    test_ids:
      - "TEST_OBSERVER_QUALIFICATION_001"
    implementation_status: "NAO_INICIADO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRC_SEGURANCA_RBAC_RLS_POLICIES"
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_001"
      - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_006"
    concept_ids:
      - "CON_CONTROLE_ACESSO_RLS"
      - "CON_PAPEL_TREINADOR_AUDITORIA"
    rule_ids:
      - "DEC-DATA-045.3"
      - "DEC-DATA-045.4"
    conceptual_entity_ids:
      - "SECURITY_POLICY"
      - "ROLE_PERMISSION"
    conceptual_relation_ids:
      - "REL_SECURITY_TABLE_POLICY"
    logical_relation_ids:
      - "LOG_REL_SECURITY_TABLE_POLICY"
    attribute_ids:
      - "factual_presences.confirmed_by"
      - "availability_declarations.athlete_id"
    physical_object_ids:
      - "public.factual_presences"
      - "public.availability_declarations"
      - "public.athletes"
    permission_requirement_ids:
      - "PERM_CONFIRMAR_PRESENCA_TREINADOR"
      - "PERM_DECLARAR_DISPONIBILIDADE_ATHLETE"
      - "PERM_SUBMIT_CONVOCATION_COACH"
    test_ids:
      - "TEST_RLS_ATHLETE_ISOLATION_001"
      - "TEST_RLS_COACH_OVERRIDE_001"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRC_SESSAO_TREINAMENTO_E_PLANO"
    evidence_ref_ids:
      - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_009"
      - "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_004"
    concept_ids:
      - "CON_PLANO_TREINO"
      - "CON_REALIZACAO_SESSAO"
    rule_ids:
      - "RN-TREINO-001"
    conceptual_entity_ids:
      - "TRAINING_SESSION"
      - "SESSION_REALIZATION"
    conceptual_relation_ids:
      - "REL_SESSION_REALIZATION"
    logical_relation_ids:
      - "LOG_REL_SESSION_REALIZATION"
    attribute_ids:
      - "training_sessions.session_date"
      - "session_realizations.realized_at"
    physical_object_ids:
      - "public.training_sessions"
      - "public.session_realizations"
    permission_requirement_ids:
      - "PERM_REGISTRAR_SESSAO_TREINADOR"
    test_ids:
      - "TEST_SESSAO_001"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRC_ATRIBUICAO_TATICA_ESPECIALISTA"
    evidence_ref_ids:
      - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_004"
      - "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_009"
      - "EVID_CEPRAEA_DATABASE_CCB2A718_004"
      - "EVID_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2_003"
    concept_ids:
      - "CON_ATRIBUICAO_TATICA"
      - "CON_ESPECIALISTA_CORINGA"
    rule_ids:
      - "RN-TACT-001"
    conceptual_entity_ids:
      - "TACTICAL_ASSIGNMENT"
      - "ATHLETE"
    conceptual_relation_ids:
      - "REL_ATHLETE_TACTICAL_ASSIGNMENT"
    logical_relation_ids:
      - "LOG_REL_ATHLETE_TACTICAL_ASSIGNMENT"
    attribute_ids:
      - "tactical_assignments.function"
      - "tactical_assignments.tactical_role"
    physical_object_ids:
      - "public.tactical_assignments"
      - "public.tactical_assignments.function"
      - "public.tactical_assignments.tactical_role"
    permission_requirement_ids: []
    test_ids:
      - "TEST_TACT_001"
    implementation_status: "NAO_INICIADO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

coverage_summary:
  rules_mapped_total: 35
  rules_with_physical_mapping: 35
  material_constraints_total: 82
  traces_total: 13
  implementation_status_counts:
    CANDIDATO: 11
    NAO_INICIADO: 2
    IMPLEMENTADO: 0
  verification_status_counts:
    NAO_EXECUTADO: 13
    PASS: 0
    FAIL: 0

orphan_checks:
  evidences_without_concepts_or_rules:
    - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_005"
    - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_006"
    - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_007"
    - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_008"
    - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_009"
    - "EVID_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56_001"
    - "EVID_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56_004"
    - "EVID_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56_005"
    - "EVID_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56_006"
    - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_001"
    - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_003"
    - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_008"
    - "EVID_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533_001"
    - "EVID_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533_004"
    - "EVID_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533_006"
    - "VAR-028"
  concepts_without_evidences_or_logic: []
  rules_without_evidences_or_logic: []
  conceptual_entities_without_logic:
    - "SESSION_SEGMENT"
    - "PLANNED_TRAINING_LOAD"
  logical_relations_without_physical_candidates:
    - "LOG_REL_SESSION_SEGMENT"
    - "LOG_REL_PLANNED_TRAINING_LOAD"
  attributes_without_physical_candidates:
    - "session_segments.segment_type"
    - "planned_training_loads.target_rpe"
    - "planned_training_loads.planned_duration"

open_issues:
  - id: "ISSUE_SHOOTOUT_SCORE_J71"
    status: "ABERTA"
    question: "Omissão do placar detalhado do shoot-out no boletim oficial da Etapa Final (partida J71), impedindo o registro exato dos tentos e atuações na disputa."
    affected_ids:
      - "SRC_CEPRAEA_DATABASE_CCB2A718"
      - "EVID_CEPRAEA_DATABASE_CCB2A718_008"
      - "public.matches"
    impact: "Comprometimento da rastreabilidade exata da pontuação e desempenho individual na disputa de shoot-out da partida J71 da Etapa Final."
    required_evidence: "Boletim oficial retificado ou súmula física assinada da partida J71 com detalhamento das cobranças de shoot-out."
    owner: "OPERADOR"

  - id: "ISSUE_FHERJ_ART25_STALE"
    status: "ABERTA"
    question: "Obsolescência e desatualização do Artigo 25º da FHERJ para atribuição de pontuação de etapa a partir da 8ª posição em diante no Circuito Carioca 2026."
    affected_ids:
      - "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
      - "SGATE-0023"
      - "DEC-DATA-042"
    impact: "Algoritmo de cálculo de pontuação de ranking estadual retorna INDETERMINATE para colocações iguais ou inferiores à 8ª posição."
    required_evidence: "Resolução oficial de diretoria ou aditivo regulamentar emitido pela FHERJ com a tabela completa de pontuação por etapa."
    owner: "OPERADOR"

  - id: "ISSUE_POSTGRES_DDL_ABSENCE"
    status: "ABERTA"
    question: "Inexistência de DDLs ativas e compiláveis para criação do esquema físico PostgreSQL nas tabelas e migrations históricas (STOP GATE Físico ativo)."
    affected_ids:
      - "SRC_04B_MODELO_LOGICO_MD_FFCFA1B3"
      - "SRC_05_SCHEMA_POSTGRESQL_SQL_B7F68C42"
      - "SRC_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E"
    impact: "Impossibilidade de verificar ou confirmar a existência e conformidade real dos objetos físicos no banco de dados PostgreSQL no estágio corrente."
    required_evidence: "Aprovação formal do operador para liberação do STOP GATE físico acompanhada dos scripts DDL compiláveis."
    owner: "OPERADOR"

  - id: "ISSUE_SOURCE_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E_002"
    status: "ABERTA"
    question: "A versão de migração 20261013000001 foi efetivamente aplicada no banco de dados de produção/staging ou permanece apenas como especificação de arquivo?"
    affected_ids:
      - "SRC_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"

  - id: "ISSUE_SOURCE_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919_001"
    status: "ABERTA"
    question: "As tabelas secondary_positions, calendar_events, competitions, convocations, convocation_athletes, matches, match_appearances, possessions, bous, tactical_events, finalizations e goalkeeper_actions têm RLS habilitado na Seção 1, mas não possuem diretivas CREATE POLICY declaradas no documento."
    affected_ids:
      - "SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"

  - id: "ISSUE_CONSTRAINT_CALCULATION_AMBIGUITY"
    status: "ABERTA"
    question: "Discrepância na contagem exata de restrições materiais decorrente da coexistência de regras normativas abstratas e restrições de integridade relacional sem DDL física compilada no banco."
    affected_ids:
      - "SRC_04B_MODELO_LOGICO_MD_FFCFA1B3"
      - "SRC_04C_DICIONARIO_DE_DADOS_MD_6B0D9716"
      - "coverage_summary.material_constraints_total"
    impact: "A contagem de 82 restrições materiais inclui projeções lógicas de NOT NULL, FK e CHECK candidates, pendente de validação contra o catálogo físico do PostgreSQL pós-liberação do STOP GATE."
    required_evidence: "Execução do script DDL físico com extração do catálogo pg_constraint do PostgreSQL."
    owner: "OPERADOR"