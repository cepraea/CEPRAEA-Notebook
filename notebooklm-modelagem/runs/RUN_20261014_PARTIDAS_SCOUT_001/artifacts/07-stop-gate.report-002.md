# Diretrizes para Elaboração do Relatório do Stop Gate (Estágio 07) — 07-stop-gate-PARTIDAS_SCOUT_ANALISE_TATICA.yaml

criteria:
  - id: "GATE_01"
    description: "Validação de Fontes e Rastreabilidade: Avaliação do alinhamento e atualização das fontes primárias e normativas, incluindo a antecipação da vigência das regras da IHF de Beach Handball para 01/04/2026."
    status: "PASS"
    evidence_refs:
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_001"
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_002"
      - "EVID_IHF_RULES_2026_EN_001"
    notes: "Linha de base normativa e regulamentar verificada. A antecipação da vigência das regras da IHF de Beach Handball para 01/04/2026 (conforme EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_002) foi integralmente reconciliada com o SOURCE_MANIFEST v0.1.0 e incorporada à arquitetura de dados promovida."

  - id: "GATE_02"
    description: "Reconciliação dos Modelos Conceitual v0.1.2 e Lógico v0.1.1: Verificação da retropropagação das 9 formalizações e 2 reconciliações do Estágio 05."
    status: "PASS"
    evidence_refs:
      - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_002"
      - "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_007"
    notes: "Retropropagação e reconciliação estrutural validadas com sucesso: (1) 7 relacionamentos conceituais específicos para FKs condicionais devidamente formalizados; (2) unicidade contextual de papel regulamentar e condição de mando assegurada; (3) alteração da cardinalidade para 0..N trechos por evento com remoção expressa da restrição UQ_TRECHO_EVENTO, viabilizando o rastreamento granular de timecode e segmentos táticos por evento sem violar restrições de unicidade em nível de banco de dados; (4) separação funcional e explícita entre CHK_INTERVALO_VIGENCIA_PARTICIPACAO (validação de limites temporais válidos: valid_from <= valid_to) e a restrição de exclusão candidata EXCL_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA (prevenção de sobreposição de intervalos de participação ativa de equipes em competições). Bloqueio de gate anterior totalmente removido."

  - id: "GATE_03"
    description: "Conformidade e Isolamento de Divergências no Dicionário v0.1.0: Análise do DATA_DICTIONARY v0.1.0 quanto a identificadores desatualizados e convergência com o Modelo Lógico v0.1.1."
    status: "PASS"
    evidence_refs:
      - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_002"
      - "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_007"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_001"
    notes: "Constatado que o DATA_DICTIONARY v0.1.0 antecede a reconciliação e ainda referencia os identificadores obsoletos UQ_TRECHO_EVENTO e CHK_VIGENCIA_PARTICIPACAO. A comparação rigorosa com o LOGICAL_MODEL v0.1.1 e a TRACEABILITY_MATRIX v0.1.0 confirma que esses IDs antigos não são implementáveis na arquitetura atual. No entanto, a divergência encontra-se estritamente isolada no artefato descritivo e não compromete a estrutura lógica nem a integridade do modelo. Emitido status PASS acompanhado da vinculação obrigatória da restrição RST_01."

  - id: "GATE_04"
    description: "Integridade de Dados e Lacuna de Placares Históricos: Avaliação da integridade dos fatos de partidas perante omissões documentadas de placares em registros operacionais."
    status: "PASS"
    evidence_refs:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_008"
    notes: "A omissão documentada de placares detalhados de shoot-out (ex.: partida J71 da Etapa Final) e de parciais de sets (ex.: 4ª Etapa Estadual) na base operacional SRC_CEPRAEA_DATABASE_CCB2A718 restringe isoladamente a carga e ingestão dos fatos de partidas afetados. É expressamente vedado o preenchimento dessas lacunas por inferência estatística ou estimativa. Emitido status PASS condicionado à limitação estrita do escopo de carga (RST_02)."

  - id: "GATE_05"
    description: "Segurança, Governança, Atribuição de Papéis e Revisão de Scout: Avaliação das políticas de auditoria, segregação de funções e controle de acesso."
    status: "PASS"
    evidence_refs:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_003"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_023"
    notes: "Requisitos formais de governança e auditoria validados: exigência de janelas de vigência e campos obrigatórios de auditoria (confirmed_by, confirmed_at), identificação explícita de responsável e proibição estrita de autoatribuição de papéis. Validada a obrigatoriedade da segregação de funções na revisão de scout tático, impondo a invariante de que o revisor deve ser distinto do analista original (reviser_id != analyst_id). Mantido o bloqueio da funcionalidade de autoconsulta por atletas enquanto não for estabelecido vínculo confiável de identidade."

  - id: "GATE_06"
    description: "Classificação de Acesso e Fronteira da Data API: Verificação da matriz de classificação de recursos para exposição via API."
    status: "PASS"
    evidence_refs:
      - "EVID_ACCESS_REQUIREMENTS_V010_PUBLIC_RESTRITO"
      - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_001"
    notes: "Confirmado com base no ACCESS_REQUIREMENTS v0.1.0 que estritamente os 9 recursos classificados na categoria PUBLICO são elegíveis para exposição pública via Data API. Todos os 23 recursos classificados nas categorias INTERNO ou RESTRITO permanecem estritamente fechados, protegidos por políticas de RLS e vedados para acesso externo."

  - id: "GATE_07"
    description: "Rastreabilidade Integrada e Cobertura do Escopo: Verificação do mapeamento completo de requisitos na TRACEABILITY_MATRIX v0.1.0."
    status: "PASS"
    evidence_refs:
      - "EVID_TRACEABILITY_MATRIX_V010"
    notes: "Rastreabilidade bidirecional e cobertura integral confirmadas: todos os requisitos operacionais, táticos e regulamentares da modalidade estão devidamente vinculados e mapeados para suas respectivas entidades e invariantes lógicas na TRACEABILITY_MATRIX v0.1.0."

