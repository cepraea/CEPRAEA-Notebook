phase: "PLANNED"
traces:
  - id: "TRACE_PARTIDAS_SCOUT_001"
    evidence_ref_ids:
      - "EVID_IHF_RULES_2026_EN_005"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_024"
    concept_ids:
      - "CONCEPT_MATCH_ROSTER_LIMITS"
    rule_ids:
      - "REG-IHF-001"
    conceptual_entity_ids:
      - "MATCH"
      - "ATHLETE"
    relationship_ids:
      - "REL_MATCH_ATHLETE_PARTICIPATION"
    logical_relation_ids:
      - "MATCH_APPEARANCE"
    attribute_ids:
      - "match_id"
      - "athlete_id"
      - "participation_status"
    physical_object_ids:
      - "TABLE_MATCH_APPEARANCE"
      - "COLUMN_MATCH_APPEARANCE_PARTICIPATION_STATUS"
    permission_requirement_ids:
      - "PERM_MANAGE_MATCH_ROSTER"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_001"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRACE_PARTIDAS_SCOUT_002"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_025"
    concept_ids:
      - "CONCEPT_TWO_EXCLUDED_SELECTION"
    rule_ids:
      - "REG-IHF-002"
    conceptual_entity_ids:
      - "CONVOCATION"
      - "MATCH_APPEARANCE"
    relationship_ids:
      - "REL_CONVOCATION_MATCH_SELECTION"
    logical_relation_ids:
      - "CONVOCATION_ATHLETE"
    attribute_ids:
      - "convocation_id"
      - "athlete_id"
      - "selection_status"
    physical_object_ids:
      - "TABLE_CONVOCATION_ATHLETE"
      - "COLUMN_CONVOCATION_ATHLETE_SELECTION_STATUS"
    permission_requirement_ids:
      - "PERM_MANAGE_CONVOCATIONS"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_002"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRACE_PARTIDAS_SCOUT_003"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_026"
    concept_ids:
      - "CONCEPT_MATCH_SCORE_DERIVATION"
    rule_ids:
      - "REG-IHF-003"
    conceptual_entity_ids:
      - "MATCH"
      - "MATCH_SCORE"
    relationship_ids:
      - "REL_MATCH_SETS_RESULT"
    logical_relation_ids:
      - "MATCH"
    attribute_ids:
      - "sets_won_team"
      - "sets_won_opponent"
      - "victory_status"
    physical_object_ids:
      - "TABLE_MATCH"
      - "COLUMN_MATCH_SETS_WON_TEAM"
      - "COLUMN_MATCH_VICTORY_STATUS"
    permission_requirement_ids:
      - "PERM_RECORD_MATCH_SCORE"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_003"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRACE_PARTIDAS_SCOUT_004"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_003"
      - "EVID_CEPRAEA_DATABASE_CCB2A718_006"
    concept_ids:
      - "CONCEPT_PROSPECTIVE_AVAILABILITY"
    rule_ids:
      - "RN-DISP-001"
    conceptual_entity_ids:
      - "AVAILABILITY_DECLARATION"
    relationship_ids:
      - "REL_ATHLETE_EVENT_AVAILABILITY"
    logical_relation_ids:
      - "AVAILABILITY_DECLARATION"
    attribute_ids:
      - "declaration_type"
      - "is_factual_presence"
    physical_object_ids:
      - "TABLE_AVAILABILITY_DECLARATION"
      - "COLUMN_AVAILABILITY_DECLARATION_IS_FACTUAL_PRESENCE"
    permission_requirement_ids:
      - "PERM_DECLARE_AVAILABILITY"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_004"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRACE_PARTIDAS_SCOUT_005"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_005"
    concept_ids:
      - "CONCEPT_CANONICAL_ATHLETE_IDENTITY"
    rule_ids:
      - "RN-DISP-003"
    conceptual_entity_ids:
      - "ATHLETE"
    relationship_ids:
      - "REL_ATHLETE_IDENTITY"
    logical_relation_ids:
      - "ATHLETE"
    attribute_ids:
      - "athlete_id"
      - "display_name"
    physical_object_ids:
      - "TABLE_ATHLETE"
      - "COLUMN_ATHLETE_ATHLETE_ID"
    permission_requirement_ids:
      - "PERM_MANAGE_ATHLETES"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_005"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRACE_PARTIDAS_SCOUT_006"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_006"
    concept_ids:
      - "CONCEPT_AVAILABILITY_STATE_UNIQUENESS"
    rule_ids:
      - "RN-DISP-004"
    conceptual_entity_ids:
      - "AVAILABILITY_DECLARATION"
      - "CALENDAR_EVENT"
    relationship_ids:
      - "REL_EVENT_ATHLETE_AVAILABILITY"
    logical_relation_ids:
      - "AVAILABILITY_DECLARATION"
    attribute_ids:
      - "event_id"
      - "athlete_id"
    physical_object_ids:
      - "TABLE_AVAILABILITY_DECLARATION"
      - "COLUMN_AVAILABILITY_DECLARATION_EVENT_ID"
      - "COLUMN_AVAILABILITY_DECLARATION_ATHLETE_ID"
    permission_requirement_ids:
      - "PERM_DECLARE_AVAILABILITY"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_006"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRACE_PARTIDAS_SCOUT_007"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_007"
    concept_ids:
      - "CONCEPT_STRICT_AVAILABILITY_DOMAIN"
    rule_ids:
      - "RN-DISP-005"
    conceptual_entity_ids:
      - "AVAILABILITY_DECLARATION"
    relationship_ids:
      - "REL_AVAILABILITY_STATUS_DOMAIN"
    logical_relation_ids:
      - "AVAILABILITY_DECLARATION"
    attribute_ids:
      - "response_status"
    physical_object_ids:
      - "TABLE_AVAILABILITY_DECLARATION"
      - "COLUMN_AVAILABILITY_DECLARATION_RESPONSE_STATUS"
    permission_requirement_ids:
      - "PERM_DECLARE_AVAILABILITY"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_007"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRACE_PARTIDAS_SCOUT_008"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_012"
    concept_ids:
      - "CONCEPT_FAIL_CLOSED_RESOLUTION"
    rule_ids:
      - "RN-DISP-010"
    conceptual_entity_ids:
      - "AVAILABILITY_DECLARATION"
    relationship_ids:
      - "REL_IDENTITY_RESOLUTION_GUARD"
    logical_relation_ids:
      - "AVAILABILITY_DECLARATION"
    attribute_ids:
      - "athlete_id"
      - "event_id"
    physical_object_ids:
      - "TABLE_AVAILABILITY_DECLARATION"
    permission_requirement_ids:
      - "PERM_DECLARE_AVAILABILITY"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_008"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRACE_PARTIDAS_SCOUT_009"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_017"
    concept_ids:
      - "CONCEPT_DECLARATION_FACT_ISOLATION"
    rule_ids:
      - "RN-DISP-015"
    conceptual_entity_ids:
      - "AVAILABILITY_DECLARATION"
      - "FACTUAL_PRESENCE"
    relationship_ids:
      - "REL_DECLARATION_FACT_ISOLATION"
    logical_relation_ids:
      - "FACTUAL_PRESENCE"
    attribute_ids:
      - "presence_status"
      - "origin_type"
    physical_object_ids:
      - "TABLE_FACTUAL_PRESENCE"
      - "COLUMN_FACTUAL_PRESENCE_ORIGIN_TYPE"
    permission_requirement_ids:
      - "PERM_RECORD_FACTUAL_PRESENCE"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_009"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRACE_PARTIDAS_SCOUT_010"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_020"
      - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_006"
    concept_ids:
      - "CONCEPT_FACTUAL_PRESENCE_SSOT"
    rule_ids:
      - "DEC-DATA-045.1"
    conceptual_entity_ids:
      - "FACTUAL_PRESENCE"
    relationship_ids:
      - "REL_FACTUAL_PRESENCE_SSOT"
    logical_relation_ids:
      - "FACTUAL_PRESENCE"
    attribute_ids:
      - "presence_id"
      - "athlete_id"
      - "event_id"
    physical_object_ids:
      - "TABLE_FACTUAL_PRESENCE"
      - "COLUMN_FACTUAL_PRESENCE_PRESENCE_ID"
    permission_requirement_ids:
      - "PERM_MANAGE_FACTUAL_PRESENCE"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_010"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRACE_PARTIDAS_SCOUT_011"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_022"
    concept_ids:
      - "CONCEPT_COACH_HUMAN_GATE"
    rule_ids:
      - "DEC-DATA-045.3"
    conceptual_entity_ids:
      - "PRESENCE_PROPOSAL"
      - "FACTUAL_PRESENCE"
    relationship_ids:
      - "REL_PROPOSAL_CONVERSION_GATE"
    logical_relation_ids:
      - "PRESENCE_PROPOSAL"
    attribute_ids:
      - "proposal_status"
      - "confirmed_by"
    physical_object_ids:
      - "TABLE_PRESENCE_PROPOSAL"
      - "COLUMN_PRESENCE_PROPOSAL_PROPOSAL_STATUS"
    permission_requirement_ids:
      - "PERM_APPROVE_PRESENCE_PROPOSAL"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_011"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

  - id: "TRACE_PARTIDAS_SCOUT_012"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_027"
      - "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_005"
    concept_ids:
      - "CONCEPT_REGIONAL_STAGE_SCORING"
    rule_ids:
      - "SGATE-0023"
      - "DEC-DATA-042"
    conceptual_entity_ids:
      - "CARIOCA_2026_SCORING_RULE"
    relationship_ids:
      - "REL_STAGE_SCORING_LOOKUP"
    logical_relation_ids:
      - "CARIOCA_2026_SCORING_RULE"
    attribute_ids:
      - "position"
      - "points_assigned"
    physical_object_ids:
      - "TABLE_CARIOCA_2026_SCORING_RULE"
      - "COLUMN_CARIOCA_2026_SCORING_RULE_POSITION"
      - "COLUMN_CARIOCA_2026_SCORING_RULE_POINTS_ASSIGNED"
    permission_requirement_ids:
      - "PERM_MANAGE_SCORING_RULES"
    test_ids:
      - "TEST_PARTIDAS_SCOUT_012"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []

