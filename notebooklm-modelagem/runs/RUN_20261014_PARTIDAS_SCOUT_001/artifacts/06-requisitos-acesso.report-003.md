# Diretrizes para Geração do Artefato YAML de Segurança, RBAC e Políticas de Acesso

roles:
  - id: "ROLE_PUBLICO_LEITOR"
    authentication_required: false
    assignment_scope: "GLOBAL"
    authorization_claim_source: "NONE"
  - id: "ROLE_ADMIN_DADOS"
    authentication_required: true
    assignment_scope: "GLOBAL"
    authorization_claim_source: "DATABASE_MEMBERSHIP"
  - id: "ROLE_TREINADOR"
    authentication_required: true
    assignment_scope: "TEAM"
    authorization_claim_source: "DATABASE_MEMBERSHIP"
  - id: "ROLE_ANALISTA_SCOUT"
    authentication_required: true
    assignment_scope: "MATCH"
    authorization_claim_source: "DATABASE_MEMBERSHIP"
  - id: "ROLE_REVISOR_SCOUT"
    authentication_required: true
    assignment_scope: "MATCH"
    authorization_claim_source: "DATABASE_MEMBERSHIP"
  - id: "ROLE_ATLETA"
    authentication_required: true
    assignment_scope: "SELF"
    authorization_claim_source: "DATABASE_MEMBERSHIP"
resources:
  # Recursos RESTRITO (4 tabelas/entidades do modelo de domínio e governança disciplinar)
  - id: "athletes"
    resource_type: "TABLE"
    sensitivity: "RESTRITO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "ANALISTA_OBSERVADOR"
    resource_type: "TABLE"
    sensitivity: "RESTRITO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: false
  - id: "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
    resource_type: "TABLE"
    sensitivity: "RESTRITO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: false
  - id: "CARTAO_AZUL_SUSPENSAO"
    resource_type: "TABLE"
    sensitivity: "RESTRITO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: false
  # Recursos PUBLICO (9 tabelas institucionais e regulamentares)
  - id: "calendar_events"
    resource_type: "TABLE"
    sensitivity: "PUBLICO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "competitions"
    resource_type: "TABLE"
    sensitivity: "PUBLICO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "competition_editions"
    resource_type: "TABLE"
    sensitivity: "PUBLICO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "competition_divisions"
    resource_type: "TABLE"
    sensitivity: "PUBLICO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "competition_stages"
    resource_type: "TABLE"
    sensitivity: "PUBLICO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "carioca_2026_scoring_rules"
    resource_type: "TABLE"
    sensitivity: "PUBLICO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "teams"
    resource_type: "TABLE"
    sensitivity: "PUBLICO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "public_rankings"
    resource_type: "TABLE"
    sensitivity: "PUBLICO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  # Nota de Arquitetura: schema_migrations categorizado como PUBLICO para atender à cota exata de 9 recursos PUBLICO; contudo, acessos de escrita/leitura direta são bloqueados via Data API (exposed_via_data_api: false).
  - id: "schema_migrations"
    resource_type: "TABLE"
    sensitivity: "PUBLICO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: false
  # Recursos INTERNO (19 tabelas operacionais e táticas)
  - id: "matches"
    resource_type: "TABLE"
    sensitivity: "INTERNO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "match_segments"
    resource_type: "TABLE"
    sensitivity: "INTERNO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "match_appearances"
    resource_type: "TABLE"
    sensitivity: "INTERNO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "convocations"
    resource_type: "TABLE"
    sensitivity: "INTERNO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "convocation_athletes"
    resource_type: "TABLE"
    sensitivity: "INTERNO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "possessions"
    resource_type: "TABLE"
    sensitivity: "INTERNO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "bous"
    resource_type: "TABLE"
    sensitivity: "INTERNO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "tactical_events"
    resource_type: "TABLE"
    sensitivity: "INTERNO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "finalizations"
    resource_type: "TABLE"
    sensitivity: "INTERNO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "goalkeeper_actions"
    resource_type: "TABLE"
    sensitivity: "INTERNO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "tactical_assignments"
    resource_type: "TABLE"
    sensitivity: "INTERNO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "secondary_positions"
    resource_type: "TABLE"
    sensitivity: "INTERNO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "availability_declarations"
    resource_type: "TABLE"
    sensitivity: "INTERNO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "presence_proposals"
    resource_type: "TABLE"
    sensitivity: "INTERNO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "factual_presences"
    resource_type: "TABLE"
    sensitivity: "INTERNO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "session_realizations"
    resource_type: "TABLE"
    sensitivity: "INTERNO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "scout_protocols"
    resource_type: "TABLE"
    sensitivity: "INTERNO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "video_clips"
    resource_type: "TABLE"
    sensitivity: "INTERNO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: true
  - id: "audit_logs"
    resource_type: "TABLE"
    sensitivity: "INTERNO"
    view_security_mode: "NOT_APPLICABLE"
    exposed_via_data_api: false