recommendation: "READY_WITH_RESTRICTIONS"

recommended_scope:
  - "Estrutura regulamentar e tática oficial da IHF 2026 / FHERJ / CBHb."
  - "Entidade Lógica Reconciliada: Partidas (public.matches)."
  - "Entidade Lógica Reconciliada: Posses de Bola (public.possessions)."
  - "Entidade Lógica Reconciliada: Unidades Básicas de Ataque - BOUs (public.bous)."
  - "Entidade Lógica Reconciliada: Eventos Táticos (public.tactical_events)."
  - "Entidade Lógica Reconciliada: Finalizações (public.finalizations)."
  - "Entidade Lógica Reconciliada: Ações de Goleiro (public.goalkeeper_actions)."
  - "Entidade Lógica Reconciliada: Atribuições Táticas (public.tactical_assignments)."
  - "Entidade Lógica Reconciliada: Presenças Factuais Auditadas (public.factual_presences)."
  - "Exposição via Data API exclusivamente para os 9 recursos pertencentes à classe PUBLICO em ACCESS_REQUIREMENTS v0.1.0."

excluded_scope:
  - "Ingestão e carga analítica de fatos de partidas com placares parciais ou de shoot-out ausentes (ex.: J71 e 4ª Etapa) até homologação oficial via súmula física impressa ou boletim assinado."
  - "Funcionalidade de autoconsulta e autorrelato por perfil de atleta enquanto não for implantado mecanismo confiável de governança e vinculação de identidade."
  - "Inclusão ou exposição de qualquer um dos 23 recursos pertencentes às classes INTERNO ou RESTRITO na Data API."
  - "Geração física de código SQL/DDL, scripts de migração física e alteração de esquema no PostgreSQL nesta etapa (manutenção estrita do STOP GATE físico)."

restrictions:
  - id: "RST_01"
    description: "Divergência de IDs legados no Dicionário de Dados v0.1.0."
    impact: "Incapacidade e proibição de implementar as restrições obsoletas UQ_TRECHO_EVENTO e CHK_VIGENCIA_PARTICIPACAO citadas na versão desatualizada do dicionário de dados."
    mitigation: "Estabelecimento explícito do LOGICAL_MODEL v0.1.1 como a Única Fonte da Verdade (SSOT) autoritativa para especificações lógicas. Modeladores e engenheiros físicos a jusante devem ignorar os IDs antigos do DATA_DICTIONARY v0.1.0, prevalecendo a cardinalidade 0..N para trechos por evento e as invariantes declarativas definidas na versão v0.1.1."

  - id: "RST_02"
    description: "Carga Parcial de Fatos de Partida por omissão de placares históricos em registros operacionais."
    impact: "Impossibilidade de consolidação completa da linha do tempo e evolução de placar das partidas afetadas sem violação de integridade auditável."
    mitigation: "Bloqueio e isolamento estrito da carga analítica dos fatos de partidas incompletas. Proibição absoluta de preenchimento por inferência estatística, condicionando a liberação à validação por documento físico oficial (súmula ou boletim impresso expedido pela FHERJ/CBHb)."

  - id: "RST_03"
    description: "Proibição de Autoatribuição de Papéis e Autoconsulta."
    impact: "Risco de contaminação de dados por autoatribuição indevida de papéis e exposição não autorizada de informações de atletas."
    mitigation: "Manutenção do bloqueio lógico, de API e de interface para autoconsulta do perfil de atleta e aplicação da regra de segregação estrita na revisão de scout (reviser_id != analyst_id)."

required_human_decisions:
  - "Homologação formal da transição de status do artefato e aprovação do Stop Gate 07 pelo operador humano/steward."
  - "Deliberação e aceite formal das restrições ativas (RST_01, RST_02, RST_03) para autorizar a transição para a fase de modelagem física e geração de DDL."
  - "Validação final e autorização do uso da mídia P0 para início da coleta do piloto de scout técnico-tático."

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

  - id: "ISSUE_SOURCE_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E_002"
    status: "ABERTA"
    question: "A versão de migração 20261013000001 foi efetivamente aplicada no banco de dados de produção/staging ou permanece apenas como especificação de arquivo?"
    affected_ids:
      - "SRC_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E"
    impact: "A reconciliação semântica da fonte permanece parcial quanto ao estado do ambiente de implantação."
    required_evidence: "Resposta documentada com localização na fonte pertinente ou confirmação do operador."
    owner: "OPERADOR"

  - id: "ISSUE_SOURCE_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919_001"
    status: "ABERTA"
    question: "As tabelas secondary_positions, calendar_events, competitions, convocations, convocation_athletes, matches, match_appearances, possessions, bous, tactical_events, finalizations e goalkeeper_actions têm RLS habilitado na Seção 1, mas não possuem diretivas CREATE POLICY declaradas no documento."
    affected_ids:
      - "SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919"
    impact: "A reconciliação semântica da fonte permanece parcial quanto às políticas RLS de tabelas secundárias."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"