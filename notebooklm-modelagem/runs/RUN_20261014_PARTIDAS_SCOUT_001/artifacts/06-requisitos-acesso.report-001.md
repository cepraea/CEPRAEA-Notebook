# Requisitos de Acesso e Matriz IAM/RLS — CEPRAEA Beach Handball Pro

roles:
  - role_id: ROLE_ANONYMOUS
    display_name: Usuário Anônimo / Visitante
    description: Acesso público sem sessão autenticada para consulta exclusiva de dados abertos de competições, partidas finalizadas, tabelas e elencos de atletas. Proibido qualquer acesso a dados internos de treinos ou avaliações restritas. O uso de user_metadata para autorização é estritamente proibido.
    requires_authentication: false
    assignment_scope: GLOBAL
    authorization_source: DATABASE_MEMBERSHIP

  - role_id: ROLE_ATHLETE
    display_name: Atleta
    description: Atleta integrante do elenco. Permite auto-declaração de disponibilidade prospectiva, submissão de propostas de bem-estar e consulta individual ao próprio histórico de atuações, convocações e atribuições táticas. Autorização gerenciada estritamente via banco de dados (DATABASE_MEMBERSHIP via associação em public.athletes com auth.uid()); a avaliação de metadados editáveis pelo usuário (user_metadata) é expressamente proibida para fins de controle de acesso.
    requires_authentication: true
    assignment_scope: TEAM
    authorization_source: DATABASE_MEMBERSHIP

  - role_id: ROLE_COACH
    display_name: Treinador / Comissão Técnica
    description: Autoridade técnica de equipe responsável pela gestão de calendário, homologação de presenças factuais, convocação oficial de etapas, escalas táticas e acompanhamento de prontidão. Autorização gerenciada via vínculo em banco de dados (DATABASE_MEMBERSHIP); o uso de user_metadata para controle de permissões é estritamente proibido para evitar elevação ilícita de privilégios.
    requires_authentication: true
    assignment_scope: TEAM
    authorization_source: DATABASE_MEMBERSHIP

  - role_id: ROLE_SCOUT_OBSERVER
    display_name: Observador / Codificador de Scout
    description: Operador qualificado (exige cumprimento de CON-006 com 90%+ de acerto e zero erros críticos) responsável por criar sessões de scout e registrar eventos táticos, posses, BUs, finalizações e ações de goleira durante gravação ou transmissão. Autorização vinculada à sessão de scout ativa e qualificação técnica no banco de dados (DATABASE_MEMBERSHIP); o uso de user_metadata é proibido.
    requires_authentication: true
    assignment_scope: MATCH
    authorization_source: DATABASE_MEMBERSHIP

  - role_id: ROLE_GOVERNANCE_STEWARD
    display_name: Steward de Governança de Dados
    description: Administrador de arquitetura de dados e segurança responsável pelo controle de acessos, esquema do banco de dados, auditoria imutável e aplicação de políticas de conformidade. Autorização gerenciada exclusivamente via privilégios de banco de dados e app_metadata assinado (DATABASE_MEMBERSHIP); a avaliação de user_metadata editável é expressamente vedada.
    requires_authentication: true
    assignment_scope: GLOBAL
    authorization_source: DATABASE_MEMBERSHIP

