# Stop Gate Físico — PARTIDAS_SCOUT_ANALISE_TATICA (v0.1.0)

criteria:
  - id: "CRT-001"
    description: "Verificação da integridade e promoção do Manifesto de Fontes (SOURCE_MANIFEST v0.1.0)"
    status: "PASS"
    deadline: "ANTES_DO_STOP_GATE_FISICO"
    evidence_refs:
      - "SOURCE_MANIFEST_v0.1.0"
    notes: "Manifesto de fontes devidamente promovido, validado e rastreável na versão v0.1.0."

  - id: "CRT-002"
    description: "Verificação da integridade e promoção do Registro Semântico (SEMANTIC_REGISTRY v0.1.0)"
    status: "PASS"
    deadline: "ANTES_DO_STOP_GATE_FISICO"
    evidence_refs:
      - "SEMANTIC_REGISTRY_v0.1.0"
    notes: "Registro semântico canônico promovido e reconciliado na versão v0.1.0."

  - id: "CRT-003"
    description: "Retropropagação das 9 formalizações condicionais e 2 divergências reconciliadas do estágio 05 para o Modelo Conceitual (CONCEPTUAL_MODEL v0.1.1)"
    status: "BLOCKED"
    deadline: "ANTES_DO_STOP_GATE_FISICO"
    evidence_refs:
      - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_001"
    notes: "Pendência não superada: as 9 formalizações condicionais e 2 divergências registradas na revisão do estágio 05 ainda não foram retropropagadas para a especificação do modelo conceitual."

  - id: "CRT-004"
    description: "Retropropagação das 9 formalizações condicionais e 2 divergências reconciliadas do estágio 05 para o Modelo Lógico (LOGICAL_MODEL v0.1.0)"
    status: "BLOCKED"
    deadline: "ANTES_DO_STOP_GATE_FISICO"
    evidence_refs:
      - "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_001"
    notes: "Pendência não superada: retropropagação obrigatória dos débitos formais do estágio 05 para o modelo lógico pendente antes da liberação da camada física."

  - id: "CRT-005"
    description: "Validação e consolidação do Dicionário de Dados Canônico (DATA_DICTIONARY v0.1.0)"
    status: "PASS"
    deadline: "ANTES_DO_STOP_GATE_FISICO"
    evidence_refs:
      - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_001"
      - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_002"
    notes: "Dicionário de dados canônico promovido, validado e reconciliado na versão v0.1.0."

  - id: "CRT-006"
    description: "Preservação da imutabilidade da Matriz de Rastreabilidade (TRACEABILITY_MATRIX v0.1.0)"
    status: "PASS"
    deadline: "ANTES_DO_STOP_GATE_FISICO"
    evidence_refs:
      - "TRACEABILITY_MATRIX_v0.1.0"
      - "ACCESS_REQUIREMENTS_v0.1.0"
    notes: "Matriz de rastreabilidade mantida imutável e auditável em v0.1.0, com respaldo do estágio 06 para superação de requisitos de acesso."

  - id: "CRT-007"
    description: "Superação das pendências de Requisitos de Acesso pela promoção formal do artefato ACCESS_REQUIREMENTS v0.1.0"
    status: "PASS"
    deadline: "ANTES_DO_STOP_GATE_FISICO"
    evidence_refs:
      - "ACCESS_REQUIREMENTS_v0.1.0"
    notes: "Requisitos de acesso formalizados e promovidos no estágio 06 (v0.1.0), superando plenamente as pendências apontadas no estágio 05."

recommendation: "BLOCKED"

recommended_scope: []

