# Fontes YAML consolidadas

## Arquivo: `notebooklm-modelagem/runs/RUN_20261014_PARTIDAS_SCOUT_001/artifacts/05-matriz-rastreabilidade.yaml`

```yaml
schema_version: "1.1"
document:
  id: "TRACEABILITY_MATRIX"
  artifact_kind: "TRACEABILITY_MATRIX"
  title: "Matriz de rastreabilidade planejada"
  version: "0.1.0"
  status: "APROVADO"
  run_id: "RUN_20261014_PARTIDAS_SCOUT_001"
  domain_id: "PARTIDAS_SCOUT_ANALISE_TATICA"
  notebook_id: "93446a17-55bf-4cd8-b9f9-18c52c8f4c1d"
  generated_at: "2026-10-15T12:22:06-03:00"
  supersedes: null
  input_artifacts:
    - document_id: "SOURCE_MANIFEST"
      version: "0.1.0"
      sha256: "4091e8f0f68cb8e5ad6aad8fbf2b5b7220131aca8ae42e48456d3fe9688209fc"
      promoted_source_id: "d0a81644-ae48-4ac8-9954-676602780417"
    - document_id: "SEMANTIC_REGISTRY"
      version: "0.1.0"
      sha256: "c793bbc79bf9a77903cfce3a2398770d82d7d5bfa02b87f65942e438895e10f7"
      promoted_source_id: "b9ddf059-9d06-4373-a828-61f409e30113"
    - document_id: "CONCEPTUAL_MODEL"
      version: "0.1.1"
      sha256: "8f3b83a34f960c4c4387462cecafec2ae6c651046e1f56e3de7710c7c2ddecff"
      promoted_source_id: "5107f1a8-c307-4203-9694-545689d7d353"
    - document_id: "LOGICAL_MODEL"
      version: "0.1.0"
      sha256: "d49ca992ba7e1ab5b2378bc24867bf876cd67f940e819be57bad297993b79712"
      promoted_source_id: "fdf6c7d9-75c7-41f3-8935-39ffaf747bb1"
    - document_id: "DATA_DICTIONARY"
      version: "0.1.0"
      sha256: "969b7479813c97f5b2da95631b185211495b509cf86147a0337a53dcbb909c2f"
      promoted_source_id: "1c227cde-1ffd-472f-b0ab-92594c05ec2b"
phase: "PLANNED"
traces:
  - id: "TRACE_RN_IHF_VIGENCIA_2026_PARTIDA"
    evidence_ref_ids:
      - "EVID_IHF_RULES_2026_EN_001"
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_002"
    concept_ids:
      - "PARTIDA"
    rule_ids:
      - "RN_IHF_VIGENCIA_2026"
    conceptual_entity_ids:
      - "PARTIDA"
      - "PERIODO_SET"
      - "SHOOT_OUT"
    relationship_ids:
      - "PARTIDA_POSSUI_PERIODO_SET"
      - "PARTIDA_POSSUI_SHOOT_OUT"
      - "PERIODO_SET_CONTEM_POSSE_DE_BOLA"
    logical_relation_ids:
      - "PARTIDA"
    attribute_ids:
      - "ID"
    physical_object_ids:
      - "TABLE_PARTIDA"
      - "COLUMN_PARTIDA_ID"
    permission_requirement_ids: []
    test_ids:
      - "TEST_REG_IHF_VIGENCIA_001"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_IHF_VIGENCIA_2026_PERIODO_SET"
    evidence_ref_ids:
      - "EVID_IHF_RULES_2026_EN_001"
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_002"
    concept_ids:
      - "PARTIDA"
    rule_ids:
      - "RN_IHF_VIGENCIA_2026"
    conceptual_entity_ids:
      - "PARTIDA"
      - "PERIODO_SET"
      - "SHOOT_OUT"
    relationship_ids:
      - "PARTIDA_POSSUI_PERIODO_SET"
      - "PARTIDA_POSSUI_SHOOT_OUT"
      - "PERIODO_SET_CONTEM_POSSE_DE_BOLA"
    logical_relation_ids:
      - "PERIODO_SET"
    attribute_ids:
      - "ID"
    physical_object_ids:
      - "TABLE_PERIODO_SET"
      - "COLUMN_PERIODO_SET_ID"
    permission_requirement_ids: []
    test_ids:
      - "TEST_REG_IHF_VIGENCIA_001"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_IHF_VIGENCIA_2026_SHOOT_OUT"
    evidence_ref_ids:
      - "EVID_IHF_RULES_2026_EN_001"
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_002"
    concept_ids:
      - "PARTIDA"
    rule_ids:
      - "RN_IHF_VIGENCIA_2026"
    conceptual_entity_ids:
      - "PARTIDA"
      - "PERIODO_SET"
      - "SHOOT_OUT"
    relationship_ids:
      - "PARTIDA_POSSUI_PERIODO_SET"
      - "PARTIDA_POSSUI_SHOOT_OUT"
      - "PERIODO_SET_CONTEM_POSSE_DE_BOLA"
    logical_relation_ids:
      - "SHOOT_OUT"
    attribute_ids:
      - "ID"
    physical_object_ids:
      - "TABLE_SHOOT_OUT"
      - "COLUMN_SHOOT_OUT_ID"
    permission_requirement_ids: []
    test_ids:
      - "TEST_REG_IHF_VIGENCIA_001"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_SGATE_0023_PONTUACAO_FHERJ_2026_COMPETICAO"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_027"
      - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_006"
    concept_ids:
      - "EQUIPE"
      - "PARTIDA"
    rule_ids:
      - "RN_SGATE_0023_PONTUACAO_FHERJ_2026"
    conceptual_entity_ids:
      - "COMPETICAO"
      - "PARTIDA"
      - "EQUIPE"
    relationship_ids:
      - "COMPETICAO_POSSUI_PARTIDA"
      - "EQUIPE_PARTICIPA_COMPETICAO"
    logical_relation_ids:
      - "COMPETICAO"
    attribute_ids:
      - "ID"
    physical_object_ids:
      - "TABLE_COMPETICAO"
      - "COLUMN_COMPETICAO_ID"
    permission_requirement_ids: []
    test_ids:
      - "TEST_SGATE_0023_SCORING"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_SGATE_0023_PONTUACAO_FHERJ_2026_PARTICIPACAO_EQUIPE_COMPETICAO"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_027"
      - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_006"
    concept_ids:
      - "EQUIPE"
      - "PARTIDA"
    rule_ids:
      - "RN_SGATE_0023_PONTUACAO_FHERJ_2026"
    conceptual_entity_ids:
      - "COMPETICAO"
      - "PARTIDA"
      - "EQUIPE"
    relationship_ids:
      - "COMPETICAO_POSSUI_PARTIDA"
      - "EQUIPE_PARTICIPA_COMPETICAO"
    logical_relation_ids:
      - "PARTICIPACAO_EQUIPE_COMPETICAO"
    attribute_ids:
      - "STATUS_ELEGIBILIDADE_RANKING"
    physical_object_ids:
      - "TABLE_PARTICIPACAO_EQUIPE_COMPETICAO"
      - "COLUMN_PARTICIPACAO_EQUIPE_COMPETICAO_STATUS_ELEGIBILIDADE_RANKING"
    permission_requirement_ids: []
    test_ids:
      - "TEST_SGATE_0023_SCORING"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_SEMANTICA_GOLEIRA_ATLETA"
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_004"
      - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_007"
    concept_ids:
      - "GOLEIRA_POSICAO"
      - "ACAO_DA_GOLEIRA"
    rule_ids:
      - "RN_SEMANTICA_GOLEIRA"
    conceptual_entity_ids:
      - "ATLETA"
    relationship_ids:
      - "EVENTO_SCOUT_ENVOLVE_ATLETA"
    logical_relation_ids:
      - "ATLETA"
    attribute_ids:
      - "ID"
      - "POSICAO_PRINCIPAL"
    physical_object_ids:
      - "TABLE_ATLETA"
      - "COLUMN_ATLETA_ID"
      - "COLUMN_ATLETA_POSICAO_PRINCIPAL"
    permission_requirement_ids: []
    test_ids:
      - "TEST_SEMANTICS_GOALKEEPER_ROLE"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_SEMANTICA_GOLEIRA_EVENTO_SCOUT"
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_004"
      - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_007"
    concept_ids:
      - "GOLEIRA_POSICAO"
      - "ACAO_DA_GOLEIRA"
    rule_ids:
      - "RN_SEMANTICA_GOLEIRA"
    conceptual_entity_ids:
      - "ATLETA"
    relationship_ids:
      - "EVENTO_SCOUT_ENVOLVE_ATLETA"
    logical_relation_ids:
      - "EVENTO_SCOUT"
    attribute_ids:
      - "ACAO_GOLEIRA"
    physical_object_ids:
      - "TABLE_EVENTO_SCOUT"
      - "COLUMN_EVENTO_SCOUT_ACAO_GOLEIRA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_SEMANTICS_GOALKEEPER_ROLE"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_TETO_PARTICIPANTES_SUMULA_PARTIDA"
    evidence_ref_ids:
      - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_007"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_024"
    concept_ids:
      - "PARTIDA"
      - "ATLETA"
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    rule_ids:
      - "RN_TETO_PARTICIPANTES_SUMULA"
    conceptual_entity_ids:
      - "PARTIDA"
      - "EQUIPE"
      - "ATLETA"
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    relationship_ids:
      - "PARTIDA_DISPUTADA_POR_EQUIPE"
    logical_relation_ids:
      - "PARTIDA"
    attribute_ids:
      - "ID"
    physical_object_ids:
      - "TABLE_PARTIDA"
      - "COLUMN_PARTIDA_ID"
    permission_requirement_ids: []
    test_ids:
      - "TEST_MATCH_ROSTER_LIMITS"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_TETO_PARTICIPANTES_SUMULA_EQUIPE"
    evidence_ref_ids:
      - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_007"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_024"
    concept_ids:
      - "PARTIDA"
      - "ATLETA"
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    rule_ids:
      - "RN_TETO_PARTICIPANTES_SUMULA"
    conceptual_entity_ids:
      - "PARTIDA"
      - "EQUIPE"
      - "ATLETA"
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    relationship_ids:
      - "PARTIDA_DISPUTADA_POR_EQUIPE"
    logical_relation_ids:
      - "EQUIPE"
    attribute_ids:
      - "ID"
    physical_object_ids:
      - "TABLE_EQUIPE"
      - "COLUMN_EQUIPE_ID"
    permission_requirement_ids: []
    test_ids:
      - "TEST_MATCH_ROSTER_LIMITS"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_TETO_PARTICIPANTES_SUMULA_PARTIDA_EQUIPE"
    evidence_ref_ids:
      - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_007"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_024"
    concept_ids:
      - "PARTIDA"
      - "ATLETA"
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    rule_ids:
      - "RN_TETO_PARTICIPANTES_SUMULA"
    conceptual_entity_ids:
      - "PARTIDA"
      - "EQUIPE"
      - "ATLETA"
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    relationship_ids:
      - "PARTIDA_DISPUTADA_POR_EQUIPE"
    logical_relation_ids:
      - "PARTIDA_EQUIPE"
    attribute_ids: []
    physical_object_ids:
      - "TABLE_PARTIDA_EQUIPE"
    permission_requirement_ids: []
    test_ids:
      - "TEST_MATCH_ROSTER_LIMITS"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_REJEICAO_VARIAVEIS_INFERENCIAIS_UNIDADE_BASICA_ATAQUE_BOU"
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
    concept_ids:
      - "OBSERVACAO_DE_SCOUT"
      - "ACAO_OBSERVADA"
      - "PROVENIENCIA_OBSERVACAO"
    rule_ids:
      - "RN_REJEICAO_VARIAVEIS_INFERENCIAIS"
    conceptual_entity_ids:
      - "UNIDADE_BASICA_ATAQUE_BOU"
      - "OBSERVACAO_DE_SCOUT"
      - "ANALISTA_OBSERVADOR"
      - "PROTOCOLO_SCOUT"
      - "MIDIA_VIDEO"
      - "PROVENIENCIA_OBSERVACAO"
    relationship_ids:
      - "POSSE_DE_BOLA_CONTEM_BOU"
      - "UNIDADE_BASICA_ATAQUE_BOU_GERA_EVENTO_SCOUT"
      - "OBSERVACAO_DE_SCOUT_REGISTRA_PARTIDA"
      - "OBSERVACAO_DE_SCOUT_UTILIZA_PROTOCOLO"
      - "OBSERVACAO_DE_SCOUT_EXECUTADA_POR_ANALISTA"
      - "OBSERVACAO_DE_SCOUT_BASEADA_EM_MIDIA"
      - "OBSERVACAO_DE_SCOUT_CONTEM_EVENTO"
    logical_relation_ids:
      - "UNIDADE_BASICA_ATAQUE_BOU"
    attribute_ids:
      - "ID"
    physical_object_ids:
      - "TABLE_UNIDADE_BASICA_ATAQUE_BOU"
      - "COLUMN_UNIDADE_BASICA_ATAQUE_BOU_ID"
    permission_requirement_ids: []
    test_ids:
      - "TEST_REJECT_INFERENTIAL_VARIABLES"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_REJEICAO_VARIAVEIS_INFERENCIAIS_OBSERVACAO_DE_SCOUT"
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
    concept_ids:
      - "OBSERVACAO_DE_SCOUT"
      - "ACAO_OBSERVADA"
      - "PROVENIENCIA_OBSERVACAO"
    rule_ids:
      - "RN_REJEICAO_VARIAVEIS_INFERENCIAIS"
    conceptual_entity_ids:
      - "UNIDADE_BASICA_ATAQUE_BOU"
      - "OBSERVACAO_DE_SCOUT"
      - "ANALISTA_OBSERVADOR"
      - "PROTOCOLO_SCOUT"
      - "MIDIA_VIDEO"
      - "PROVENIENCIA_OBSERVACAO"
    relationship_ids:
      - "POSSE_DE_BOLA_CONTEM_BOU"
      - "UNIDADE_BASICA_ATAQUE_BOU_GERA_EVENTO_SCOUT"
      - "OBSERVACAO_DE_SCOUT_REGISTRA_PARTIDA"
      - "OBSERVACAO_DE_SCOUT_UTILIZA_PROTOCOLO"
      - "OBSERVACAO_DE_SCOUT_EXECUTADA_POR_ANALISTA"
      - "OBSERVACAO_DE_SCOUT_BASEADA_EM_MIDIA"
      - "OBSERVACAO_DE_SCOUT_CONTEM_EVENTO"
    logical_relation_ids:
      - "OBSERVACAO_DE_SCOUT"
    attribute_ids:
      - "ID"
    physical_object_ids:
      - "TABLE_OBSERVACAO_DE_SCOUT"
      - "COLUMN_OBSERVACAO_DE_SCOUT_ID"
    permission_requirement_ids: []
    test_ids:
      - "TEST_REJECT_INFERENTIAL_VARIABLES"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_REJEICAO_VARIAVEIS_INFERENCIAIS_ANALISTA_OBSERVADOR"
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
    concept_ids:
      - "OBSERVACAO_DE_SCOUT"
      - "ACAO_OBSERVADA"
      - "PROVENIENCIA_OBSERVACAO"
    rule_ids:
      - "RN_REJEICAO_VARIAVEIS_INFERENCIAIS"
    conceptual_entity_ids:
      - "UNIDADE_BASICA_ATAQUE_BOU"
      - "OBSERVACAO_DE_SCOUT"
      - "ANALISTA_OBSERVADOR"
      - "PROTOCOLO_SCOUT"
      - "MIDIA_VIDEO"
      - "PROVENIENCIA_OBSERVACAO"
    relationship_ids:
      - "POSSE_DE_BOLA_CONTEM_BOU"
      - "UNIDADE_BASICA_ATAQUE_BOU_GERA_EVENTO_SCOUT"
      - "OBSERVACAO_DE_SCOUT_REGISTRA_PARTIDA"
      - "OBSERVACAO_DE_SCOUT_UTILIZA_PROTOCOLO"
      - "OBSERVACAO_DE_SCOUT_EXECUTADA_POR_ANALISTA"
      - "OBSERVACAO_DE_SCOUT_BASEADA_EM_MIDIA"
      - "OBSERVACAO_DE_SCOUT_CONTEM_EVENTO"
    logical_relation_ids:
      - "ANALISTA_OBSERVADOR"
    attribute_ids:
      - "ID"
    physical_object_ids:
      - "TABLE_ANALISTA_OBSERVADOR"
      - "COLUMN_ANALISTA_OBSERVADOR_ID"
    permission_requirement_ids: []
    test_ids:
      - "TEST_REJECT_INFERENTIAL_VARIABLES"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_REJEICAO_VARIAVEIS_INFERENCIAIS_PROTOCOLO_SCOUT"
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
    concept_ids:
      - "OBSERVACAO_DE_SCOUT"
      - "ACAO_OBSERVADA"
      - "PROVENIENCIA_OBSERVACAO"
    rule_ids:
      - "RN_REJEICAO_VARIAVEIS_INFERENCIAIS"
    conceptual_entity_ids:
      - "UNIDADE_BASICA_ATAQUE_BOU"
      - "OBSERVACAO_DE_SCOUT"
      - "ANALISTA_OBSERVADOR"
      - "PROTOCOLO_SCOUT"
      - "MIDIA_VIDEO"
      - "PROVENIENCIA_OBSERVACAO"
    relationship_ids:
      - "POSSE_DE_BOLA_CONTEM_BOU"
      - "UNIDADE_BASICA_ATAQUE_BOU_GERA_EVENTO_SCOUT"
      - "OBSERVACAO_DE_SCOUT_REGISTRA_PARTIDA"
      - "OBSERVACAO_DE_SCOUT_UTILIZA_PROTOCOLO"
      - "OBSERVACAO_DE_SCOUT_EXECUTADA_POR_ANALISTA"
      - "OBSERVACAO_DE_SCOUT_BASEADA_EM_MIDIA"
      - "OBSERVACAO_DE_SCOUT_CONTEM_EVENTO"
    logical_relation_ids:
      - "PROTOCOLO_SCOUT"
    attribute_ids:
      - "ID"
    physical_object_ids:
      - "TABLE_PROTOCOLO_SCOUT"
      - "COLUMN_PROTOCOLO_SCOUT_ID"
    permission_requirement_ids: []
    test_ids:
      - "TEST_REJECT_INFERENTIAL_VARIABLES"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_REJEICAO_VARIAVEIS_INFERENCIAIS_MIDIA_VIDEO"
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
    concept_ids:
      - "OBSERVACAO_DE_SCOUT"
      - "ACAO_OBSERVADA"
      - "PROVENIENCIA_OBSERVACAO"
    rule_ids:
      - "RN_REJEICAO_VARIAVEIS_INFERENCIAIS"
    conceptual_entity_ids:
      - "UNIDADE_BASICA_ATAQUE_BOU"
      - "OBSERVACAO_DE_SCOUT"
      - "ANALISTA_OBSERVADOR"
      - "PROTOCOLO_SCOUT"
      - "MIDIA_VIDEO"
      - "PROVENIENCIA_OBSERVACAO"
    relationship_ids:
      - "POSSE_DE_BOLA_CONTEM_BOU"
      - "UNIDADE_BASICA_ATAQUE_BOU_GERA_EVENTO_SCOUT"
      - "OBSERVACAO_DE_SCOUT_REGISTRA_PARTIDA"
      - "OBSERVACAO_DE_SCOUT_UTILIZA_PROTOCOLO"
      - "OBSERVACAO_DE_SCOUT_EXECUTADA_POR_ANALISTA"
      - "OBSERVACAO_DE_SCOUT_BASEADA_EM_MIDIA"
      - "OBSERVACAO_DE_SCOUT_CONTEM_EVENTO"
    logical_relation_ids:
      - "MIDIA_VIDEO"
    attribute_ids:
      - "ID"
    physical_object_ids:
      - "TABLE_MIDIA_VIDEO"
      - "COLUMN_MIDIA_VIDEO_ID"
    permission_requirement_ids: []
    test_ids:
      - "TEST_REJECT_INFERENTIAL_VARIABLES"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_PASSIVO_QUATRO_PASSES_POSSE_DE_BOLA"
    evidence_ref_ids:
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_004"
    concept_ids:
      - "FASE_OFENSIVA"
      - "ACAO_OBSERVADA"
    rule_ids:
      - "RN_PASSIVO_QUATRO_PASSES"
    conceptual_entity_ids:
      - "POSSE_DE_BOLA"
    relationship_ids: []
    logical_relation_ids:
      - "POSSE_DE_BOLA"
    attribute_ids:
      - "ID"
    physical_object_ids:
      - "TABLE_POSSE_DE_BOLA"
      - "COLUMN_POSSE_DE_BOLA_ID"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PASSIVE_PLAY_FOUR_PASSES"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_SANCAO_FINAL_15_SEGUNDOS_PERIODO_SET"
    evidence_ref_ids:
      - "EVID_IHF_RULES_2026_EN_012"
      - "EVID_IHF_RULES_2026_EN_013"
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_005"
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_008"
    concept_ids:
      - "PUNICAO_DISCIPLINAR"
      - "CONSEQUENCIA_DISCIPLINAR"
      - "TIRO_SEIS_METROS"
    rule_ids:
      - "RN_SANCAO_FINAL_15_SEGUNDOS"
    conceptual_entity_ids:
      - "PERIODO_SET"
    relationship_ids: []
    logical_relation_ids:
      - "PERIODO_SET"
    attribute_ids:
      - "ID"
      - "HOUVE_GOL_DE_OURO"
    physical_object_ids:
      - "TABLE_PERIODO_SET"
      - "COLUMN_PERIODO_SET_ID"
      - "COLUMN_PERIODO_SET_HOUVE_GOL_DE_OURO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_LAST_15_SECONDS_SANCTION"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_PROTECAO_CABECA_GOLEIRA_EVENTO_SCOUT"
    evidence_ref_ids:
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_009"
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_010"
    concept_ids:
      - "GOLEIRA_POSICAO"
      - "PUNICAO_DISCIPLINAR"
      - "ACAO_DA_GOLEIRA"
    rule_ids:
      - "RN_PROTECAO_CABECA_GOLEIRA"
    conceptual_entity_ids:
      - "EVENTO_SCOUT"
    relationship_ids: []
    logical_relation_ids:
      - "EVENTO_SCOUT"
    attribute_ids:
      - "ID"
    physical_object_ids:
      - "TABLE_EVENTO_SCOUT"
      - "COLUMN_EVENTO_SCOUT_ID"
    permission_requirement_ids: []
    test_ids:
      - "TEST_GOALKEEPER_HEAD_HIT_AND_SIMULATION"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_PROIBICAO_RETARDO_REPETIDO_POSSE_DE_BOLA"
    evidence_ref_ids:
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_003"
    concept_ids:
      - "PUNICAO_DISCIPLINAR"
      - "ACAO_OBSERVADA"
    rule_ids:
      - "RN_PROIBICAO_RETARDO_REPETIDO"
    conceptual_entity_ids:
      - "POSSE_DE_BOLA"
    relationship_ids: []
    logical_relation_ids:
      - "POSSE_DE_BOLA"
    attribute_ids:
      - "ID"
    physical_object_ids:
      - "TABLE_POSSE_DE_BOLA"
      - "COLUMN_POSSE_DE_BOLA_ID"
    permission_requirement_ids: []
    test_ids:
      - "TEST_REPEATED_RESTART_DELAY"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_PRAZO_INSCRICAO_ATLETA_72H_EQUIPE"
    evidence_ref_ids:
      - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_004"
    concept_ids:
      - "COMPETICAO"
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    rule_ids:
      - "RN_PRAZO_INSCRICAO_ATLETA_72H"
    conceptual_entity_ids:
      - "COMPETICAO"
      - "EQUIPE"
      - "ATLETA"
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    relationship_ids:
      - "EQUIPE_INSCREVE_ATLETA"
    logical_relation_ids:
      - "EQUIPE"
    attribute_ids:
      - "ID"
    physical_object_ids:
      - "TABLE_EQUIPE"
      - "COLUMN_EQUIPE_ID"
    permission_requirement_ids: []
    test_ids:
      - "TEST_ATHLETE_REGISTRATION_72H_DEADLINE"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_PRAZO_INSCRICAO_ATLETA_72H_ATLETA"
    evidence_ref_ids:
      - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_004"
    concept_ids:
      - "COMPETICAO"
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    rule_ids:
      - "RN_PRAZO_INSCRICAO_ATLETA_72H"
    conceptual_entity_ids:
      - "COMPETICAO"
      - "EQUIPE"
      - "ATLETA"
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    relationship_ids:
      - "EQUIPE_INSCREVE_ATLETA"
    logical_relation_ids:
      - "ATLETA"
    attribute_ids:
      - "ID"
    physical_object_ids:
      - "TABLE_ATLETA"
      - "COLUMN_ATLETA_ID"
    permission_requirement_ids: []
    test_ids:
      - "TEST_ATHLETE_REGISTRATION_72H_DEADLINE"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_PRAZO_INSCRICAO_ATLETA_72H_EQUIPE_ATLETA_INSCRICAO"
    evidence_ref_ids:
      - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_004"
    concept_ids:
      - "COMPETICAO"
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    rule_ids:
      - "RN_PRAZO_INSCRICAO_ATLETA_72H"
    conceptual_entity_ids:
      - "COMPETICAO"
      - "EQUIPE"
      - "ATLETA"
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    relationship_ids:
      - "EQUIPE_INSCREVE_ATLETA"
    logical_relation_ids:
      - "EQUIPE_ATLETA_INSCRICAO"
    attribute_ids:
      - "DATA_INSCRICAO"
    physical_object_ids:
      - "TABLE_EQUIPE_ATLETA_INSCRICAO"
      - "COLUMN_EQUIPE_ATLETA_INSCRICAO_DATA_INSCRICAO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_ATHLETE_REGISTRATION_72H_DEADLINE"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_RN_REGRAS_EXECUCAO_TIRO_SEIS_METROS_EVENTO_SCOUT"
    evidence_ref_ids:
      - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_009"
      - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_010"
      - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_011"
      - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_012"
      - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_013"
    concept_ids:
      - "EVENTO_DE_PONTUACAO"
      - "ACAO_OBSERVADA"
    rule_ids:
      - "RN_REGRAS_EXECUCAO_TIRO_SEIS_METROS"
    conceptual_entity_ids:
      - "EVENTO_SCOUT"
    relationship_ids: []
    logical_relation_ids:
      - "EVENTO_SCOUT"
    attribute_ids:
      - "ID"
    physical_object_ids:
      - "TABLE_EVENTO_SCOUT"
      - "COLUMN_EVENTO_SCOUT_ID"
    permission_requirement_ids: []
    test_ids:
      - "TEST_SIX_METRE_THROW_EXECUTION"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_PARTIDA_COMPETICAO"
    evidence_ref_ids: []
    concept_ids:
      - "PARTIDA"
    rule_ids: []
    conceptual_entity_ids:
      - "PARTIDA"
    relationship_ids:
      - "COMPETICAO_POSSUI_PARTIDA"
    logical_relation_ids:
      - "PARTIDA"
    attribute_ids:
      - "COMPETICAO_ID"
    physical_object_ids:
      - "TABLE_PARTIDA"
      - "CONSTRAINT_FK_PARTIDA_COMPETICAO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_001"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_PARTIDA_EQUIPE_PARTIDA"
    evidence_ref_ids: []
    concept_ids:
      - "PARTIDA"
      - "EQUIPE"
    rule_ids: []
    conceptual_entity_ids:
      - "PARTIDA"
      - "EQUIPE"
    relationship_ids:
      - "PARTIDA_DISPUTADA_POR_EQUIPE"
    logical_relation_ids:
      - "PARTIDA_EQUIPE"
    attribute_ids:
      - "PARTIDA_ID"
    physical_object_ids:
      - "TABLE_PARTIDA_EQUIPE"
      - "CONSTRAINT_FK_PARTIDA_EQUIPE_PARTIDA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_002"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_PARTIDA_EQUIPE_EQUIPE"
    evidence_ref_ids: []
    concept_ids:
      - "PARTIDA"
      - "EQUIPE"
    rule_ids: []
    conceptual_entity_ids:
      - "PARTIDA"
      - "EQUIPE"
    relationship_ids:
      - "PARTIDA_DISPUTADA_POR_EQUIPE"
    logical_relation_ids:
      - "PARTIDA_EQUIPE"
    attribute_ids:
      - "EQUIPE_ID"
    physical_object_ids:
      - "TABLE_PARTIDA_EQUIPE"
      - "CONSTRAINT_FK_PARTIDA_EQUIPE_EQUIPE"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_003"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_INSCRICAO_EQUIPE"
    evidence_ref_ids: []
    concept_ids:
      - "EQUIPE"
      - "ATLETA"
    rule_ids: []
    conceptual_entity_ids:
      - "EQUIPE"
      - "ATLETA"
    relationship_ids:
      - "EQUIPE_INSCREVE_ATLETA"
    logical_relation_ids:
      - "EQUIPE_ATLETA_INSCRICAO"
    attribute_ids:
      - "EQUIPE_ID"
    physical_object_ids:
      - "TABLE_EQUIPE_ATLETA_INSCRICAO"
      - "CONSTRAINT_FK_INSCRICAO_EQUIPE"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_004"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_INSCRICAO_ATLETA"
    evidence_ref_ids: []
    concept_ids:
      - "EQUIPE"
      - "ATLETA"
    rule_ids: []
    conceptual_entity_ids:
      - "EQUIPE"
      - "ATLETA"
    relationship_ids:
      - "EQUIPE_INSCREVE_ATLETA"
    logical_relation_ids:
      - "EQUIPE_ATLETA_INSCRICAO"
    attribute_ids:
      - "ATLETA_ID"
    physical_object_ids:
      - "TABLE_EQUIPE_ATLETA_INSCRICAO"
      - "CONSTRAINT_FK_INSCRICAO_ATLETA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_005"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_INSCRICAO_COMPETICAO"
    evidence_ref_ids: []
    concept_ids:
      - "EQUIPE"
      - "ATLETA"
    rule_ids: []
    conceptual_entity_ids:
      - "EQUIPE"
      - "ATLETA"
    relationship_ids:
      - "EQUIPE_INSCREVE_ATLETA"
    logical_relation_ids:
      - "EQUIPE_ATLETA_INSCRICAO"
    attribute_ids:
      - "COMPETICAO_ID"
    physical_object_ids:
      - "TABLE_EQUIPE_ATLETA_INSCRICAO"
      - "CONSTRAINT_FK_INSCRICAO_COMPETICAO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_006"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_PERIODO_SET_PARTIDA"
    evidence_ref_ids: []
    concept_ids:
      - "PERIODO_SET"
    rule_ids: []
    conceptual_entity_ids:
      - "PERIODO_SET"
    relationship_ids:
      - "PARTIDA_POSSUI_PERIODO_SET"
    logical_relation_ids:
      - "PERIODO_SET"
    attribute_ids:
      - "PARTIDA_ID"
    physical_object_ids:
      - "TABLE_PERIODO_SET"
      - "CONSTRAINT_FK_PERIODO_SET_PARTIDA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_007"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_PERIODO_SET_EQUIPE_VENCEDORA"
    evidence_ref_ids: []
    concept_ids:
      - "PERIODO_SET"
    rule_ids: []
    conceptual_entity_ids:
      - "PERIODO_SET"
    relationship_ids: []
    logical_relation_ids:
      - "PERIODO_SET"
    attribute_ids:
      - "EQUIPE_VENCEDORA_ID"
    physical_object_ids:
      - "TABLE_PERIODO_SET"
      - "CONSTRAINT_FK_PERIODO_SET_EQUIPE_VENCEDORA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_008"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_SHOOT_OUT_PARTIDA"
    evidence_ref_ids: []
    concept_ids:
      - "SHOOT_OUT"
    rule_ids: []
    conceptual_entity_ids:
      - "SHOOT_OUT"
    relationship_ids:
      - "PARTIDA_POSSUI_SHOOT_OUT"
    logical_relation_ids:
      - "SHOOT_OUT"
    attribute_ids:
      - "PARTIDA_ID"
    physical_object_ids:
      - "TABLE_SHOOT_OUT"
      - "CONSTRAINT_FK_SHOOT_OUT_PARTIDA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_009"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_SHOOT_OUT_EQUIPE_VENCEDORA"
    evidence_ref_ids: []
    concept_ids:
      - "SHOOT_OUT"
    rule_ids: []
    conceptual_entity_ids:
      - "SHOOT_OUT"
    relationship_ids: []
    logical_relation_ids:
      - "SHOOT_OUT"
    attribute_ids:
      - "EQUIPE_VENCEDORA_ID"
    physical_object_ids:
      - "TABLE_SHOOT_OUT"
      - "CONSTRAINT_FK_SHOOT_OUT_EQUIPE_VENCEDORA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_010"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_POSSE_DE_BOLA_PERIODO_SET"
    evidence_ref_ids: []
    concept_ids:
      - "POSSE_DE_BOLA"
    rule_ids: []
    conceptual_entity_ids:
      - "POSSE_DE_BOLA"
    relationship_ids:
      - "PERIODO_SET_CONTEM_POSSE_DE_BOLA"
    logical_relation_ids:
      - "POSSE_DE_BOLA"
    attribute_ids:
      - "PERIODO_SET_ID"
    physical_object_ids:
      - "TABLE_POSSE_DE_BOLA"
      - "CONSTRAINT_FK_POSSE_DE_BOLA_PERIODO_SET"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_011"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_POSSE_DE_BOLA_EQUIPE"
    evidence_ref_ids: []
    concept_ids:
      - "POSSE_DE_BOLA"
    rule_ids: []
    conceptual_entity_ids:
      - "POSSE_DE_BOLA"
    relationship_ids: []
    logical_relation_ids:
      - "POSSE_DE_BOLA"
    attribute_ids:
      - "EQUIPE_POSSUIDORA_ID"
    physical_object_ids:
      - "TABLE_POSSE_DE_BOLA"
      - "CONSTRAINT_FK_POSSE_DE_BOLA_EQUIPE"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_012"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_BOU_POSSE_DE_BOLA"
    evidence_ref_ids: []
    concept_ids:
      - "UNIDADE_BASICA_ATAQUE_BOU"
    rule_ids: []
    conceptual_entity_ids:
      - "UNIDADE_BASICA_ATAQUE_BOU"
    relationship_ids:
      - "POSSE_DE_BOLA_CONTEM_BOU"
    logical_relation_ids:
      - "UNIDADE_BASICA_ATAQUE_BOU"
    attribute_ids:
      - "POSSE_DE_BOLA_ID"
    physical_object_ids:
      - "TABLE_UNIDADE_BASICA_ATAQUE_BOU"
      - "CONSTRAINT_FK_BOU_POSSE_DE_BOLA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_013"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_EVENTO_SCOUT_OBSERVACAO"
    evidence_ref_ids: []
    concept_ids:
      - "EVENTO_SCOUT"
    rule_ids: []
    conceptual_entity_ids:
      - "EVENTO_SCOUT"
    relationship_ids:
      - "OBSERVACAO_DE_SCOUT_CONTEM_EVENTO"
    logical_relation_ids:
      - "EVENTO_SCOUT"
    attribute_ids:
      - "OBSERVACAO_DE_SCOUT_ID"
    physical_object_ids:
      - "TABLE_EVENTO_SCOUT"
      - "CONSTRAINT_FK_EVENTO_SCOUT_OBSERVACAO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_014"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_EVENTO_SCOUT_BOU"
    evidence_ref_ids: []
    concept_ids:
      - "EVENTO_SCOUT"
    rule_ids: []
    conceptual_entity_ids:
      - "EVENTO_SCOUT"
    relationship_ids:
      - "UNIDADE_BASICA_ATAQUE_BOU_GERA_EVENTO_SCOUT"
    logical_relation_ids:
      - "EVENTO_SCOUT"
    attribute_ids:
      - "UNIDADE_BASICA_ATAQUE_BOU_ID"
    physical_object_ids:
      - "TABLE_EVENTO_SCOUT"
      - "CONSTRAINT_FK_EVENTO_SCOUT_BOU"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_015"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_EVENTO_SCOUT_ATLETA_EXEC"
    evidence_ref_ids: []
    concept_ids:
      - "EVENTO_SCOUT"
    rule_ids: []
    conceptual_entity_ids:
      - "EVENTO_SCOUT"
    relationship_ids:
      - "EVENTO_SCOUT_ENVOLVE_ATLETA"
    logical_relation_ids:
      - "EVENTO_SCOUT"
    attribute_ids:
      - "ATLETA_EXECUTOR_ID"
    physical_object_ids:
      - "TABLE_EVENTO_SCOUT"
      - "CONSTRAINT_FK_EVENTO_SCOUT_ATLETA_EXEC"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_016"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_EVENTO_SCOUT_ATLETA_ALVO"
    evidence_ref_ids: []
    concept_ids:
      - "EVENTO_SCOUT"
    rule_ids: []
    conceptual_entity_ids:
      - "EVENTO_SCOUT"
    relationship_ids:
      - "EVENTO_SCOUT_ENVOLVE_ATLETA"
    logical_relation_ids:
      - "EVENTO_SCOUT"
    attribute_ids:
      - "ATLETA_ALVO_ID"
    physical_object_ids:
      - "TABLE_EVENTO_SCOUT"
      - "CONSTRAINT_FK_EVENTO_SCOUT_ATLETA_ALVO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_017"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_OBSERVACAO_SCOUT_PARTIDA"
    evidence_ref_ids: []
    concept_ids:
      - "OBSERVACAO_DE_SCOUT"
    rule_ids: []
    conceptual_entity_ids:
      - "OBSERVACAO_DE_SCOUT"
    relationship_ids:
      - "OBSERVACAO_DE_SCOUT_REGISTRA_PARTIDA"
    logical_relation_ids:
      - "OBSERVACAO_DE_SCOUT"
    attribute_ids:
      - "PARTIDA_ID"
    physical_object_ids:
      - "TABLE_OBSERVACAO_DE_SCOUT"
      - "CONSTRAINT_FK_OBSERVACAO_SCOUT_PARTIDA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_018"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_OBSERVACAO_SCOUT_ANALISTA"
    evidence_ref_ids: []
    concept_ids:
      - "OBSERVACAO_DE_SCOUT"
    rule_ids: []
    conceptual_entity_ids:
      - "OBSERVACAO_DE_SCOUT"
    relationship_ids:
      - "OBSERVACAO_DE_SCOUT_EXECUTADA_POR_ANALISTA"
    logical_relation_ids:
      - "OBSERVACAO_DE_SCOUT"
    attribute_ids:
      - "ANALISTA_OBSERVADOR_ID"
    physical_object_ids:
      - "TABLE_OBSERVACAO_DE_SCOUT"
      - "CONSTRAINT_FK_OBSERVACAO_SCOUT_ANALISTA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_019"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_OBSERVACAO_SCOUT_PROTOCOLO"
    evidence_ref_ids: []
    concept_ids:
      - "OBSERVACAO_DE_SCOUT"
    rule_ids: []
    conceptual_entity_ids:
      - "OBSERVACAO_DE_SCOUT"
    relationship_ids:
      - "OBSERVACAO_DE_SCOUT_UTILIZA_PROTOCOLO"
    logical_relation_ids:
      - "OBSERVACAO_DE_SCOUT"
    attribute_ids:
      - "PROTOCOLO_SCOUT_ID"
    physical_object_ids:
      - "TABLE_OBSERVACAO_DE_SCOUT"
      - "CONSTRAINT_FK_OBSERVACAO_SCOUT_PROTOCOLO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_020"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_OBSERVACAO_SCOUT_MIDIA"
    evidence_ref_ids: []
    concept_ids:
      - "OBSERVACAO_DE_SCOUT"
    rule_ids: []
    conceptual_entity_ids:
      - "OBSERVACAO_DE_SCOUT"
    relationship_ids:
      - "OBSERVACAO_DE_SCOUT_BASEADA_EM_MIDIA"
    logical_relation_ids:
      - "OBSERVACAO_DE_SCOUT"
    attribute_ids:
      - "MIDIA_VIDEO_ID"
    physical_object_ids:
      - "TABLE_OBSERVACAO_DE_SCOUT"
      - "CONSTRAINT_FK_OBSERVACAO_SCOUT_MIDIA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_021"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_MIDIA_VIDEO_PARTIDA"
    evidence_ref_ids: []
    concept_ids:
      - "MIDIA_VIDEO"
    rule_ids: []
    conceptual_entity_ids:
      - "MIDIA_VIDEO"
    relationship_ids: []
    logical_relation_ids:
      - "MIDIA_VIDEO"
    attribute_ids:
      - "PARTIDA_ID"
    physical_object_ids:
      - "TABLE_MIDIA_VIDEO"
      - "CONSTRAINT_FK_MIDIA_VIDEO_PARTIDA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_022"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_SEGMENTO_OBSERVADO_PARTIDA"
    evidence_ref_ids: []
    concept_ids:
      - "SEGMENTO_OBSERVADO"
    rule_ids: []
    conceptual_entity_ids:
      - "SEGMENTO_OBSERVADO"
    relationship_ids:
      - "PARTIDA_POSSUI_SEGMENTO_OBSERVADO"
    logical_relation_ids:
      - "SEGMENTO_OBSERVADO"
    attribute_ids:
      - "PARTIDA_ID"
    physical_object_ids:
      - "TABLE_SEGMENTO_OBSERVADO"
      - "CONSTRAINT_FK_SEGMENTO_OBSERVADO_PARTIDA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_023"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_SEGMENTO_OBSERVADO_MIDIA"
    evidence_ref_ids: []
    concept_ids:
      - "SEGMENTO_OBSERVADO"
    rule_ids: []
    conceptual_entity_ids:
      - "SEGMENTO_OBSERVADO"
    relationship_ids:
      - "SEGMENTO_OBSERVADO_MAPPED_TO_MIDIA_VIDEO"
    logical_relation_ids:
      - "SEGMENTO_OBSERVADO"
    attribute_ids:
      - "MIDIA_VIDEO_ID"
    physical_object_ids:
      - "TABLE_SEGMENTO_OBSERVADO"
      - "CONSTRAINT_FK_SEGMENTO_OBSERVADO_MIDIA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_024"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_PLACAR_JOGO_PARTIDA"
    evidence_ref_ids: []
    concept_ids:
      - "PLACAR_JOGO"
    rule_ids: []
    conceptual_entity_ids:
      - "PLACAR_JOGO"
    relationship_ids:
      - "PARTIDA_POSSUI_PLACAR_JOGO"
    logical_relation_ids:
      - "PLACAR_JOGO"
    attribute_ids:
      - "PARTIDA_ID"
    physical_object_ids:
      - "TABLE_PLACAR_JOGO"
      - "CONSTRAINT_FK_PLACAR_JOGO_PARTIDA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_025"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_PLACAR_JOGO_EQUIPE_VENCEDORA"
    evidence_ref_ids: []
    concept_ids:
      - "PLACAR_JOGO"
    rule_ids: []
    conceptual_entity_ids:
      - "PLACAR_JOGO"
    relationship_ids: []
    logical_relation_ids:
      - "PLACAR_JOGO"
    attribute_ids:
      - "EQUIPE_VENCEDORA_ID"
    physical_object_ids:
      - "TABLE_PLACAR_JOGO"
      - "CONSTRAINT_FK_PLACAR_JOGO_EQUIPE_VENCEDORA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_026"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_ESTADO_PLACAR_PLACAR_JOGO"
    evidence_ref_ids: []
    concept_ids:
      - "ESTADO_DO_PLACAR"
    rule_ids: []
    conceptual_entity_ids:
      - "ESTADO_DO_PLACAR"
    relationship_ids:
      - "PLACAR_JOGO_REGISTRA_ESTADO"
    logical_relation_ids:
      - "ESTADO_DO_PLACAR"
    attribute_ids:
      - "PLACAR_JOGO_ID"
    physical_object_ids:
      - "TABLE_ESTADO_DO_PLACAR"
      - "CONSTRAINT_FK_ESTADO_PLACAR_PLACAR_JOGO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_027"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_ESTADO_PLACAR_PERIODO_SET"
    evidence_ref_ids: []
    concept_ids:
      - "ESTADO_DO_PLACAR"
    rule_ids: []
    conceptual_entity_ids:
      - "ESTADO_DO_PLACAR"
    relationship_ids:
      - "ESTADO_DO_PLACAR_PERTENCE_A_PERIODO_SET"
    logical_relation_ids:
      - "ESTADO_DO_PLACAR"
    attribute_ids:
      - "PERIODO_SET_ID"
    physical_object_ids:
      - "TABLE_ESTADO_DO_PLACAR"
      - "CONSTRAINT_FK_ESTADO_PLACAR_PERIODO_SET"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_028"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_EVOLUCAO_PLACAR_PARTIDA"
    evidence_ref_ids: []
    concept_ids:
      - "EVOLUCAO_DO_PLACAR"
    rule_ids: []
    conceptual_entity_ids:
      - "EVOLUCAO_DO_PLACAR"
    relationship_ids:
      - "PARTIDA_REGISTRA_EVOLUCAO_PLACAR"
    logical_relation_ids:
      - "EVOLUCAO_DO_PLACAR"
    attribute_ids:
      - "PARTIDA_ID"
    physical_object_ids:
      - "TABLE_EVOLUCAO_DO_PLACAR"
      - "CONSTRAINT_FK_EVOLUCAO_PLACAR_PARTIDA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_029"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_EVOLUCAO_PLACAR_EVENTO_SCOUT"
    evidence_ref_ids: []
    concept_ids:
      - "EVOLUCAO_DO_PLACAR"
    rule_ids: []
    conceptual_entity_ids:
      - "EVOLUCAO_DO_PLACAR"
    relationship_ids: []
    logical_relation_ids:
      - "EVOLUCAO_DO_PLACAR"
    attribute_ids:
      - "EVENTO_SCOUT_ID"
    physical_object_ids:
      - "TABLE_EVOLUCAO_DO_PLACAR"
      - "CONSTRAINT_FK_EVOLUCAO_PLACAR_EVENTO_SCOUT"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_030"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_EVOLUCAO_PLACAR_EQUIPE"
    evidence_ref_ids: []
    concept_ids:
      - "EVOLUCAO_DO_PLACAR"
    rule_ids: []
    conceptual_entity_ids:
      - "EVOLUCAO_DO_PLACAR"
    relationship_ids: []
    logical_relation_ids:
      - "EVOLUCAO_DO_PLACAR"
    attribute_ids:
      - "EQUIPE_BENEFICIADA_ID"
    physical_object_ids:
      - "TABLE_EVOLUCAO_DO_PLACAR"
      - "CONSTRAINT_FK_EVOLUCAO_PLACAR_EQUIPE"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_031"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_SISTEMA_DEFENSIVO_POSSE"
    evidence_ref_ids: []
    concept_ids:
      - "SISTEMA_DEFENSIVO"
    rule_ids: []
    conceptual_entity_ids:
      - "SISTEMA_DEFENSIVO"
    relationship_ids:
      - "POSSE_DE_BOLA_POSSUI_SISTEMA_DEFENSIVO"
    logical_relation_ids:
      - "SISTEMA_DEFENSIVO"
    attribute_ids:
      - "POSSE_DE_BOLA_ID"
    physical_object_ids:
      - "TABLE_SISTEMA_DEFENSIVO"
      - "CONSTRAINT_FK_SISTEMA_DEFENSIVO_POSSE"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_032"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_SISTEMA_DEFENSIVO_EQUIPE"
    evidence_ref_ids: []
    concept_ids:
      - "SISTEMA_DEFENSIVO"
    rule_ids: []
    conceptual_entity_ids:
      - "SISTEMA_DEFENSIVO"
    relationship_ids:
      - "SISTEMA_DEFENSIVO_PERTENCE_A_EQUIPE"
    logical_relation_ids:
      - "SISTEMA_DEFENSIVO"
    attribute_ids:
      - "EQUIPE_ID"
    physical_object_ids:
      - "TABLE_SISTEMA_DEFENSIVO"
      - "CONSTRAINT_FK_SISTEMA_DEFENSIVO_EQUIPE"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_033"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_SISTEMA_DEFENSIVO_SISTEMA_TATICO"
    evidence_ref_ids: []
    concept_ids:
      - "SISTEMA_DEFENSIVO"
    rule_ids: []
    conceptual_entity_ids:
      - "SISTEMA_DEFENSIVO"
    relationship_ids:
      - "SISTEMA_DEFENSIVO_ESPECIALIZA_SISTEMA_TATICO"
    logical_relation_ids:
      - "SISTEMA_DEFENSIVO"
    attribute_ids:
      - "SISTEMA_TATICO_ID"
    physical_object_ids:
      - "TABLE_SISTEMA_DEFENSIVO"
      - "CONSTRAINT_FK_SISTEMA_DEFENSIVO_SISTEMA_TATICO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_034"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_CONFIABILIDADE_ANALISTA"
    evidence_ref_ids: []
    concept_ids:
      - "CONFIABILIDADE_OBSERVADOR"
    rule_ids: []
    conceptual_entity_ids:
      - "CONFIABILIDADE_OBSERVADOR"
    relationship_ids:
      - "ANALISTA_OBSERVADOR_POSSUI_CONFIABILIDADE"
    logical_relation_ids:
      - "CONFIABILIDADE_OBSERVADOR"
    attribute_ids:
      - "ANALISTA_OBSERVADOR_ID"
    physical_object_ids:
      - "TABLE_CONFIABILIDADE_OBSERVADOR"
      - "CONSTRAINT_FK_CONFIABILIDADE_ANALISTA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_035"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_REVISAO_OBSERVACAO_OBS"
    evidence_ref_ids: []
    concept_ids:
      - "REVISAO_DA_OBSERVACAO"
    rule_ids: []
    conceptual_entity_ids:
      - "REVISAO_DA_OBSERVACAO"
    relationship_ids:
      - "OBSERVACAO_DE_SCOUT_SOFRE_REVISAO"
    logical_relation_ids:
      - "REVISAO_DA_OBSERVACAO"
    attribute_ids:
      - "OBSERVACAO_DE_SCOUT_ID"
    physical_object_ids:
      - "TABLE_REVISAO_DA_OBSERVACAO"
      - "CONSTRAINT_FK_REVISAO_OBSERVACAO_OBS"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_036"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_REVISAO_OBSERVACAO_ANALISTA"
    evidence_ref_ids: []
    concept_ids:
      - "REVISAO_DA_OBSERVACAO"
    rule_ids: []
    conceptual_entity_ids:
      - "REVISAO_DA_OBSERVACAO"
    relationship_ids:
      - "REVISAO_DA_OBSERVACAO_EXECUTADA_POR_ANALISTA"
    logical_relation_ids:
      - "REVISAO_DA_OBSERVACAO"
    attribute_ids:
      - "ANALISTA_REVISOR_ID"
    physical_object_ids:
      - "TABLE_REVISAO_DA_OBSERVACAO"
      - "CONSTRAINT_FK_REVISAO_OBSERVACAO_ANALISTA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_037"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_ESTADO_REVISAO_OBSERVACAO"
    evidence_ref_ids: []
    concept_ids:
      - "ESTADO_DE_REVISAO"
    rule_ids: []
    conceptual_entity_ids:
      - "ESTADO_DE_REVISAO"
    relationship_ids:
      - "OBSERVACAO_DE_SCOUT_POSSUI_ESTADO_DE_REVISAO"
    logical_relation_ids:
      - "ESTADO_DE_REVISAO"
    attribute_ids:
      - "OBSERVACAO_DE_SCOUT_ID"
    physical_object_ids:
      - "TABLE_ESTADO_DE_REVISAO"
      - "CONSTRAINT_FK_ESTADO_REVISAO_OBSERVACAO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_038"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_ESTADO_REVISAO_REVISAO"
    evidence_ref_ids: []
    concept_ids:
      - "ESTADO_DE_REVISAO"
    rule_ids: []
    conceptual_entity_ids:
      - "ESTADO_DE_REVISAO"
    relationship_ids:
      - "REVISAO_DA_OBSERVACAO_GERA_ESTADO_DE_REVISAO"
    logical_relation_ids:
      - "ESTADO_DE_REVISAO"
    attribute_ids:
      - "REVISAO_DA_OBSERVACAO_ID"
    physical_object_ids:
      - "TABLE_ESTADO_DE_REVISAO"
      - "CONSTRAINT_FK_ESTADO_REVISAO_REVISAO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_039"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_PROVENIENCIA_OBSERVACAO_OBS"
    evidence_ref_ids: []
    concept_ids:
      - "PROVENIENCIA_OBSERVACAO"
    rule_ids: []
    conceptual_entity_ids:
      - "PROVENIENCIA_OBSERVACAO"
    relationship_ids:
      - "OBSERVACAO_DE_SCOUT_TEM_PROVENIENCIA"
    logical_relation_ids:
      - "PROVENIENCIA_OBSERVACAO"
    attribute_ids:
      - "OBSERVACAO_DE_SCOUT_ID"
    physical_object_ids:
      - "TABLE_PROVENIENCIA_OBSERVACAO"
      - "CONSTRAINT_FK_PROVENIENCIA_OBSERVACAO_OBS"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_040"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_PROVENIENCIA_PROTOCOLO"
    evidence_ref_ids: []
    concept_ids:
      - "PROVENIENCIA_OBSERVACAO"
    rule_ids: []
    conceptual_entity_ids:
      - "PROVENIENCIA_OBSERVACAO"
    relationship_ids:
      - "PROVENIENCIA_OBSERVACAO_VINCULA_PROTOCOLO_SCOUT"
    logical_relation_ids:
      - "PROVENIENCIA_OBSERVACAO"
    attribute_ids:
      - "PROTOCOLO_SCOUT_ID"
    physical_object_ids:
      - "TABLE_PROVENIENCIA_OBSERVACAO"
      - "CONSTRAINT_FK_PROVENIENCIA_PROTOCOLO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_041"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_PROVENIENCIA_MIDIA"
    evidence_ref_ids: []
    concept_ids:
      - "PROVENIENCIA_OBSERVACAO"
    rule_ids: []
    conceptual_entity_ids:
      - "PROVENIENCIA_OBSERVACAO"
    relationship_ids:
      - "PROVENIENCIA_OBSERVACAO_REFERENCIA_MIDIA_VIDEO"
    logical_relation_ids:
      - "PROVENIENCIA_OBSERVACAO"
    attribute_ids:
      - "MIDIA_VIDEO_ID"
    physical_object_ids:
      - "TABLE_PROVENIENCIA_OBSERVACAO"
      - "CONSTRAINT_FK_PROVENIENCIA_MIDIA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_042"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_TRECHO_OBSERVADO_EVENTO"
    evidence_ref_ids: []
    concept_ids:
      - "TRECHO_OBSERVADO"
    rule_ids: []
    conceptual_entity_ids:
      - "TRECHO_OBSERVADO"
    relationship_ids:
      - "EVENTO_SCOUT_VINCULA_TRECHO_OBSERVADO"
    logical_relation_ids:
      - "TRECHO_OBSERVADO"
    attribute_ids:
      - "EVENTO_SCOUT_ID"
    physical_object_ids:
      - "TABLE_TRECHO_OBSERVADO"
      - "CONSTRAINT_FK_TRECHO_OBSERVADO_EVENTO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_043"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_TRECHO_OBSERVADO_MIDIA"
    evidence_ref_ids: []
    concept_ids:
      - "TRECHO_OBSERVADO"
    rule_ids: []
    conceptual_entity_ids:
      - "TRECHO_OBSERVADO"
    relationship_ids:
      - "TRECHO_OBSERVADO_PERTENCE_A_MIDIA_VIDEO"
    logical_relation_ids:
      - "TRECHO_OBSERVADO"
    attribute_ids:
      - "MIDIA_VIDEO_ID"
    physical_object_ids:
      - "TABLE_TRECHO_OBSERVADO"
      - "CONSTRAINT_FK_TRECHO_OBSERVADO_MIDIA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_044"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_SPIN_SHOT_EVENTO"
    evidence_ref_ids: []
    concept_ids:
      - "SPIN_SHOT"
    rule_ids: []
    conceptual_entity_ids:
      - "SPIN_SHOT"
    relationship_ids:
      - "EVENTO_SCOUT_CLASSIFICA_SPIN_SHOT"
    logical_relation_ids:
      - "SPIN_SHOT"
    attribute_ids:
      - "EVENTO_SCOUT_ID"
    physical_object_ids:
      - "TABLE_SPIN_SHOT"
      - "CONSTRAINT_FK_SPIN_SHOT_EVENTO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_045"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_IN_FLIGHT_SHOT_EVENTO"
    evidence_ref_ids: []
    concept_ids:
      - "IN_FLIGHT_SHOT"
    rule_ids: []
    conceptual_entity_ids:
      - "IN_FLIGHT_SHOT"
    relationship_ids:
      - "EVENTO_SCOUT_CLASSIFICA_IN_FLIGHT_SHOT"
    logical_relation_ids:
      - "IN_FLIGHT_SHOT"
    attribute_ids:
      - "EVENTO_SCOUT_ID"
    physical_object_ids:
      - "TABLE_IN_FLIGHT_SHOT"
      - "CONSTRAINT_FK_IN_FLIGHT_SHOT_EVENTO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_046"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_DESQUALIFICACAO_EVENTO"
    evidence_ref_ids: []
    concept_ids:
      - "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
    rule_ids: []
    conceptual_entity_ids:
      - "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
    relationship_ids:
      - "DESQUALIFICACAO_REGISTRADA_EM_EVENTO_SCOUT"
    logical_relation_ids:
      - "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
    attribute_ids:
      - "EVENTO_SCOUT_ID"
    physical_object_ids:
      - "TABLE_DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
      - "CONSTRAINT_FK_DESQUALIFICACAO_EVENTO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_047"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_DESQUALIFICACAO_ATLETA"
    evidence_ref_ids: []
    concept_ids:
      - "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
    rule_ids: []
    conceptual_entity_ids:
      - "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
    relationship_ids:
      - "DESQUALIFICACAO_ATINGE_ATLETA"
    logical_relation_ids:
      - "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
    attribute_ids:
      - "ATLETA_ID"
    physical_object_ids:
      - "TABLE_DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
      - "CONSTRAINT_FK_DESQUALIFICACAO_ATLETA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_048"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_DESQUALIFICACAO_PARTIDA"
    evidence_ref_ids: []
    concept_ids:
      - "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
    rule_ids: []
    conceptual_entity_ids:
      - "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
    relationship_ids:
      - "DESQUALIFICACAO_OCORRE_EM_PARTIDA"
    logical_relation_ids:
      - "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
    attribute_ids:
      - "PARTIDA_ID"
    physical_object_ids:
      - "TABLE_DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
      - "CONSTRAINT_FK_DESQUALIFICACAO_PARTIDA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_049"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_CARTAO_AZUL_EVENTO"
    evidence_ref_ids: []
    concept_ids:
      - "CARTAO_AZUL_SUSPENSAO"
    rule_ids: []
    conceptual_entity_ids:
      - "CARTAO_AZUL_SUSPENSAO"
    relationship_ids:
      - "CARTAO_AZUL_REGISTRADO_EM_EVENTO_SCOUT"
    logical_relation_ids:
      - "CARTAO_AZUL_SUSPENSAO"
    attribute_ids:
      - "EVENTO_SCOUT_ID"
    physical_object_ids:
      - "TABLE_CARTAO_AZUL_SUSPENSAO"
      - "CONSTRAINT_FK_CARTAO_AZUL_EVENTO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_050"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_CARTAO_AZUL_PARTIDA"
    evidence_ref_ids: []
    concept_ids:
      - "CARTAO_AZUL_SUSPENSAO"
    rule_ids: []
    conceptual_entity_ids:
      - "CARTAO_AZUL_SUSPENSAO"
    relationship_ids:
      - "CARTAO_AZUL_OCORRE_EM_PARTIDA"
    logical_relation_ids:
      - "CARTAO_AZUL_SUSPENSAO"
    attribute_ids:
      - "PARTIDA_ID"
    physical_object_ids:
      - "TABLE_CARTAO_AZUL_SUSPENSAO"
      - "CONSTRAINT_FK_CARTAO_AZUL_PARTIDA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_051"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_CARTAO_AZUL_ATLETA"
    evidence_ref_ids: []
    concept_ids:
      - "CARTAO_AZUL_SUSPENSAO"
    rule_ids: []
    conceptual_entity_ids:
      - "CARTAO_AZUL_SUSPENSAO"
    relationship_ids:
      - "CARTAO_AZUL_ATINGE_ATLETA"
    logical_relation_ids:
      - "CARTAO_AZUL_SUSPENSAO"
    attribute_ids:
      - "ATLETA_ID"
    physical_object_ids:
      - "TABLE_CARTAO_AZUL_SUSPENSAO"
      - "CONSTRAINT_FK_CARTAO_AZUL_ATLETA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_052"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_CARTAO_AZUL_PAPEL_OPERACIONAL"
    evidence_ref_ids: []
    concept_ids:
      - "CARTAO_AZUL_SUSPENSAO"
    rule_ids: []
    conceptual_entity_ids:
      - "CARTAO_AZUL_SUSPENSAO"
    relationship_ids:
      - "CARTAO_AZUL_ATINGE_PAPEL_OPERACIONAL"
    logical_relation_ids:
      - "CARTAO_AZUL_SUSPENSAO"
    attribute_ids:
      - "PAPEL_OPERACIONAL_ID"
    physical_object_ids:
      - "TABLE_CARTAO_AZUL_SUSPENSAO"
      - "CONSTRAINT_FK_CARTAO_AZUL_PAPEL_OPERACIONAL"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_053"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_SISTEMA_TATICO_POSSE"
    evidence_ref_ids: []
    concept_ids:
      - "SISTEMA_TATICO"
    rule_ids: []
    conceptual_entity_ids:
      - "SISTEMA_TATICO"
    relationship_ids:
      - "SISTEMA_TATICO_CONTEXTUALIZA_POSSE"
    logical_relation_ids:
      - "SISTEMA_TATICO"
    attribute_ids:
      - "POSSE_DE_BOLA_ID"
    physical_object_ids:
      - "TABLE_SISTEMA_TATICO"
      - "CONSTRAINT_FK_SISTEMA_TATICO_POSSE"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_054"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_SISTEMA_TATICO_EQUIPE"
    evidence_ref_ids: []
    concept_ids:
      - "SISTEMA_TATICO"
    rule_ids: []
    conceptual_entity_ids:
      - "SISTEMA_TATICO"
    relationship_ids:
      - "SISTEMA_TATICO_ADOTADO_POR_EQUIPE"
    logical_relation_ids:
      - "SISTEMA_TATICO"
    attribute_ids:
      - "EQUIPE_ID"
    physical_object_ids:
      - "TABLE_SISTEMA_TATICO"
      - "CONSTRAINT_FK_SISTEMA_TATICO_EQUIPE"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_055"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_PAPEL_OPERACIONAL_PARTIDA"
    evidence_ref_ids: []
    concept_ids:
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    rule_ids: []
    conceptual_entity_ids:
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    relationship_ids:
      - "PAPEL_OPERACIONAL_ATRIBUIDO_EM_PARTIDA"
    logical_relation_ids:
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    attribute_ids:
      - "PARTIDA_ID"
    physical_object_ids:
      - "TABLE_PAPEL_ESPORTIVO_OPERACIONAL"
      - "CONSTRAINT_FK_PAPEL_OPERACIONAL_PARTIDA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_056"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_PAPEL_OPERACIONAL_EQUIPE"
    evidence_ref_ids: []
    concept_ids:
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    rule_ids: []
    conceptual_entity_ids:
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    relationship_ids:
      - "PAPEL_OPERACIONAL_VINCULADO_A_EQUIPE"
    logical_relation_ids:
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    attribute_ids:
      - "EQUIPE_ID"
    physical_object_ids:
      - "TABLE_PAPEL_ESPORTIVO_OPERACIONAL"
      - "CONSTRAINT_FK_PAPEL_OPERACIONAL_EQUIPE"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_057"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_PARTICIPACAO_EQUIPE_COMPETICAO_COMPETICAO"
    evidence_ref_ids: []
    concept_ids:
      - "EQUIPE"
      - "COMPETICAO"
    rule_ids: []
    conceptual_entity_ids:
      - "EQUIPE"
      - "COMPETICAO"
    relationship_ids:
      - "EQUIPE_PARTICIPA_COMPETICAO"
    logical_relation_ids:
      - "PARTICIPACAO_EQUIPE_COMPETICAO"
    attribute_ids:
      - "COMPETICAO_ID"
    physical_object_ids:
      - "TABLE_PARTICIPACAO_EQUIPE_COMPETICAO"
      - "CONSTRAINT_FK_PARTICIPACAO_EQUIPE_COMPETICAO_COMPETICAO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_058"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_FK_PARTICIPACAO_EQUIPE_COMPETICAO_EQUIPE"
    evidence_ref_ids: []
    concept_ids:
      - "EQUIPE"
      - "COMPETICAO"
    rule_ids: []
    conceptual_entity_ids:
      - "EQUIPE"
      - "COMPETICAO"
    relationship_ids:
      - "EQUIPE_PARTICIPA_COMPETICAO"
    logical_relation_ids:
      - "PARTICIPACAO_EQUIPE_COMPETICAO"
    attribute_ids:
      - "EQUIPE_ID"
    physical_object_ids:
      - "TABLE_PARTICIPACAO_EQUIPE_COMPETICAO"
      - "CONSTRAINT_FK_PARTICIPACAO_EQUIPE_COMPETICAO_EQUIPE"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_059"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_CHK_PARTIDA_VIGENCIA_2026"
    evidence_ref_ids:
      - "EVID_IHF_RULES_2026_EN_001"
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_002"
    concept_ids:
      - "PARTIDA"
    rule_ids:
      - "RN_IHF_VIGENCIA_2026"
    conceptual_entity_ids:
      - "PARTIDA"
    relationship_ids: []
    logical_relation_ids:
      - "PARTIDA"
    attribute_ids: []
    physical_object_ids:
      - "TABLE_PARTIDA"
      - "CONSTRAINT_CHK_PARTIDA_VIGENCIA_2026"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_060"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_CHK_ATLETA_SEMANTICA_GOLEIRA"
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_004"
      - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_007"
    concept_ids:
      - "ATLETA"
    rule_ids:
      - "RN_SEMANTICA_GOLEIRA"
    conceptual_entity_ids:
      - "ATLETA"
    relationship_ids: []
    logical_relation_ids:
      - "ATLETA"
    attribute_ids: []
    physical_object_ids:
      - "TABLE_ATLETA"
      - "CONSTRAINT_CHK_ATLETA_SEMANTICA_GOLEIRA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_061"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_UQ_PARTIDA_PAPEL_REGULAMENTAR"
    evidence_ref_ids: []
    concept_ids:
      - "PARTIDA"
      - "EQUIPE"
    rule_ids: []
    conceptual_entity_ids:
      - "PARTIDA"
      - "EQUIPE"
    relationship_ids: []
    logical_relation_ids:
      - "PARTIDA_EQUIPE"
    attribute_ids:
      - "PARTIDA_ID"
      - "PAPEL_REGULAMENTAR"
    physical_object_ids:
      - "TABLE_PARTIDA_EQUIPE"
      - "CONSTRAINT_UQ_PARTIDA_PAPEL_REGULAMENTAR"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_062"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_UQ_PARTIDA_CONDICAO_MANDO"
    evidence_ref_ids: []
    concept_ids:
      - "PARTIDA"
      - "EQUIPE"
    rule_ids: []
    conceptual_entity_ids:
      - "PARTIDA"
      - "EQUIPE"
    relationship_ids: []
    logical_relation_ids:
      - "PARTIDA_EQUIPE"
    attribute_ids:
      - "PARTIDA_ID"
      - "CONDICAO_MANDO"
    physical_object_ids:
      - "TABLE_PARTIDA_EQUIPE"
      - "CONSTRAINT_UQ_PARTIDA_CONDICAO_MANDO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_063"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_CHK_TETO_PARTICIPANTES_SUMULA"
    evidence_ref_ids:
      - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_007"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_024"
    concept_ids:
      - "PARTIDA"
      - "EQUIPE"
    rule_ids:
      - "RN_TETO_PARTICIPANTES_SUMULA"
    conceptual_entity_ids:
      - "PARTIDA"
      - "EQUIPE"
    relationship_ids: []
    logical_relation_ids:
      - "PARTIDA_EQUIPE"
    attribute_ids: []
    physical_object_ids:
      - "TABLE_PARTIDA_EQUIPE"
      - "CONSTRAINT_CHK_TETO_PARTICIPANTES_SUMULA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_064"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_UQ_EQUIPE_ATLETA_COMPETICAO"
    evidence_ref_ids: []
    concept_ids:
      - "EQUIPE"
      - "ATLETA"
    rule_ids: []
    conceptual_entity_ids:
      - "EQUIPE"
      - "ATLETA"
    relationship_ids: []
    logical_relation_ids:
      - "EQUIPE_ATLETA_INSCRICAO"
    attribute_ids:
      - "EQUIPE_ID"
      - "ATLETA_ID"
      - "COMPETICAO_ID"
    physical_object_ids:
      - "TABLE_EQUIPE_ATLETA_INSCRICAO"
      - "CONSTRAINT_UQ_EQUIPE_ATLETA_COMPETICAO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_065"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_CHK_PRAZO_INSCRICAO_72H"
    evidence_ref_ids:
      - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_004"
    concept_ids:
      - "EQUIPE"
      - "ATLETA"
    rule_ids:
      - "RN_PRAZO_INSCRICAO_ATLETA_72H"
    conceptual_entity_ids:
      - "EQUIPE"
      - "ATLETA"
    relationship_ids: []
    logical_relation_ids:
      - "EQUIPE_ATLETA_INSCRICAO"
    attribute_ids: []
    physical_object_ids:
      - "TABLE_EQUIPE_ATLETA_INSCRICAO"
      - "CONSTRAINT_CHK_PRAZO_INSCRICAO_72H"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_066"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_UQ_PARTIDA_NUMERO_SET"
    evidence_ref_ids: []
    concept_ids:
      - "PERIODO_SET"
    rule_ids: []
    conceptual_entity_ids:
      - "PERIODO_SET"
    relationship_ids: []
    logical_relation_ids:
      - "PERIODO_SET"
    attribute_ids:
      - "PARTIDA_ID"
      - "NUMERO_SET"
    physical_object_ids:
      - "TABLE_PERIODO_SET"
      - "CONSTRAINT_UQ_PARTIDA_NUMERO_SET"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_067"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_CHK_NUMERO_SET_VALIDO"
    evidence_ref_ids:
      - "EVID_IHF_RULES_2026_EN_001"
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_002"
    concept_ids:
      - "PERIODO_SET"
    rule_ids:
      - "RN_IHF_VIGENCIA_2026"
    conceptual_entity_ids:
      - "PERIODO_SET"
    relationship_ids: []
    logical_relation_ids:
      - "PERIODO_SET"
    attribute_ids: []
    physical_object_ids:
      - "TABLE_PERIODO_SET"
      - "CONSTRAINT_CHK_NUMERO_SET_VALIDO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_068"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_UQ_SHOOT_OUT_PARTIDA"
    evidence_ref_ids: []
    concept_ids:
      - "SHOOT_OUT"
    rule_ids: []
    conceptual_entity_ids:
      - "SHOOT_OUT"
    relationship_ids: []
    logical_relation_ids:
      - "SHOOT_OUT"
    attribute_ids:
      - "PARTIDA_ID"
    physical_object_ids:
      - "TABLE_SHOOT_OUT"
      - "CONSTRAINT_UQ_SHOOT_OUT_PARTIDA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_069"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_CHK_SHOOT_OUT_COMPLETUDE"
    evidence_ref_ids: []
    concept_ids:
      - "SHOOT_OUT"
    rule_ids: []
    conceptual_entity_ids:
      - "SHOOT_OUT"
    relationship_ids: []
    logical_relation_ids:
      - "SHOOT_OUT"
    attribute_ids: []
    physical_object_ids:
      - "TABLE_SHOOT_OUT"
      - "CONSTRAINT_CHK_SHOOT_OUT_COMPLETUDE"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_070"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_UQ_POSSE_PERIODO_SEQ"
    evidence_ref_ids: []
    concept_ids:
      - "POSSE_DE_BOLA"
    rule_ids: []
    conceptual_entity_ids:
      - "POSSE_DE_BOLA"
    relationship_ids: []
    logical_relation_ids:
      - "POSSE_DE_BOLA"
    attribute_ids:
      - "PERIODO_SET_ID"
      - "SEQUENCIAL_POSSE"
    physical_object_ids:
      - "TABLE_POSSE_DE_BOLA"
      - "CONSTRAINT_UQ_POSSE_PERIODO_SEQ"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_071"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_CHK_PASSIVO_QUATRO_PASSES"
    evidence_ref_ids:
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_004"
    concept_ids:
      - "POSSE_DE_BOLA"
    rule_ids:
      - "RN_PASSIVO_QUATRO_PASSES"
    conceptual_entity_ids:
      - "POSSE_DE_BOLA"
    relationship_ids: []
    logical_relation_ids:
      - "POSSE_DE_BOLA"
    attribute_ids: []
    physical_object_ids:
      - "TABLE_POSSE_DE_BOLA"
      - "CONSTRAINT_CHK_PASSIVO_QUATRO_PASSES"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_072"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_UQ_BOU_POSSE_SEQ"
    evidence_ref_ids: []
    concept_ids:
      - "UNIDADE_BASICA_ATAQUE_BOU"
    rule_ids: []
    conceptual_entity_ids:
      - "UNIDADE_BASICA_ATAQUE_BOU"
    relationship_ids: []
    logical_relation_ids:
      - "UNIDADE_BASICA_ATAQUE_BOU"
    attribute_ids:
      - "POSSE_DE_BOLA_ID"
      - "SEQUENCIAL_BOU"
    physical_object_ids:
      - "TABLE_UNIDADE_BASICA_ATAQUE_BOU"
      - "CONSTRAINT_UQ_BOU_POSSE_SEQ"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_073"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_CHK_BOU_REJEICAO_INFERENCIAIS"
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
    concept_ids:
      - "UNIDADE_BASICA_ATAQUE_BOU"
    rule_ids:
      - "RN_REJEICAO_VARIAVEIS_INFERENCIAIS"
    conceptual_entity_ids:
      - "UNIDADE_BASICA_ATAQUE_BOU"
    relationship_ids: []
    logical_relation_ids:
      - "UNIDADE_BASICA_ATAQUE_BOU"
    attribute_ids: []
    physical_object_ids:
      - "TABLE_UNIDADE_BASICA_ATAQUE_BOU"
      - "CONSTRAINT_CHK_BOU_REJEICAO_INFERENCIAIS"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_074"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_CHK_PROTECAO_CABECA_GOLEIRA"
    evidence_ref_ids:
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_009"
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_010"
    concept_ids:
      - "EVENTO_SCOUT"
    rule_ids:
      - "RN_PROTECAO_CABECA_GOLEIRA"
    conceptual_entity_ids:
      - "EVENTO_SCOUT"
    relationship_ids: []
    logical_relation_ids:
      - "EVENTO_SCOUT"
    attribute_ids: []
    physical_object_ids:
      - "TABLE_EVENTO_SCOUT"
      - "CONSTRAINT_CHK_PROTECAO_CABECA_GOLEIRA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_075"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_CHK_REGRAS_EXECUCAO_TIRO_SEIS_METROS"
    evidence_ref_ids:
      - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_009"
      - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_010"
      - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_011"
      - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_012"
      - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_013"
    concept_ids:
      - "EVENTO_SCOUT"
    rule_ids:
      - "RN_REGRAS_EXECUCAO_TIRO_SEIS_METROS"
    conceptual_entity_ids:
      - "EVENTO_SCOUT"
    relationship_ids: []
    logical_relation_ids:
      - "EVENTO_SCOUT"
    attribute_ids: []
    physical_object_ids:
      - "TABLE_EVENTO_SCOUT"
      - "CONSTRAINT_CHK_REGRAS_EXECUCAO_TIRO_SEIS_METROS"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_076"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_CHK_REJEICAO_VARIAVEIS_INFERENCIAIS"
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
    concept_ids:
      - "OBSERVACAO_DE_SCOUT"
    rule_ids:
      - "RN_REJEICAO_VARIAVEIS_INFERENCIAIS"
    conceptual_entity_ids:
      - "OBSERVACAO_DE_SCOUT"
    relationship_ids: []
    logical_relation_ids:
      - "OBSERVACAO_DE_SCOUT"
    attribute_ids: []
    physical_object_ids:
      - "TABLE_OBSERVACAO_DE_SCOUT"
      - "CONSTRAINT_CHK_REJEICAO_VARIAVEIS_INFERENCIAIS"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_077"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_UQ_SEGMENTO_ORDEM"
    evidence_ref_ids: []
    concept_ids:
      - "SEGMENTO_OBSERVADO"
    rule_ids: []
    conceptual_entity_ids:
      - "SEGMENTO_OBSERVADO"
    relationship_ids: []
    logical_relation_ids:
      - "SEGMENTO_OBSERVADO"
    attribute_ids:
      - "PARTIDA_ID"
      - "ORDEM_INTERVALO"
    physical_object_ids:
      - "TABLE_SEGMENTO_OBSERVADO"
      - "CONSTRAINT_UQ_SEGMENTO_ORDEM"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_078"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_UQ_PLACAR_PARTIDA"
    evidence_ref_ids: []
    concept_ids:
      - "PLACAR_JOGO"
    rule_ids: []
    conceptual_entity_ids:
      - "PLACAR_JOGO"
    relationship_ids: []
    logical_relation_ids:
      - "PLACAR_JOGO"
    attribute_ids:
      - "PARTIDA_ID"
    physical_object_ids:
      - "TABLE_PLACAR_JOGO"
      - "CONSTRAINT_UQ_PLACAR_PARTIDA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_079"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_UQ_EVOLUCAO_PARTIDA_SEQ"
    evidence_ref_ids: []
    concept_ids:
      - "EVOLUCAO_DO_PLACAR"
    rule_ids: []
    conceptual_entity_ids:
      - "EVOLUCAO_DO_PLACAR"
    relationship_ids: []
    logical_relation_ids:
      - "EVOLUCAO_DO_PLACAR"
    attribute_ids:
      - "PARTIDA_ID"
      - "SEQUENCIAL_PONTUACAO"
    physical_object_ids:
      - "TABLE_EVOLUCAO_DO_PLACAR"
      - "CONSTRAINT_UQ_EVOLUCAO_PARTIDA_SEQ"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_080"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_UQ_ESTADO_REVISAO_OBSERVA"
    evidence_ref_ids: []
    concept_ids:
      - "ESTADO_DE_REVISAO"
    rule_ids: []
    conceptual_entity_ids:
      - "ESTADO_DE_REVISAO"
    relationship_ids: []
    logical_relation_ids:
      - "ESTADO_DE_REVISAO"
    attribute_ids:
      - "OBSERVACAO_DE_SCOUT_ID"
    physical_object_ids:
      - "TABLE_ESTADO_DE_REVISAO"
      - "CONSTRAINT_UQ_ESTADO_REVISAO_OBSERVA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_081"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_UQ_PROVENIENCIA_OBS"
    evidence_ref_ids: []
    concept_ids:
      - "PROVENIENCIA_OBSERVACAO"
    rule_ids: []
    conceptual_entity_ids:
      - "PROVENIENCIA_OBSERVACAO"
    relationship_ids: []
    logical_relation_ids:
      - "PROVENIENCIA_OBSERVACAO"
    attribute_ids:
      - "OBSERVACAO_DE_SCOUT_ID"
    physical_object_ids:
      - "TABLE_PROVENIENCIA_OBSERVACAO"
      - "CONSTRAINT_UQ_PROVENIENCIA_OBS"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_082"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_UQ_SPIN_SHOT_EVENTO"
    evidence_ref_ids: []
    concept_ids:
      - "SPIN_SHOT"
    rule_ids: []
    conceptual_entity_ids:
      - "SPIN_SHOT"
    relationship_ids: []
    logical_relation_ids:
      - "SPIN_SHOT"
    attribute_ids:
      - "EVENTO_SCOUT_ID"
    physical_object_ids:
      - "TABLE_SPIN_SHOT"
      - "CONSTRAINT_UQ_SPIN_SHOT_EVENTO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_084"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_UQ_IN_FLIGHT_EVENTO"
    evidence_ref_ids: []
    concept_ids:
      - "IN_FLIGHT_SHOT"
    rule_ids: []
    conceptual_entity_ids:
      - "IN_FLIGHT_SHOT"
    relationship_ids: []
    logical_relation_ids:
      - "IN_FLIGHT_SHOT"
    attribute_ids:
      - "EVENTO_SCOUT_ID"
    physical_object_ids:
      - "TABLE_IN_FLIGHT_SHOT"
      - "CONSTRAINT_UQ_IN_FLIGHT_EVENTO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_085"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_UQ_DESQ_EXC_EVENTO"
    evidence_ref_ids: []
    concept_ids:
      - "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
    rule_ids: []
    conceptual_entity_ids:
      - "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
    relationship_ids: []
    logical_relation_ids:
      - "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
    attribute_ids:
      - "EVENTO_SCOUT_ID"
    physical_object_ids:
      - "TABLE_DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
      - "CONSTRAINT_UQ_DESQ_EXC_EVENTO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_086"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_UQ_CARTAO_AZUL_EVENTO"
    evidence_ref_ids: []
    concept_ids:
      - "CARTAO_AZUL_SUSPENSAO"
    rule_ids: []
    conceptual_entity_ids:
      - "CARTAO_AZUL_SUSPENSAO"
    relationship_ids: []
    logical_relation_ids:
      - "CARTAO_AZUL_SUSPENSAO"
    attribute_ids:
      - "EVENTO_SCOUT_ID"
    physical_object_ids:
      - "TABLE_CARTAO_AZUL_SUSPENSAO"
      - "CONSTRAINT_UQ_CARTAO_AZUL_EVENTO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_087"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_UQ_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA"
    evidence_ref_ids: []
    concept_ids:
      - "EQUIPE"
      - "COMPETICAO"
    rule_ids: []
    conceptual_entity_ids:
      - "EQUIPE"
      - "COMPETICAO"
    relationship_ids: []
    logical_relation_ids:
      - "PARTICIPACAO_EQUIPE_COMPETICAO"
    attribute_ids:
      - "COMPETICAO_ID"
      - "EQUIPE_ID"
      - "VALIDO_DESDE"
    physical_object_ids:
      - "TABLE_PARTICIPACAO_EQUIPE_COMPETICAO"
      - "CONSTRAINT_UQ_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_088"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_CHK_ELEGIBILIDADE_RANKING_CONTEXTUAL"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_027"
      - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_006"
    concept_ids:
      - "EQUIPE"
      - "COMPETICAO"
    rule_ids:
      - "RN_SGATE_0023_PONTUACAO_FHERJ_2026"
    conceptual_entity_ids:
      - "EQUIPE"
      - "COMPETICAO"
    relationship_ids: []
    logical_relation_ids:
      - "PARTICIPACAO_EQUIPE_COMPETICAO"
    attribute_ids: []
    physical_object_ids:
      - "TABLE_PARTICIPACAO_EQUIPE_COMPETICAO"
      - "CONSTRAINT_CHK_ELEGIBILIDADE_RANKING_CONTEXTUAL"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_089"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_CHK_INTERVALO_VIGENCIA_PARTICIPACAO"
    evidence_ref_ids: []
    concept_ids:
      - "EQUIPE"
      - "COMPETICAO"
    rule_ids: []
    conceptual_entity_ids:
      - "EQUIPE"
      - "COMPETICAO"
    relationship_ids:
      - "EQUIPE_PARTICIPA_COMPETICAO"
    logical_relation_ids:
      - "PARTICIPACAO_EQUIPE_COMPETICAO"
    attribute_ids:
      - "VALIDO_DESDE"
      - "VALIDO_ATE"
    physical_object_ids:
      - "TABLE_PARTICIPACAO_EQUIPE_COMPETICAO"
      - "CONSTRAINT_CHK_INTERVALO_VIGENCIA_PARTICIPACAO"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_090"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
  - id: "TRACE_EXCL_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA"
    evidence_ref_ids: []
    concept_ids:
      - "EQUIPE"
      - "COMPETICAO"
    rule_ids: []
    conceptual_entity_ids:
      - "EQUIPE"
      - "COMPETICAO"
    relationship_ids:
      - "EQUIPE_PARTICIPA_COMPETICAO"
    logical_relation_ids:
      - "PARTICIPACAO_EQUIPE_COMPETICAO"
    attribute_ids:
      - "COMPETICAO_ID"
      - "EQUIPE_ID"
      - "VALIDO_DESDE"
      - "VALIDO_ATE"
    physical_object_ids:
      - "TABLE_PARTICIPACAO_EQUIPE_COMPETICAO"
      - "CONSTRAINT_EXCL_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA"
    permission_requirement_ids: []
    test_ids:
      - "TEST_PARTIDAS_SCOUT_083"
    implementation_status: "CANDIDATO"
    verification_status: "NAO_EXECUTADO"
    verification_evidence_ids: []
coverage_summary:
  source_rules_total: 11
  rules_with_logical_mapping: 11
  rules_with_physical_mapping: 11
  material_constraints_total: 101
  material_constraints_with_tests: 101
  unresolved_trace_ids: []
orphan_checks:
  sources_without_use:
    - "SRC_CTRL_FLUXO_MODELAGEM_ACF6AFA2AAB0_C17B2843"
    - "SRC_CTRL_INSTRUCOES_NOTEBOOK_A6EDE74B1BAA_63B2FA9E"
    - "SRC_CTRL_CONTRATO_ARTEFATOS_DB2D64DA9680_5CDE0B19"
    - "SRC_00_MANIFESTO_FONTES_TEMPLATE_8F26F1D8"
    - "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    - "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    - "SRC_REGULAMENTO_CBHB_2026_PDF_818BCC8B"
    - "SRC_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5"
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
    - "PAPEL_ESPORTIVO_OPERACIONAL"
  attributes_without_definition: []
  physical_objects_without_logical_origin: []
  tests_without_rule:
    - "TEST_PARTIDAS_SCOUT_001"
    - "TEST_PARTIDAS_SCOUT_002"
    - "TEST_PARTIDAS_SCOUT_003"
    - "TEST_PARTIDAS_SCOUT_004"
    - "TEST_PARTIDAS_SCOUT_005"
    - "TEST_PARTIDAS_SCOUT_006"
    - "TEST_PARTIDAS_SCOUT_007"
    - "TEST_PARTIDAS_SCOUT_008"
    - "TEST_PARTIDAS_SCOUT_009"
    - "TEST_PARTIDAS_SCOUT_010"
    - "TEST_PARTIDAS_SCOUT_011"
    - "TEST_PARTIDAS_SCOUT_012"
    - "TEST_PARTIDAS_SCOUT_013"
    - "TEST_PARTIDAS_SCOUT_014"
    - "TEST_PARTIDAS_SCOUT_015"
    - "TEST_PARTIDAS_SCOUT_016"
    - "TEST_PARTIDAS_SCOUT_017"
    - "TEST_PARTIDAS_SCOUT_018"
    - "TEST_PARTIDAS_SCOUT_019"
    - "TEST_PARTIDAS_SCOUT_020"
    - "TEST_PARTIDAS_SCOUT_021"
    - "TEST_PARTIDAS_SCOUT_022"
    - "TEST_PARTIDAS_SCOUT_023"
    - "TEST_PARTIDAS_SCOUT_024"
    - "TEST_PARTIDAS_SCOUT_025"
    - "TEST_PARTIDAS_SCOUT_026"
    - "TEST_PARTIDAS_SCOUT_027"
    - "TEST_PARTIDAS_SCOUT_028"
    - "TEST_PARTIDAS_SCOUT_029"
    - "TEST_PARTIDAS_SCOUT_030"
    - "TEST_PARTIDAS_SCOUT_031"
    - "TEST_PARTIDAS_SCOUT_032"
    - "TEST_PARTIDAS_SCOUT_033"
    - "TEST_PARTIDAS_SCOUT_034"
    - "TEST_PARTIDAS_SCOUT_035"
    - "TEST_PARTIDAS_SCOUT_036"
    - "TEST_PARTIDAS_SCOUT_037"
    - "TEST_PARTIDAS_SCOUT_038"
    - "TEST_PARTIDAS_SCOUT_039"
    - "TEST_PARTIDAS_SCOUT_040"
    - "TEST_PARTIDAS_SCOUT_041"
    - "TEST_PARTIDAS_SCOUT_042"
    - "TEST_PARTIDAS_SCOUT_043"
    - "TEST_PARTIDAS_SCOUT_044"
    - "TEST_PARTIDAS_SCOUT_045"
    - "TEST_PARTIDAS_SCOUT_046"
    - "TEST_PARTIDAS_SCOUT_047"
    - "TEST_PARTIDAS_SCOUT_048"
    - "TEST_PARTIDAS_SCOUT_049"
    - "TEST_PARTIDAS_SCOUT_050"
    - "TEST_PARTIDAS_SCOUT_051"
    - "TEST_PARTIDAS_SCOUT_052"
    - "TEST_PARTIDAS_SCOUT_053"
    - "TEST_PARTIDAS_SCOUT_054"
    - "TEST_PARTIDAS_SCOUT_055"
    - "TEST_PARTIDAS_SCOUT_056"
    - "TEST_PARTIDAS_SCOUT_057"
    - "TEST_PARTIDAS_SCOUT_058"
    - "TEST_PARTIDAS_SCOUT_059"
    - "TEST_PARTIDAS_SCOUT_062"
    - "TEST_PARTIDAS_SCOUT_063"
    - "TEST_PARTIDAS_SCOUT_065"
    - "TEST_PARTIDAS_SCOUT_067"
    - "TEST_PARTIDAS_SCOUT_069"
    - "TEST_PARTIDAS_SCOUT_070"
    - "TEST_PARTIDAS_SCOUT_071"
    - "TEST_PARTIDAS_SCOUT_073"
    - "TEST_PARTIDAS_SCOUT_078"
    - "TEST_PARTIDAS_SCOUT_079"
    - "TEST_PARTIDAS_SCOUT_080"
    - "TEST_PARTIDAS_SCOUT_081"
    - "TEST_PARTIDAS_SCOUT_082"
    - "TEST_PARTIDAS_SCOUT_083"
    - "TEST_PARTIDAS_SCOUT_084"
    - "TEST_PARTIDAS_SCOUT_085"
    - "TEST_PARTIDAS_SCOUT_086"
    - "TEST_PARTIDAS_SCOUT_087"
    - "TEST_PARTIDAS_SCOUT_088"
    - "TEST_PARTIDAS_SCOUT_090"
open_issues:
  - id: "ISSUE_LACUNA_PLACAR_SHOOTOUT_E_ETAPAS"
    status: "ABERTA"
    question: "Como completar a lacuna de documentação de placar detalhado de shoot-out em jogos específicos da Etapa Final\
      \ (ex.: J71) e parciais de sets da 4ª Etapa Estadual?"
    affected_ids:
      - "PLACAR_JOGO"
      - "EVOLUCAO_DO_PLACAR"
      - "PARTIDA"
      - "SHOOT_OUT"
    impact: "Incompletude no histórico cronológico e auditável do placar em partidas passadas específicas sem registro de\
      \ vídeo em arquivo."
    required_evidence: "Súmula física impressa assinada ou boletim impresso oficial expedido pela FHERJ/CBHb."
    owner: "OPERADOR"
  - id: "ISSUE_REQUISITOS_ACESSO_STAGE_06"
    status: "ABERTA"
    question: "Quais IDs de requisitos de permissão serão aprovados para as relações não públicas?"
    affected_ids:
      - "ATLETA"
      - "EQUIPE_ATLETA_INSCRICAO"
      - "POSSE_DE_BOLA"
      - "UNIDADE_BASICA_ATAQUE_BOU"
      - "EVENTO_SCOUT"
      - "OBSERVACAO_DE_SCOUT"
      - "ANALISTA_OBSERVADOR"
      - "PROTOCOLO_SCOUT"
      - "MIDIA_VIDEO"
      - "SEGMENTO_OBSERVADO"
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
      - "PAPEL_ESPORTIVO_OPERACIONAL"
      - "PARTICIPACAO_EQUIPE_COMPETICAO"
    impact: "permission_requirement_ids permanece vazio até a geração e aprovação do estágio 06."
    required_evidence: "Artefato ACCESS_REQUIREMENTS promovido no estágio 06."
    owner: "OPERADOR"
```