resources:
  - resource_id: RES_TABLE_COMPETITIONS
    logical_relation_id: public.competitions
    resource_type: TABLE
    data_classification: PUBLICO
    semantic_ownership_rule: Cadastro mestre global de competições esportivas; leitura pública irrestrita, escrita e alteração restritas ao ROLE_GOVERNANCE_STEWARD.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_COMPETITION_EDITIONS
    logical_relation_id: public.competition_editions
    resource_type: TABLE
    data_classification: PUBLICO
    semantic_ownership_rule: Herda governança do cadastro mestre da competição; leitura pública irrestrita, escrita restrita ao ROLE_GOVERNANCE_STEWARD.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_COMPETITION_DIVISIONS
    logical_relation_id: public.competition_divisions
    resource_type: TABLE
    data_classification: PUBLICO
    semantic_ownership_rule: Herda governança da edição de competição; leitura pública, escrita restrita ao ROLE_GOVERNANCE_STEWARD.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_COMPETITION_STAGES
    logical_relation_id: public.competition_stages
    resource_type: TABLE
    data_classification: PUBLICO
    semantic_ownership_rule: Fases e etapas de competição; leitura pública para etapas publicadas, escrita restrita ao ROLE_GOVERNANCE_STEWARD.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_TEAMS
    logical_relation_id: public.teams
    resource_type: TABLE
    data_classification: PUBLICO
    semantic_ownership_rule: Cadastro institucional de equipes esportivas; leitura pública, escrita e manutenção restritas ao ROLE_GOVERNANCE_STEWARD.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_MATCHES
    logical_relation_id: public.matches
    resource_type: TABLE
    data_classification: PUBLICO
    semantic_ownership_rule: Registro canônico de partidas; leitura pública restrita a partidas finalizadas/publicadas, escrita restrita a ROLE_GOVERNANCE_STEWARD e operação técnica autorizada.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_MATCH_SEGMENTS
    logical_relation_id: public.match_segments
    resource_type: TABLE
    data_classification: PUBLICO
    semantic_ownership_rule: Sets e Shoot-out das partidas; leitura pública vinculada a partidas finalizadas, escrita restrita ao ROLE_GOVERNANCE_STEWARD.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_ATHLETES
    logical_relation_id: public.athletes
    resource_type: TABLE
    data_classification: PUBLICO
    semantic_ownership_rule: Cadastro mestre imutável do elenco de atletas; leitura pública de dados cadastrais gerais, mutação restrita ao ROLE_GOVERNANCE_STEWARD e vinculo individual de conta.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_SECONDARY_POSITIONS
    logical_relation_id: public.secondary_positions
    resource_type: TABLE
    data_classification: PUBLICO
    semantic_ownership_rule: Mapeamento secundário de posições de atletas; leitura pública, escrita restrita ao ROLE_COACH e ROLE_GOVERNANCE_STEWARD.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_CALENDAR_EVENTS
    logical_relation_id: public.calendar_events
    resource_type: TABLE
    data_classification: INTERNO
    semantic_ownership_rule: Agenda de treinos e jogos da equipe; leitura restrita a membros da equipe e atletas elegíveis, escrita e gestão exclusivas do ROLE_COACH.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_CONVOCATIONS
    logical_relation_id: public.convocations
    resource_type: TABLE
    data_classification: INTERNO
    semantic_ownership_rule: Relação nominal de convocações por etapa; leitura para membros e atletas da equipe, criação e alteração exclusivas do ROLE_COACH.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_CONVOCATION_ATHLETES
    logical_relation_id: public.convocation_athletes
    resource_type: TABLE
    data_classification: INTERNO
    semantic_ownership_rule: Atletas vinculadas à convocação oficial (máximo 12 por etapa por REG-IHF-002); leitura restrita à equipe, gestão restrita ao ROLE_COACH.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_MATCH_APPEARANCES
    logical_relation_id: public.match_appearances
    resource_type: TABLE
    data_classification: INTERNO
    semantic_ownership_rule: Atuação factual individual em partidas; leitura restrita a atletas da equipe e comissão técnica, escrita via homologação/sincronização do ROLE_COACH.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_POSSESSIONS
    logical_relation_id: public.possessions
    resource_type: TABLE
    data_classification: INTERNO
    semantic_ownership_rule: Unidades de posse de bola (UNT-003); leitura por analistas, atletas e comissão técnica, escrita restrita ao ROLE_SCOUT_OBSERVER em sessão ativa.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_BOUS
    logical_relation_id: public.bous
    resource_type: TABLE
    data_classification: INTERNO
    semantic_ownership_rule: Unidades Básicas de Ataque posicional (UNT-004); leitura por analistas e comissão, escrita restrita ao ROLE_SCOUT_OBSERVER em sessão ativa.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_TACTICAL_EVENTS
    logical_relation_id: public.tactical_events
    resource_type: TABLE
    data_classification: INTERNO
    semantic_ownership_rule: Eventos táticos codificados durante a partida; leitura por analistas e comissão, escrita restrita ao ROLE_SCOUT_OBSERVER qualificado (CON-006).
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_FINALIZATIONS
    logical_relation_id: public.finalizations
    resource_type: TABLE
    data_classification: INTERNO
    semantic_ownership_rule: Registros detalhados de arremessos e finalizações; leitura por analistas e comissão, escrita restrita ao ROLE_SCOUT_OBSERVER em sessão ativa.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_GOALKEEPER_ACTIONS
    logical_relation_id: public.goalkeeper_actions
    resource_type: TABLE
    data_classification: INTERNO
    semantic_ownership_rule: Ações e defesas técnicas das goleiras (T1-T4); leitura por analistas e comissão, escrita restrita ao ROLE_SCOUT_OBSERVER em sessão ativa.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_TACTICAL_ASSIGNMENTS
    logical_relation_id: public.tactical_assignments
    resource_type: TABLE
    data_classification: INTERNO
    semantic_ownership_rule: Atribuições e papéis táticos por atleta; leitura pela própria atleta e comissão técnica, gestão e escrita restritas ao ROLE_COACH.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_PRESENCE_PROPOSALS
    logical_relation_id: public.presence_proposals
    resource_type: TABLE
    data_classification: INTERNO
    semantic_ownership_rule: Fila transitória de autorrelatos/wellness (DEC-DATA-045.2); escrita por ROLE_ATHLETE, leitura e homologação exclusiva pelo ROLE_COACH.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_REFEREE_ASSIGNMENTS
    logical_relation_id: public.referee_assignments
    resource_type: TABLE
    data_classification: INTERNO
    semantic_ownership_rule: Escala e atribuição de arbitragem por partida; leitura restrita à organização e comissão técnica, escrita por ROLE_GOVERNANCE_STEWARD.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_SCOUT_SESSIONS
    logical_relation_id: public.scout_sessions
    resource_type: TABLE
    data_classification: INTERNO
    semantic_ownership_rule: Sessões ativas de coleta de scout; leitura e gestão restritas ao ROLE_SCOUT_OBSERVER atribuído e ROLE_GOVERNANCE_STEWARD.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_SCOUT_OBSERVATIONS
    logical_relation_id: public.scout_observations
    resource_type: TABLE
    data_classification: INTERNO
    semantic_ownership_rule: Observações pontuais do codificador de scout; leitura por analistas e comissão, escrita restrita ao ROLE_SCOUT_OBSERVER da sessão.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_VIDEO_TIMECODES
    logical_relation_id: public.video_timecodes
    resource_type: TABLE
    data_classification: INTERNO
    semantic_ownership_rule: Sincronização de timecodes de vídeo com eventos táticos; leitura por comissão e atletas, escrita restrita ao ROLE_SCOUT_OBSERVER.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_OBSERVER_QUALIFICATIONS
    logical_relation_id: public.observer_qualifications
    resource_type: TABLE
    data_classification: INTERNO
    semantic_ownership_rule: Histórico de certificação e validação técnica de observadores (CON-006); leitura e escrita exclusivas do ROLE_GOVERNANCE_STEWARD.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_RANKING_ELIGIBILITY
    logical_relation_id: public.ranking_eligibility
    resource_type: TABLE
    data_classification: INTERNO
    semantic_ownership_rule: Elegibilidade e exceções de ranqueamento de equipes; leitura pública/interna, escrita restrita ao ROLE_GOVERNANCE_STEWARD.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_SCORING_RULES
    logical_relation_id: public.scoring_rules
    resource_type: TABLE
    data_classification: INTERNO
    semantic_ownership_rule: Tabelas e regras de cálculo de pontuação (SGATE-0023/DEC-DATA-042); leitura por comissão técnica, manutenção restrita ao ROLE_GOVERNANCE_STEWARD.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_SCHEMA_MIGRATIONS
    logical_relation_id: public.schema_migrations
    resource_type: TABLE
    data_classification: INTERNO
    semantic_ownership_rule: Histórico de migrações técnicas do banco de dados; acesso isolado ao pipeline de DDL, totalmente oculto da Data API.
    exposed_via_data_api: false
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_FACTUAL_PRESENCES
    logical_relation_id: public.factual_presences
    resource_type: TABLE
    data_classification: RESTRITO
    semantic_ownership_rule: Fonte única da verdade (SSOT) de presenças confirmadas (DEC-DATA-045.1); leitura restrita à comissão técnica e à própria atleta, inserção e homologação exclusivas do ROLE_COACH.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_AVAILABILITY_DECLARATIONS
    logical_relation_id: public.availability_declarations
    resource_type: TABLE
    data_classification: RESTRITO
    semantic_ownership_rule: Declarações prospectivas de disponibilidade (RN-DISP-001); upsert exclusivo da própria atleta (ROLE_ATHLETE), leitura pela comissão técnica (ROLE_COACH).
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_WELLNESS_EVALUATIONS
    logical_relation_id: public.wellness_evaluations
    resource_type: TABLE
    data_classification: RESTRITO
    semantic_ownership_rule: Avaliações individuais de carga percebida e estado de bem-estar de saúde desportiva; leitura e escrita restritas à própria atleta e ao ROLE_COACH com projeção restrita de colunas.
    exposed_via_data_api: true
    security_invoker: NOT_APPLICABLE

  - resource_id: RES_TABLE_AUDIT_LOGS
    logical_relation_id: public.audit_logs
    resource_type: TABLE
    data_classification: RESTRITO
    semantic_ownership_rule: Trilhas imutáveis de auditoria de segurança e mutação de dados; não exposto via Data API, consulta restrita ao ROLE_GOVERNANCE_STEWARD.
    exposed_via_data_api: false
    security_invoker: NOT_APPLICABLE

