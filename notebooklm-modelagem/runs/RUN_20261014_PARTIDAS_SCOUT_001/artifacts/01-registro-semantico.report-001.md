# Registro Semântico Canônico — Handebol de Praia e Scout Tático CEPRAEA

semantic_registry:
  concepts:
    - id: "CON-PARTIDA"
      term: "Partida"
      definition: "Confronto esportivo regulamentado de Handebol de Praia disputado entre duas equipes, estruturado em dois períodos independentes de 10 minutos cada, com eventual desempate por Gol de Ouro no período ou Shoot-out na partida."
      context: "Regulamento IHF"
      synonyms: []
      inclusions:
        - "Primeiro Período"
        - "Segundo Período"
        - "Gol de Ouro"
        - "Shoot-out"
      exclusions:
        - "Prorrogação contínua de dois tempos"
      epistemology: "FATO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_002"
        - "EVID_IHF_RULES_2026_EN_003"
        - "EVID_IHF_RULES_2026_EN_004"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_003"
        - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_012"

    - id: "CON-SET-PERIODO"
      term: "Sets / Períodos"
      definition: "Unidade estrutural temporal de jogo com duração oficial de 10 minutos cada, cuja pontuação de gols é contabilizada de forma totalmente independente entre o primeiro e o segundo tempo."
      context: "Regulamento IHF"
      synonyms:
        - "Período de Jogo"
        - "Set"
      inclusions:
        - "Primeiro Período (10 min)"
        - "Segundo Período (10 min)"
        - "Intervalo de 5 minutos"
      exclusions:
        - "Cômputo geral acumulado de gols entre os períodos para definir o vencedor do jogo"
      epistemology: "FATO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_002"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_003"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_004"

    - id: "CON-GOL-DE-OURO"
      term: "Gol de Ouro (Golden Goal)"
      definition: "Método de desempate utilizado ao final de qualquer um dos dois períodos regulamentares quando o placar terminar empatado, reiniciando o jogo com tiro de árbitro no centro da quadra e consagrando vencedora a equipe que marcar o primeiro gol."
      context: "Regulamento IHF"
      synonyms:
        - "Golden Goal"
      inclusions:
        - "Tiro de árbitro no centro da quadra"
        - "Encerramento imediato do período após o primeiro gol validado"
      exclusions:
        - "Decisão da partida quando o resultado dos sets for 1 a 1"
      epistemology: "FATO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_003"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_005"
        - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_013"

    - id: "CON-SHOOT-OUT"
      term: "Shoot-out"
      definition: "Segmento de desempate da partida ativado quando cada equipe vence um dos períodos regulamentares (empate em 1x1 em sets), consistente em uma série inicial de 5 cobranças alternadas de 1 contra o goleiro por equipe. Caso um goleiro atue como arremessador na cobrança do Shoot-out, este é classificado e avaliado estritamente como jogador de linha para a execução da referida ação."
      context: "Regulamento IHF"
      synonyms:
        - "Um contra o Goleiro"
        - "1 contra o Goleiro"
      inclusions:
        - "Série de 5 cobranças alternadas por equipe com atletas elegíveis"
        - "Cobrança de morte súbita caso persista empate após as 5 cobranças"
        - "Classificação do goleiro como jogador de linha ao atuar como arremessador"
      exclusions:
        - "Cobrança direta estática sem passe a partir da área de gol"
      epistemology: "FATO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_004"
        - "EVID_IHF_RULES_2026_EN_009"
        - "EVID_IHF_RULES_2026_EN_010"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_006"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_012"
        - "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_012"

    - id: "CON-GOL-SIMPLES"
      term: "Gol Simples (1 Ponto)"
      definition: "Finalização convertida que ultrapassa totalmente a linha de gol e atribui 1 ponto no placar, decorrente de arremessos clássicos/normais executados por jogadores de linha comuns ou gol contra."
      context: "Regulamento IHF"
      synonyms:
        - "Gol de 1 ponto"
        - "Regular goal"
      inclusions:
        - "Arremesso frontal simples de jogador de linha"
        - "Tapa ou empurrão de bola em jogada aérea"
        - "Gol contra anotado por qualquer atleta"
      exclusions:
        - "Gols por Spin Shot, In-flight, Tiro de 6m ou convertidos por Goleira/Especialista"
      epistemology: "FATO"
      evidence_ref_ids:
        - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_003"
        - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_004"
        - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_007"
        - "EVID_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_002"

    - id: "CON-GOL-DUPLO"
      term: "Gol Duplo / Valor Dobrado (2 Pontos)"
      definition: "Finalização convertida que atribui 2 pontos no placar da partida em virtude do elevado grau de espetacularidade técnica, origem regulamentar especial ou função/posição de quem a executa."
      context: "Regulamento IHF"
      synonyms:
        - "Gol de 2 pontos"
        - "GOAL2"
      inclusions:
        - "Spin Shot (360°)"
        - "In-flight (ponte aérea com controle e arremesso no ar)"
        - "Tiro de 6 Metros"
        - "Gol marcado por Goleira ou Especialista"
      exclusions:
        - "Arremesso simples de jogador de linha sem giro completo ou sem suspensão no ar"
      epistemology: "FATO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_006"
        - "EVID_IHF_RULES_2026_EN_007"
        - "EVID_IHF_RULES_2026_EN_008"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_009"
        - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_005"
        - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_006"

    - id: "CON-SPIN-SHOT"
      term: "Spin Shot (360°)"
      definition: "Técnica espetacular de finalização que concede 2 pontos, caracterizada pelo salto e rotação completa do corpo (360º) no ar, exigindo que os pés de impulsão estejam direcionados ao gol no momento da saída do solo."
      context: "Regulamento IHF"
      synonyms:
        - "Giro 360°"
        - "Arremesso em giro"
      inclusions:
        - "Giro corporal completo em suspensão no ar com impulsão virada para a baliza"
      exclusions:
        - "Meio-giro incompleto com toque na areia antes do arremesso"
      epistemology: "FATO"
      evidence_ref_ids:
        - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_005"
        - "EVID_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_002"

    - id: "CON-IN-FLIGHT"
      term: "In-flight (Ponte Aérea)"
      definition: "Técnica espetacular de finalização que concede 2 pontos, na qual o atleta capta a bola no ar após passe de um companheiro, domina o controle do balão e realiza a finalização à baliza antes de tocar o solo."
      context: "Regulamento IHF"
      synonyms:
        - "Ponte Aérea"
        - "Fly"
      inclusions:
        - "Recepção, controle e arremesso efetuados totalmente no ar"
      exclusions:
        - "Tapa ou empurrão de bola sem controle no ar (valem 1 ponto)"
      epistemology: "FATO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_014"
        - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_006"
        - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_007"

    - id: "CON-GOL-CONTRA"
      term: "Gol Contra"
      definition: "Ação em que um jogador introduz a bola em sua própria baliza, sendo concedido 1 ponto à equipe adversária, salvo no tiro de meta executado pelo goleiro em que a bola não saia da área de gol."
      context: "Regulamento IHF"
      synonyms:
        - "Own goal"
      inclusions:
        - "Bola jogada na própria baliza por qualquer atleta de linha ou goleiro"
      exclusions:
        - "Tiro de meta do goleiro que entra na própria baliza sem sair da área de gol"
      epistemology: "FATO"
      evidence_ref_ids:
        - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_003"

    - id: "CON-TIRO-6-METROS"
      term: "Tiro de 6 Metros"
      definition: "Sanção técnica concedida quando uma clara oportunidade de gol é destruída ilicitamente por um adversário ou oficial em qualquer parte da quadra. Sua execução exige arremesso direto ao gol em até 3 segundos após o apito do árbitro, sem que o executante toque ou cruze a linha de 6 metros, com goleiro e defensores mantendo distância mínima de 1 metro e vedada a substituição do goleiro após o cobrador estar pronto."
      context: "Regulamento IHF"
      synonyms:
        - "Tiro de 6m"
        - "6-metre throw"
      inclusions:
        - "Destruição de clara ocasião de gol"
        - "Obstrução irregular nos últimos 15 segundos ou Gol de Ouro"
        - "Apito injustificado ou interferência externa em clara ocasião"
        - "Execução restrita a 3 segundos e afastamento de 1 metro dos defensores"
      exclusions:
        - "Faltas ordinárias sem destruição de clara ocasião de gol"
      epistemology: "FATO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_007"
        - "EVID_IHF_RULES_2026_EN_011"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_010"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_013"
        - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_002"
        - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_009"
        - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_010"
        - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_011"
        - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_012"
        - "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_013"

    - id: "CON-EXCLUSAO"
      term: "Exclusão"
      definition: "Sanção disciplinar pessoal aplicável a atletas por faltas graves ou recorrentes, implicando a saída de quadra até que haja a troca de posse de bola; o acúmulo de 2 exclusões resulta na desqualificação do atleta."
      context: "Regulamento IHF"
      synonyms:
        - "Suspensão temporária"
      inclusions:
        - "Afastamento imediato de quadra até a transição de posse de bola"
      exclusions:
        - "Advertência verbal ou Cartão Amarelo"
      epistemology: "FATO"
      evidence_ref_ids:
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_014"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_015"

    - id: "CON-CARTAO-AZUL"
      term: "Cartão Azul e Suspensão"
      definition: "Sinalização ostensiva exibida pelos árbitros após uma desqualificação para indicar que um relatório disciplinar será redigido, acarretando a suspensão automática por no mínimo uma partida para o atleta ou oficial punido."
      context: "Regulamento FHERJ e IHF"
      synonyms:
        - "Desqualificação com relatório"
      inclusions:
        - "Suspensão automática de no mínimo 1 partida vindoura"
        - "Envio de relatório escrito para comissão disciplinar"
      exclusions:
        - "Desqualificação direta resultante de segunda exclusão por faltas do jogo"
      epistemology: "FATO"
      evidence_ref_ids:
        - "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_015"
        - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_017"
        - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_018"

    - id: "CON-REGRA-15-SEGUNDOS"
      term: "Regra dos 15 Segundos Finais / Golden Goal"
      definition: "Dispositivo regulamentar de proteção extrema aplicado nos últimos 15 segundos de cada período e durante todo o Gol de Ouro, onde qualquer infração deliberada para impedir/atrasar reinícios com bola fora ou faltas graves com bola em jogo gera desqualificação direta do infrator e concessão automática de tiro de 6 metros."
      context: "Regulamento IHF 2026"
      synonyms:
        - "Regra do Trecho Final"
      inclusions:
        - "Interferência com bola fora ou em jogo nos 15s finais e Gol de Ouro"
        - "Desqualificação direta do infrator acompanhada de tiro de 6 metros"
      exclusions:
        - "Faltas ordinárias ocorridas fora do intervalo dos 15 segundos finais"
      epistemology: "FATO"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_012"
        - "EVID_IHF_RULES_2026_EN_013"
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_005"
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_008"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_016"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_017"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_018"

    - id: "CON-POSSE-UNT003"
      term: "Posse de Bola (UNT-003)"
      definition: "Unidade primária de observação do scout (UNT-003) caracterizada pelo intervalo de direito ou controle funcional/legal da bola por uma equipe, iniciado pelo primeiro controle inequívoco em bola viva ou reinício legal, e encerrado por gol validado, perda de controle ou apito regulamentar."
      context: "Protocolo de Scout CEPRAEA"
      synonyms:
        - "UNT-003"
        - "Possessão"
      inclusions:
        - "Controle funcional em bola viva registrado por codificação direta em vídeo"
        - "Direito legal atribuído por reinício de jogo"
      exclusions:
        - "Toque fortuito sem controle"
        - "Interrupções temporárias sem mudança do direito à bola"
      epistemology: "FATO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"

    - id: "CON-BOU-UNT004"
      term: "Unidade Básica de Ataque (UNT-004 / BOU)"
      definition: "Unidade primária de observação tática (UNT-004) correspondente ao intervalo do ataque posicional que se inicia quando a equipe atacante apresenta organização estável em postos ofensivos contra uma defesa organizada e termina na interrupção do ataque ou perda da posse."
      context: "Protocolo de Scout CEPRAEA"
      synonyms:
        - "UNT-004"
        - "Basic Attack Unit"
        - "BOU"
      inclusions:
        - "Organização posicional estável em superioridade ou igualdade registrada por codificação direta em vídeo"
      exclusions:
        - "Ataque em transição rápida ou contra-ataque direto"
      epistemology: "FATO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_004"
        - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_001"

    - id: "CON-FASES-TATICAS-TAX001"
      term: "Fases Táticas (TAX-001)"
      definition: "Categorização sistemática dos quatro estados operacionais ordinários de jogo no scout, compostos por Transição Ofensiva (TO), Ataque Posicional (AP), Transição Defensiva (TD) e Defesa Posicional (DP), além da categoria Indeterminada (F_IND)."
      context: "Protocolo de Scout CEPRAEA"
      synonyms:
        - "TAX-001"
        - "Fases de Jogo"
      inclusions:
        - "TO — Transição Ofensiva"
        - "AP — Ataque Posicional"
        - "TD — Transição Defensiva"
        - "DP — Defesa Posicional"
        - "F_IND — Fronteira Indeterminável"
      exclusions:
        - "Paralisações administrativas e tempos mortos"
      epistemology: "INTERPRETAÇÃO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_005"

    - id: "CON-ZONAS-QUADRA-TAX006"
      term: "Zonas Analíticas de Quadra (TAX-006)"
      definition: "Divisão geométrica analítica da largura de 12 metros da quadra de jogo em quatro faixas longitudinais paralelas de 3 metros cada: Zona Esquerda (ZE), Zona Central Esquerda (ZCE), Zona Central Direita (ZCD) e Zona Direita (ZD)."
      context: "Protocolo de Scout CEPRAEA"
      synonyms:
        - "TAX-006"
        - "Faixas de Arremesso"
      inclusions:
        - "ZE (0 a 3m)"
        - "ZCE (3 a 6m)"
        - "ZCD (6 a 9m)"
        - "ZD (9 a 12m)"
      exclusions:
        - "Marcações oficiais de quadra reconhecidas pela IHF"
      epistemology: "INTERPRETAÇÃO"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_006"

    - id: "CON-GOLEIRA"
      term: "Goleira"
      definition: "Posição especializada do elenco cuja atuação primária pertence à função tática de Defesa, sendo responsável pela proteção da baliza na área de gol e pela iniciação da transição ofensiva via tiro de meta. Seu retorno à área defensiva reestabelece a organização posicional padrão."
      context: "Modelagem CEPRAEA / Taxonomia Tática"
      synonyms:
        - "Guarda-redes"
        - "Goalkeeper"
        - "GK"
      inclusions:
        - "Posição do elenco pertencente à função Defesa"
        - "Iniciação de transição ofensiva na ausência de tiro de saída tradicional"
      exclusions:
        - "Classificação como Função tática ou Papel tático na taxonomia TACT V2"
      epistemology: "INTERPRETAÇÃO"
      evidence_ref_ids:
        - "EVID_CEPRAEA_DATABASE_CCB2A718_004"
        - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_004"
        - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_007"
        - "EVID_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0_009"

    - id: "CON-ESPECIALISTA-CORINGA"
      term: "Especialista / Coringa"
      definition: "Papel tático de ataque exercido por atleta que substitui a goleira na transição ofensiva para gerar superioridade numérica (4x3 em sistemas 3:1, 2:2 ou 4:0). A valoração de 2 pontos atribuída ao especialista aplica-se exclusivamente a ações ofensivas de arremesso, vestindo uniforme de cor distinta."
      context: "Modelagem CEPRAEA / Regulamento IHF"
      synonyms:
        - "Specialist"
        - "Peto"
      inclusions:
        - "Papel tático ortogonal permitido exclusivamente em atribuições ofensivas"
        - "Substituição para geração de assimetria numérica ofensiva (4x3)"
      exclusions:
        - "Atuação na função defensiva dentro da área de gol"
      epistemology: "INTERPRETAÇÃO"
      evidence_ref_ids:
        - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_012"
        - "EVID_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2_003"
        - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_004"

    - id: "CON-COMISSAO-TECNICA"
      term: "Comissão Técnica"
      definition: "Grupo oficial de até 4 dirigentes inscritos em súmula por partida (técnico, auxiliar, médico e fisioterapeuta), dos quais no máximo 2 podem permanecer na área de substituição durante o jogo. Apresenta divergência regulamentar jurisdicional: a CBHb (Art. 8º) exige obrigatoriamente formação em Educação Física (CREF) para o Técnico Principal no Circuito Brasileiro, ao passo que a FHERJ (Art. 10 §20º) dispensa formalmente a exigência de CREF e curso da CBHb no Circuito Estadual do Rio de Janeiro."
      context: "Regulamento CBHb e FHERJ"
      synonyms:
        - "Oficiais de Equipe"
        - "Dirigentes"
      inclusions:
        - "Técnico, Auxiliar Técnico, Médico e Fisioterapeuta"
      exclusions:
        - "Atletas uniformizados em condição de jogo"
      epistemology: "FATO"
      evidence_ref_ids:
        - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_007"
        - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_008"
        - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_009"
        - "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_004"
        - "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_005"

  rules:
    - id: "RL-COMPOSICAO-SUMULA-QUADRA"
      title: "Limites Numéricos de Súmula, Quadra e Comissão Técnica"
      rule_type: "OBLIGATION"
      statement: "Cada equipe pode inscrever no máximo 10 atletas uniformizadas e 4 oficiais na súmula por partida, devendo manter no máximo 4 atletas simultaneamente em quadra (3 de linha e 1 goleira), o mínimo de 6 atletas para iniciar o jogo, e no máximo 2 oficiais na área de substituição. Aplica-se a exigência de CREF ao técnico em âmbito nacional (CBHb Art. 8º), ficando dispensada no circuito estadual FHERJ (Art. 10 §20º)."
      temporality: "Vigente para a temporada 2026"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_005"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_007"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_008"
        - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_007"
        - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_008"
        - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_009"
        - "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_004"
        - "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_005"
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_024"

    - id: "RL-TWO-EXCLUDED-OF-TWELVE"
      title: "Regra das Duas Ausentes na Convocação de 12"
      rule_type: "CONDITION"
      statement: "Quando a convocação oficial para a etapa contiver 12 atletas, o treinador deve informar formalmente as 2 atletas que ficarão fora de cada partida (status 'NAO_JOGOU'), materializando as demais 10 como 'JOGOU'."
      temporality: "Vigência operacional permanente"
      evidence_ref_ids:
        - "EVID_CEPRAEA_DATABASE_CCB2A718_005"
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_025"

    - id: "RL-PROIBICAO-RETARDO-REINICIO"
      title: "Proibição de Retardo Repetido em Reinícios"
      rule_type: "PROHIBITION"
      statement: "É proibido atrasar ou retardar repetidamente a execução de tiro livre, tiro lateral (throw-in) ou tiro de goleiro por qualquer equipe."
      temporality: "A partir de 01/04/2026 (IHF 2026)"
      evidence_ref_ids:
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_003"

    - id: "RL-PASSIVO-4-PASSES"
      title: "Limite de 4 Passes no Jogo Passivo"
      rule_type: "OBLIGATION"
      statement: "Após a exibição do sinal de advertência de jogo passivo (Gesto nº 16), a equipe atacante dispõe de no máximo 4 passes para realizar um arremesso à baliza antes que o tiro livre seja assinalado contra si."
      temporality: "A partir de 01/04/2026 (IHF 2026)"
      evidence_ref_ids:
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_004"

    - id: "RL-GOLEIRA-CABECA"
      title: "Sanção por Arremesso Desimpedido na Cabeça da Goleira"
      rule_type: "OBLIGATION"
      statement: "É obrigatória a aplicação de suspensão/exclusão ao arremessador sem marcação defensiva que, em situação de jogo aberto, atingir diretamente a cabeça do goleiro em primeiro contato; caso o goleiro simule lesão, ele será punido."
      temporality: "A partir de 01/04/2026 (IHF 2026)"
      evidence_ref_ids:
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_009"
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_010"

    - id: "RL-UNIFORMES-OBRIGACAO"
      title: "Obrigatoriedade de Pés Descalços e Padronização de Meias"
      rule_type: "OBLIGATION"
      statement: "É obrigatório jogar descalço, sendo permitidas meias esportivas comuns de tecido (que devem ser curtas) ou bandagens; caso mais de um atleta da mesma equipe as utilize, o uso de cor idêntica é obrigatório."
      temporality: "Vigente desde a edição IHF 2026 / FHERJ"
      evidence_ref_ids:
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_011"
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_012"
        - "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_002"
        - "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_003"

    - id: "RL-CALCADOS-PROIBICAO"
      title: "Proibição Estrita de Meias de Areia e Calçados Rígidos"
      rule_type: "PROHIBITION"
      statement: "É estritamente proibido o uso de meias de areia (sand socks), bem como qualquer tipo de calçado sintético ou de borracha durante as partidas."
      temporality: "Vigente desde a edição IHF 2026 / FHERJ"
      evidence_ref_ids:
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_013"
        - "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_002"

    - id: "RL-PONTUACAO-ESTADUAL-FHERJ"
      title: "Cálculo de Pontuação por Etapa no Circuito FHERJ 2026"
      rule_type: "CALCULATION"
      statement: "A atribuição de pontos por colocação em etapa do Circuito FHERJ 2026 é válida para as posições de 1ª a 7ª, seguindo a escala {1ª:16, 2ª:13, 3ª:11, 4ª:10, 5ª:9, 6ª:8, 7ª:7}; posições 8ª em diante sem tabela validada devem retornar 'INDETERMINATE'."
      temporality: "Circuito Estadual FHERJ 2026"
      evidence_ref_ids:
        - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_006"
        - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_008"
        - "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_005"
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_027"

    - id: "RL-RN-DISP-001"
      title: "Declaração de Disponibilidade é Intenção, Não Presença"
      rule_type: "PROHIBITION"
      statement: "A declaração de disponibilidade ou compromisso expressa única e exclusivamente intenção prospectiva e jamais constitui, promove, infere ou substitui presença factual."
      temporality: "Atemporal / Invariante de Negócio"
      evidence_ref_ids:
        - "EVID_CEPRAEA_DATABASE_CCB2A718_006"
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_003"

    - id: "RL-RN-DISP-015"
      title: "Isolamento Estrito entre Propostas e Fato de Presença"
      rule_type: "PROHIBITION"
      statement: "Nenhuma disponibilidade declarada ou proposta de autorrelato é convertida automaticamente em registro factual de presença em 'factual_presences'."
      temporality: "Atemporal / Invariante de Negócio"
      evidence_ref_ids:
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_017"

  decisions:
    - id: "DEC-GOLEIRA-POSICAO"
      decision_maker: "Steward de Governança de Dados"
      description: "Definição de que GOLEIRA é uma posição de elenco pertencente à função DEFESA, ficando proibida sua utilização como função tática na taxonomia TACT V2."
      rationale: "Unificação da taxonomia e prevenção de ambiguidades entre funções táticas ofensivas/defensivas e posições administrativas/esportivas do elenco."
      status: "APPROVED"
      evidence_ref_ids:
        - "EVID_CEPRAEA_DATABASE_CCB2A718_004"
        - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_007"

    - id: "DEC-EXCLUSAO-VAR28"
      decision_maker: "Equipe Metodológica de Scout e Steward"
      description: "Exclusão definitiva da variável inferencial VAR-028 ('troca_necessaria') da camada P1 de observação de scout."
      rationale: "Ausência de observabilidade objetiva em vídeo de broadcast que sustente julgamentos subjetivos sobre a necessidade ou tempo correto de uma substituição."
      status: "APPROVED"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"

    - id: "DEC-VIGENCIA-IHF-APR2026"
      decision_maker: "Congresso Ordinário da IHF (Cairo 2025)"
      description: "Antecipação da data de vigência das novas regras de jogo do Handebol de Praia de 01/07/2026 para 01/04/2026."
      rationale: "Decisão institucional do Congresso Ordinário da IHF em Cairo para uniformizar a aplicação das regras nas competições internacionais e estaduais de 2026."
      status: "VIGENTE"
      evidence_ref_ids:
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_001"
        - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_002"

    - id: "DEC-GATE-HUMANO-TREINADOR"
      decision_maker: "Steward de Governança de Dados (DEC-DATA-045.3)"
      description: "Exigência de ação explícita, autenticada e individualizada do treinador para homologar propostas de presença e materializá-las em 'factual_presences'."
      rationale: "Garantir a integridade epistemológica da base de dados, assegurando que apenas presenças verificadas por autoridade humana constituam a fonte primária de verdade."
      status: "HOMOLOGATED"
      evidence_ref_ids:
        - "EVID_CEPRAEA_DATABASE_CCB2A718_003"
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_022"

  open_issues:
    - id: "ISSUE_SOURCE_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E_002"
      status: "ABERTA"
      question: "A versão de migração 20261013000001 foi efetivamente aplicada no banco de dados de produção/staging ou permanece apenas como especificação de arquivo?"
      affected_ids:
        - "SRC_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E"
      impact: "Incerteza sobre a paridade entre o estado físico do banco de dados e a documentação histórica, mantendo a reconciliação semântica da fonte parcial."
      required_evidence: "Confirmação documentada do log de execução da tabela public.schema_migrations em ambiente de produção."
      owner: "OPERADOR"

    - id: "ISSUE_SOURCE_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919_001"
      status: "ABERTA"
      question: "As tabelas do domínio tático e de scout (secondary_positions, calendar_events, competitions, convocations, convocation_athletes, matches, match_appearances, possessions, bous, tactical_events, finalizations e goalkeeper_actions) possuem RLS habilitado mas não apresentam diretivas CREATE POLICY declaradas no documento 07."
      affected_ids:
        - "SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919"
      impact: "Lacuna na especificação da matriz de permissões e risco de bloqueio inadvertido de acesso ou exposição indevida de dados nessas tabelas."
      required_evidence: "Aditivo ao documento de políticas RLS contendo os comandos CREATE POLICY específicos para cada uma das tabelas omitidas."
      owner: "STEWARD"