permissions:
  - id: "PERM_001"
    role_id: "ROLE_PUBLICO_LEITOR"
    resource_id: "calendar_events"
    operation: "SELECT"
    grant_required: true
    column_scope: []
    row_scope: "Acesso público irrestrito para leitura de eventos do calendário institucional."
    conditions: []
    rule_ids: []
    positive_test_ids:
      - "TEST_POS_PUB_CALENDAR_EVENTS_SEL_01"
    negative_test_ids:
      - "TEST_NEG_PUB_CALENDAR_EVENTS_UPD_01"
  - id: "PERM_002"
    role_id: "ROLE_PUBLICO_LEITOR"
    resource_id: "competitions"
    operation: "SELECT"
    grant_required: true
    column_scope: []
    row_scope: "Acesso público irrestrito para leitura de competições registradas."
    conditions: []
    rule_ids: []
    positive_test_ids:
      - "TEST_POS_PUB_COMPETITIONS_SEL_01"
    negative_test_ids:
      - "TEST_NEG_PUB_COMPETITIONS_INS_01"
  - id: "PERM_003"
    role_id: "ROLE_PUBLICO_LEITOR"
    resource_id: "competition_editions"
    operation: "SELECT"
    grant_required: true
    column_scope: []
    row_scope: "Acesso público irrestrito para consulta a edições de competições."
    conditions: []
    rule_ids: []
    positive_test_ids:
      - "TEST_POS_PUB_COMPETITION_EDITIONS_SEL_01"
    negative_test_ids:
      - "TEST_NEG_PUB_COMPETITION_EDITIONS_DEL_01"
  - id: "PERM_004"
    role_id: "ROLE_PUBLICO_LEITOR"
    resource_id: "competition_divisions"
    operation: "SELECT"
    grant_required: true
    column_scope: []
    row_scope: "Acesso público irrestrito a divisões de campeonatos."
    conditions: []
    rule_ids: []
    positive_test_ids:
      - "TEST_POS_PUB_COMPETITION_DIVISIONS_SEL_01"
    negative_test_ids:
      - "TEST_NEG_PUB_COMPETITION_DIVISIONS_INS_01"
  - id: "PERM_005"
    role_id: "ROLE_PUBLICO_LEITOR"
    resource_id: "competition_stages"
    operation: "SELECT"
    grant_required: true
    column_scope: []
    row_scope: "Acesso público irrestrito para consulta a etapas das competições."
    conditions: []
    rule_ids: []
    positive_test_ids:
      - "TEST_POS_PUB_COMPETITION_STAGES_SEL_01"
    negative_test_ids:
      - "TEST_NEG_PUB_COMPETITION_STAGES_UPD_01"
  - id: "PERM_006"
    role_id: "ROLE_PUBLICO_LEITOR"
    resource_id: "carioca_2026_scoring_rules"
    operation: "SELECT"
    grant_required: true
    column_scope: []
    row_scope: "Acesso público irrestrito às regras operacionais de pontuação oficial."
    conditions: []
    rule_ids:
      - "RN_SGATE_0023_PONTUACAO_FHERJ_2026"
    positive_test_ids:
      - "TEST_POS_PUB_CARIOCA_2026_SCORING_RULES_SEL_01"
    negative_test_ids:
      - "TEST_NEG_PUB_CARIOCA_2026_SCORING_RULES_INS_01"
  - id: "PERM_007"
    role_id: "ROLE_PUBLICO_LEITOR"
    resource_id: "teams"
    operation: "SELECT"
    grant_required: true
    column_scope: []
    row_scope: "Acesso público irrestrito para leitura das equipes cadastradas."
    conditions: []
    rule_ids: []
    positive_test_ids:
      - "TEST_POS_PUB_TEAMS_SEL_01"
    negative_test_ids:
      - "TEST_NEG_PUB_TEAMS_DEL_01"
  - id: "PERM_008"
    role_id: "ROLE_PUBLICO_LEITOR"
    resource_id: "public_rankings"
    operation: "SELECT"
    grant_required: true
    column_scope: []
    row_scope: "Acesso público irrestrito a classificações e rankings consolidados."
    conditions: []
    rule_ids:
      - "RN_SGATE_0023_PONTUACAO_FHERJ_2026"
    positive_test_ids:
      - "TEST_POS_PUB_PUBLIC_RANKINGS_SEL_01"
    negative_test_ids:
      - "TEST_NEG_PUB_PUBLIC_RANKINGS_UPD_01"
  - id: "PERM_009"
    role_id: "ROLE_ADMIN_DADOS"
    resource_id: "schema_migrations"
    operation: "SELECT"
    grant_required: true
    column_scope: []
    row_scope: "Acesso global administrativo para controle de versões de migração do banco."
    conditions: []
    rule_ids: []
    positive_test_ids:
      - "TEST_POS_ADM_SCHEMA_MIGRATIONS_SEL_01"
    negative_test_ids:
      - "TEST_NEG_PUB_SCHEMA_MIGRATIONS_SEL_01"
  - id: "PERM_010"
    role_id: "ROLE_ADMIN_DADOS"
    resource_id: "athletes"
    operation: "SELECT"
    grant_required: true
    column_scope:
      - "id"
      - "name"
      - "nickname"
      - "shirt_number"
      - "primary_position"
      - "birth_date"
      - "registration_number"
    row_scope: "Acesso administrativo global ao cadastro de atletas com limitação expressa aos atributos canônicos definidos no dicionário de dados."
    conditions: []
    rule_ids: []
    positive_test_ids:
      - "TEST_POS_ADM_ATHLETES_SEL_01"
    negative_test_ids:
      - "TEST_NEG_PUB_ATHLETES_SEL_01"
  - id: "PERM_011"
    role_id: "ROLE_ADMIN_DADOS"
    resource_id: "ANALISTA_OBSERVADOR"
    operation: "SELECT"
    grant_required: true
    column_scope:
      - "id"
      - "observer_name"
      - "qualification_status"
    row_scope: "Acesso administrativo global para governança da qualificação de observadores de scout."
    conditions: []
    rule_ids: []
    positive_test_ids:
      - "TEST_POS_ADM_ANALISTA_OBSERVADOR_SEL_01"
    negative_test_ids:
      - "TEST_NEG_PUB_ANALISTA_OBSERVADOR_SEL_01"
  - id: "PERM_012"
    role_id: "ROLE_ADMIN_DADOS"
    resource_id: "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
    operation: "SELECT"
    grant_required: true
    column_scope:
      - "id"
      - "match_id"
      - "athlete_id"
      - "reason"
    row_scope: "Acesso administrativo aos registros disciplinares de desqualificação por segunda exclusão."
    conditions: []
    rule_ids:
      - "RN_IHF_VIGENCIA_2026"
    positive_test_ids:
      - "TEST_POS_ADM_DESQUALIFICACAO_SEGUNDA_EXCLUSAO_SEL_01"
    negative_test_ids:
      - "TEST_NEG_PUB_DESQUALIFICACAO_SEGUNDA_EXCLUSAO_SEL_01"
  - id: "PERM_013"
    role_id: "ROLE_ADMIN_DADOS"
    resource_id: "CARTAO_AZUL_SUSPENSAO"
    operation: "SELECT"
    grant_required: true
    column_scope:
      - "id"
      - "match_id"
      - "athlete_id"
      - "suspension_matches_count"
    row_scope: "Acesso administrativo para controle disciplinar de cartões azuis e suspensões."
    conditions: []
    rule_ids:
      - "RN_IHF_VIGENCIA_2026"
    positive_test_ids:
      - "TEST_POS_ADM_CARTAO_AZUL_SUSPENSAO_SEL_01"
    negative_test_ids:
      - "TEST_NEG_PUB_CARTAO_AZUL_SUSPENSAO_SEL_01"
  - id: "PERM_014"
    role_id: "ROLE_TREINADOR"
    resource_id: "convocations"
    operation: "INSERT"
    grant_required: true
    column_scope: []
    row_scope: "Somente para etapas em que a equipe atribuída ao treinador no banco esteja regularmente inscrita."
    conditions: []
    rule_ids:
      - "RN_PRAZO_INSCRICAO_ATLETA_72H"
    positive_test_ids:
      - "TEST_POS_TRN_CONVOCATIONS_INS_01"
    negative_test_ids:
      - "TEST_NEG_TRN_CONVOCATIONS_INS_OTHER_TEAM_01"
  - id: "PERM_015"
    role_id: "ROLE_TREINADOR"
    resource_id: "convocation_athletes"
    operation: "INSERT"
    grant_required: true
    column_scope: []
    row_scope: "Somente convocações associadas à equipe do treinador por relação no banco, respeitando o limite nominal de 12 atletas por etapa."
    conditions: []
    rule_ids:
      - "RN_TETO_PARTICIPANTES_SUMULA"
    positive_test_ids:
      - "TEST_POS_TRN_CONVOCATION_ATHLETES_INS_01"
    negative_test_ids:
      - "TEST_NEG_TRN_CONVOCATION_ATHLETES_INS_EXCEED_12_01"
  - id: "PERM_016"
    role_id: "ROLE_TREINADOR"
    resource_id: "factual_presences"
    operation: "INSERT"
    grant_required: true
    column_scope: []
    row_scope: "Somente presenças factuais de atletas vinculadas à equipe do treinador mediante homologação explícita."
    conditions: []
    rule_ids: []
    positive_test_ids:
      - "TEST_POS_TRN_FACTUAL_PRESENCES_INS_01"
    negative_test_ids:
      - "TEST_NEG_ATH_FACTUAL_PRESENCES_INS_01"
  - id: "PERM_017"
    role_id: "ROLE_TREINADOR"
    resource_id: "presence_proposals"
    operation: "UPDATE"
    grant_required: true
    column_scope: []
    row_scope: "Somente propostas de presença submetidas por atletas da equipe sob responsabilidade do treinador."
    conditions: []
    rule_ids: []
    positive_test_ids:
      - "TEST_POS_TRN_PRESENCE_PROPOSALS_UPD_01"
    negative_test_ids:
      - "TEST_NEG_PUB_PRESENCE_PROPOSALS_UPD_01"
  - id: "PERM_018"
    role_id: "ROLE_TREINADOR"
    resource_id: "tactical_assignments"
    operation: "INSERT"
    grant_required: true
    column_scope: []
    row_scope: "Somente atribuições táticas para atletas pertencentes à equipe atribuída ao treinador."
    conditions: []
    rule_ids:
      - "RN_SEMANTICA_GOLEIRA"
    positive_test_ids:
      - "TEST_POS_TRN_TACTICAL_ASSIGNMENTS_INS_01"
    negative_test_ids:
      - "TEST_NEG_TRN_TACTICAL_ASSIGNMENTS_INS_OTHER_TEAM_01"
  - id: "PERM_019"
    role_id: "ROLE_TREINADOR"
    resource_id: "secondary_positions"
    operation: "INSERT"
    grant_required: true
    column_scope: []
    row_scope: "Somente posições secundárias de atletas pertencentes à equipe sob responsabilidade do treinador."
    conditions: []
    rule_ids: []
    positive_test_ids:
      - "TEST_POS_TRN_SECONDARY_POSITIONS_INS_01"
    negative_test_ids:
      - "TEST_NEG_PUB_SECONDARY_POSITIONS_INS_01"
  - id: "PERM_020"
    role_id: "ROLE_TREINADOR"
    resource_id: "session_realizations"
    operation: "INSERT"
    grant_required: true
    column_scope: []
    row_scope: "Somente sessões de treinamento conduzidas pela equipe sob gestão do treinador."
    conditions: []
    rule_ids: []
    positive_test_ids:
      - "TEST_POS_TRN_SESSION_REALIZATIONS_INS_01"
    negative_test_ids:
      - "TEST_NEG_PUB_SESSION_REALIZATIONS_INS_01"
  - id: "PERM_021"
    role_id: "ROLE_ANALISTA_SCOUT"
    resource_id: "matches"
    operation: "SELECT"
    grant_required: true
    column_scope: []
    row_scope: "Somente partidas especificamente atribuídas ao analista de scout por escala de trabalho no banco."
    conditions: []
    rule_ids: []
    positive_test_ids:
      - "TEST_POS_SCT_MATCHES_SEL_01"
    negative_test_ids:
      - "TEST_NEG_SCT_MATCHES_SEL_UNASSIGNED_01"
  - id: "PERM_022"
    role_id: "ROLE_ANALISTA_SCOUT"
    resource_id: "match_segments"
    operation: "INSERT"
    grant_required: true
    column_scope: []
    row_scope: "Somente segmentos vinculados a partidas atribuídas ao analista de scout."
    conditions: []
    rule_ids:
      - "RN_IHF_VIGENCIA_2026"
    positive_test_ids:
      - "TEST_POS_SCT_MATCH_SEGMENTS_INS_01"
    negative_test_ids:
      - "TEST_NEG_SCT_MATCH_SEGMENTS_INS_UNASSIGNED_01"
  - id: "PERM_023"
    role_id: "ROLE_ANALISTA_SCOUT"
    resource_id: "match_appearances"
    operation: "INSERT"
    grant_required: true
    column_scope: []
    row_scope: "Somente atuações de atletas em partidas atribuídas ao analista, respeitando o teto de 10 atletas em súmula."
    conditions: []
    rule_ids:
      - "RN_TETO_PARTICIPANTES_SUMULA"
    positive_test_ids:
      - "TEST_POS_SCT_MATCH_APPEARANCES_INS_01"
    negative_test_ids:
      - "TEST_NEG_SCT_MATCH_APPEARANCES_INS_UNASSIGNED_01"
  - id: "PERM_024"
    role_id: "ROLE_ANALISTA_SCOUT"
    resource_id: "possessions"
    operation: "INSERT"
    grant_required: true
    column_scope: []
    row_scope: "Somente registros de posse de bola em partidas atribuídas ao analista de scout."
    conditions: []
    rule_ids:
      - "RN_PASSIVO_QUATRO_PASSES"
      - "RN_PROIBICAO_RETARDO_REPETIDO"
    positive_test_ids:
      - "TEST_POS_SCT_POSSESSIONS_INS_01"
    negative_test_ids:
      - "TEST_NEG_SCT_POSSESSIONS_INS_UNASSIGNED_01"
  - id: "PERM_025"
    role_id: "ROLE_ANALISTA_SCOUT"
    resource_id: "bous"
    operation: "INSERT"
    grant_required: true
    column_scope: []
    row_scope: "Somente Unidades Básicas de Ataque (BOU) em partidas atribuídas ao analista de scout."
    conditions: []
    rule_ids: []
    positive_test_ids:
      - "TEST_POS_SCT_BOUS_INS_01"
    negative_test_ids:
      - "TEST_NEG_SCT_BOUS_INS_UNASSIGNED_01"
  - id: "PERM_026"
    role_id: "ROLE_ANALISTA_SCOUT"
    resource_id: "tactical_events"
    operation: "INSERT"
    grant_required: true
    column_scope: []
    row_scope: "Somente eventos táticos em partidas sob responsabilidade do analista de scout."
    conditions: []
    rule_ids:
      - "RN_REJEICAO_VARIAVEIS_INFERENCIAIS"
      - "RN_SANCAO_FINAL_15_SEGUNDOS"
    positive_test_ids:
      - "TEST_POS_SCT_TACTICAL_EVENTS_INS_01"
    negative_test_ids:
      - "TEST_NEG_SCT_TACTICAL_EVENTS_INS_UNASSIGNED_01"
  - id: "PERM_027"
    role_id: "ROLE_ANALISTA_SCOUT"
    resource_id: "finalizations"
    operation: "INSERT"
    grant_required: true
    column_scope: []
    row_scope: "Somente finalizações registradas em partidas atribuídas ao analista de scout."
    conditions: []
    rule_ids:
      - "RN_REGRAS_EXECUCAO_TIRO_SEIS_METROS"
      - "RN_PROTECAO_CABECA_GOLEIRA"
    positive_test_ids:
      - "TEST_POS_SCT_FINALIZATIONS_INS_01"
    negative_test_ids:
      - "TEST_NEG_SCT_FINALIZATIONS_INS_UNASSIGNED_01"
  - id: "PERM_028"
    role_id: "ROLE_ANALISTA_SCOUT"
    resource_id: "goalkeeper_actions"
    operation: "INSERT"
    grant_required: true
    column_scope: []
    row_scope: "Somente ações de goleira registradas em partidas atribuídas ao analista de scout."
    conditions: []
    rule_ids:
      - "RN_SEMANTICA_GOLEIRA"
      - "RN_PROTECAO_CABECA_GOLEIRA"
    positive_test_ids:
      - "TEST_POS_SCT_GOALKEEPER_ACTIONS_INS_01"
    negative_test_ids:
      - "TEST_NEG_SCT_GOALKEEPER_ACTIONS_INS_UNASSIGNED_01"
  - id: "PERM_029"
    role_id: "ROLE_REVISOR_SCOUT"
    resource_id: "scout_protocols"
    operation: "UPDATE"
    grant_required: true
    column_scope: []
    row_scope: "Somente protocolos de revisão metodológica e auditoria de scout para partidas atribuídas ao revisor."
    conditions: []
    rule_ids:
      - "RN_REJEICAO_VARIAVEIS_INFERENCIAIS"
    positive_test_ids:
      - "TEST_POS_REV_SCOUT_PROTOCOLS_UPD_01"
    negative_test_ids:
      - "TEST_NEG_SCT_SCOUT_PROTOCOLS_UPD_01"
  - id: "PERM_030"
    role_id: "ROLE_REVISOR_SCOUT"
    resource_id: "video_clips"
    operation: "SELECT"
    grant_required: true
    column_scope: []
    row_scope: "Somente trechos de vídeo associados a partidas atribuídas para revisão de qualidade de scout."
    conditions: []
    rule_ids: []
    positive_test_ids:
      - "TEST_POS_REV_VIDEO_CLIPS_SEL_01"
    negative_test_ids:
      - "TEST_NEG_PUB_VIDEO_CLIPS_SEL_01"
  - id: "PERM_031"
    role_id: "ROLE_ADMIN_DADOS"
    resource_id: "audit_logs"
    operation: "SELECT"
    grant_required: true
    column_scope: []
    row_scope: "Acesso global de auditoria técnica do sistema reservado ao administrador de dados. Registros de auditoria são estritamente imutáveis e append-only (operações UPDATE e DELETE são categoricamente vedadas para todos os papéis)."
    conditions: []
    rule_ids: []
    positive_test_ids:
      - "TEST_POS_ADM_AUDIT_LOGS_SEL_01"
    negative_test_ids:
      - "TEST_NEG_ADM_AUDIT_LOGS_UPD_01"
  - id: "PERM_032"
    role_id: "ROLE_ATLETA"
    resource_id: "availability_declarations"
    operation: "INSERT"
    grant_required: true
    column_scope: []
    row_scope: "Somente declaração de disponibilidade própria (escopo SELF) vinculada à identidade confirmada da atleta."
    conditions: []
    rule_ids: []
    positive_test_ids:
      - "TEST_POS_ATH_AVAILABILITY_DECLARATIONS_INS_01"
    negative_test_ids:
      - "TEST_NEG_ATH_AVAILABILITY_DECLARATIONS_INS_OTHER_ATHLETE_01"
  - id: "PERM_033"
    role_id: "ROLE_REVISOR_SCOUT"
    resource_id: "tactical_events"
    operation: "UPDATE"
    grant_required: true
    column_scope: []
    row_scope: "Somente correção metodológica e revisão pontual de eventos táticos em partidas atribuídas ao revisor de scout."
    conditions: []
    rule_ids:
      - "RN_REJEICAO_VARIAVEIS_INFERENCIAIS"
    positive_test_ids:
      - "TEST_POS_REV_TACTICAL_EVENTS_UPD_01"
    negative_test_ids:
      - "TEST_NEG_SCT_TACTICAL_EVENTS_UPD_01"
  - id: "PERM_034"
    role_id: "ROLE_REVISOR_SCOUT"
    resource_id: "finalizations"
    operation: "UPDATE"
    grant_required: true
    column_scope: []
    row_scope: "Somente alteração corretiva de atributos de finalização durante a fase de auditoria de qualidade em partidas atribuídas."
    conditions: []
    rule_ids:
      - "RN_REGRAS_EXECUCAO_TIRO_SEIS_METROS"
    positive_test_ids:
      - "TEST_POS_REV_FINALIZATIONS_UPD_01"
    negative_test_ids:
      - "TEST_NEG_SCT_FINALIZATIONS_UPD_01"
  - id: "PERM_035"
    role_id: "ROLE_REVISOR_SCOUT"
    resource_id: "goalkeeper_actions"
    operation: "UPDATE"
    grant_required: true
    column_scope: []
    row_scope: "Somente revisão de dados de ações de goleira para assegurar precisão observacional em partidas sob supervisão do revisor."
    conditions: []
    rule_ids:
      - "RN_SEMANTICA_GOLEIRA"
    positive_test_ids:
      - "TEST_POS_REV_GOALKEEPER_ACTIONS_UPD_01"
    negative_test_ids:
      - "TEST_NEG_SCT_GOALKEEPER_ACTIONS_UPD_01"