permissions:
  - permission_id: PERM_ANONYMOUS_SELECT_PUBLIC_COMPETITIONS
    resource_id: RES_TABLE_COMPETITIONS
    role_id: ROLE_ANONYMOUS
    operation: SELECT
    required_grant: GRANT SELECT ON public.competitions TO role_anonymous
    row_scope: true
    columns:
      - id
      - code
      - name
      - federation
      - scope
      - created_at
    conditions: Acesso de leitura irrestrito a competições cadastradas.
    rule_ids: []
    evidence_ref_ids:
      - EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_001
    planned_tests:
      - test_id: TEST_POS_ANONYMOUS_READ_COMPETITIONS
        test_role: ROLE_ANONYMOUS
        test_context: Leitura pública do catálogo de competições na Data API.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_ANONYMOUS_UPDATE_COMPETITIONS
        test_role: ROLE_ANONYMOUS
        test_context: Tentativa de inserção ou alteração em competições por visitante.
        expected_result: EXPECT_DENY

  - permission_id: PERM_ANONYMOUS_SELECT_PUBLIC_EDITIONS
    resource_id: RES_TABLE_COMPETITION_EDITIONS
    role_id: ROLE_ANONYMOUS
    operation: SELECT
    required_grant: GRANT SELECT ON public.competition_editions TO role_anonymous
    row_scope: true
    columns:
      - id
      - competition_id
      - year
      - name
      - start_date
      - end_date
      - status
    conditions: Acesso de leitura público a edições de competições.
    rule_ids: []
    evidence_ref_ids:
      - EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_005
    planned_tests:
      - test_id: TEST_POS_ANONYMOUS_READ_EDITIONS
        test_role: ROLE_ANONYMOUS
        test_context: Leitura pública de edições de campeonatos.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_ANONYMOUS_DELETE_EDITIONS
        test_role: ROLE_ANONYMOUS
        test_context: Tentativa de remoção de edições por usuário não autenticado.
        expected_result: EXPECT_DENY

  - permission_id: PERM_ANONYMOUS_SELECT_PUBLIC_DIVISIONS
    resource_id: RES_TABLE_COMPETITION_DIVISIONS
    role_id: ROLE_ANONYMOUS
    operation: SELECT
    required_grant: GRANT SELECT ON public.competition_divisions TO role_anonymous
    row_scope: true
    columns:
      - id
      - edition_id
      - gender
      - category_code
      - name
    conditions: Leitura aberta para divisões e categorias esportivas.
    rule_ids: []
    evidence_ref_ids:
      - EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_005
    planned_tests:
      - test_id: TEST_POS_ANONYMOUS_READ_DIVISIONS
        test_role: ROLE_ANONYMOUS
        test_context: Consulta a divisões da competição.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_ANONYMOUS_INSERT_DIVISIONS
        test_role: ROLE_ANONYMOUS
        test_context: Tentativa de inserção de divisão por usuário anônimo.
        expected_result: EXPECT_DENY

  - permission_id: PERM_ANONYMOUS_SELECT_PUBLIC_STAGES
    resource_id: RES_TABLE_COMPETITION_STAGES
    role_id: ROLE_ANONYMOUS
    operation: SELECT
    required_grant: GRANT SELECT ON public.competition_stages TO role_anonymous
    row_scope: status = 'PUBLICADA'
    columns:
      - id
      - division_id
      - stage_number
      - name
      - location
      - start_date
      - end_date
      - status
    conditions: Leitura pública restrita a etapas com status PUBLICADA.
    rule_ids: []
    evidence_ref_ids:
      - EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_005
    planned_tests:
      - test_id: TEST_POS_ANONYMOUS_READ_PUBLISHED_STAGES
        test_role: ROLE_ANONYMOUS
        test_context: Consulta de etapas publicadas na tabela oficial.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_ANONYMOUS_READ_DRAFT_STAGES
        test_role: ROLE_ANONYMOUS
        test_context: Tentativa de leitura de etapa em rascunho por usuário anônimo.
        expected_result: EXPECT_DENY

  - permission_id: PERM_ANONYMOUS_SELECT_PUBLIC_TEAMS
    resource_id: RES_TABLE_TEAMS
    role_id: ROLE_ANONYMOUS
    operation: SELECT
    required_grant: GRANT SELECT ON public.teams TO role_anonymous
    row_scope: true
    columns:
      - id
      - code
      - name
      - short_name
      - city
      - state
      - is_cepraea
    conditions: Consulta aberta às equipes cadastradas no sistema.
    rule_ids: []
    evidence_ref_ids:
      - EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_001
    planned_tests:
      - test_id: TEST_POS_ANONYMOUS_READ_TEAMS
        test_role: ROLE_ANONYMOUS
        test_context: Listagem pública de equipes participantes.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_ANONYMOUS_UPDATE_TEAMS
        test_role: ROLE_ANONYMOUS
        test_context: Tentativa de alteração de dados de equipe por visitante.
        expected_result: EXPECT_DENY

  - permission_id: PERM_ANONYMOUS_SELECT_PUBLIC_MATCHES
    resource_id: RES_TABLE_MATCHES
    role_id: ROLE_ANONYMOUS
    operation: SELECT
    required_grant: GRANT SELECT ON public.matches TO role_anonymous
    row_scope: status = 'FINALIZADA'
    columns:
      - id
      - stage_id
      - team_a_id
      - team_b_id
      - scheduled_time
      - status
      - sets_won_cepraea
      - sets_won_opponent
      - cepraea_victory
    conditions: Exibe apenas partidas com status de finalização confirmada.
    rule_ids:
      - REG-IHF-003
    evidence_ref_ids:
      - EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_009
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_026
    planned_tests:
      - test_id: TEST_POS_ANONYMOUS_READ_FINALIZED_MATCHES
        test_role: ROLE_ANONYMOUS
        test_context: Leitura pública de resultados de partidas finalizadas.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_ANONYMOUS_READ_SCHEDULED_MATCHES
        test_role: ROLE_ANONYMOUS
        test_context: Tentativa de acesso direto a partidas em andamento/agendadas antes da publicação.
        expected_result: EXPECT_DENY

  - permission_id: PERM_ANONYMOUS_SELECT_PUBLIC_MATCH_SEGMENTS
    resource_id: RES_TABLE_MATCH_SEGMENTS
    role_id: ROLE_ANONYMOUS
    operation: SELECT
    required_grant: GRANT SELECT ON public.match_segments TO role_anonymous
    row_scope: match_id IN (SELECT id FROM public.matches WHERE status = 'FINALIZADA')
    columns:
      - id
      - match_id
      - segment_type
      - segment_number
      - score_team_a
      - score_team_b
      - winner_team_id
    conditions: Placar detalhado por set e shoot-out visível apenas para partidas finalizadas.
    rule_ids:
      - REG-IHF-003
    evidence_ref_ids:
      - EVID_IHF_RULES_2026_EN_002
      - EVID_IHF_RULES_2026_EN_004
    planned_tests:
      - test_id: TEST_POS_ANONYMOUS_READ_MATCH_SEGMENTS
        test_role: ROLE_ANONYMOUS
        test_context: Leitura pública dos placares dos sets de partidas finalizadas.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_ANONYMOUS_WRITE_MATCH_SEGMENTS
        test_role: ROLE_ANONYMOUS
        test_context: Tentativa de alteração manual de placar por visitante.
        expected_result: EXPECT_DENY

  - permission_id: PERM_ANONYMOUS_SELECT_PUBLIC_ATHLETES
    resource_id: RES_TABLE_ATHLETES
    role_id: ROLE_ANONYMOUS
    operation: SELECT
    required_grant: GRANT SELECT ON public.athletes TO role_anonymous
    row_scope: true
    columns:
      - id
      - name
      - nickname
      - primary_position
      - jersey_number
    conditions: Projeção estrita de dados públicos cadastrais do elenco, omitindo dados pessoais sensíveis ou de contato.
    rule_ids:
      - RN-DISP-003
    evidence_ref_ids:
      - EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_005
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_005
    planned_tests:
      - test_id: TEST_POS_ANONYMOUS_READ_PUBLIC_ATHLETES
        test_role: ROLE_ANONYMOUS
        test_context: Leitura pública de nomes e posições do elenco.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_ANONYMOUS_SELECT_SENSITIVE_ATHLETE_FIELDS
        test_role: ROLE_ANONYMOUS
        test_context: Tentativa de consulta a colunas de dados pessoais restritos em public.athletes.
        expected_result: EXPECT_DENY

  - permission_id: PERM_ANONYMOUS_SELECT_PUBLIC_SECONDARY_POSITIONS
    resource_id: RES_TABLE_SECONDARY_POSITIONS
    role_id: ROLE_ANONYMOUS
    operation: SELECT
    required_grant: GRANT SELECT ON public.secondary_positions TO role_anonymous
    row_scope: true
    columns:
      - id
      - athlete_id
      - position
    conditions: Consulta aberta ao mapeamento secundário de posições.
    rule_ids: []
    evidence_ref_ids:
      - EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_001
    planned_tests:
      - test_id: TEST_POS_ANONYMOUS_READ_SECONDARY_POSITIONS
        test_role: ROLE_ANONYMOUS
        test_context: Leitura de posições secundárias de atletas.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_ANONYMOUS_INSERT_SECONDARY_POSITIONS
        test_role: ROLE_ANONYMOUS
        test_context: Inserção não autorizada de posição por visitante.
        expected_result: EXPECT_DENY

  - permission_id: PERM_ATHLETE_SELECT_OWN_PROFILE
    resource_id: RES_TABLE_ATHLETES
    role_id: ROLE_ATHLETE
    operation: SELECT
    required_grant: GRANT SELECT ON public.athletes TO role_athlete
    row_scope: id IN (SELECT id FROM public.athletes WHERE user_id = auth.uid())
    columns:
      - id
      - user_id
      - name
      - nickname
      - primary_position
      - jersey_number
      - birth_date
      - created_at
    conditions: Atleta acessa dados completos do próprio perfil cadastral.
    rule_ids:
      - RN-DISP-003
    evidence_ref_ids:
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_005
    planned_tests:
      - test_id: TEST_POS_ATHLETE_READ_OWN_PROFILE
        test_role: ROLE_ATHLETE
        test_context: Atleta consultando os dados do próprio perfil.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_ATHLETE_READ_OTHER_ATHLETE_FULL_PROFILE
        test_role: ROLE_ATHLETE
        test_context: Atleta tentando acessar colunas restritas do perfil de outro atleta.
        expected_result: EXPECT_DENY

  - permission_id: PERM_ATHLETE_UPSERT_AVAILABILITY
    resource_id: RES_TABLE_AVAILABILITY_DECLARATIONS
    role_id: ROLE_ATHLETE
    operation: UPDATE
    required_grant: GRANT SELECT, INSERT, UPDATE ON public.availability_declarations TO role_athlete
    row_scope: athlete_id IN (SELECT id FROM public.athletes WHERE user_id = auth.uid()) AND event_id IN (SELECT id FROM public.calendar_events WHERE accepts_availability = true)
    columns:
      - id
      - event_id
      - athlete_id
      - response_status
      - updated_at
    conditions: Permite operação de merge/upsert da declaração de disponibilidade apenas para eventos elegíveis e no próprio identificador de atleta.
    rule_ids:
      - RN-DISP-001
      - RN-DISP-003
      - RN-DISP-004
      - RN-DISP-005
      - RN-DISP-008
      - RN-DISP-010
      - RN-DISP-013
      - RN-DISP-015
    evidence_ref_ids:
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_003
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_005
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_006
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_010
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_015
    planned_tests:
      - test_id: TEST_POS_ATHLETE_UPSERT_OWN_AVAILABILITY
        test_role: ROLE_ATHLETE
        test_context: Atleta atualizando o estado de disponibilidade para evento elegível.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_ATHLETE_UPSERT_OTHER_AVAILABILITY
        test_role: ROLE_ATHLETE
        test_context: Atleta tentando alterar a disponibilidade de outra integrante do elenco.
        expected_result: EXPECT_DENY

  - permission_id: PERM_ATHLETE_INSERT_PRESENCE_PROPOSAL
    resource_id: RES_TABLE_PRESENCE_PROPOSALS
    role_id: ROLE_ATHLETE
    operation: INSERT
    required_grant: GRANT SELECT, INSERT ON public.presence_proposals TO role_athlete
    row_scope: athlete_id IN (SELECT id FROM public.athletes WHERE user_id = auth.uid())
    columns:
      - id
      - event_id
      - athlete_id
      - proposed_status
      - wellness_score
      - rpe_score
      - status
      - submitted_at
    conditions: Submissão de autorrelato pós-treino gravada com status inicial AGUARDANDO_CONFIRMACAO.
    rule_ids:
      - DEC-DATA-045.2
      - RN-DISP-015
    evidence_ref_ids:
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_021
      - EVID_CEPRAEA_DATABASE_CCB2A718_003
    planned_tests:
      - test_id: TEST_POS_ATHLETE_SUBMIT_PRESENCE_PROPOSAL
        test_role: ROLE_ATHLETE
        test_context: Atleta enviando proposta de presença/wellness no próprio nome.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_ATHLETE_DIRECT_INSERT_FACTUAL_PRESENCE
        test_role: ROLE_ATHLETE
        test_context: Atleta tentando inserir diretamente em public.factual_presences pulando a fila transitória.
        expected_result: EXPECT_DENY

  - permission_id: PERM_ATHLETE_SELECT_OWN_MATCH_APPEARANCES
    resource_id: RES_TABLE_MATCH_APPEARANCES
    role_id: ROLE_ATHLETE
    operation: SELECT
    required_grant: GRANT SELECT ON public.match_appearances TO role_athlete
    row_scope: athlete_id IN (SELECT id FROM public.athletes WHERE user_id = auth.uid())
    columns:
      - id
      - match_id
      - athlete_id
      - participation_status
      - minutes_played
      - goals_scored
    conditions: Leitura restrita aos próprios dados de atuação factual na partida.
    rule_ids:
      - REG-IHF-002
    evidence_ref_ids:
      - EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_010
    planned_tests:
      - test_id: TEST_POS_ATHLETE_READ_OWN_MATCH_APPEARANCE
        test_role: ROLE_ATHLETE
        test_context: Atleta visualizando suas estatísticas individuais da partida.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_ATHLETE_READ_OTHER_MATCH_APPEARANCE
        test_role: ROLE_ATHLETE
        test_context: Atleta tentando consultar atuações individuais restritas de terceiros.
        expected_result: EXPECT_DENY

  - permission_id: PERM_ATHLETE_SELECT_OWN_TACTICAL_ASSIGNMENTS
    resource_id: RES_TABLE_TACTICAL_ASSIGNMENTS
    role_id: ROLE_ATHLETE
    operation: SELECT
    required_grant: GRANT SELECT ON public.tactical_assignments TO role_athlete
    row_scope: athlete_id IN (SELECT id FROM public.athletes WHERE user_id = auth.uid())
    columns:
      - id
      - match_id
      - athlete_id
      - tactical_function
      - system_formation
      - primary_role
      - is_specialist_coringa
    conditions: Visualização das atribuições táticas designadas pelo treinador para a partida.
    rule_ids: []
    evidence_ref_ids:
      - EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_004
    planned_tests:
      - test_id: TEST_POS_ATHLETE_READ_OWN_TACTICAL_ASSIGNMENT
        test_role: ROLE_ATHLETE
        test_context: Atleta consultando sua instrução e papel tático na partida.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_ATHLETE_UPDATE_TACTICAL_ASSIGNMENT
        test_role: ROLE_ATHLETE
        test_context: Atleta tentando alterar seu próprio papel tático no sistema.
        expected_result: EXPECT_DENY

  - permission_id: PERM_ATHLETE_SELECT_OWN_WELLNESS
    resource_id: RES_TABLE_WELLNESS_EVALUATIONS
    role_id: ROLE_ATHLETE
    operation: SELECT
    required_grant: GRANT SELECT ON public.wellness_evaluations TO role_athlete
    row_scope: athlete_id IN (SELECT id FROM public.athletes WHERE user_id = auth.uid())
    columns:
      - id
      - athlete_id
      - evaluation_date
      - fatigue_level
      - soreness_level
      - stress_level
      - sleep_quality
    conditions: Leitura exclusiva do próprio histórico de avaliações de bem-estar.
    rule_ids: []
    evidence_ref_ids:
      - EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_001
    planned_tests:
      - test_id: TEST_POS_ATHLETE_READ_OWN_WELLNESS
        test_role: ROLE_ATHLETE
        test_context: Atleta consultando seu histórico de fadiga e bem-estar.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_ATHLETE_READ_OTHER_WELLNESS
        test_role: ROLE_ATHLETE
        test_context: Atleta tentando visualizar avaliações de bem-estar de outra atleta.
        expected_result: EXPECT_DENY

  - permission_id: PERM_ATHLETE_INSERT_OWN_WELLNESS
    resource_id: RES_TABLE_WELLNESS_EVALUATIONS
    role_id: ROLE_ATHLETE
    operation: INSERT
    required_grant: GRANT SELECT, INSERT ON public.wellness_evaluations TO role_athlete
    row_scope: athlete_id IN (SELECT id FROM public.athletes WHERE user_id = auth.uid())
    columns:
      - id
      - athlete_id
      - evaluation_date
      - fatigue_level
      - soreness_level
      - stress_level
      - sleep_quality
      - recorded_at
    conditions: Inserção de avaliação diária do próprio estado de bem-estar desportivo.
    rule_ids: []
    evidence_ref_ids:
      - EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_001
    planned_tests:
      - test_id: TEST_POS_ATHLETE_INSERT_OWN_WELLNESS
        test_role: ROLE_ATHLETE
        test_context: Atleta registrando formulário diário de wellness.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_ATHLETE_INSERT_OTHER_WELLNESS
        test_role: ROLE_ATHLETE
        test_context: Atleta tentando enviar dados de wellness em nome de colega.
        expected_result: EXPECT_DENY

  - permission_id: PERM_COACH_MANAGE_CALENDAR_EVENTS
    resource_id: RES_TABLE_CALENDAR_EVENTS
    role_id: ROLE_COACH
    operation: INSERT
    required_grant: GRANT SELECT, INSERT, UPDATE, DELETE ON public.calendar_events TO role_coach
    row_scope: team_id IN (SELECT team_id FROM public.team_memberships WHERE user_id = auth.uid() AND role = 'COACH')
    columns:
      - id
      - team_id
      - event_type
      - title
      - location
      - start_time
      - end_time
      - accepts_availability
    conditions: Criação e alteração de agenda restrita aos treinos e jogos da equipe vinculada.
    rule_ids:
      - RN-DISP-013
      - RN-DISP-014
    evidence_ref_ids:
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_015
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_016
    planned_tests:
      - test_id: TEST_POS_COACH_INSERT_CALENDAR_EVENT
        test_role: ROLE_COACH
        test_context: Treinador configurando novo treino no calendário de sua equipe.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_COACH_MANAGE_OTHER_TEAM_EVENT
        test_role: ROLE_COACH
        test_context: Treinador tentando criar eventos na agenda de outra equipe.
        expected_result: EXPECT_DENY

  - permission_id: PERM_COACH_SELECT_AVAILABILITY_DECLARATIONS
    resource_id: RES_TABLE_AVAILABILITY_DECLARATIONS
    role_id: ROLE_COACH
    operation: SELECT
    required_grant: GRANT SELECT ON public.availability_declarations TO role_coach
    row_scope: event_id IN (SELECT id FROM public.calendar_events WHERE team_id IN (SELECT team_id FROM public.team_memberships WHERE user_id = auth.uid() AND role = 'COACH'))
    columns:
      - id
      - event_id
      - athlete_id
      - response_status
      - updated_at
    conditions: Leitura consolidada da intenção de presença das atletas para os eventos da equipe.
    rule_ids:
      - RN-DISP-001
      - RN-DISP-012
      - RN-DISP-015
    evidence_ref_ids:
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_003
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_014
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_017
    planned_tests:
      - test_id: TEST_POS_COACH_READ_TEAM_AVAILABILITY
        test_role: ROLE_COACH
        test_context: Treinador consultando relatório de disponibilidade para o próximo jogo.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_COACH_READ_OTHER_TEAM_AVAILABILITY
        test_role: ROLE_COACH
        test_context: Treinador tentando ler disponibilidades de atletas de equipe adversária.
        expected_result: EXPECT_DENY

  - permission_id: PERM_COACH_CONFIRM_FACTUAL_PRESENCES
    resource_id: RES_TABLE_FACTUAL_PRESENCES
    role_id: ROLE_COACH
    operation: INSERT
    required_grant: GRANT SELECT, INSERT, UPDATE ON public.factual_presences TO role_coach
    row_scope: event_id IN (SELECT id FROM public.calendar_events WHERE team_id IN (SELECT team_id FROM public.team_memberships WHERE user_id = auth.uid() AND role = 'COACH'))
    columns:
      - id
      - event_id
      - athlete_id
      - presence_status
      - confirmed_by
      - confirmed_at
    conditions: Homologação humana primária e auditada de presenças factuais da comissão técnica.
    rule_ids:
      - DEC-DATA-045.1
      - DEC-DATA-045.3
      - DEC-DATA-045.4
    evidence_ref_ids:
      - EVID_CEPRAEA_DATABASE_CCB2A718_003
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_020
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_022
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_023
    planned_tests:
      - test_id: TEST_POS_COACH_CONFIRM_FACTUAL_PRESENCE
        test_role: ROLE_COACH
        test_context: Treinador confirmando presença realizada em treino da equipe.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_COACH_CONFIRM_FACTUAL_PRESENCE_UNASSIGNED_EVENT
        test_role: ROLE_COACH
        test_context: Treinador tentando homologar presença em evento de equipe não atribuída.
        expected_result: EXPECT_DENY

  - permission_id: PERM_COACH_MANAGE_CONVOCATIONS
    resource_id: RES_TABLE_CONVOCATIONS
    role_id: ROLE_COACH
    operation: INSERT
    required_grant: GRANT SELECT, INSERT, UPDATE ON public.convocations TO role_coach
    row_scope: stage_id IN (SELECT id FROM public.competition_stages WHERE division_id IN (SELECT id FROM public.competition_divisions WHERE edition_id IN (SELECT id FROM public.competition_editions))) AND team_id IN (SELECT team_id FROM public.team_memberships WHERE user_id = auth.uid() AND role = 'COACH')
    columns:
      - id
      - stage_id
      - team_id
      - convocation_title
      - max_stage_athletes
      - max_match_athletes
      - status
    conditions: Emissão da convocação oficial com teto nominal de 12 atletas para a etapa.
    rule_ids:
      - REG-IHF-001
      - REG-IHF-002
    evidence_ref_ids:
      - EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_007
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_024
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_025
    planned_tests:
      - test_id: TEST_POS_COACH_CREATE_STAGE_CONVOCATION
        test_role: ROLE_COACH
        test_context: Treinador emitindo convocação nominal da equipe para a 1ª Etapa.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_COACH_CREATE_CONVOCATION_OTHER_TEAM
        test_role: ROLE_COACH
        test_context: Treinador tentando registrar convocação em nome de clube rival.
        expected_result: EXPECT_DENY

  - permission_id: PERM_COACH_MANAGE_CONVOCATION_ATHLETES
    resource_id: RES_TABLE_CONVOCATION_ATHLETES
    role_id: ROLE_COACH
    operation: INSERT
    required_grant: GRANT SELECT, INSERT, UPDATE, DELETE ON public.convocation_athletes TO role_coach
    row_scope: convocation_id IN (SELECT id FROM public.convocations WHERE team_id IN (SELECT team_id FROM public.team_memberships WHERE user_id = auth.uid() AND role = 'COACH'))
    columns:
      - id
      - convocation_id
      - athlete_id
      - selection_status
    conditions: Associação de atletas à relação nominal de até 12 convocadas.
    rule_ids:
      - REG-IHF-002
    evidence_ref_ids:
      - EVID_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB_003
    planned_tests:
      - test_id: TEST_POS_COACH_ADD_ATHLETE_TO_CONVOCATION
        test_role: ROLE_COACH
        test_context: Treinador adicionando atleta elegível à lista da convocação.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_COACH_ADD_ATHLETE_OVER_LIMIT
        test_role: ROLE_COACH
        test_context: Tentativa de inserção do 13º atleta em desacordo com a cardinalidade 1..12 da relação nominal.
        expected_result: EXPECT_DENY

  - permission_id: PERM_COACH_MANAGE_TACTICAL_ASSIGNMENTS
    resource_id: RES_TABLE_TACTICAL_ASSIGNMENTS
    role_id: ROLE_COACH
    operation: INSERT
    required_grant: GRANT SELECT, INSERT, UPDATE, DELETE ON public.tactical_assignments TO role_coach
    row_scope: match_id IN (SELECT id FROM public.matches WHERE team_a_id IN (SELECT team_id FROM public.team_memberships WHERE user_id = auth.uid() AND role = 'COACH') OR team_b_id IN (SELECT team_id FROM public.team_memberships WHERE user_id = auth.uid() AND role = 'COACH'))
    columns:
      - id
      - match_id
      - athlete_id
      - tactical_function
      - system_formation
      - primary_role
      - is_specialist_coringa
    conditions: Definição da escala tática e vinculação de especialista/coringa exclusivamente em funções ofensivas.
    rule_ids: []
    evidence_ref_ids:
      - EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_004
    planned_tests:
      - test_id: TEST_POS_COACH_SET_OFFENSIVE_TACTICAL_ASSIGNMENT
        test_role: ROLE_COACH
        test_context: Treinador definindo Especialista/Coringa em sistema 3x1 de ataque.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_COACH_SET_DEFENSIVE_CORINGA
        test_role: ROLE_COACH
        test_context: Tentativa de atribuir papel de Especialista/Coringa em função defensiva (violação da taxonomia TACT V2).
        expected_result: EXPECT_DENY

  - permission_id: PERM_COACH_UPDATE_PRESENCE_PROPOSALS
    resource_id: RES_TABLE_PRESENCE_PROPOSALS
    role_id: ROLE_COACH
    operation: UPDATE
    required_grant: GRANT SELECT, UPDATE ON public.presence_proposals TO role_coach
    row_scope: event_id IN (SELECT id FROM public.calendar_events WHERE team_id IN (SELECT team_id FROM public.team_memberships WHERE user_id = auth.uid() AND role = 'COACH'))
    columns:
      - status
      - reviewed_by
      - reviewed_at
    conditions: Ação de homologação humana (CONFIRMAR, AJUSTAR ou REJEITAR) sobre a fila de propostas de presença.
    rule_ids:
      - DEC-DATA-045.3
    evidence_ref_ids:
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_022
    planned_tests:
      - test_id: TEST_POS_COACH_APPROVE_PRESENCE_PROPOSAL
        test_role: ROLE_COACH
        test_context: Treinador aprovando autorrelato de atleta na fila transitória.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_ATHLETE_APPROVE_PRESENCE_PROPOSAL
        test_role: ROLE_ATHLETE
        test_context: Atleta tentando alterar o status de aprovação de sua própria proposta.
        expected_result: EXPECT_DENY

  - permission_id: PERM_COACH_SELECT_WELLNESS_EVALUATIONS
    resource_id: RES_TABLE_WELLNESS_EVALUATIONS
    role_id: ROLE_COACH
    operation: SELECT
    required_grant: GRANT SELECT ON public.wellness_evaluations TO role_coach
    row_scope: athlete_id IN (SELECT id FROM public.athletes WHERE team_id IN (SELECT team_id FROM public.team_memberships WHERE user_id = auth.uid() AND role = 'COACH'))
    columns:
      - id
      - athlete_id
      - evaluation_date
      - fatigue_level
      - soreness_level
      - stress_level
      - sleep_quality
    conditions: Acompanhamento da carga interna e indicadores de fadiga das atletas do elenco.
    rule_ids: []
    evidence_ref_ids:
      - EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_001
    planned_tests:
      - test_id: TEST_POS_COACH_READ_TEAM_WELLNESS
        test_role: ROLE_COACH
        test_context: Treinador consultando relatório de fadiga pré-jogo da equipe.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_COACH_READ_OPPONENT_WELLNESS
        test_role: ROLE_COACH
        test_context: Treinador tentando acessar avaliações de wellness de atletas adversárias.
        expected_result: EXPECT_DENY

  - permission_id: PERM_COACH_MANAGE_MATCH_APPEARANCES
    resource_id: RES_TABLE_MATCH_APPEARANCES
    role_id: ROLE_COACH
    operation: INSERT
    required_grant: GRANT SELECT, INSERT, UPDATE ON public.match_appearances TO role_coach
    row_scope: match_id IN (SELECT id FROM public.matches WHERE team_a_id IN (SELECT team_id FROM public.team_memberships WHERE user_id = auth.uid() AND role = 'COACH') OR team_b_id IN (SELECT team_id FROM public.team_memberships WHERE user_id = auth.uid() AND role = 'COACH'))
    columns:
      - id
      - match_id
      - athlete_id
      - participation_status
      - minutes_played
      - goals_scored
    conditions: Registro factual da escalação de 10 atletas e status de participação na partida por exclusão das 2 ausentes.
    rule_ids:
      - REG-IHF-001
      - REG-IHF-002
    evidence_ref_ids:
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_024
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_025
    planned_tests:
      - test_id: TEST_POS_COACH_SET_MATCH_PARTICIPATION
        test_role: ROLE_COACH
        test_context: Treinador registrando status JOGOU/NAO_JOGOU no fechamento da súmula.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_COACH_SET_ELEVEN_PLAYERS_JOGOU
        test_role: ROLE_COACH
        test_context: Tentativa de atribuir status JOGOU a 11 atletas na mesma partida (violação do teto de 10 em súmula por REG-IHF-001).
        expected_result: EXPECT_DENY

  - permission_id: PERM_SCOUT_MANAGE_SCOUT_SESSIONS
    resource_id: RES_TABLE_SCOUT_SESSIONS
    role_id: ROLE_SCOUT_OBSERVER
    operation: INSERT
    required_grant: GRANT SELECT, INSERT, UPDATE ON public.scout_sessions TO role_scout_observer
    row_scope: observer_id = auth.uid()
    columns:
      - id
      - match_id
      - observer_id
      - session_status
      - started_at
      - ended_at
    conditions: Abertura de sessão de coleta condicionada a registro de qualificação ativa (CON-006).
    rule_ids:
      - CON-006
    evidence_ref_ids:
      - EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009
    planned_tests:
      - test_id: TEST_POS_QUALIFIED_SCOUT_OPEN_SESSION
        test_role: ROLE_SCOUT_OBSERVER
        test_context: Observador qualificado iniciando sessão de codificação de partida.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_UNQUALIFIED_SCOUT_OPEN_SESSION
        test_role: ROLE_SCOUT_OBSERVER
        test_context: Operador reprovado em teste teórico/erros críticos tentando abrir sessão de scout.
        expected_result: EXPECT_DENY

  - permission_id: PERM_SCOUT_INSERT_POSSESSIONS
    resource_id: RES_TABLE_POSSESSIONS
    role_id: ROLE_SCOUT_OBSERVER
    operation: INSERT
    required_grant: GRANT SELECT, INSERT, UPDATE ON public.possessions TO role_scout_observer
    row_scope: scout_session_id IN (SELECT id FROM public.scout_sessions WHERE observer_id = auth.uid() AND session_status = 'EM_ANDAMENTO')
    columns:
      - id
      - scout_session_id
      - match_id
      - attacking_team_id
      - possession_number
      - start_timecode
      - end_timecode
      - outcome
    conditions: Delimitação operacional de sequências de posse de bola (UNT-003) em sessão ativa.
    rule_ids:
      - UNT-003
    evidence_ref_ids:
      - EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003
    planned_tests:
      - test_id: TEST_POS_SCOUT_RECORD_POSSESSION
        test_role: ROLE_SCOUT_OBSERVER
        test_context: Registro do início e fim de posse de bola na partida atribuída.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_SCOUT_RECORD_POSSESSION_CLOSED_SESSION
        test_role: ROLE_SCOUT_OBSERVER
        test_context: Tentativa de inserir posse em sessão já finalizada.
        expected_result: EXPECT_DENY

  - permission_id: PERM_SCOUT_INSERT_BOUS
    resource_id: RES_TABLE_BOUS
    role_id: ROLE_SCOUT_OBSERVER
    operation: INSERT
    required_grant: GRANT SELECT, INSERT, UPDATE ON public.bous TO role_scout_observer
    row_scope: possession_id IN (SELECT id FROM public.possessions WHERE scout_session_id IN (SELECT id FROM public.scout_sessions WHERE observer_id = auth.uid() AND session_status = 'EM_ANDAMENTO'))
    columns:
      - id
      - possession_id
      - bou_number
      - offensive_system
      - tactical_procedure
      - start_timecode
      - end_timecode
    conditions: Codificação da Unidade Básica de Ataque posicional organizada (UNT-004).
    rule_ids:
      - UNT-004
    evidence_ref_ids:
      - EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_004
      - EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_001
    planned_tests:
      - test_id: TEST_POS_SCOUT_RECORD_BOU
        test_role: ROLE_SCOUT_OBSERVER
        test_context: Codificador registrando BOU de ataque posicional em sistema 3:1.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_SCOUT_RECORD_BOU_UNAUTHORIZED_MATCH
        test_role: ROLE_SCOUT_OBSERVER
        test_context: Codificador tentando incluir BOU em partida sem atribuição de sessão.
        expected_result: EXPECT_DENY

  - permission_id: PERM_SCOUT_INSERT_TACTICAL_EVENTS
    resource_id: RES_TABLE_TACTICAL_EVENTS
    role_id: ROLE_SCOUT_OBSERVER
    operation: INSERT
    required_grant: GRANT SELECT, INSERT, UPDATE ON public.tactical_events TO role_scout_observer
    row_scope: match_id IN (SELECT match_id FROM public.scout_sessions WHERE observer_id = auth.uid() AND session_status = 'EM_ANDAMENTO')
    columns:
      - id
      - match_id
      - possession_id
      - bou_id
      - event_type
      - player_id
      - timecode
    conditions: Registro de eventos táticos de quadra por observador com qualificação ativa.
    rule_ids:
      - CON-006
    evidence_ref_ids:
      - EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009
    planned_tests:
      - test_id: TEST_POS_SCOUT_INSERT_TACTICAL_EVENT
        test_role: ROLE_SCOUT_OBSERVER
        test_context: Observador qualificado inserindo evento de falta técnica em sessão ativa.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_SCOUT_INSERT_TACTICAL_EVENT_WRONG_SESSION
        test_role: ROLE_SCOUT_OBSERVER
        test_context: Observador tentando gravar evento tático com match_id divergente da sessão aberta.
        expected_result: EXPECT_DENY

  - permission_id: PERM_SCOUT_INSERT_FINALIZATIONS
    resource_id: RES_TABLE_FINALIZATIONS
    role_id: ROLE_SCOUT_OBSERVER
    operation: INSERT
    required_grant: GRANT SELECT, INSERT, UPDATE ON public.finalizations TO role_scout_observer
    row_scope: match_id IN (SELECT match_id FROM public.scout_sessions WHERE observer_id = auth.uid() AND session_status = 'EM_ANDAMENTO')
    columns:
      - id
      - match_id
      - bou_id
      - shooter_id
      - shot_type
      - shot_zone
      - outcome
      - point_value
      - timecode
    conditions: Codificação de arremessos categorizados por zona (ZE, ZCE, ZCD, ZD) e valoração de pontuação (1 vs 2 pontos).
    rule_ids:
      - TAX-006
    evidence_ref_ids:
      - EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_006
      - EVID_IHF_RULES_2026_EN_006
      - EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_005
    planned_tests:
      - test_id: TEST_POS_SCOUT_RECORD_SPIN_SHOT_FINALIZATION
        test_role: ROLE_SCOUT_OBSERVER
        test_context: Registro de finalização em giro 360° valendo 2 pontos na zona ZCE.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_SCOUT_RECORD_INVALID_ZONE_FINALIZATION
        test_role: ROLE_SCOUT_OBSERVER
        test_context: Inserção com zona tática fora da geometria estipulada de 4 faixas de 3m.
        expected_result: EXPECT_DENY

  - permission_id: PERM_SCOUT_INSERT_GOALKEEPER_ACTIONS
    resource_id: RES_TABLE_GOALKEEPER_ACTIONS
    role_id: ROLE_SCOUT_OBSERVER
    operation: INSERT
    required_grant: GRANT SELECT, INSERT, UPDATE ON public.goalkeeper_actions TO role_scout_observer
    row_scope: match_id IN (SELECT match_id FROM public.scout_sessions WHERE observer_id = auth.uid() AND session_status = 'EM_ANDAMENTO')
    columns:
      - id
      - match_id
      - finalization_id
      - goalkeeper_id
      - action_stage
      - action_type
      - result
      - timecode
    conditions: Mapeamento dos tempos de defesa da goleira (estágios T1 a T4) vinculados à finalização.
    rule_ids: []
    evidence_ref_ids:
      - EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_008
      - EVID_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0_003
    planned_tests:
      - test_id: TEST_POS_SCOUT_RECORD_GOALKEEPER_DEFENSE
        test_role: ROLE_SCOUT_OBSERVER
        test_context: Codificação de defesa efetuada no estágio T3 em arremesso de in-flight.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_SCOUT_RECORD_GOALKEEPER_ACTION_INACTIVE_SESSION
        test_role: ROLE_SCOUT_OBSERVER
        test_context: Tentativa de codificar ação de goleira sem sessão de scout em andamento.
        expected_result: EXPECT_DENY

  - permission_id: PERM_SCOUT_INSERT_SCOUT_OBSERVATIONS
    resource_id: RES_TABLE_SCOUT_OBSERVATIONS
    role_id: ROLE_SCOUT_OBSERVER
    operation: INSERT
    required_grant: GRANT SELECT, INSERT, UPDATE ON public.scout_observations TO role_scout_observer
    row_scope: scout_session_id IN (SELECT id FROM public.scout_sessions WHERE observer_id = auth.uid() AND session_status = 'EM_ANDAMENTO')
    columns:
      - id
      - scout_session_id
      - match_id
      - observation_text
      - timecode
      - created_at
    conditions: Inserção de notas qualitativas e observações contextuais do codificador.
    rule_ids: []
    evidence_ref_ids:
      - EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001
    planned_tests:
      - test_id: TEST_POS_SCOUT_ADD_OBSERVATION_NOTE
        test_role: ROLE_SCOUT_OBSERVER
        test_context: Adição de nota explicativa sobre parada de arbitragem.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_SCOUT_ADD_OBSERVATION_OTHER_SESSION
        test_role: ROLE_SCOUT_OBSERVER
        test_context: Tentativa de registrar observação em sessão de outro operador.
        expected_result: EXPECT_DENY

  - permission_id: PERM_SCOUT_INSERT_VIDEO_TIMECODES
    resource_id: RES_TABLE_VIDEO_TIMECODES
    role_id: ROLE_SCOUT_OBSERVER
    operation: INSERT
    required_grant: GRANT SELECT, INSERT, UPDATE ON public.video_timecodes TO role_scout_observer
    row_scope: match_id IN (SELECT match_id FROM public.scout_sessions WHERE observer_id = auth.uid() AND session_status = 'EM_ANDAMENTO')
    columns:
      - id
      - match_id
      - event_id
      - video_url
      - timecode_start
      - timecode_end
      - frame_number
    conditions: Sincronização de trechos e timecodes de transmissão/vídeo com os eventos da partida.
    rule_ids: []
    evidence_ref_ids:
      - EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001
    planned_tests:
      - test_id: TEST_POS_SCOUT_LINK_VIDEO_TIMECODE
        test_role: ROLE_SCOUT_OBSERVER
        test_context: Vinculação de timecode de vídeo ao gol de Shoot-out.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_SCOUT_DELETE_VIDEO_TIMECODES
        test_role: ROLE_SCOUT_OBSERVER
        test_context: Tentativa de exclusão em lote de registros de timecode de vídeo.
        expected_result: EXPECT_DENY

  - permission_id: PERM_STEWARD_ALL_OBSERVER_QUALIFICATIONS
    resource_id: RES_TABLE_OBSERVER_QUALIFICATIONS
    role_id: ROLE_GOVERNANCE_STEWARD
    operation: SELECT
    required_grant: GRANT SELECT, INSERT, UPDATE ON public.observer_qualifications TO role_governance_steward
    row_scope: true
    columns:
      - id
      - observer_id
      - evaluation_date
      - theoretical_score
      - critical_errors_count
      - qualification_status
    conditions: Gestão de autorizações e auditoria do cumprimento do protocolo CON-006 (90%+ acerto, 0 erro crítico).
    rule_ids:
      - CON-006
    evidence_ref_ids:
      - EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009
    planned_tests:
      - test_id: TEST_POS_STEWARD_MANAGE_QUALIFICATIONS
        test_role: ROLE_GOVERNANCE_STEWARD
        test_context: Steward cadastrando resultado de teste de qualificação de observador.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_SCOUT_WRITE_OWN_QUALIFICATION
        test_role: ROLE_SCOUT_OBSERVER
        test_context: Observador tentando alterar seu próprio status de qualificação para aprovado.
        expected_result: EXPECT_DENY

  - permission_id: PERM_STEWARD_ALL_REFEREE_ASSIGNMENTS
    resource_id: RES_TABLE_REFEREE_ASSIGNMENTS
    role_id: ROLE_GOVERNANCE_STEWARD
    operation: SELECT
    required_grant: GRANT SELECT, INSERT, UPDATE, DELETE ON public.referee_assignments TO role_governance_steward
    row_scope: true
    columns:
      - id
      - match_id
      - referee_a_id
      - referee_b_id
      - delegate_a_id
      - delegate_b_id
      - secretary_id
      - timekeeper_id
    conditions: Manutenção e registro da equipe sextet de arbitragem oficial por partida.
    rule_ids: []
    evidence_ref_ids:
      - EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_003
    planned_tests:
      - test_id: TEST_POS_STEWARD_MANAGE_REFEREE_ASSIGNMENT
        test_role: ROLE_GOVERNANCE_STEWARD
        test_context: Homologação da escala de 6 oficiais de arbitragem para a partida final.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_COACH_MANAGE_REFEREE_ASSIGNMENT
        test_role: ROLE_COACH
        test_context: Treinador tentando alterar a escala de árbitros e delegados.
        expected_result: EXPECT_DENY

  - permission_id: PERM_STEWARD_ALL_RANKING_ELIGIBILITY
    resource_id: RES_TABLE_RANKING_ELIGIBILITY
    role_id: ROLE_GOVERNANCE_STEWARD
    operation: SELECT
    required_grant: GRANT SELECT, INSERT, UPDATE, DELETE ON public.ranking_eligibility TO role_governance_steward
    row_scope: true
    columns:
      - id
      - stage_id
      - team_id
      - eligibility_status
      - exception_note
    conditions: Configuração de exceções regulamentares de elegibilidade no circuito (ex.: exceção Campinas/SP).
    rule_ids: []
    evidence_ref_ids:
      - EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_008
    planned_tests:
      - test_id: TEST_POS_STEWARD_SET_RANKING_ELIGIBILITY
        test_role: ROLE_GOVERNANCE_STEWARD
        test_context: Steward definindo status de inelegibilidade por exceção de convidado extra-estadual.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_ANONYMOUS_SET_RANKING_ELIGIBILITY
        test_role: ROLE_ANONYMOUS
        test_context: Tentativa de alteração de regras de elegibilidade por visitante.
        expected_result: EXPECT_DENY

  - permission_id: PERM_STEWARD_ALL_SCORING_RULES
    resource_id: RES_TABLE_SCORING_RULES
    role_id: ROLE_GOVERNANCE_STEWARD
    operation: SELECT
    required_grant: GRANT SELECT, INSERT, UPDATE, DELETE ON public.scoring_rules TO role_governance_steward
    row_scope: true
    columns:
      - id
      - competition_id
      - position
      - points_awarded
      - is_stale
    conditions: Gestão da tabela canônica de pontuação por colocação (SGATE-0023 / DEC-DATA-042).
    rule_ids:
      - SGATE-0023
      - DEC-DATA-042
    evidence_ref_ids:
      - EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_006
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_027
    planned_tests:
      - test_id: TEST_POS_STEWARD_MANAGE_SCORING_RULES
        test_role: ROLE_GOVERNANCE_STEWARD
        test_context: Atualização da tabela de pontos da 1ª à 7ª posições para a temporada 2026.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_COACH_UPDATE_SCORING_RULES
        test_role: ROLE_COACH
        test_context: Treinador tentando alterar a tabela de pontuação do campeonato.
        expected_result: EXPECT_DENY

  - permission_id: PERM_STEWARD_SELECT_SCHEMA_MIGRATIONS
    resource_id: RES_TABLE_SCHEMA_MIGRATIONS
    role_id: ROLE_GOVERNANCE_STEWARD
    operation: SELECT
    required_grant: GRANT SELECT ON public.schema_migrations TO role_governance_steward
    row_scope: true
    columns:
      - version
      - inserted_at
    conditions: Auditoria de versão de esquema DDL aplicada no banco de dados.
    rule_ids: []
    evidence_ref_ids:
      - EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_001
    planned_tests:
      - test_id: TEST_POS_STEWARD_READ_SCHEMA_MIGRATIONS
        test_role: ROLE_GOVERNANCE_STEWARD
        test_context: Consulta de histórico de migrações por administrador de dados.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_ANONYMOUS_READ_SCHEMA_MIGRATIONS
        test_role: ROLE_ANONYMOUS
        test_context: Tentativa de leitura de controle interno de migrações por usuário anônimo.
        expected_result: EXPECT_DENY

  - permission_id: PERM_STEWARD_ALL_AUDIT_LOGS
    resource_id: RES_TABLE_AUDIT_LOGS
    role_id: ROLE_GOVERNANCE_STEWARD
    operation: SELECT
    required_grant: GRANT SELECT ON public.audit_logs TO role_governance_steward
    row_scope: true
    columns:
      - id
      - table_name
      - operation
      - performed_by
      - performed_at
      - payload
    conditions: Acesso pleno às trilhas imutáveis de auditoria do sistema em sessão global autenticada.
    rule_ids: []
    evidence_ref_ids:
      - EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_001
      - EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_002
    planned_tests:
      - test_id: TEST_POS_STEWARD_READ_AUDIT_LOGS
        test_role: ROLE_GOVERNANCE_STEWARD
        test_context: Steward inspecionando logs de auditoria de alterações de segurança.
        expected_result: EXPECT_ALLOW
      - test_id: TEST_NEG_COACH_READ_AUDIT_LOGS
        test_role: ROLE_COACH
        test_context: Treinador tentando ler registros restritos na tabela de audit_logs.
        expected_result: EXPECT_DENY