## Arquivo: `notebooklm-modelagem/runs/RUN_20261014_PARTIDAS_SCOUT_001/artifacts/05-matriz-rastreabilidade.operator-review.yaml`

```yaml
schema_version: "1.0"
review_id: "STAGE_05_OPERATOR_REVIEW_001"
run_id: "RUN_20261014_PARTIDAS_SCOUT_001"
stage_id: "STAGE_05"
status: "APROVADO"
reviewed_at: "2026-10-15T12:22:06-03:00"
base_candidate:
  path: "notebooklm-modelagem/runs/RUN_20261014_PARTIDAS_SCOUT_001/artifacts/05-matriz-rastreabilidade.candidate.yaml"
  sha256: "875e9f4d03ba39ca476460761435c45aff9d7b86a9cf26352d6c3137b519cbec"
decision_authority:
  actor: "USUARIO"
  authorization: "Registrar 68 derivações, formalizar 9 condicionais, reconciliar 2 divergentes, aprovar e promover o estágio\
    \ 05."
summary:
  reviewed_total: 79
  accepted_structural_derivations: 68
  formalized_conditionals: 9
  reconciled_divergences: 2
accepted_structural_derivations:
  basis: "Cardinalidade, identidade e integridade referencial coerentes com o modelo lógico promovido; FKs também possuem\
    \ tipos compatíveis e índice candidato."
  foreign_key_ids:
    - "FK_BOU_POSSE_DE_BOLA"
    - "FK_CARTAO_AZUL_ATLETA"
    - "FK_CARTAO_AZUL_EVENTO"
    - "FK_CARTAO_AZUL_PAPEL_OPERACIONAL"
    - "FK_CARTAO_AZUL_PARTIDA"
    - "FK_CONFIABILIDADE_ANALISTA"
    - "FK_DESQUALIFICACAO_ATLETA"
    - "FK_DESQUALIFICACAO_EVENTO"
    - "FK_DESQUALIFICACAO_PARTIDA"
    - "FK_ESTADO_PLACAR_PERIODO_SET"
    - "FK_ESTADO_PLACAR_PLACAR_JOGO"
    - "FK_ESTADO_REVISAO_OBSERVACAO"
    - "FK_ESTADO_REVISAO_REVISAO"
    - "FK_EVENTO_SCOUT_ATLETA_ALVO"
    - "FK_EVENTO_SCOUT_ATLETA_EXEC"
    - "FK_EVENTO_SCOUT_BOU"
    - "FK_EVENTO_SCOUT_OBSERVACAO"
    - "FK_EVOLUCAO_PLACAR_PARTIDA"
    - "FK_INSCRICAO_ATLETA"
    - "FK_INSCRICAO_COMPETICAO"
    - "FK_INSCRICAO_EQUIPE"
    - "FK_IN_FLIGHT_SHOT_EVENTO"
    - "FK_OBSERVACAO_SCOUT_ANALISTA"
    - "FK_OBSERVACAO_SCOUT_MIDIA"
    - "FK_OBSERVACAO_SCOUT_PARTIDA"
    - "FK_OBSERVACAO_SCOUT_PROTOCOLO"
    - "FK_PAPEL_OPERACIONAL_EQUIPE"
    - "FK_PAPEL_OPERACIONAL_PARTIDA"
    - "FK_PARTICIPACAO_EQUIPE_COMPETICAO_COMPETICAO"
    - "FK_PARTICIPACAO_EQUIPE_COMPETICAO_EQUIPE"
    - "FK_PARTIDA_COMPETICAO"
    - "FK_PARTIDA_EQUIPE_EQUIPE"
    - "FK_PARTIDA_EQUIPE_PARTIDA"
    - "FK_PERIODO_SET_PARTIDA"
    - "FK_PLACAR_JOGO_PARTIDA"
    - "FK_POSSE_DE_BOLA_PERIODO_SET"
    - "FK_PROVENIENCIA_MIDIA"
    - "FK_PROVENIENCIA_OBSERVACAO_OBS"
    - "FK_PROVENIENCIA_PROTOCOLO"
    - "FK_REVISAO_OBSERVACAO_ANALISTA"
    - "FK_REVISAO_OBSERVACAO_OBS"
    - "FK_SEGMENTO_OBSERVADO_MIDIA"
    - "FK_SEGMENTO_OBSERVADO_PARTIDA"
    - "FK_SHOOT_OUT_PARTIDA"
    - "FK_SISTEMA_DEFENSIVO_EQUIPE"
    - "FK_SISTEMA_DEFENSIVO_POSSE"
    - "FK_SISTEMA_DEFENSIVO_SISTEMA_TATICO"
    - "FK_SISTEMA_TATICO_EQUIPE"
    - "FK_SISTEMA_TATICO_POSSE"
    - "FK_SPIN_SHOT_EVENTO"
    - "FK_TRECHO_OBSERVADO_EVENTO"
    - "FK_TRECHO_OBSERVADO_MIDIA"
  unique_constraint_ids:
    - "UQ_BOU_POSSE_SEQ"
    - "UQ_CARTAO_AZUL_EVENTO"
    - "UQ_DESQ_EXC_EVENTO"
    - "UQ_EQUIPE_ATLETA_COMPETICAO"
    - "UQ_ESTADO_REVISAO_OBSERVA"
    - "UQ_EVOLUCAO_PARTIDA_SEQ"
    - "UQ_IN_FLIGHT_EVENTO"
    - "UQ_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA"
    - "UQ_PARTIDA_NUMERO_SET"
    - "UQ_PLACAR_PARTIDA"
    - "UQ_POSSE_PERIODO_SEQ"
    - "UQ_PROVENIENCIA_OBS"
    - "UQ_SEGMENTO_ORDEM"
    - "UQ_SHOOT_OUT_PARTIDA"
    - "UQ_SPIN_SHOT_EVENTO"
  check_constraint_ids:
    - "CHK_SHOOT_OUT_COMPLETUDE"
formalized_conditionals:
  - trace_id: "TRACE_FK_PERIODO_SET_EQUIPE_VENCEDORA"
    constraint_id: "FK_PERIODO_SET_EQUIPE_VENCEDORA"
    formalization_id: "REFINEMENT_PERIODO_SET_EQUIPE_VENCEDORA"
    statement: "Cada período/set pode referenciar a equipe vencedora participante da mesma partida."
    status: "FORMALIZADA"
    upstream_backport_required: true
  - trace_id: "TRACE_FK_SHOOT_OUT_EQUIPE_VENCEDORA"
    constraint_id: "FK_SHOOT_OUT_EQUIPE_VENCEDORA"
    formalization_id: "REFINEMENT_SHOOT_OUT_EQUIPE_VENCEDORA"
    statement: "Cada shoot-out concluído pode referenciar a equipe vencedora participante da mesma partida."
    status: "FORMALIZADA"
    upstream_backport_required: true
  - trace_id: "TRACE_FK_POSSE_DE_BOLA_EQUIPE"
    constraint_id: "FK_POSSE_DE_BOLA_EQUIPE"
    formalization_id: "REFINEMENT_POSSE_DE_BOLA_EQUIPE_POSSUIDORA"
    statement: "Cada posse pertence à equipe que detém a bola no contexto da partida do período/set."
    status: "FORMALIZADA"
    upstream_backport_required: true
  - trace_id: "TRACE_FK_MIDIA_VIDEO_PARTIDA"
    constraint_id: "FK_MIDIA_VIDEO_PARTIDA"
    formalization_id: "REFINEMENT_MIDIA_VIDEO_PARTIDA"
    statement: "Cada mídia de vídeo pode ser vinculada à partida que registra."
    status: "FORMALIZADA"
    upstream_backport_required: true
  - trace_id: "TRACE_FK_PLACAR_JOGO_EQUIPE_VENCEDORA"
    constraint_id: "FK_PLACAR_JOGO_EQUIPE_VENCEDORA"
    formalization_id: "REFINEMENT_PLACAR_JOGO_EQUIPE_VENCEDORA"
    statement: "O placar consolidado pode referenciar a equipe vencedora participante da partida."
    status: "FORMALIZADA"
    upstream_backport_required: true
  - trace_id: "TRACE_FK_EVOLUCAO_PLACAR_EVENTO_SCOUT"
    constraint_id: "FK_EVOLUCAO_PLACAR_EVENTO_SCOUT"
    formalization_id: "REFINEMENT_EVOLUCAO_PLACAR_EVENTO_SCOUT"
    statement: "Uma alteração do placar pode ser vinculada ao evento de scout que a originou."
    status: "FORMALIZADA"
    upstream_backport_required: true
  - trace_id: "TRACE_FK_EVOLUCAO_PLACAR_EQUIPE"
    constraint_id: "FK_EVOLUCAO_PLACAR_EQUIPE"
    formalization_id: "REFINEMENT_EVOLUCAO_PLACAR_EQUIPE_BENEFICIADA"
    statement: "Uma alteração do placar identifica a equipe beneficiada no contexto da partida."
    status: "FORMALIZADA"
    upstream_backport_required: true
  - trace_id: "TRACE_UQ_PARTIDA_PAPEL_REGULAMENTAR"
    constraint_id: "UQ_PARTIDA_PAPEL_REGULAMENTAR"
    formalization_id: "INV_PARTIDA_EQUIPE_PAPEL_REGULAMENTAR_UNICO"
    statement: "Em uma partida, cada papel regulamentar de equipe ocorre no máximo uma vez."
    status: "FORMALIZADA"
    upstream_backport_required: true
  - trace_id: "TRACE_UQ_PARTIDA_CONDICAO_MANDO"
    constraint_id: "UQ_PARTIDA_CONDICAO_MANDO"
    formalization_id: "INV_PARTIDA_EQUIPE_CONDICAO_MANDO_UNICA"
    statement: "Em uma partida, cada condição de mando ocorre no máximo uma vez."
    status: "FORMALIZADA"
    upstream_backport_required: true
reconciled_divergences:
  - trace_id: "TRACE_UQ_TRECHO_EVENTO"
    decision: "REMOVER_RESTRICAO_UNIQUE"
    reason: "A cardinalidade conceitual aprovada permite zero a muitos trechos por evento de scout."
    result: "Preservada a relação EVENTO_SCOUT para TRECHO_OBSERVADO em 1:N; o teste liberado foi realocado à exclusão temporal."
    replacement_trace_ids:
      - "TRACE_EXCL_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA"
  - trace_id: "TRACE_CHK_VIGENCIA_PARTICIPACAO"
    decision: "SEPARAR_VALIDACAO_DE_LINHA_E_NAO_SOBREPOSICAO"
    reason: "CHECK valida a ordem das datas na linha, mas não impede sobreposição entre linhas no PostgreSQL."
    result: "Criados um CHECK de intervalo válido e uma exclusão temporal candidata para a mesma equipe e competição."
    replacement_trace_ids:
      - "TRACE_CHK_INTERVALO_VIGENCIA_PARTICIPACAO"
      - "TRACE_EXCL_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA"
diagnostic_preserved:
  tests_without_semantic_rule_count: 79
  reason: "A revisão do operador resolve a decisão, mas não inventa rule_ids nos artefatos semânticos já promovidos."
downstream_requirements:
  - requirement: "Retropropagar as 9 formalizações e as 2 reconciliações nos modelos conceitual e lógico."
    deadline: "ANTES_DO_STOP_GATE_FISICO"
    status: "OBRIGATORIO"
  - requirement: "Implementar a não sobreposição com EXCLUDE USING gist e intervalo daterange, validando a extensão btree_gist."
    deadline: "ESTAGIO_FISICO_POSTGRESQL"
    status: "PLANEJADO"
```