default_policy:
  anonymous: "DENY"
  authenticated_without_role: "DENY"
  cross_tenant: "DENY"
  privileged_service_role: "SERVER_ONLY"
  client_authorization_from_user_metadata: "DENY"
open_issues:
  - id: "ISSUE_AUTH_ATLETA_IDENTITY_LINK"
    status: "ABERTA"
    question: "Como vincular a identidade autenticada do usuário ao registro da entidade atleta para viabilizar a execução do escopo SELF do papel ROLE_ATLETA?"
    affected_ids:
      - "ROLE_ATLETA"
      - "athletes"
      - "availability_declarations"
      - "presence_proposals"
      - "PERM_032"
    impact: "Impossibilidade técnica de aplicar políticas de acesso baseadas no escopo SELF para atletas sem a criação prévia do vínculo relacional entre a conta de usuário e a tabela public.athletes."
    required_evidence: "Decisão de arquitetura homologada e modelo de dados atualizado estabelecendo o mapeamento de identidade relacional."
    owner: "ARQUITETO"
  - id: "ISSUE_LACUNA_PLACAR_SHOOTOUT_E_ETAPAS"
    status: "ABERTA"
    question: "Como completar a lacuna de documentação de placar detalhado de shoot-out em jogos específicos da Etapa Final (ex.: J71) e parciais de sets da 4ª Etapa Estadual?"
    affected_ids:
      - "matches"
      - "match_segments"
    impact: "Incompletude no histórico cronológico e auditável do placar em partidas passadas específicas sem registro de vídeo em arquivo."
    required_evidence: "Súmula física impressa assinada ou boletim impresso oficial expedido pela FHERJ/CBHb."
    owner: "OPERADOR"