excluded_scope:
  - "Tabela física public.athletes"
  - "Tabela física public.secondary_positions"
  - "Tabela física public.calendar_events"
  - "Tabela física public.competitions"
  - "Tabela física public.convocations"
  - "Tabela física public.convocation_athletes"
  - "Tabela física public.matches"
  - "Tabela física public.match_appearances"
  - "Tabela física public.possessions"
  - "Tabela física public.bous"
  - "Tabela física public.tactical_events"
  - "Tabela física public.finalizations"
  - "Tabela física public.goalkeeper_actions"
  - "Tabela física public.factual_presences"
  - "Tabela física public.presence_proposals"
  - "Tabela física public.availability_declarations"
  - "Tabela física public.carioca_2026_scoring_rules"
  - "Tabela física public.final_ranking_eligibilities"
  - "Tabela física public.training_sessions"
  - "Tabela física public.schema_migrations"
  - "ENUM físico enum_court_position"
  - "ENUM físico enum_tactical_function"
  - "ENUM físico enum_tactical_system"
  - "ENUM físico enum_tactical_role"
  - "ENUM físico enum_event_type"
  - "ENUM físico enum_competition_type"
  - "ENUM físico enum_match_status"
  - "ENUM físico enum_participation_status"
  - "ENUM físico enum_presence_status"
  - "AUTOCONSULTA_ATLETA: Consulta direta do atleta por autoatendimento, vedada por ausência de mecanismo de vinculação forte e confiável de identidade."
  - "23 recursos do catálogo de dados pertencentes às classes não-PÚBLICO, mantendo liberação exclusiva para Data API apenas aos 9 recursos autorizados no estágio 06."
  - "SESSION_SEGMENT: Objeto descontinuado/bloqueado contra materialização física."
  - "PLANNED_TRAINING_LOAD: Objeto descontinuado/bloqueado contra materialização física."
  - "Tabelas históricas e registros não reconciliados do CEPRAEA (ex.: DB_PRESENCA_LEGADO)."

restrictions:
  - "Proibição absoluta de geração automática ou inferência de dados para preencher lacunas históricas de placares detalhados de shoot-out e parciais de etapas (ex.: partida J71 e 4ª Etapa Estadual). As lacunas devem ser isoladas, bloqueando a carga dos dados afetados sem impedir a criação do schema."
  - "Exigência estrita de implementação de RBAC e RLS no PostgreSQL/Supabase com atribuição de papéis auditável, obrigatoriedade de vigência/temporalidade e proibição absoluta de autoatribuição de papéis."
  - "Separação obrigatória de papéis para a revisão de scout (REVISOR_SCOUT), sendo categoricamente vedada a autorrevisão pelo mesmo operador responsável pela codificação primária."
  - "Proibição estrita de conversão, geração ou execução de scripts SQL DDL na presente etapa."

required_human_decisions:
  - "Homologação do manifesto do Stop Gate pela autoridade de governança para alteração formal do status de PROPOSTO para APROVADO."
  - "Gate humano de confirmação do treinador: exigência de ação explícita e autenticada para validação de presenças factuais e convocações, gravando compulsoriamente confirmed_by e confirmed_at."
  - "Aprovação humana e definição do mecanismo de vinculação forte de identidade para autorização futura da liberação de consulta por autoatendimento do atleta (AUTOCONSULTA_ATLETA)."

open_issues:
  - id: "ISSUE_LACUNA_PLACAR_SHOOTOUT_E_ETAPAS"
    status: "ABERTA"
    question: "Como completar a lacuna de documentação de placar detalhado de shoot-out em jogos específicos da Etapa Final (ex.: J71) e parciais de sets da 4ª Etapa Estadual?"
    affected_ids:
      - "PLACAR_JOGO"
      - "EVOLUCAO_DO_PLACAR"
      - "PARTIDA"
      - "SHOOT_OUT"
    impact: "Incompletude no histórico cronológico e auditável do placar em partidas passadas específicas sem registro de vídeo em arquivo."
    required_evidence: "Súmula física impressa assinada ou boletim impresso oficial expedido pela FHERJ/CBHb."
    owner: "OPERADOR"

  - id: "ISSUE_QUALIFICACAO_OBSERVADOR_SCOUT"
    status: "ABERTA"
    question: "Como operacionalizar e registrar o procedimento formal de qualificação teórica do observador de scout conforme CON-006?"
    affected_ids:
      - "CON-006"
      - "OBSERVADOR_SCOUT"
    impact: "Impossibilidade de liberação de novos observadores para coletas de dados de scout em partidas de produção."
    required_evidence: "Registro assinado do teste teórico com aproveitamento mínimo de 90% (18/20 acertos) e zero erro crítico."
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