default_policy:
  anonymous: DENY
  authenticated_without_role: DENY
  cross_tenant: DENY
  privileged_service_role: SERVER_ONLY
  client_authorization_from_user_metadata: DENY
  scope_enforcement_policy: Escopos de equipe, competição e partida dependem obrigatoriamente de associação confiável no banco de dados (DATABASE_MEMBERSHIP) verificada via tabelas relacionais de vínculo ou JWT claims do app_metadata. Quaisquer identificadores fornecidos livremente pelo cliente em payloads de requisição ou user_metadata são sumariamente rejeitados para prevenir privilege escalation.

open_issues:
  - issue_id: ISSUE_REQUISITOS_ACESSO_STAGE_06
    status: ABERTA
    description: Acompanhamento e manutenção da proposta de requisitos de acesso do Estágio 06. Este documento estabelece a especificação declarativa de requisitos de acesso e políticas RLS/RBAC propostas, mas não altera diretamente a matriz histórica nem encerra formalmente a pendência.
    affected_ids:
      - SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919
    impact: A definição de permissões opera como especificação declarativa até homologação final e aplicação das migrações físicas pelo operador.
    owner: OPERADOR

  - issue_id: ISSUE_SOURCE_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919_001
    status: ABERTA
    description: O documento histórico 07-matriz-rbac-e-politicas-rls (SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919) omitiu a declaração formal de instruções CREATE POLICY para a maioria das tabelas habilitadas na Seção 1 (ex.: matches, bous, tactical_events, convocations, calendar_events), exigindo a recomposição integral das políticas RLS no presente modelo.
    affected_ids:
      - SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919
    impact: Inconsistência entre a lista de tabelas habilitadas para RLS no documento histórico e os scripts DDL de criação de políticas.
    owner: OPERADOR

  - issue_id: ISSUE_DERIVED_SECURITY_DECISIONS_HOMOLOGATION
    status: ABERTA
    description: Necessidade de homologação humana formal para permissões e políticas de escopo baseadas exclusivamente em decisões derivadas de arquitetura de segurança IAM/RLS onde não há rule_id direto apontado no catálogo de regras invariantes.
    affected_ids:
      - SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7
    impact: Regras derivadas de segurança operam sob presunção técnica até chancela final do Steward de Governança de Dados.
    owner: OPERADOR