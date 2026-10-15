semantic_registry:
  concepts:
    - id: "PARTIDA"
      preferred_term: "Partida de Handebol de Praia"
      canonical_name: "Beach Handball Match"
      classification: "ENTIDADE_ESPORTIVA"
      definition: "Confronto esportivo regulamentado composto por dois períodos (sets) independentes de 10 minutos cada, podendo incluir Gol de Ouro para desempate de período e Shoot-out para desempate da partida."
      valid_context: "Competições oficiais de Handebol de Praia e sistemas de registro de scout/partidas."
      invalid_context: "Treinos sem estrutura regulamentar ou modalidades de handebol de quadra/indoor."
      inclusions:
        - "Períodos regulamentares (sets)"
        - "Prorrogação por Gol de Ouro"
        - "Disputa de Shoot-out"
      exclusions:
        - "Tempo extra continuado de 2x5 minutos típico do handebol de quadra"
      synonyms:
        - "Jogo"
        - "Match"
      related_concept_ids:
        - "PERIODO_SET"
        - "GOL_DE_OURO"
        - "SHOOT_OUT"
        - "EQUIPE"
      allowed_values: []
      temporality: "TEMPORAL"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_002"
        - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_012"
        - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_009"

    - id: "EQUIPE"
      preferred_term: "Equipe de Handebol de Praia"
      canonical_name: "Beach Handball Team"
      classification: "ENTIDADE_ESPORTIVA"
      definition: "Coletivo esportivo composto por até 10 atletas inscritos por partida (com o mínimo de 6 para início de jogo) e até 4 oficiais/dirigentes de comissão técnica."
      valid_context: "Inscrições oficiais em súmula, partidas e circuitos estaduais/nacionais."
      invalid_context: "Atletas avulsos sem vínculo de inscrição ou equipes de modalidades indoor."
      inclusions:
        - "Atletas de linha"
        - "Goleiros/Especialistas"
        - "Oficiais de comissão técnica (máximo 4 em súmula, 2 na área de substituição)"
      exclusions:
        - "Torcedores"
        - "Pessoas não inscritas na súmula oficial"
      synonyms:
        - "Time"
        - "Clube"
      related_concept_ids:
        - "ATLETA"
        - "PARTIDA"
      allowed_values: []
      temporality: "PERMANENTE"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_005"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_007"

    - id: "ATLETA"
      preferred_term: "Atleta"
      canonical_name: "Beach Handball Athlete"
      classification: "ENTIDADE_INDIVIDUAL"
      definition: "Pessoa física devidamente cadastrada e elegível para competir por uma equipe no domínio de Handebol de Praia, identificada por um ID canônico único."
      valid_context: "Sistemas de cadastro, convocações, atribuições táticas e scouts de jogo."
      invalid_context: "Membros exclusivamente administrativos ou comissão técnica sem registro de atleta."
      inclusions:
        - "Atletas federadas/confederadas ativas em cadastro"
      exclusions:
        - "Membros da comissão técnica"
        - "Oficiais de arbitragem"
      synonyms:
        - "Jogadora"
        - "Jogador"
      related_concept_ids:
        - "EQUIPE"
        - "GOLEIRA_POSICAO"
      allowed_values: []
      temporality: "PERMANENTE"
      privacy_classification: "DADO_PESSOAL"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_005"
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_005"

    - id: "GOLEIRA_POSICAO"
      preferred_term: "Posição de Goleira"
      canonical_name: "Goalkeeper Position"
      classification: "POSICAO_TATICA"
      definition: "Posição tática de atuação esportiva pertencente exclusivamente à função DEFESA. Não constitui uma função tática independente, sendo restrita à dimensão de posição tática de origem/atuação."
      valid_context: "Modelagem tática, escalações e estatísticas de jogo na fase defensiva."
      invalid_context: "Classificação da Goleira/Goleiro como Função Tática (TAX_FUNCTION) isolada."
      inclusions:
        - "Atuação na área de gol sob o sistema defensivo"
      exclusions:
        - "Função tática isolada da taxonomia primária"
      synonyms:
        - "Goleiro"
        - "Guardiana"
        - "GK"
      related_concept_ids:
        - "ATLETA"
        - "POSSE_DE_BOLA"
        - "SISTEMA_TATICO"
      allowed_values: []
      temporality: "TEMPORAL"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_CEPRAEA_DATABASE_CCB2A718_004"
        - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_007"

    - id: "PERIODO_SET"
      preferred_term: "Período / Set"
      canonical_name: "Match Period / Set"
      classification: "ESTRUTURA_TEMPORAL"
      definition: "Unidade temporal de jogo de duração exata de 10 minutos corridos, pontuada de forma totalmente independente em relação aos demais períodos da partida."
      valid_context: "Cronometragem e contagem de placar de partidas oficiais."
      invalid_context: "Tempos contínuos cumulativos sem pontuação zerada entre etapas."
      inclusions:
        - "Primeiro Período (Set 1)"
        - "Segundo Período (Set 2)"
      exclusions:
        - "Intervalo de 5 minutos entre períodos"
      synonyms:
        - "Set"
        - "Tempo regulamentar"
      related_concept_ids:
        - "PARTIDA"
        - "GOL_DE_OURO"
      allowed_values:
        - "SET_1"
        - "SET_2"
      temporality: "TEMPORAL"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_002"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_003"

    - id: "GOL_DE_OURO"
      preferred_term: "Gol de Ouro"
      canonical_name: "Golden Goal"
      classification: "REGRA_DESEMPATE"
      definition: "Mecanismo de desempate applied imediatamente quando um período de 10 minutos termina empatado, declarando-se vencedora do período a primeira equipe que marcar um gol."
      valid_context: "Encerramento de períodos regulamentares empatados."
      invalid_context: "Desempate do resultado final de partidas empatadas em sets (1x1)."
      inclusions:
        - "Reinício por bola ao alto (tiro de árbitro) para início do Gol de Ouro"
      exclusions:
        - "Prorrogação por tempo fixo"
      synonyms:
        - "Golden Goal"
      related_concept_ids:
        - "PERIODO_SET"
        - "PARTIDA"
      allowed_values: []
      temporality: "EVENTUAL"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_003"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_005"

    - id: "SHOOT_OUT"
      preferred_term: "Shoot-out"
      canonical_name: "Shoot-out"
      classification: "ESTRUTURA_DESEMPATE"
      definition: "Série de desempate da partida utilizada quando cada equipe vence um período (1x1). Consiste em 5 arremessos alternados no formato '1 contra o Goleiro'."
      valid_context: "Decisão do vencedor da partida em empate de sets."
      invalid_context: "Desempate dentro de um único período regulamentar."
      inclusions:
        - "Série inicial de 5 cobranças alternadas por equipe"
        - "Cobranças de morte súbita em caso de empate na primeira série"
      exclusions:
        - "Tiro livre direto após o apito final"
      synonyms:
        - "1 contra o Goleiro"
        - "Disputa de Shoot-out"
      related_concept_ids:
        - "PARTIDA"
        - "PERIODO_SET"
      allowed_values: []
      temporality: "EVENTUAL"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_009"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_012"
        - "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_012"

    - id: "GOL_SIMPLES"
      preferred_term: "Gol Simples"
      canonical_name: "One-Point Goal"
      classification: "EVENTO_PONTUACAO"
      definition: "Finalização válida com conversão de pontuação regular equivalente a 1 (um) ponto, efetuada por jogador de linha sem uso de técnicas espetaculares ou situações especiais."
      valid_context: "Pontuação em partidas de Handebol de Praia."
      invalid_context: "Gols marcados por goleiro/especialista, giros 360°, pontes aéreas ou tiros de 6 metros."
      inclusions:
        - "Arremesso convencional de jogador de linha"
        - "Tapas/empurrões na bola em jogadas aéreas"
        - "Gols contra efetuados por jogadores de linha"
      exclusions:
        - "Gols espetaculares de 2 pontos"
      synonyms:
        - "Gol de 1 Ponto"
        - "Regular Goal"
      related_concept_ids:
        - "GOL_DUPLO"
        - "PARTIDA"
      allowed_values: []
      temporality: "TEMPORAL"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_004"

    - id: "GOL_DUPLO"
      preferred_term: "Gol Duplo"
      canonical_name: "Two-Point Goal"
      classification: "EVENTO_PONTUACAO"
      definition: "Finalização válida com conversão de pontuação valorizada equivalente a 2 (dois) pontos, decorrente de técnicas criativas/espetaculares, arremesso de goleiro/especialista ou tiro de 6 metros."
      valid_context: "Pontuação em partidas de Handebol de Praia."
      invalid_context: "Arremessos simples de jogadores de linha."
      inclusions:
        - "Spin Shot (giro 360°)"
        - "In-flight Shot (ponte aérea)"
        - "Gol marcado por goleira/goleiro ou especialista"
        - "Gol resultante de tiro de 6 metros"
      exclusions:
        - "Arremesso simples de quadra"
      synonyms:
        - "Gol de 2 Pontos"
        - "Creative Goal"
      related_concept_ids:
        - "GOL_SIMPLES"
        - "SPIN_SHOT"
        - "IN_FLIGHT_SHOT"
        - "TIRO_SEIS_METROS"
      allowed_values: []
      temporality: "TEMPORAL"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_006"
        - "EVID_IHF_RULES_2026_EN_007"
        - "EVID_IHF_RULES_2026_EN_008"

    - id: "SPIN_SHOT"
      preferred_term: "Spin Shot"
      canonical_name: "Spin Shot (360° Turn)"
      classification: "TECNICA_FINALIZACAO"
      definition: "Técnica de arremesso valorizada em 2 pontos na qual o atleta realiza uma rotação completa do corpo (360°) no ar antes da liberação da bola, iniciando o salto com os pés direcionados ao gol."
      valid_context: "Ações de ataque posicional e finalizações."
      invalid_context: "Giros incompletos no solo ou sem fase aérea."
      inclusions:
        - "Giro 360° completo suspenso no ar com arremesso a gol"
      exclusions:
        - "Semi-giro com apoio dos pés na areia durante o lançamento"
      synonyms:
        - "Arremesso com giro"
        - "Giro 360"
      related_concept_ids:
        - "GOL_DUPLO"
        - "IN_FLIGHT_SHOT"
      allowed_values: []
      temporality: "TEMPORAL"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_005"

    - id: "IN_FLIGHT_SHOT"
      preferred_term: "In-flight Shot"
      canonical_name: "In-flight Shot (Fly)"
      classification: "TECNICA_FINALIZACAO"
      definition: "Técnica de arremesso valorizada em 2 pontos na qual o atleta domina a bola enquanto está suspenso no ar (recebimento do passe) e efetua o arremesso ao gol antes de tocar o solo."
      valid_context: "Ações de ataque posicional, transições e finalizações."
      invalid_context: "Ações em que o atleta segura a bola e pisa na areia antes de arremessar."
      inclusions:
        - "Recepção e arremesso sem qualquer contato do atleta com a areia durante a posse"
      exclusions:
        - "Tapas ou empurrões diretos na bola (que valem apenas 1 ponto)"
      synonyms:
        - "Ponte Aérea"
        - "Fly"
      related_concept_ids:
        - "GOL_DUPLO"
        - "SPIN_SHOT"
      allowed_values: []
      temporality: "TEMPORAL"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_014"
        - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_006"

    - id: "TIRO_SEIS_METROS"
      preferred_term: "Tiro de Seis Metros"
      canonical_name: "6-Metre Throw"
      classification: "SANCAO_TECNICA"
      definition: "Cobrança de arremesso direto concedida à equipe atacante quando uma clara ocasião de gol for destruída ilicitamente em qualquer parte da quadra por adversário ou oficial."
      valid_context: "Infrações graves que impedem oportunidade clara de gol."
      invalid_context: "Faltas ordinárias sem destruição de ocasião clara de gol."
      inclusions:
        - "Arremesso executado em até 3 segundos a 1 metro da linha de 6m"
        - "Gols valendo 2 pontos se convertidos"
      exclusions:
        - "Tiro livre ordinário"
      synonyms:
        - "Tiro de 6m"
        - "Penalidade máxima"
      related_concept_ids:
        - "GOL_DUPLO"
        - "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
      allowed_values: []
      temporality: "TEMPORAL"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_011"
        - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_002"

    - id: "EXCLUSAO_DISCIPLINAR"
      preferred_term: "Exclusão Disciplinar"
      canonical_name: "Suspension / Exclusion"
      classification: "SANCAO_DISCIPLINAR"
      definition: "Penalização disciplinar temporária aplicada a um atleta por infrações às regras, obrigando a equipe a atuar em inferioridade numérica até a mudança de posse de bola."
      valid_context: "Sanções disciplinares em quadra."
      invalid_context: "Advertências verbais sem penalização de saída de quadra."
      inclusions:
        - "Saída imediata do atleta da quadra até a troca de posse"
      exclusions:
        - "Desqualificação direta com cartão vermelho"
      synonyms:
        - "Exclusão temporária"
        - "Suspension"
      related_concept_ids:
        - "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
        - "CARTAO_AZUL_SUSPENSAO"
      allowed_values: []
      temporality: "TEMPORAL"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_014"

    - id: "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
      preferred_term: "Desqualificação por 2ª Exclusão"
      canonical_name: "Disqualification via Second Suspension"
      classification: "SANCAO_DISCIPLINAR"
      definition: "Afastamento definitivo do atleta da partida decorrente do acúmulo da segunda exclusão disciplinar no mesmo jogo."
      valid_context: "Acúmulo de sanções disciplinares individuais em uma partida."
      invalid_context: "Primeira exclusão disciplinar ou desqualificação direta com relatório."
      inclusions:
        - "Obrigação de deixar a área de jogo pelo restante da partida"
      exclusions:
        - "Suspensão automática compulsória para partidas subsequentes (salvo se acompanhada de Cartão Azul)"
      synonyms:
        - "Segunda Exclusão"
        - "Cartão Vermelho por acúmulo"
      related_concept_ids:
        - "EXCLUSAO_DISCIPLINAR"
        - "CARTAO_AZUL_SUSPENSAO"
      allowed_values: []
      temporality: "TEMPORAL"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_015"

    - id: "CARTAO_AZUL_SUSPENSAO"
      preferred_term: "Cartão Azul e Suspensão"
      canonical_name: "Blue Card Disqualification"
      classification: "SANCAO_DISCIPLINAR"
      definition: "Desqualificação direta acompanhada de relatório por escrito da arbitragem, que acarreta suspensão automática mínima de 1 (uma) partida para o atleta ou oficial infrator."
      valid_context: "Infrações disciplinares de gravidade extrema em partidas oficiais."
      invalid_context: "Desqualificações ordinárias por acúmulo de duas exclusões."
      inclusions:
        - "Exibição do Cartão Azul pela arbitragem"
        - "Registro em relatório oficial"
        - "Suspensão automática da partida subsequente"
      exclusions:
        - "Desqualificação sem relatório disciplinar"
      synonyms:
        - "Cartão Azul"
        - "Desqualificação com relatório"
      related_concept_ids:
        - "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
        - "EXCLUSAO_DISCIPLINAR"
      allowed_values: []
      temporality: "TEMPORAL"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_015"
        - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_017"

    - id: "POSSE_DE_BOLA"
      preferred_term: "Posse de Bola"
      canonical_name: "Ball Possession Unit (UNT-003)"
      classification: "UNIDADE_ANALITICA"
      definition: "Intervalo temporal de direito, controle funcional ou legal da bola por uma equipe. Inicia pelo controle inequívoco da bola ou por reinício de jogo e termina por gol, perda do controle ou evento regulamentar."
      valid_context: "Análise tática e codificação observacional de scout."
      invalid_context: "Meros toques involuntários ou desvios na bola sem controle funcional."
      inclusions:
        - "Posse de bola ativa em jogo vivo"
        - "Direito de retenção em reinício regulamentar"
      exclusions:
        - "Interrupções de jogo que mantêm a posse com a mesma equipe"
      synonyms:
        - "Posse"
        - "Possession Unit"
      related_concept_ids:
        - "UNIDADE_BASICA_ATAQUE_BOU"
        - "FASE_TATICA"
        - "PARTIDA"
      allowed_values: []
      temporality: "TEMPORAL"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"

    - id: "UNIDADE_BASICA_ATAQUE_BOU"
      preferred_term: "Unidade Básica de Ataque (BOU)"
      canonical_name: "Basic Attack Unit (BOU)"
      classification: "UNIDADE_ANALITICA"
      definition: "Intervalo delimitado do ataque posicional que se inicia quando a equipe atacante apresenta organização estável em postos ofensivos diante de uma defesa organizada, encerrando-se na perda de posse ou interrupção tática."
      valid_context: "Análise tática de ataque posicional."
      invalid_context: "Fases de transição ofensiva rápida ou contra-ataque desorganizado."
      inclusions:
        - "Ataque posicional 4x3 estruturado com especialista ou goleira"
      exclusions:
        - "Contra-ataque direto de área a área"
      synonyms:
        - "BOU"
        - "Basic Attack Unit"
      related_concept_ids:
        - "POSSE_DE_BOLA"
        - "FASE_TATICA"
        - "SISTEMA_TATICO"
        - "ZONA_ANALITICA_QUADRA"
      allowed_values: []
      temporality: "TEMPORAL"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_004"
        - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_001"

    - id: "FASE_TATICA"
      preferred_term: "Fase Tática"
      canonical_name: "Tactical Phase (TAX-001)"
      classification: "ESTRUTURA_TATICA"
      definition: "Classificação do momento do jogo em uma das quatro fases ordinárias da modalidade (Transição Ofensiva - TO, Ataque Posicional - AP, Transição Defensiva - TD, Defesa Posicional - DP) ou fase indeterminável (F_IND)."
      valid_context: "Codificação de scout, análise tática e categorização de vídeo."
      invalid_context: "Ações individuais fora da dinâmica coletiva do jogo."
      inclusions:
        - "Transição Ofensiva (TO)"
        - "Ataque Posicional (AP)"
        - "Transição Defensiva (TD)"
        - "Defesa Posicional (DP)"
        - "Fase Indeterminável (F_IND)"
      exclusions:
        - "Paradas de jogo com bola fora de jogo (out of play)"
      synonyms:
        - "Fase de Jogo"
        - "Tactical Phase"
      related_concept_ids:
        - "POSSE_DE_BOLA"
        - "UNIDADE_BASICA_ATAQUE_BOU"
        - "SISTEMA_TATICO"
      allowed_values:
        - "TO"
        - "AP"
        - "TD"
        - "DP"
        - "F_IND"
      temporality: "TEMPORAL"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_005"

    - id: "SISTEMA_TATICO"
      preferred_term: "Sistema Tático"
      canonical_name: "Tactical System"
      classification: "ESTRUTURA_TATICA"
      definition: "Disposição e organização espacial coletiva dos atletas na quadra para atuação na fase de ataque posicional (ex.: 3:1, 2:2, 4:0 em assimetria ofensiva com especialista) ou na fase defensiva (ex.: 3:0, 2:1, 1:2)."
      valid_context: "Análise tática coletiva de ataque posicional e organização defensiva."
      invalid_context: "Formações de modalidades indoor com 6 jogadoras de linha."
      inclusions:
        - "Sistemas ofensivos em superioridade numérica 4x3 (3:1, 2:2, 4:0)"
        - "Sistemas defensivos (3:0, 2:1, 1:2)"
      exclusions:
        - "Atuações individuais sem coordenação com a estrutura coletiva"
      synonyms:
        - "Sistema Ofensivo"
        - "Sistema Defensivo"
        - "Formação Tática"
      related_concept_ids:
        - "FASE_TATICA"
        - "UNIDADE_BASICA_ATAQUE_BOU"
        - "GOLEIRA_POSICAO"
      allowed_values:
        - "ATAQUE_3_1"
        - "ATAQUE_2_2"
        - "ATAQUE_4_0"
        - "DEFESA_3_0"
        - "DEFESA_2_1"
        - "DEFESA_1_2"
      temporality: "TEMPORAL"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2_005"
        - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_006"
        - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_007"
        - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_004"

    - id: "ZONA_ANALITICA_QUADRA"
      preferred_term: "Zona Analítica da Quadra"
      canonical_name: "Analytical Court Zone"
      classification: "TAXONOMIA_GEOMETRICA"
      definition: "Divisão geométrica analítica da largura regulamentar de 12 metros da quadra em 4 faixas quatrilaterais laterais analíticas de 3 metros cada: ZE (Esquerda), ZCE (Centro-Esquerda), ZCD (Centro-Direita) e ZD (Direita)."
      valid_context: "Registro de Scout e mapeamento da origem geométrica de finalizações."
      invalid_context: "Marcações físicas oficiais da quadra da IHF (linhas delimitadoras inexistentes)."
      inclusions:
        - "Divisões ZE, ZCE, ZCD, ZD para registro analítico de arremessos"
      exclusions:
        - "Marcações físicas regulamentares desenhadas na areia"
      synonyms:
        - "Faixa analítica"
        - "Zona de scout"
      related_concept_ids:
        - "UNIDADE_BASICA_ATAQUE_BOU"
        - "PROTOCOLO_SCOUT"
      allowed_values:
        - "ZE"
        - "ZCE"
        - "ZCD"
        - "ZD"
      temporality: "PERMANENTE"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_006"

    - id: "PROTOCOLO_SCOUT"
      preferred_term: "Protocolo de Scout"
      canonical_name: "Scout Protocol Methodology"
      classification: "METODOLOGIA_OBSERVACIONAL"
      definition: "Conjunto de regras canônicas e diretrizes de codificação observacional sistemática que governam o registro de eventos, tempos e conceitos táticos em vídeo de partidas de Handebol de Praia."
      valid_context: "Codificação de scout primário (P1) e revisão estatística."
      invalid_context: "Coleta automática de dados cinemáticos via GPS/LPS sem observação humana de vídeo."
      inclusions:
        - "Diretrizes metodológicas canônicas congeladas para análise de mídia"
      exclusions:
        - "Estatísticas subjetivas sem padronização de variáveis"
      synonyms:
        - "Protocolo Metodológico de Scout"
        - "SSOT de Scout"
      related_concept_ids:
        - "CONFIABILIDADE_OBSERVADOR"
        - "EVENTO_SCOUT"
        - "ANALISTA_OBSERVADOR"
        - "UNIDADE_BASICA_ATAQUE_BOU"
      allowed_values: []
      temporality: "PERMANENTE"
      privacy_classification: "USO_INTERNO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"

    - id: "CONFIABILIDADE_OBSERVADOR"
      preferred_term: "Confiabilidade do Observador"
      canonical_name: "Observer Reliability Standard"
      classification: "CRITERIO_QUALIFICACAO"
      definition: "Critério teórico de qualificação observacional exigido para liberação de analistas de scout, estipulado em no mínimo 90% de acertos (18/20 respostas) e ZERO erro crítico no teste de cenários."
      valid_context: "Habilitação de observadores/analistas para coleta de dados de scout."
      invalid_context: "Coleta operada por observadores não qualificados ou sem teste prévio."
      inclusions:
        - "Aprovação prévia nos cenários teóricos e ausência de erro crítico"
      exclusions:
        - "Avaliação de carga física do observador"
      synonyms:
        - "Confiabilidade CON-006"
        - "Qualificação do Observador"
      related_concept_ids:
        - "PROTOCOLO_SCOUT"
        - "ANALISTA_OBSERVADOR"
      allowed_values:
        - "QUALIFICADO"
        - "NAO_QUALIFICADO"
      temporality: "PERMANENTE"
      privacy_classification: "USO_INTERNO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"

    - id: "EVENTO_SCOUT"
      preferred_term: "Evento de Scout"
      canonical_name: "Scout Event"
      classification: "REGISTRO_OBSERVACIONAL"
      definition: "Ocorrência técnica ou tática discreta registrada por um analista durante a observação de vídeo, associada a um instante temporal (timecode), atleta, equipe e parâmetros de codificação."
      valid_context: "Coleta observacional primária (P1) e análises estatísticas de jogo."
      invalid_context: "Impressões genéricas sem registro de tempo ou atleta."
      inclusions:
        - "Finalizações"
        - "Passes"
        - "Ações defensivas e defesas de goleiro"
        - "Punições e faltas"
      exclusions:
        - "Métricas fisiológicas não observáveis em vídeo"
      synonyms:
        - "Evento Tático"
        - "Ocorrência de Scout"
        - "Tactical Event"
      related_concept_ids:
        - "PROTOCOLO_SCOUT"
        - "TIMECODE"
        - "TRECHO_OBSERVADO"
        - "ANALISTA_OBSERVADOR"
      allowed_values: []
      temporality: "TEMPORAL"
      privacy_classification: "USO_INTERNO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"

    - id: "ANALISTA_OBSERVADOR"
      preferred_term: "Analista Observador de Scout"
      canonical_name: "Scout Observer Analyst"
      classification: "PAPEL_OPERACIONAL"
      definition: "Pessoa qualificada responsável por realizar a codificação e registro dos eventos observacionais de vídeo segundo o protocolo canônico de scout."
      valid_context: "Processo de gravação de dados de scout primário (P1) e auditoria de confiabilidade."
      invalid_context: "Público geral ou torcedores sem qualificação ou teste CON-006."
      inclusions:
        - "Analistas táticos e observadores certificados pelo protocolo"
      exclusions:
        - "Sistemas automatizados de gravação sem intervenção humana"
      synonyms:
        - "Observador"
        - "Analista de Scout"
        - "Coder"
      related_concept_ids:
        - "PROTOCOLO_SCOUT"
        - "CONFIABILIDADE_OBSERVADOR"
        - "EVENTO_SCOUT"
      allowed_values: []
      temporality: "PERMANENTE"
      privacy_classification: "DADO_PESSOAL"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"

    - id: "TIMECODE"
      preferred_term: "Timecode"
      canonical_name: "Video Timecode"
      classification: "ESTRUTURA_METRICA"
      definition: "Marcador temporal preciso (horas:minutos:segundos:quadros ou milissegundos) extraído da mídia de vídeo de broadcast para ancoragem exata dos eventos observados de scout."
      valid_context: "Sincronização de vídeo e identificação precisa de eventos de jogo."
      invalid_context: "Horário de relógio de parede não sincronizado com o vídeo."
      inclusions:
        - "Marcação temporal de início e fim de posses, BOUs e eventos"
      exclusions:
        - "Cronômetro regressivo da arbitragem na quadra sem referência ao vídeo"
      synonyms:
        - "Estampa de Tempo"
        - "Timestamp de Vídeo"
      related_concept_ids:
        - "TRECHO_OBSERVADO"
        - "EVENTO_SCOUT"
      allowed_values: []
      temporality: "TEMPORAL"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"

    - id: "TRECHO_OBSERVADO"
      preferred_term: "Trecho Observado"
      canonical_name: "Observed Video Segment"
      classification: "UNIDADE_ANALITICA"
      definition: "Segmento contínuo do arquivo de mídia de vídeo delimitado por timecodes de início e fim, contendo um trecho específico de jogo (posse, BOU, período) sob análise."
      valid_context: "Corte de vídeo para análise tática, revisão de scout e treinamento."
      invalid_context: "Arquivo bruto de partida sem delimitação de início e fim."
      inclusions:
        - "Clipes e segmentos de vídeo de ataques posicionais, defesas ou cobranças"
      exclusions:
        - "Intervalos entre períodos sem ações de jogo"
      synonyms:
        - "Clipe de Vídeo"
        - "Segmento de Vídeo"
        - "Video Clip"
      related_concept_ids:
        - "TIMECODE"
        - "EVENTO_SCOUT"
        - "UNIDADE_BASICA_ATAQUE_BOU"
      allowed_values: []
      temporality: "TEMPORAL"
      privacy_classification: "PUBLICO"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_004"

  rules:
    - id: "RN_IHF_VIGENCIA_2026"
      name: "Vigência das Atualizações das Regras IHF 2026"
      rule_type: "REGULAMENTAR"
      subject_ids:
        - "PARTIDA"
      statement: "As alterações atualizadas das Regras de Jogo do Handebol de Praia da IHF entram em vigor oficialmente em 1º de abril de 2026 (ou 1º de julho de 2026 para disposições específicas de uniformes)."
      conditions: "Partidas disputadas sob a égide da IHF/CBHb a partir de 01/04/2026."
      exceptions: "Regulamentos estaduais ou edições anteriores com salvaguarda explícita de transição."
      valid_from: "2026-04-01"
      valid_to: null
      valid_context: "Competições oficiais de Handebol de Praia."
      invalid_context: "Competições encerradas antes de 01/04/2026."
      implementation_targets:
        - "motor_regras_ihf"
        - "validacao_partidas"
      verification_test_ids:
        - "TEST_REG_IHF_VIGENCIA_001"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_001"
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_002"

    - id: "RN_IHF_LIMITE_ATLETAS_QUADRA"
      name: "Limite Máximo de Atletas Simultâneos em Quadra"
      rule_type: "INVARIANTE_JOGO"
      subject_ids:
        - "EQUIPE"
        - "ATLETA"
      statement: "Cada equipe pode manter no máximo 4 (quatro) atletas simultaneamente na quadra de jogo (sendo 3 de linha e 1 goleira/goleiro)."
      conditions: "Bola em jogo durante períodos regulamentares, Gol de Ouro ou Shoot-out."
      exceptions: "Atuação com atletas a menos decorrente de exclusões disciplinares ativas."
      valid_from: "2026-04-01"
      valid_to: null
      valid_context: "Todas as partidas disputadas de Handebol de Praia."
      invalid_context: "Substituições irregulares ou invasão de área por suplentes."
      implementation_targets:
        - "validacao_sula_escalacao"
        - "controle_substituicao"
      verification_test_ids:
        - "TEST_RN_IHF_MAX_PLAYERS_001"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_005"

    - id: "RN_IHF_ULTIMOS_15_SEGUNDOS"
      name: "Penalização Especial dos Últimos 15 Segundos e Gol de Ouro"
      rule_type: "SANCAO_DISCIPLINAR"
      subject_ids:
        - "ATLETA"
        - "EQUIPE"
        - "PARTIDA"
      statement: "A obstrução ou retardo da execução de arremesso adversário nos últimos 15 segundos do período ou durante o Gol de Ouro acarreta desqualificação direta do infrator e concessão de tiro de 6 metros."
      conditions: "Cronômetro nos últimos 15 segundos de qualquer período ou vigência do Gol de Ouro com bola fora de jogo ou infrações das regras 8:5/8:6/8:7/8:10 com bola em jogo."
      exceptions: "Nenhuma."
      valid_from: "2026-04-01"
      valid_to: null
      valid_context: "Trecho final de períodos ou disputa de Gol de Ouro."
      invalid_context: "Tempo regulamentar anterior aos últimos 15 segundos."
      implementation_targets:
        - "sancao_disciplinar_arbitragem"
      verification_test_ids:
        - "TEST_RN_LAST_15S_001"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_012"
        - "EVID_IHF_RULES_2026_EN_013"
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_006"

    - id: "RN_IHF_JOGO_PASSIVO_PASSES"
      name: "Limite de Passes no Jogo Passivo"
      rule_type: "REGRA_TECNICA"
      subject_ids:
        - "EQUIPE"
        - "UNIDADE_BASICA_ATAQUE_BOU"
      statement: "Após a exibição do sinal de advertência de jogo passivo (Gesto nº 16), a equipe atacante dispõe de no máximo 4 (quatro) passes para realizar uma tentativa de arremesso ao gol."
      conditions: "Sinal de advertência de jogo passivo exibido pela arbitragem."
      exceptions: "Tiro livre ou tiro lateral concedido à equipe atacante pode resetar/ajustar a contagem conforme regras da IHF."
      valid_from: "2026-04-01"
      valid_to: null
      valid_context: "Fase de ataque posicional sob advertência de jogo passivo."
      invalid_context: "Ataque regular sem sinalização de advertência."
      implementation_targets:
        - "scout_modulo_passivo"
      verification_test_ids:
        - "TEST_PASSIVE_PLAY_4PASSES"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_004"

    - id: "RN_IHF_PROTECAO_GOLEIRO_CABECA"
      name: "Proteção de Integridade do Goleiro em Arremessos na Cabeça"
      rule_type: "SANCAO_DISCIPLINAR"
      subject_ids:
        - "ATLETA"
        - "GOLEIRA_POSICAO"
      statement: "Aplica-se suspensão obrigatória ao arremessador sem marcação em jogo aberto cujo arremesso atinja diretamente a cabeça do goleiro como primeiro ponto de contato."
      conditions: "Arremessador completamente desimpedido, duelo direto em jogo aberto, atingimento direto da cabeça do goleiro."
      exceptions: "Se o goleiro mover a cabeça em direção à trajetória da bola ou simular a lesão (hipótese em que o goleiro é punido)."
      valid_from: "2026-04-01"
      valid_to: null
      valid_context: "Arremessos de jogo aberto desimpedidos."
      invalid_context: "Arremessos com desvio prévio em defensor ou marcação faltosa sobre o arremessador."
      implementation_targets:
        - "sancao_disciplinar_arbitragem"
      verification_test_ids:
        - "TEST_HEAD_SHOT_GOALKEEPER"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_009"

    - id: "RN_DISP_001_DECLARACAO_INTENCAO"
      name: "Independência entre Disponibilidade Declarada e Presença Factual"
      rule_type: "RESTRICAO_NEGOCIO"
      subject_ids:
        - "ATLETA"
      statement: "A disponibilidade declarada expressa estritamente intenção prospectiva e jamais constitui, promove ou substitui a confirmação de presença factual."
      conditions: "Processamento e sincronização de declarações de atletas."
      exceptions: "Nenhuma."
      valid_from: "2026-01-01"
      valid_to: null
      valid_context: "Módulo de disponibilidade e agenda do CEPRAEA."
      invalid_context: "Promoção automática de intenção declarada para registro factual de presença."
      implementation_targets:
        - "service_availability"
        - "service_presences"
      verification_test_ids:
        - "TEST_RN_DISP_001_ISOLATION"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_003"

    - id: "RN_DEC_DATA_045_1_SSOT_PRESENCA"
      name: "Single Source of Truth e Gate Humano para Presença Factual"
      rule_type: "GOVERNANCA_DADOS"
      subject_ids:
        - "ATLETA"
      statement: "A tabela factual_presences é a única fonte de verdade para presenças factuais, exigindo obrigatoriamente confirmação explícita e autenticada do treinador."
      conditions: "Homologação de relatórios pós-treino ou presenças em eventos."
      exceptions: "Nenhuma."
      valid_from: "2026-01-01"
      valid_to: null
      valid_context: "Registro definitivo de presenças no banco de dados."
      invalid_context: "Gravação de presença por autorrelato direto da atleta sem validação."
      implementation_targets:
        - "public.factual_presences"
        - "gate_treinador_approval"
      verification_test_ids:
        - "TEST_SSOT_PRESENCE_GATE"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_020"
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_022"

    - id: "RN_REG_IHF_002_EXCLUSAO_DUAS_ATLETAS"
      name: "Regra de Determinação por Exclusão de Atletas em Partida"
      rule_type: "REGRA_NEGOCIO"
      subject_ids:
        - "EQUIPE"
        - "ATLETA"
        - "PARTIDA"
      statement: "Quando a convocação oficial da etapa contiver 12 atletas e a partida limitar a 10 jogadoras em súmula, informa-se as 2 atletas ausentes para materializar as demais 10 como JOGOU."
      conditions: "Convocação de 12 atletas para a etapa e súmula de partida com limite de 10 jogadoras."
      exceptions: "Ausência explícita adicional por motivo médico ou disciplinar formalizado."
      valid_from: "2026-01-01"
      valid_to: null
      valid_context: "Montagem da súmula e registro de participação em partidas."
      invalid_context: "Partidas com convocações de tamanho diferente de 12 atletas."
      implementation_targets:
        - "public.match_appearances"
      verification_test_ids:
        - "TEST_TWO_EXCLUDED_OF_TWELVE"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_025"

    - id: "RN_SGATE_0023_PONTUACAO_FHERJ_2026"
      name: "Tabela Válida de Pontuação da FHERJ 2026"
      rule_type: "REGRA_NEGOCIO"
      subject_ids:
        - "EQUIPE"
        - "PARTIDA"
      statement: "A atribuição de pontos por colocação no Circuito FHERJ 2026 é estritamente dada pelas posições 1ª a 7ª ({1ª:16, 2ª:13, 3ª:11, 4ª:10, 5ª:9, 6ª:8, 7ª:7}), retornando INDETERMINATE para a 8ª posição em diante."
      conditions: "Cálculo de pontuação do ranking do Circuito FHERJ 2026."
      exceptions: "Equipes inelegíveis por exceções contextuais regulamentares."
      valid_from: "2026-01-01"
      valid_to: "2026-12-31"
      valid_context: "Classificação das etapas do Circuito FHERJ 2026."
      invalid_context: "Inferência não auditada de pontos a partir da 8ª posição."
      implementation_targets:
        - "service_ranking_fherj"
      verification_test_ids:
        - "TEST_SGATE_0023_SCORING"
      status: "PROPOSTO"
      evidence_ref_ids:
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_027"
        - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_006"

  decisions:
    - id: "DEC_ON_GOLEIRA_SEMANTICS"
      question: "Qual a natureza ontológica e taxonômica do termo GOLEIRA no modelo de dados do CEPRAEA Beach Pro?"
      alternatives:
        - "Representar GOLEIRA como uma função tática (TAX_FUNCTION) primária ortogonal ao lado de Ataque e Defesa."
        - "Representar GOLEIRA estritamente como uma Posição Tática (TAX_POSITION) vinculada à função DEFESA."
      selected_alternative: null
      rationale: "O NotebookLM não possui autoridade para aprovar decisões ativas. O alinhamento semântico estabelece que a atuação no gol ocorre na fase defensiva, devendo ser modelada como Posição e não Função isolada."
      affected_ids:
        - "GOLEIRA_POSICAO"
        - "SISTEMA_TATICO"
        - "ATLETA"
      risk: "Reintrodução incorreta do termo como função tática em relatórios de scout, gerando inconsistência nas agregações de estatísticas de ataque/defesa."
      evidence_ref_ids:
        - "EVID_CEPRAEA_DATABASE_CCB2A718_004"
        - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_007"
      status: "EM_REVISAO"

    - id: "DEC_ON_REJECTION_INFERENTIAL_VAR_28"
      question: "Devo manter a variável inferencial VAR-028 (troca_necessaria) na camada primária de observação de scout (P1)?"
      alternatives:
        - "Manter VAR-028 na ficha de codificação P1 sob julgamento do observador."
        - "Excluir VAR-028 da camada P1 por falta de sustentação objetiva do vídeo e inviabilidade de verificação direta."
      selected_alternative: null
      rationale: "O vídeo de broadcast não permite julgar com rigor objetivo a necessidade, correção ou atraso de uma troca tática sem pressuposições subjetivas do observador."
      affected_ids:
        - "PROTOCOLO_SCOUT"
        - "EVENTO_SCOUT"
      risk: "Comprometimento da reprodutibilidade dos dados de scout e rebaixamento do índice de concordância entre observadores (Kappa de Cohen)."
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
      status: "EM_REVISAO"

    - id: "DEC_ON_EXCECAO_CAMPINAS_FHERJ_2026"
      question: "Como modelar no banco de dados a inelegibilidade de pontuação do ranking final para a equipe de Campinas/SP no Circuito FHERJ 2026?"
      alternatives:
        - "Alterar a estrutura do objeto global TEAM e criar uma nova enumeração geral 'equipe_fora_do_estado'."
        - "Tratar como uma instância contextual de FINAL_RANKING_ELIGIBILITY associada especificamente à participação da equipe na competição FHERJ 2026."
      selected_alternative: null
      rationale: "A exceção é de natureza puramente regulamentar e contextual da competição regional, não devendo poluir a entidade canônica e imutável de Equipe."
      affected_ids:
        - "EQUIPE"
        - "RN_SGATE_0023_PONTUACAO_FHERJ_2026"
      risk: "Rigidez na modelagem de equipes de fora do estado em outros campeonatos onde a pontuação seja permitida."
      evidence_ref_ids:
        - "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_008"
      status: "EM_REVISAO"

  open_issues:
    - id: "ISSUE_MIGRATION_VERSION_STATUS"
      description: "Verificar se a versão de migração SQL 20261013000001 descrita no documento historicamente associado foi efetivamente executada nos ambientes de staging e produção ou se permanece restrita à especificação em arquivo."
      affected_ids:
        - "SRC_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E"
      status: "ABERTA"
      evidence_ref_ids:
        - "SRC_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E"

    - id: "ISSUE_MISSING_RLS_POLICIES"
      description: "Ausência da declaração explícita de instruções CREATE POLICY para as tabelas habilitadas com RLS na Seção 1 do documento de segurança (incluindo matches, convocations, possessions, bous e tactical_events)."
      affected_ids:
        - "SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919"
      status: "ABERTA"
      evidence_ref_ids:
        - "SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919"

    - id: "ISSUE_FHERJ_SCORING_POSITIONS_8_PLUS"
      description: "Indeterminação da tabela oficial de pontuação para a 8ª colocação em diante no Circuito FHERJ 2026 em virtude da marcação do Artigo 25º do regulamento armazenado como STALE_FOR_SCORING."
      affected_ids:
        - "RN_SGATE_0023_PONTUACAO_FHERJ_2026"
      status: "ABERTA"
      evidence_ref_ids:
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_027"
        - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_006"

    - id: "ISSUE_SHOOTOUT_SCORE_MISSING_ETAPA_FINAL"
      description: "Omissão factual do registro de placar do Shoot-out no boletim oficial da partida J71 (Etapa Final do Circuito Brasileiro em São Miguel do Iguaçu/PR)."
      affected_ids:
        - "PARTIDA"
        - "SHOOT_OUT"
      status: "ABERTA"
      evidence_ref_ids:
        - "EVID_CEPRAEA_DATABASE_CCB2A718_008"