coverage_summary:
  source_rules_total: 12
  rules_with_logical_mapping: 12
  rules_with_physical_mapping: 12
  material_constraints_total: 12
  material_constraints_with_tests: 12
  unresolved_trace_ids: []

orphan_checks:
  sources_without_use: []
  rules_without_source: []
  entities_without_rules: []
  attributes_without_definition: []
  physical_objects_without_logical_origin: []
  tests_without_rule: []

open_issues:
  - id: "ISSUE_SRC_CEPRAEA_DATABASE_CCB2A718_001"
    status: "ABERTA"
    question: "O boletim oficial da Etapa Final omite o placar detalhado do shoot-out da partida J71 (2x1 vs APCEF/CT Rossana Marques), impedindo a reconciliação completa da pontuação parcial dos sets e shoot-out."
    affected_ids:
      - "SRC_CEPRAEA_DATABASE_CCB2A718"
    impact: "A reconciliação dos atributos de placar detalhado de shoot-out permanece incompleta para a partida J71."
    required_evidence: "Boletim oficial retificado ou súmula assinada da partida J71 da Etapa Final de São Miguel do Iguaçu/PR."
    owner: "OPERADOR"

  - id: "ISSUE_SOURCE_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919_001"
    status: "ABERTA"
    question: "As tabelas do domínio têm RLS habilitado na Seção 1, mas não possuem diretivas CREATE POLICY explicitamente declaradas na matriz de segurança."
    affected_ids:
      - "SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919"
    impact: "Planejamento de permissões RLS incompleto para as entidades lógicas do domínio."
    required_evidence: "Matriz RBAC com definições explícitas de CREATE POLICY para as tabelas do domínio."
    owner: "OPERADOR"