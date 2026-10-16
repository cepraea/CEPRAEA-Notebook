# Registro Semântico Suplementar — Partidas, Scout e Análise Tática
schema_version: "1.1"
document:
  id: "PARTIDAS_SCOUT_ANALISE_TATICA_SUPLEMENTO"
  artifact_kind: "SEMANTIC_REGISTRY"
  title: "Registro Semântico Suplementar — Partidas, Scout e Análise Tática"
  version: "0.1.0"
  status: "PROPOSTO"
  run_id: "RUN_20261014_PARTIDAS_SCOUT_001"
  domain_id: "PARTIDAS_SCOUT_ANALISE_TATICA"
  notebook_id: "93446a17-55bf-4cd8-b9f9-18c52c8f4c1d"
  generated_at: null
  supersedes: null
  input_artifacts: []
semantic_registry:
  concepts:
    - id: "COMPETICAO"
      preferred_term: "Competição"
      canonical_name: "COMPETICAO"
      classification: "ENTITY"
      definition: "Evento ou torneio esportivo estruturado sob regulamento oficial (ex.: Circuito Brasileiro, Circuito Carioca / Campeonato Estadual), agregando etapas, divisões e partidas."
      valid_context:
        - "Gestão de calendário e registro de torneios estaduais e nacionais de handebol de praia"
      invalid_context:
        - "Treinos internos e sessões recreativas sem vinculação a federações"
      inclusions:
        - "Etapas classificatórias"
        - "Fases finais de circuitos oficiais"
        - "Copas regionais"
      exclusions:
        - "Partidas amistosas não oficiais"
        - "Atividades de preparação física isoladas"
      synonyms:
        - "Torneio"
        - "Campeonato"
        - "Circuito Esportivo"
      related_concept_ids:
        - "PARTIDA"
        - "EQUIPE"
      allowed_values: []
      temporality: "PERSISTENTE"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_001"
        - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_002"

    - id: "PAPEL_ESPORTIVO_OPERACIONAL"
      preferred_term: "Papel Esportivo ou Operacional"
      canonical_name: "PAPEL_ESPORTIVO_OPERACIONAL"
      classification: "ROLE"
      definition: "Função formal atribuída a um indivíduo na comissão técnica, arbitragem ou organização em súmula de jogo (ex.: Dirigente, Técnico, Oficial de Arbitragem, Delegado, Secretário, Cronometrista)."
      valid_context:
        - "Preenchimento de súmula oficial e credenciamento de membros da comissão técnica ou arbitragem"
      invalid_context:
        - "Atuação tática de atletas em quadra durante o jogo"
      inclusions:
        - "Oficiais de arbitragem"
        - "Delegados de mesa"
        - "Técnicos e auxiliares"
        - "Médicos e fisioterapeutas de equipe"
      exclusions:
        - "Atletas participantes da partida"
      synonyms:
        - "Função na Súmula"
        - "Cargo Operacional"
      related_concept_ids:
        - "PARTIDA"
        - "EQUIPE"
      allowed_values:
        - "TECNICO"
        - "AUXILIAR_TECNICO"
        - "MEDICO"
        - "FISIOTERAPEUTA"
        - "DELEGADO_A"
        - "DELEGADO_B"
        - "SECRETARIO"
        - "CRONOMETRISTA"
        - "OFICIAL_ARBITRAGEM"
      temporality: "TRANSITORIO_POR_PARTIDA"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_003"
        - "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_005"

    - id: "SEGMENTO_OBSERVADO"
      preferred_term: "Segmento Observado"
      canonical_name: "SEGMENTO_OBSERVADO"
      classification: "VALUE_OBJECT"
      definition: "Unidade de recorte temporal ou de vídeo correspondente a um período contínuo ou fatiado de observação e codificação para análise tática e scout."
      valid_context:
        - "Análise audiovisual e fatiamento de mídias de partida no protocolo de scout"
      invalid_context:
        - "Divisão regulamentar do jogo em sets ou Golden Goal"
      inclusions:
        - "Trechos de vídeo contínuos"
        - "Recortes analíticos de ataques posicionados"
      exclusions:
        - "Períodos oficiais de jogo definidos pela regra (PERIODO_SET)"
      synonyms:
        - "Clipe de Vídeo"
        - "Trecho Analítico"
      related_concept_ids:
        - "TIMECODE"
        - "TRECHO_OBSERVADO"
        - "MIDIA_VIDEO"
      allowed_values: []
      temporality: "PERSISTENTE"
      privacy_classification: "INTERNO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - "EVID_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_004"

    - id: "PLACAR_JOGO"
      preferred_term: "Placar do Jogo e do Set"
      canonical_name: "PLACAR_JOGO"
      classification: "ATTRIBUTE"
      definition: "Contagem acumulada de pontos em cada set individual e total de sets conquistados por cada equipe durante a partida."
      valid_context:
        - "Acompanhamento do resultado da partida e registro oficial em súmula"
      invalid_context:
        - "Contagem estatística individual de scout desvinculada do resultado do jogo"
      inclusions:
        - "Pontos do Set 1"
        - "Pontos do Set 2"
        - "Pontos do Shoot-out"
        - "Placar consolidado em sets"
      exclusions:
        - "Estatísticas de arremessos fora do alvo"
      synonyms:
        - "Pontuação da Partida"
        - "Resultado Parcial"
      related_concept_ids:
        - "PARTIDA"
        - "PERIODO_SET"
        - "EVENTO_DE_PONTUACAO"
      allowed_values: []
      temporality: "MUTAVEL_DURANTE_PARTIDA"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_002"
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_026"

    - id: "ESTADO_DO_PLACAR"
      preferred_term: "Estado do Placar"
      canonical_name: "ESTADO_DO_PLACAR"
      classification: "STATE"
      definition: "Situação relacional momentânea da pontuação de uma equipe em relação à adversária no instante da ação (Empatado, Favorável/Vencendo, Desfavorável/Perdendo)."
      valid_context:
        - "Análise situacional contextual de tomada de decisão e eficácia tática"
      invalid_context:
        - "Resultado final homologado pós-partida"
      inclusions:
        - "Placar Favorável"
        - "Placar Desfavorável"
        - "Placar Empatado"
      exclusions:
        - "Saldo de gols acumulado do campeonato"
      synonyms:
        - "Contexto do Placar"
        - "Condição Momentânea de Pontuação"
      related_concept_ids:
        - "PLACAR_JOGO"
        - "EVOLUCAO_DO_PLACAR"
      allowed_values:
        - "EMPATADO"
        - "FAVORAVEL"
        - "DESFAVORAVEL"
      temporality: "MUTAVEL_DURANTE_PARTIDA"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56_004"
        - "EVID_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_007"

    - id: "EVOLUCAO_DO_PLACAR"
      preferred_term: "Evolução do Placar"
      canonical_name: "EVOLUCAO_DO_PLACAR"
      classification: "SNAPSHOT"
      definition: "Sequência cronológica auditável das alterações da pontuação e alternância de liderança ao longo dos períodos e sets de uma partida."
      valid_context:
        - "Análise de dinâmica temporal de partida e momentos críticos de virada"
      invalid_context:
        - "Estatística agregada de fim de torneio"
      inclusions:
        - "Histórico ponto a ponto"
        - "Registros de marcação por timecode"
      exclusions:
        - "Estatísticas individuais desvinculadas do tempo de jogo"
      synonyms:
        - "Cronologia da Pontuação"
        - "Histórico do Placar"
      related_concept_ids:
        - "PLACAR_JOGO"
        - "EVENTO_DE_PONTUACAO"
        - "TIMECODE"
      allowed_values: []
      temporality: "HISTORICO_ACUMULATIVO"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_002"
        - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_009"

    - id: "EVENTO_DE_PONTUACAO"
      preferred_term: "Evento de Pontuação"
      canonical_name: "EVENTO_DE_PONTUACAO"
      classification: "EVENT"
      definition: "Ocorrência discreta de validação de gol pela arbitragem que resulta na atribuição de 1 ou 2 pontos à equipe atacante ou adversária (incluindo gols contra de 1 ponto)."
      valid_context:
        - "Registro em tempo real de gols validados e atualização do placar"
      invalid_context:
        - "Finalizações anuladas pela arbitragem ou arremessos fora do alvo"
      inclusions:
        - "Gol simples de 1 ponto"
        - "Gol duplo de 2 pontos"
        - "Gol contra valendo 1 ponto"
      exclusions:
        - "Arremessos defendidos sem ultrapassagem da linha de gol"
      synonyms:
        - "Gol Validado"
        - "Acontecimento de Gol"
      related_concept_ids:
        - "GOL_SIMPLES"
        - "GOL_DUPLO"
        - "PLACAR_JOGO"
      allowed_values:
        - "PONTUACAO_SIMPLES"
        - "PONTUACAO_DUPLA"
      temporality: "DISCRETO_INSTANTANEO"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_006"
        - "EVID_IHF_RULES_2026_EN_007"
        - "EVID_IHF_RULES_2026_EN_008"
        - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_001"
        - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_003"

    - id: "PUNICAO_DISCIPLINAR"
      preferred_term: "Punição Disciplinar"
      canonical_name: "PUNICAO_DISCIPLINAR"
      classification: "EVENT"
      definition: "Sanção formal aplicada pela arbitragem por infração às regras ou conduta antidesportiva, englobando advertência, exclusão temporária, desqualificação direta ou cartão azul acompanhado de relatório."
      valid_context:
        - "Registro de ocorrências disciplinares em partida e relatório de arbitragem"
      invalid_context:
        - "Faltas táticas ordinárias sem sanção pessoal disciplinar"
      inclusions:
        - "Advertência"
        - "Exclusão temporária"
        - "Desqualificação direta"
        - "Cartão Azul acompanhado de relatório"
      exclusions:
        - "Tiro livre ordinário concedido ao adversário"
      synonyms:
        - "Sanção Disciplinar"
        - "Penalização Pessoal"
      related_concept_ids:
        - "EXCLUSAO_DISCIPLINAR"
        - "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
        - "CARTAO_AZUL_SUSPENSAO"
      allowed_values:
        - "ADVERTENCIA"
        - "EXCLUSAO_TEMPORARIA"
        - "DESQUALIFICACAO_DIRETA"
        - "CARTAO_AZUL"
      temporality: "DISCRETO_INSTANTANEO"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_014"
        - "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_015"

    - id: "CONSEQUENCIA_DISCIPLINAR"
      preferred_term: "Consequência Disciplinar"
      canonical_name: "CONSEQUENCIA_DISCIPLINAR"
      classification: "STATE"
      definition: "Efeito operacional, tático ou esportivo decorrente da aplicação de uma punição disciplinar (ex.: redução numérica em quadra, suspensão automática mínima de 1 partida por desqualificação direta/cartão azul, concessão de tiro de 6m)."
      valid_context:
        - "Controle de atletas elegíveis, obrigações de substituição e suspensões administrativas"
      invalid_context:
        - "Instruções táticas internas da comissão técnica"
      inclusions:
        - "Saída de atleta de quadra por exclusão"
        - "Redução numérica de equipe"
        - "Suspensão automática de 1 partida"
        - "Concessão de tiro de 6 metros"
      exclusions:
        - "Substituições táticas regulares"
      synonyms:
        - "Efeito da Sanção"
        - "Medida Disciplinar Decorrente"
      related_concept_ids:
        - "PUNICAO_DISCIPLINAR"
        - "TIRO_SEIS_METROS"
      allowed_values:
        - "REDUCAO_NUMERICA_QUADRA"
        - "SUSPENSAO_PROXIMA_PARTIDA"
        - "CONCESSAO_TIRO_SIX_METROS"
      temporality: "DURADOURO_DETERMINADO"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_008"
        - "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_015"
        - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_017"

    - id: "FASE_OFENSIVA"
      preferred_term: "Fase Ofensiva"
      canonical_name: "FASE_OFENSIVA"
      classification: "STATE"
      definition: "Macrosubdivisão tática do jogo em que uma equipe possui o controle funcional ou legal da bola, englobando o Ataque Posicional (AP) e a Transição Ofensiva (TO)."
      valid_context:
        - "Classificação tática sistemática de ações de jogo no scout"
      invalid_context:
        - "Momentos em que a equipe não possui a posse da bola"
      inclusions:
        - "Ataque Posicional (AP)"
        - "Transição Ofensiva (TO)"
        - "Ataque em Superioridade com Especialista"
      exclusions:
        - "Defesa Posicional (DP)"
        - "Transição Defensiva (TD)"
      synonyms:
        - "Momento de Ataque"
        - "Organização Ofensiva"
      related_concept_ids:
        - "FASE_TATICA"
        - "POSSE_DE_BOLA"
        - "UNIDADE_BASICA_ATAQUE_BOU"
      allowed_values:
        - "TRANSICAO_OFENSIVA"
        - "ATAQUE_POSICIONAL"
      temporality: "MUTAVEL_DURANTE_PARTIDA"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_005"
        - "EVID_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2_001"

    - id: "FASE_DEFENSIVA"
      preferred_term: "Fase Defensiva"
      canonical_name: "FASE_DEFENSIVA"
      classification: "STATE"
      definition: "Macrosubdivisão tática do jogo em que uma equipe não possui a posse da bola, englobando a Defesa Posicional (DP) e a Transição Defensiva (TD)."
      valid_context:
        - "Classificação tática sistemática de comportamento defensivo e bloqueios"
      invalid_context:
        - "Momentos de controle funcional da bola pela equipe em ataque"
      inclusions:
        - "Defesa Posicional (DP)"
        - "Transição Defensiva (TD)"
        - "Recuo defensivo rápido"
      exclusions:
        - "Ataque Posicional (AP)"
        - "Transição Ofensiva (TO)"
      synonyms:
        - "Momento de Defesa"
        - "Organização Defensiva"
      related_concept_ids:
        - "FASE_TATICA"
        - "SISTEMA_DEFENSIVO"
      allowed_values:
        - "TRANSICAO_DEFENSIVA"
        - "DEFESA_POSICIONAL"
      temporality: "MUTAVEL_DURANTE_PARTIDA"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_005"
        - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_001"

    - id: "SISTEMA_DEFENSIVO"
      preferred_term: "Sistema Defensivo"
      canonical_name: "SISTEMA_DEFENSIVO"
      classification: "CATALOG"
      definition: "Arranjo geométrico, atitude tática e distribuição funcional dos defensores na quadra (ex.: 3:0, 2:1 no meio/lateral, 1:2, linha avançada a 7 metros, atitude reativa ou proativa)."
      valid_context:
        - "Mapeamento tático de organização defensiva e categorização no scout"
      invalid_context:
        - "Sistemas de posicionamento do ataque posicionado"
      inclusions:
        - "Sistema 3:0"
        - "Sistema 2:1 (central ou lateral)"
        - "Sistema 1:2"
        - "Linha avançada a 7 metros"
        - "Atitude Reativa ou Proativa"
      exclusions:
        - "Sistemas ofensivos (3:1, 2:2, 4:0)"
      synonyms:
        - "Esquema Defensivo"
        - "Formação Defensiva"
      related_concept_ids:
        - "SISTEMA_TATICO"
        - "FASE_DEFENSIVA"
      allowed_values:
        - "SIS_3_0"
        - "SIS_2_1_CENTRAL"
        - "SIS_2_1_LATERAL"
        - "SIS_1_2"
        - "SIS_AVANCADO_7M"
        - "SIS_REATIVO"
        - "SIS_PROATIVO"
      temporality: "MUTAVEL_DURANTE_PARTIDA"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_005"
        - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_006"
        - "EVID_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94_002"

    - id: "ACAO_DA_GOLEIRA"
      preferred_term: "Ação da Goleira"
      canonical_name: "ACAO_DA_GOLEIRA"
      classification: "EVENT"
      definition: "Conduta motora e tática específica executada pela atleta na posição de goleira na defesa ou transição (ex.: defesa/parada, counter-spin, counter-fly, passe de transição T4, arremesso direto ao gol, intervenção no shoot-out)."
      valid_context:
        - "Registro de eficácia de goleira e análise de tempos defensivos (T1 a T4)"
      invalid_context:
        - "Ações executadas por atletas de linha fora da posição de goleira/especialista"
      inclusions:
        - "Defesa/Parada (PAR)"
        - "Ação de Counter-spin"
        - "Ação de Counter-fly"
        - "Passe de transição para contra-ataque (T4)"
        - "Arremesso direto da área de gol"
        - "Intervenção em Shoot-out"
      exclusions:
        - "Arremesso de atleta de linha comum"
      synonyms:
        - "Intervenção da Goleira"
        - "Atuação da Guarda-Redes"
      related_concept_ids:
        - "GOLEIRA_POSICAO"
        - "RESULTADO_DA_ACAO"
      allowed_values:
        - "DEFESA_PARADA"
        - "DEFESA_COUNTER_SPIN"
        - "DEFESA_COUNTER_FLY"
        - "PASSE_TRANSICAO_T4"
        - "ARREMESSO_DIRETO_GOLEIRA"
        - "INTERVENCAO_SHOOTOUT"
      temporality: "DISCRETO_INSTANTANEO"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94_003"
        - "EVID_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_005"
        - "EVID_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0_003"

    - id: "ACAO_OBSERVADA"
      preferred_term: "Ação Observada"
      canonical_name: "ACAO_OBSERVADA"
      classification: "EVENT"
      definition: "Qualquer comportamento técnico-tático individual ou coletivo passível de identificação e codificação objetiva em vídeo durante uma partida."
      valid_context:
        - "Coleta de dados observacionais sistemáticos no protocolo de scout"
      invalid_context:
        - "Julgamentos inferenciais não observáveis visualmente na mídia primária"
      inclusions:
        - "Arremessos (spin, in-flight, simples)"
        - "Passes e recepções"
        - "Bloqueios e desarmes"
        - "Faltas cometidas e sofridas"
      exclusions:
        - "Avaliações de intenção ou estado psicológico interno"
      synonyms:
        - "Comportamento Motor Observado"
        - "Ação Tática Discreta"
      related_concept_ids:
        - "EVENTO_SCOUT"
        - "RESULTADO_DA_ACAO"
      allowed_values: []
      temporality: "DISCRETO_INSTANTANEO"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_004"

    - id: "RESULTADO_DA_ACAO"
      preferred_term: "Resultado da Ação"
      canonical_name: "RESULTADO_DA_ACAO"
      classification: "VALUE_OBJECT"
      definition: "Desfecho imediato codificado decorrente de uma ação observada durante a partida (ex.: gol, defesa, erro técnico, falta sofrida, bola fora)."
      valid_context:
        - "Qualificação do desfecho de finalizações e procedimentos táticos no scout"
      invalid_context:
        - "Resultado final da partida ou do campeonato"
      inclusions:
        - "Gol"
        - "Defesa da Goleira"
        - "Bola Fora / Trave"
        - "Erro Técnico / Erro de Passe"
        - "Falta Sofrida / Tiro de 6m"
      exclusions:
        - "Placar consolidado do jogo"
      synonyms:
        - "Desfecho da Ação"
        - "Resultado Imediato"
      related_concept_ids:
        - "ACAO_OBSERVADA"
        - "EVENTO_SCOUT"
      allowed_values:
        - "GOL"
        - "DEFESA"
        - "FORA"
        - "TRAVE"
        - "ERRO_TECNICO"
        - "FALTA_SOFRIDA"
      temporality: "DISCRETO_INSTANTANEO"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_008"
        - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_001"

    - id: "OBSERVACAO_DE_SCOUT"
      preferred_term: "Observação de Scout"
      canonical_name: "OBSERVACAO_DE_SCOUT"
      classification: "EVENT"
      definition: "Ato discreto de registro e codificação efetuado pelo analista observador atribuindo atributos e categorias a um evento ou segmento de jogo."
      valid_context:
        - "Processamento de dados primários (P1) e inserção de eventos em software de scout"
      invalid_context:
        - "Registros administrativos fora do escopo de análise de vídeo"
      inclusions:
        - "Marcação de timecode de evento"
        - "Atribuição de zona analítica"
        - "Registro de tipo de arremesso"
      exclusions:
        - "Preenchimento de súmula impressa oficial"
      synonyms:
        - "Codificação de Scout"
        - "Registro do Observador"
      related_concept_ids:
        - "PROTOCOLO_SCOUT"
        - "ANALISTA_OBSERVADOR"
        - "EVENTO_SCOUT"
      allowed_values: []
      temporality: "DISCRETO_INSTANTANEO"
      privacy_classification: "INTERNO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"

    - id: "VERSAO_PROTOCOLO_SCOUT"
      preferred_term: "Versão do Protocolo de Scout"
      canonical_name: "VERSAO_PROTOCOLO_SCOUT"
      classification: "VALUE_OBJECT"
      definition: "Identificador formal de revisão do conjunto de diretrizes, variáveis e regras de codificação vigente no projeto de scout (ex.: v0.9.2)."
      valid_context:
        - "Garantia de rastreabilidade metodológica e reprodutibilidade dos dados de scout"
      invalid_context:
        - "Versão do livro de regras da IHF"
      inclusions:
        - "Número de versão (v0.9.2)"
        - "Data de congelamento do protocolo"
      exclusions:
        - "Edição de regulamento de campeonato"
      synonyms:
        - "Versão Metodológica"
        - "Revisão do Protocolo"
      related_concept_ids:
        - "PROTOCOLO_SCOUT"
        - "OBSERVACAO_DE_SCOUT"
      allowed_values: []
      temporality: "PERSISTENTE"
      privacy_classification: "INTERNO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"

    - id: "REVISAO_DA_OBSERVACAO"
      preferred_term: "Revisão da Observação"
      canonical_name: "REVISAO_DA_OBSERVACAO"
      classification: "EVENT"
      definition: "Procedimento sistemático de auditoria ou segunda checagem da codificação efetuada para verificação de confiabilidade intra ou inter-observador (índices Kappa)."
      valid_context:
        - "Controle de qualidade de dados de scout e qualificação de observadores"
      invalid_context:
        - "Revisão de lances por arbitragem de vídeo durante a partida"
      inclusions:
        - "Auditoria por segundo observador"
        - "Revisão de conflitos de codificação"
        - "Cálculo de concordância Kappa"
      exclusions:
        - "Recurso administrativo de partida"
      synonyms:
        - "Auditoria de Scout"
        - "Checagem de Confiabilidade"
      related_concept_ids:
        - "CONFIABILIDADE_OBSERVADOR"
        - "ESTADO_DE_REVISAO"
      allowed_values: []
      temporality: "DISCRETO_INSTANTANEO"
      privacy_classification: "INTERNO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
        - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_007"

    - id: "ESTADO_DE_REVISAO"
      preferred_term: "Estado de Revisão"
      canonical_name: "ESTADO_DE_REVISAO"
      classification: "STATE"
      definition: "Situação do fluxo de homologação e validação da observação de scout (PENDENTE, APROVADO, REJEITADO, EM_AUDITORIA)."
      valid_context:
        - "Gerenciamento do ciclo de vida dos registros de scout antes da promoção à base consolidada"
      invalid_context:
        - "Status de aprovação de regulamento esportivo"
      inclusions:
        - "PENDENTE"
        - "APROVADO"
        - "REJEITADO"
        - "EM_AUDITORIA"
      exclusions:
        - "Status de presença factual"
      synonyms:
        - "Status de Validação"
        - "Situação da Codificação"
      related_concept_ids:
        - "REVISAO_DA_OBSERVACAO"
        - "OBSERVACAO_DE_SCOUT"
      allowed_values:
        - "PENDENTE"
        - "APROVADO"
        - "REJEITADO"
        - "EM_AUDITORIA"
      temporality: "MUTAVEL_DURANTE_PROCESSO"
      privacy_classification: "INTERNO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_006"
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_022"

    - id: "MIDIA_VIDEO"
      preferred_term: "Mídia ou Vídeo"
      canonical_name: "MIDIA_VIDEO"
      classification: "ENTITY"
      definition: "Arquivo de gravação audiovisual ou sinal de transmissão (broadcast P0) utilizado como fonte primária para a extração visual de eventos de scout."
      valid_context:
        - "Gerenciamento de acervo audiovisual e sincronização de timecode"
      invalid_context:
        - "Transmissões de rádio ou relatos textuais sem suporte de imagem"
      inclusions:
        - "Vídeo broadcast P0"
        - "Gravação tática em câmara alta"
        - "Mídia de partida gravada"
      exclusions:
        - "Súmula em papel ou boletim PDF"
      synonyms:
        - "Arquivo de Vídeo"
        - "Mídia Primária P0"
      related_concept_ids:
        - "TIMECODE"
        - "SEGMENTO_OBSERVADO"
      allowed_values: []
      temporality: "PERSISTENTE"
      privacy_classification: "INTERNO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"

    - id: "PROVENIENCIA_OBSERVACAO"
      preferred_term: "Proveniência da Observação ou Evento"
      canonical_name: "PROVENIENCIA_OBSERVACAO"
      classification: "ATTRIBUTE"
      definition: "Atributo de metadado que indica a origem da extração do dado (ex.: codificação humana primária P1, extração automatizada, súmula oficial)."
      valid_context:
        - "Auditoria de dados, linhagem de informação e classificação epistemológica"
      invalid_context:
        - "Local geográfico de realização da partida"
      inclusions:
        - "Codificação Humana P1"
        - "Súmula Oficial"
        - "IA / Extração Automatizada"
      exclusions:
        - "Origem de nascimento do atleta"
      synonyms:
        - "Origem do Dado"
        - "Linhagem da Codificação"
      related_concept_ids:
        - "OBSERVACAO_DE_SCOUT"
        - "EVENTO_SCOUT"
      allowed_values:
        - "CODIFICACAO_HUMANA_P1"
        - "SUMULA_OFICIAL"
        - "EXTRACAO_AUTOMATIZADA"
      temporality: "IMMUTABLE"
      privacy_classification: "INTERNO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
        - "EVID_CEPRAEA_DATABASE_CCB2A718_001"

  rules:
    - id: "RN_SEMANTICA_GOLEIRA"
      name: "Regra de Governança Semântica da Goleira"
      rule_type: "CLASSIFICATION"
      subject_ids:
        - "GOLEIRA_POSICAO"
        - "ACAO_DA_GOLEIRA"
      statement: "GOLEIRA é categoricamente uma posição e pertence taxiologicamente à função DEFESA, sendo proibida a sua reclassificação como uma função tática isolada ou separada no sistema."
      conditions:
        - "Sempre que for atribuída a posição GOLEIRA a uma atleta"
      exceptions: []
      valid_context:
        - "Modelagem conceitual, lógica e cadastro tático de atletas"
      invalid_context:
        - "Criação de taxonomias legadas desalinhadas com a decisão humana de governança"
      implementation_targets:
        - "Modelo Conceitual"
        - "Modelo Lógico"
        - "Dicionário de Dados"
      verification_test_ids:
        - "TEST_SEMANTICS_GOALKEEPER_ROLE"
      evidence_ref_ids:
        - "EVID_CEPRAEA_DATABASE_CCB2A718_004"
        - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_007"
      valid_from: "2026-08-10"
      valid_to: null
      status: "PROPOSTO"

    - id: "RN_TETO_PARTICIPANTES_SUMULA"
      name: "Regra do Teto de Participantes por Súmula"
      rule_type: "OBLIGATION"
      subject_ids:
        - "PARTIDA"
        - "ATLETA"
        - "PAPEL_ESPORTIVO_OPERACIONAL"
      statement: "Cada equipe pode relacionar na súmula individual de jogo no máximo 10 atletas e 4 dirigentes, sendo permitido no máximo 4 atletas simultâneas na quadra de jogo (3 de linha e 1 goleira)."
      conditions:
        - "No momento da emissão da súmula de partida e início do jogo"
      exceptions: []
      valid_context:
        - "Validação de escalação e registros oficiais de partida"
      invalid_context:
        - "Lista larga de inscrição do campeonato (até 18 ou 20 atletas)"
      implementation_targets:
        - "Sistema de Registro de Partidas"
        - "Validação de Súmula"
      verification_test_ids:
        - "TEST_MATCH_ROSTER_LIMITS"
      evidence_ref_ids:
        - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_007"
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_024"
      valid_from: "2026-03-01"
      valid_to: null
      status: "PROPOSTO"

    - id: "RN_REJEICAO_VARIAVEIS_INFERENCIAIS"
      name: "Regra de Rejeição de Variáveis Inferenciais na Codificação Primária"
      rule_type: "PROHIBITION"
      subject_ids:
        - "OBSERVACAO_DE_SCOUT"
        - "ACAO_OBSERVADA"
        - "PROVENIENCIA_OBSERVACAO"
      statement: "É proibido registrar na camada de observação primária (P1) variáveis que exijam julgamentos subjetivos ou inferências não sustentáveis exclusivamente pela mídia de vídeo."
      conditions:
        - "Durante o processo de codificação primária de vídeo de scout"
      exceptions: []
      valid_context:
        - "Protocolo metodológico de scout e fichas de codificação P1"
      invalid_context:
        - "Análises subjetivas qualitativas de comissão técnica fora do banco de scout"
      implementation_targets:
        - "Protocolo de Scout"
        - "Interface do Analista Observador"
      verification_test_ids:
        - "TEST_REJECT_INFERENTIAL_VARIABLES"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
      valid_from: "2026-08-26"
      valid_to: null
      status: "PROPOSTO"

    - id: "RN_PASSIVO_QUATRO_PASSES"
      name: "Regra do Limite de Passes no Jogo Passivo"
      rule_type: "CONDITION"
      subject_ids:
        - "FASE_OFENSIVA"
        - "ACAO_OBSERVADA"
      statement: "Exibido o sinal de advertência de jogo passivo pela arbitragem (Gesto nº 16), a equipe atacante dispõe de no máximo quatro passes para tentar um arremesso a gol antes que a posse seja revertida."
      conditions:
        - "Sinalização de advertência de jogo passivo ativa pela arbitragem"
      exceptions: []
      valid_context:
        - "Regulamento oficial IHF 2026 e codificação de scout"
      invalid_context:
        - "Ataques normais sem sinalização de jogo passivo"
      implementation_targets:
        - "Motor de Regras de Jogo"
        - "Protocolo de Scout"
      verification_test_ids:
        - "TEST_PASSIVE_PLAY_FOUR_PASSES"
      evidence_ref_ids:
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_004"
      valid_from: "2026-04-01"
      valid_to: null
      status: "PROPOSTO"

    - id: "RN_SANCAO_FINAL_15_SEGUNDOS"
      name: "Regra de Obstrução Severa nos Últimos 15 Segundos e Gol de Ouro"
      rule_type: "OBLIGATION"
      subject_ids:
        - "PUNICAO_DISCIPLINAR"
        - "CONSEQUENCIA_DISCIPLINAR"
        - "TIRO_SEIS_METROS"
      statement: "Nos últimos 15 segundos de qualquer período ou durante o Gol de Ouro, impedir a execução de tiro ou cometer falta grave para impedir gol acarreta desqualificação direta do infrator e concessão de tiro de 6 metros para os adversários."
      conditions:
        - "Tempo de jogo nos últimos 15 segundos de um período ou durante a prorrogação por Gol de Ouro"
      exceptions: []
      valid_context:
        - "Aplicação das Regras da IHF 2026 pela arbitragem e registro disciplinar de partida"
      invalid_context:
        - "Faltas ordinárias ocorridas fora do trecho dos últimos 15 segundos ou Gol de Ouro"
      implementation_targets:
        - "Súmula Eletrônica"
        - "Motor de Validação Disciplinar"
      verification_test_ids:
        - "TEST_LAST_15_SECONDS_SANCTION"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_012"
        - "EVID_IHF_RULES_2026_EN_013"
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_005"
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_008"
      valid_from: "2026-04-01"
      valid_to: null
      status: "PROPOSTO"

    - id: "RN_PROTECAO_CABECA_GOLEIRA"
      name: "Regra de Proteção à Cabeça da Goleira e Proibição de Simulação"
      rule_type: "OBLIGATION"
      subject_ids:
        - "GOLEIRA_POSICAO"
        - "PUNICAO_DISCIPLINAR"
        - "ACAO_DA_GOLEIRA"
      statement: "É obrigatória a aplicação de suspensão/exclusão ao arremessador sem marcação em situação de jogo aberto que atinja diretamente a cabeça da goleira no primeiro contato. Caso a goleira simule lesão por contato no peito/corpo, a própria goleira deve ser sancionada."
      conditions:
        - "Arremessador sem marcação em jogo aberto ou simulação de lesão na área de gol"
      exceptions:
        - "Arremessos com desvio prévio no defensor antes de atingir a cabeça"
      valid_context:
        - "Aplicação das atualizações regulamentares IHF 2026 em quadra e no scout disciplinar"
      invalid_context:
        - "Disputas com bloqueio tático direto ou contato acidental indireto"
      implementation_targets:
        - "Motor de Regras de Jogo"
        - "Módulo de Registro Disciplinar"
      verification_test_ids:
        - "TEST_GOALKEEPER_HEAD_HIT_AND_SIMULATION"
      evidence_ref_ids:
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_009"
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_010"
      valid_from: "2026-04-01"
      valid_to: null
      status: "PROPOSTO"

    - id: "RN_PROIBICAO_RETARDO_REPETIDO"
      name: "Regra de Proibição de Retardo Repetido do Reinício"
      rule_type: "PROHIBITION"
      subject_ids:
        - "PUNICAO_DISCIPLINAR"
        - "ACAO_OBSERVADA"
      statement: "É proibido a uma equipe retardar repetidamente a execução de tiros livres, tiros de lateral (throw-in) ou tiros de goleira (Rule 7:10), sob pena de sanção disciplinar e reversão de posse."
      conditions:
        - "Fase de reinício de jogo com retenção ou obstrução deliberada da bola"
      exceptions: []
      valid_context:
        - "Controle de tempo de jogo e aplicação de regras IHF 2026"
      invalid_context:
        - "Posicionamento tático regular sem conduta de retardo"
      implementation_targets:
        - "Súmula Eletrônica"
        - "Motor de Regras de Jogo"
      verification_test_ids:
        - "TEST_REPEATED_RESTART_DELAY"
      evidence_ref_ids:
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_003"
      valid_from: "2026-04-01"
      valid_to: null
      status: "PROPOSTO"

    - id: "RN_PRAZO_INSCRICAO_ATLETA_72H"
      name: "Regra do Prazo Limite de Inscrição de Atletas (72 Horas)"
      rule_type: "CONDITION"
      subject_ids:
        - "COMPETICAO"
        - "PAPEL_ESPORTIVO_OPERACIONAL"
      statement: "Para que um novo atleta atue de forma elegível na etapa classificatória do campeonato estadual (FHERJ), a inscrição formal deve ser realizada com antecedência mínima de 72 horas (3 dias) antes da partida na rodada."
      conditions:
        - "Inscrição de novos atletas para a etapa classificatória do circuito estadual"
      exceptions: []
      valid_context:
        - "Validação administrativa de elegibilidade de atletas em súmula"
      invalid_context:
        - "Inscrições mantidas na lista larga nacional (CBHb) enviada no início do ano"
      implementation_targets:
        - "Sistema de Inscrição e Credenciamento"
        - "Validador de Súmula"
      verification_test_ids:
        - "TEST_ATHLETE_REGISTRATION_72H_DEADLINE"
      evidence_ref_ids:
        - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_004"
      valid_from: "2026-03-01"
      valid_to: null
      status: "PROPOSTO"

    - id: "RN_REGRAS_EXECUCAO_TIRO_SEIS_METROS"
      name: "Regra Restritiva de Execução do Tiro de 6 Metros"
      rule_type: "OBLIGATION"
      subject_ids:
        - "EVENTO_DE_PONTUACAO"
        - "ACAO_OBSERVADA"
      statement: "A cobrança do tiro de 6 metros deve ser realizada como arremesso direto ao gol em até 3 segundos após o apito (14.5), mantendo defensores/goleira a no mínimo 1 metro de distância (14.8), sendo vedada a substituição da goleira após o executante estar pronto (14.9), pisar/ultrapassar a linha de 6 metros (14.6) ou tocar na bola antes que esta atinja a baliza/adversário (14.7)."
      conditions:
        - "Execução de tiro de 6 metros assinalado pela arbitragem"
      exceptions: []
      valid_context:
        - "Regulamentação e codificação visual de tiros de penalidade máxima"
      invalid_context:
        - "Tiros livres ordinários fora da marca de 6 metros"
      implementation_targets:
        - "Motor de Regras de Jogo"
        - "Protocolo de Scout"
      verification_test_ids:
        - "TEST_SIX_METRE_THROW_EXECUTION"
      evidence_ref_ids:
        - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_009"
        - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_010"
        - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_011"
        - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_012"
        - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_013"
      valid_from: "2026-03-01"
      valid_to: null
      status: "PROPOSTO"

  decisions: []

  open_issues:
    - id: "ISSUE_LACUNA_PLACAR_SHOOTOUT_E_ETAPAS"
      description: "Identificada ausência de documentação do placar detalhado de shoot-out em boletim oficial de partida específica (ex.: jogo J71 na Etapa Final) e pendências de dados de parciais de sets na 4ª Etapa Estadual."
      affected_ids:
        - "PLACAR_JOGO"
        - "EVOLUCAO_DO_PLACAR"
        - "PARTIDA"
      status: "ABERTA"
      evidence_ref_ids:
        - "EVID_CEPRAEA_DATABASE_CCB2A718_008"

    - id: "ISSUE_SOURCE_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E_002"
      description: "A versão de migração física 20261013000001 permanece sem confirmação de execução em ambiente de produção/staging, contendo instruções de rollback inativas por estarem em bloco de comentário SQL."
      affected_ids:
        - "PROVENIENCIA_OBSERVACAO"
      status: "ABERTA"
      evidence_ref_ids:
        - "SRC_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E"

    - id: "ISSUE_SOURCE_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919_001"
      description: "As tabelas de scout e análise tática (matches, match_appearances, possessions, bous, tactical_events, finalizations, goalkeeper_actions) possuem indicação de RLS habilitado na Seção 1, mas carecem de diretivas CREATE POLICY explicitamente declaradas."
      affected_ids:
        - "OBSERVACAO_DE_SCOUT"
        - "ESTADO_DE_REVISAO"
      status: "ABERTA"
      evidence_ref_ids:
        - "SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919"