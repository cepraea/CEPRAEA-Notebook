# Modelo Conceitual Revisado do Domínio de Beach Handball

```yaml
conceptual_model_revision:
  entities:
    - id: "SEGMENTO_OBSERVADO"
      name: "Segmento Observado"
      concept_id: "SEGMENTO_OBSERVADO"
      definition: "Delimitação contínua de vídeo ou tempo de jogo associada à partida para análise tática, marcação temporal e codificação de scout."
      identity_rule: "Identificado pela chave composta (partida_id, midia_video_id, timecode_inicio, timecode_fim)."
      temporality: "INTERVALO"
      history_required: true
      aggregate_root: false
      rule_ids:
        - "DEC-001"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_002"

    - id: "PLACAR_JOGO"
      name: "Placar do Jogo"
      concept_id: "PLACAR_JOGO"
      definition: "Estado global e agregado do placar de uma partida, registrando a contagem consolidada de sets (2:0 ou 2:1) e o resultado final da disputa."
      identity_rule: "Identificado unicamente pelo identificador da partida (partida_id) à qual está vinculado."
      temporality: "SNAPSHOT"
      history_required: true
      aggregate_root: false
      rule_ids:
        - "REG-IHF-003"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_002"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_003"
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_026"

    - id: "ESTADO_DO_PLACAR"
      name: "Estado do Placar"
      concept_id: "ESTADO_DO_PLACAR"
      definition: "Instante pontual que reflete a pontuação exata e a situação de vantagem ou desvantagem das equipes em um dado momento da partida e do set."
      identity_rule: "Identificado pela chave composta (partida_id, periodo_set_id, timestamp_instante)."
      temporality: "INSTANTANEA"
      history_required: false
      aggregate_root: false
      rule_ids:
        - "REG-IHF-003"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_002"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_003"
        - "EVID_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56_004"
        - "EVID_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_007"

    - id: "EVOLUCAO_DO_PLACAR"
      name: "Evolução do Placar"
      concept_id: "EVOLUCAO_DO_PLACAR"
      definition: "Sequência ordenada de alterações de pontos ocorridas durante a partida, derivada deterministicamente de eventos de pontuação regulamentares (1 ou 2 pontos)."
      identity_rule: "Identificado pela chave composta (partida_id, sequencial_ocorrencia) associada ao evento de pontuação correspondente."
      temporality: "EVENTO"
      history_required: true
      aggregate_root: false
      rule_ids:
        - "REG-IHF-003"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_006"
        - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_009"

    - id: "SISTEMA_DEFENSIVO"
      name: "Sistema Defensivo"
      concept_id: "SISTEMA_DEFENSIVO"
      definition: "Configuração tática defensiva posicionada em quadra pela equipe defensora (ex.: 3:0, 2:1, 1:2) durante uma posse de bola ou fase de defesa."
      identity_rule: "Identificado pela chave composta (equipe_id, posse_de_bola_id, codigo_sistema_defensivo)."
      temporality: "INTERVALO"
      history_required: false
      aggregate_root: false
      rule_ids:
        - "TAX-001"
      evidence_ref_ids:
        - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_006"
        - "EVID_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94_002"

    - id: "CONFIABILIDADE_OBSERVADOR"
      name: "Confiabilidade do Observador"
      concept_id: "CONFIABILIDADE_OBSERVADOR"
      definition: "Métrica de qualificação técnica, concordância intra/inter-observador (índices Kappa de Cohen e Fleiss) e precisão de codificação do analista."
      identity_rule: "Identificado pela chave composta (analista_observador_id, versao_avaliacao, data_avaliacao)."
      temporality: "VERSIONADA"
      history_required: true
      aggregate_root: false
      rule_ids:
        - "CON-006"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
        - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_007"

    - id: "REVISAO_DA_OBSERVACAO"
      name: "Revisão da Observação"
      concept_id: "REVISAO_DA_OBSERVACAO"
      definition: "Evento de auditoria, moderação, alteração ou re-validação executado por um analista sobre um registro prévio de observação de scout."
      identity_rule: "Identificado pela chave composta (observacao_de_scout_id, analista_observador_id, timestamp_revisao)."
      temporality: "EVENTO"
      history_required: true
      aggregate_root: false
      rule_ids:
        - "DEC-001"
        - "CON-006"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"

    - id: "ESTADO_DE_REVISAO"
      name: "Estado de Revisão"
      concept_id: "ESTADO_DE_REVISAO"
      definition: "Situação corrente do ciclo de vida da observação de scout (ex.: PENDENTE, APROVADO, REJEITADO, EM_REVISAO) mantida ao longo do tempo até sua transição."
      identity_rule: "Identificado pela chave composta (observacao_de_scout_id, codigo_status_revisao)."
      temporality: "VERSIONADA"
      history_required: true
      aggregate_root: false
      rule_ids:
        - "DEC-001"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"

    - id: "PROVENIENCIA_OBSERVACAO"
      name: "Proveniência da Observação"
      concept_id: "PROVENIENCIA_OBSERVACAO"
      definition: "Registro imutável de linhagem de dados, especificando software gerador (ex.: LINCE PLUS), protocolo, arquivo de mídia e contexto de captura da observação."
      identity_rule: "Identificado unicamente pelo identificador da observação de scout (observacao_de_scout_id) associada."
      temporality: "ATEMPORAL"
      history_required: false
      aggregate_root: false
      rule_ids:
        - "DEC-001"
      evidence_ref_ids:
        - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_005"
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"

    - id: "TRECHO_OBSERVADO"
      name: "Trecho Observado"
      concept_id: "TRECHO_OBSERVADO"
      definition: "Recorte delimitado de timecode no arquivo de vídeo correspondente a um evento discreto de scout ou unidade de observação tática."
      identity_rule: "Identificado pela chave composta (evento_scout_id, midia_video_id, timecode_inicio, timecode_fim)."
      temporality: "INTERVALO"
      history_required: false
      aggregate_root: false
      rule_ids:
        - "DEC-001"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"

  relationships:
    - id: "PARTIDA_POSSUI_SEGMENTO_OBSERVADO"
      name: "Partida possui Segmento Observado"
      from_entity_id: "PARTIDA"
      to_entity_id: "SEGMENTO_OBSERVADO"
      meaning: "Delimita os intervalos contínuos de análise tática e observação associados a uma partida."
      cardinality:
        from_to:
          min: 0
          max: "N"
        to_from:
          min: 1
          max: 1
      relationship_attributes:
        - "intervalo_ordem"
        - "faixa_tempo_inicio"
        - "faixa_tempo_fim"
      exclusivity_rules:
        - "O segmento observado não pode se estender além dos limites operacionais de tempo da partida."
      rule_ids:
        - "DEC-001"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
      temporality: "INTERVALO"

    - id: "SEGMENTO_OBSERVADO_MAPPED_TO_MIDIA_VIDEO"
      name: "Segmento Observado mapeado para Mídia Vídeo"
      from_entity_id: "SEGMENTO_OBSERVADO"
      to_entity_id: "MIDIA_VIDEO"
      meaning: "Associa o segmento contínuo de análise ao arquivo físico de mídia de vídeo correspondente."
      cardinality:
        from_to:
          min: 1
          max: 1
        to_from:
          min: 0
          max: "N"
      relationship_attributes:
        - "timecode_start_frame"
        - "timecode_end_frame"
      exclusivity_rules:
        - "O timecode do segmento deve estar integralmente contido na duração do arquivo de mídia."
      rule_ids:
        - "DEC-001"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
      temporality: "ATEMPORAL"

    - id: "PARTIDA_POSSUI_PLACAR_JOGO"
      name: "Partida possui Placar do Jogo"
      from_entity_id: "PARTIDA"
      to_entity_id: "PLACAR_JOGO"
      meaning: "Relaciona a partida ao seu estado global consolidado de placar de sets e pontos."
      cardinality:
        from_to:
          min: 1
          max: 1
        to_from:
          min: 1
          max: 1
      relationship_attributes:
        - "sets_vencidos_equipe_a"
        - "sets_vencidos_equipe_b"
        - "vencedor_partida_id"
      exclusivity_rules:
        - "A soma dos sets vencidos deve encerrar rigorosamente em 2:0 ou 2:1 conforme regras IHF."
      rule_ids:
        - "REG-IHF-003"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_002"
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_026"
      temporality: "SNAPSHOT"

    - id: "PLACAR_JOGO_REGISTRA_ESTADO"
      name: "Placar do Jogo registra Estado do Placar"
      from_entity_id: "PLACAR_JOGO"
      to_entity_id: "ESTADO_DO_PLACAR"
      meaning: "Mapeia os estados pontuais e instantâneos de pontuação registrados ao longo da partida."
      cardinality:
        from_to:
          min: 1
          max: "N"
        to_from:
          min: 1
          max: 1
      relationship_attributes:
        - "pontos_equipe_a"
        - "pontos_equipe_b"
        - "situacao_vantagem"
      exclusivity_rules:
        - "O estado instantâneo reflete estritamente o somatório acumulado até o timestamp informado."
      rule_ids:
        - "REG-IHF-003"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_002"
        - "EVID_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56_004"
      temporality: "INSTANTANEA"

    - id: "ESTADO_DO_PLACAR_PERTENCE_A_PERIODO_SET"
      name: "Estado do Placar pertence a Período Set"
      from_entity_id: "ESTADO_DO_PLACAR"
      to_entity_id: "PERIODO_SET"
      meaning: "Localiza temporalmente a pontuação instantânea no âmbito específico de um set do jogo."
      cardinality:
        from_to:
          min: 1
          max: 1
        to_from:
          min: 0
          max: "N"
      relationship_attributes:
        - "numero_set"
        - "tempo_decorrido_segundos"
      exclusivity_rules:
        - "Os pontos acumulados no Estado do Placar pertencem unicamente ao set no qual foram marcados."
      rule_ids:
        - "REG-IHF-003"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_002"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_003"
      temporality: "INSTANTANEA"

    - id: "PARTIDA_REGISTRA_EVOLUCAO_PLACAR"
      name: "Partida registra Evolução do Placar"
      from_entity_id: "PARTIDA"
      to_entity_id: "EVOLUCAO_DO_PLACAR"
      meaning: "Associa a partida à série cronológica e ordenada de eventos de alteração de placar."
      cardinality:
        from_to:
          min: 0
          max: "N"
        to_from:
          min: 1
          max: 1
      relationship_attributes:
        - "sequencia_pontuacao"
        - "valor_incremento"
        - "equipe_beneficiada_id"
      exclusivity_rules:
        - "A sequência de alterações deve ser estritamente monotônica crescente no tempo."
      rule_ids:
        - "REG-IHF-003"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_006"
        - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_009"
      temporality: "EVENTO"

    - id: "POSSE_DE_BOLA_POSSUI_SISTEMA_DEFENSIVO"
      name: "Posse de Bola possui Sistema Defensivo"
      from_entity_id: "POSSE_DE_BOLA"
      to_entity_id: "SISTEMA_DEFENSIVO"
      meaning: "Caracteriza o arranjo tático estruturado da equipe defensora durante uma posse de bola."
      cardinality:
        from_to:
          min: 0
          max: 1
        to_from:
          min: 0
          max: "N"
      relationship_attributes:
        - "codigo_sistema_defensivo"
        - "disposicao_central_lateral"
      exclusivity_rules:
        - "Somente a equipe sem a posse de bola pode registrar um sistema defensivo ativo no intervalo."
      rule_ids:
        - "TAX-001"
      evidence_ref_ids:
        - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_006"
        - "EVID_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94_002"
      temporality: "INTERVALO"

    - id: "SISTEMA_DEFENSIVO_PERTENCE_A_EQUIPE"
      name: "Sistema Defensivo pertence a Equipe"
      from_entity_id: "SISTEMA_DEFENSIVO"
      to_entity_id: "EQUIPE"
      meaning: "Identifica explicitamente qual equipe adotou a configuração tática defensiva em quadra."
      cardinality:
        from_to:
          min: 1
          max: 1
        to_from:
          min: 0
          max: "N"
      relationship_attributes:
        - "equipe_defensora_id"
        - "em_desvantagem_numerica"
      exclusivity_rules:
        - "A equipe proprietária do sistema defensivo deve ser a equipe contrária ao possuidor da bola."
      rule_ids:
        - "TAX-001"
      evidence_ref_ids:
        - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_006"
      temporality: "INTERVALO"

    - id: "ANALISTA_OBSERVADOR_POSSUI_CONFIABILIDADE"
      name: "Analista Observador possui Confiabilidade"
      from_entity_id: "ANALISTA_OBSERVADOR"
      to_entity_id: "CONFIABILIDADE_OBSERVADOR"
      meaning: "Vincula o analista de scout ao seu histórico de testes de calibração e métricas de precisão."
      cardinality:
        from_to:
          min: 0
          max: "N"
        to_from:
          min: 1
          max: 1
      relationship_attributes:
        - "indice_kappa_cohen"
        - "indice_kappa_fleiss"
        - "taxa_acerto_percentual"
      exclusivity_rules:
        - "A avaliação de confiabilidade é individual e não pode ser compartilhada entre analistas."
      rule_ids:
        - "CON-006"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
      temporality: "VERSIONADA"

    - id: "OBSERVACAO_DE_SCOUT_SOFRE_REVISAO"
      name: "Observação de Scout sofre Revisão"
      from_entity_id: "OBSERVACAO_DE_SCOUT"
      to_entity_id: "REVISAO_DA_OBSERVACAO"
      meaning: "Registra os eventos formais de auditoria, edição e moderação sobre uma observação."
      cardinality:
        from_to:
          min: 0
          max: "N"
        to_from:
          min: 1
          max: 1
      relationship_attributes:
        - "timestamp_revisao"
        - "motivo_revisao"
        - "campo_alterado"
      exclusivity_rules:
        - "Cada evento de revisão modifica o registro mantendo a auditabilidade do histórico."
      rule_ids:
        - "DEC-001"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
      temporality: "EVENTO"

    - id: "REVISAO_DA_OBSERVACAO_EXECUTADA_POR_ANALISTA"
      name: "Revisão da Observação executada por Analista"
      from_entity_id: "REVISAO_DA_OBSERVACAO"
      to_entity_id: "ANALISTA_OBSERVADOR"
      meaning: "Identifica o analista observador com autoridade responsável pela execução da revisão."
      cardinality:
        from_to:
          min: 1
          max: 1
        to_from:
          min: 0
          max: "N"
      relationship_attributes:
        - "analista_revisor_id"
        - "nivel_autoridade"
      exclusivity_rules:
        - "O analista revisor deve ser um usuário autenticado e habilitado no protocolo CON-006."
      rule_ids:
        - "CON-006"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
      temporality: "EVENTO"

    - id: "REVISAO_DA_OBSERVACAO_GERA_ESTADO_DE_REVISAO"
      name: "Revisão da Observação gera Estado de Revisão"
      from_entity_id: "REVISAO_DA_OBSERVACAO"
      to_entity_id: "ESTADO_DE_REVISAO"
      meaning: "Mapeia a transição de estado da observação decorrente do evento de revisão efetuado."
      cardinality:
        from_to:
          min: 1
          max: 1
        to_from:
          min: 0
          max: "N"
      relationship_attributes:
        - "codigo_status_resultante"
        - "timestamp_transicao"
      exclusivity_rules:
        - "Uma revisão concluída atualiza obrigatoriamente o Estado de Revisão da observação."
      rule_ids:
        - "DEC-001"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
      temporality: "EVENTO"

    - id: "OBSERVACAO_DE_SCOUT_POSSUI_ESTADO_DE_REVISAO"
      name: "Observação de Scout possui Estado de Revisão"
      from_entity_id: "OBSERVACAO_DE_SCOUT"
      to_entity_id: "ESTADO_DE_REVISAO"
      meaning: "Indica a situação corrente de aprovação e governança da observação de scout."
      cardinality:
        from_to:
          min: 1
          max: 1
        to_from:
          min: 0
          max: "N"
      relationship_attributes:
        - "status_corrente"
        - "data_ultima_atualizacao"
      exclusivity_rules:
        - "A observação possui exatamente um Estado de Revisão ativo em um dado momento."
      rule_ids:
        - "DEC-001"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
      temporality: "VERSIONADA"

    - id: "OBSERVACAO_DE_SCOUT_TEM_PROVENIENCIA"
      name: "Observação de Scout tem Proveniência"
      from_entity_id: "OBSERVACAO_DE_SCOUT"
      to_entity_id: "PROVENIENCIA_OBSERVACAO"
      meaning: "Associa a observação de scout ao registro único e imutável de proveniência de dados."
      cardinality:
        from_to:
          min: 1
          max: 1
        to_from:
          min: 1
          max: 1
      relationship_attributes:
        - "ferramenta_software"
        - "versao_protocolo"
        - "checksum_midia"
      exclusivity_rules:
        - "A proveniência é gerada no momento do registro e torna-se imutável."
      rule_ids:
        - "DEC-001"
      evidence_ref_ids:
        - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_005"
      temporality: "ATEMPORAL"

    - id: "PROVENIENCIA_OBSERVACAO_VINCULA_PROTOCOLO_SCOUT"
      name: "Proveniência da Observação vincula Protocolo Scout"
      from_entity_id: "PROVENIENCIA_OBSERVACAO"
      to_entity_id: "PROTOCOLO_SCOUT"
      meaning: "Especifica a versão e diretrizes do protocolo metodológico seguidas na geração da observação."
      cardinality:
        from_to:
          min: 1
          max: 1
        to_from:
          min: 0
          max: "N"
      relationship_attributes:
        - "versao_protocolo_aplicada"
        - "guia_metodologia_ref"
      exclusivity_rules:
        - "O protocolo referenciado deve ser uma especificação cadastrada e ativa."
      rule_ids:
        - "DEC-001"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
      temporality: "ATEMPORAL"

    - id: "PROVENIENCIA_OBSERVACAO_REFERENCIA_MIDIA_VIDEO"
      name: "Proveniência da Observação referência Mídia Vídeo"
      from_entity_id: "PROVENIENCIA_OBSERVACAO"
      to_entity_id: "MIDIA_VIDEO"
      meaning: "Conecta a proveniência da observação ao arquivo físico de vídeo utilizado na codificação."
      cardinality:
        from_to:
          min: 1
          max: 1
        to_from:
          min: 0
          max: "N"
      relationship_attributes:
        - "arquivo_midia_id"
        - "hash_arquivo_video"
      exclusivity_rules:
        - "O hash do arquivo garante a integridade e não repúdio da fonte audiovisual."
      rule_ids:
        - "DEC-001"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
      temporality: "ATEMPORAL"

    - id: "EVENTO_SCOUT_VINCULA_TRECHO_OBSERVADO"
      name: "Evento Scout vincula Trecho Observado"
      from_entity_id: "EVENTO_SCOUT"
      to_entity_id: "TRECHO_OBSERVADO"
      meaning: "Associa o evento tático discreto de scout ao recorte preciso de timecode de vídeo."
      cardinality:
        from_to:
          min: 0
          max: "N"
        to_from:
          min: 1
          max: 1
      relationship_attributes:
        - "timecode_in"
        - "timecode_out"
        - "duracao_frames"
      exclusivity_rules:
        - "O trecho observado deve delimitar exatamente a janela de ocorrência da ação tática."
      rule_ids:
        - "DEC-001"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
      temporality: "INTERVALO"

    - id: "TRECHO_OBSERVADO_PERTENCE_A_MIDIA_VIDEO"
      name: "Trecho Observado pertence a Mídia Vídeo"
      from_entity_id: "TRECHO_OBSERVADO"
      to_entity_id: "MIDIA_VIDEO"
      meaning: "Identifica o arquivo de vídeo no qual o recorte delimitado de timecode está localizado."
      cardinality:
        from_to:
          min: 1
          max: 1
        to_from:
          min: 0
          max: "N"
      relationship_attributes:
        - "offset_milissegundos"
        - "velocidade_reproducao"
      exclusivity_rules:
        - "O intervalo do trecho observado não pode ultrapassar o limite temporal do arquivo de mídia."
      rule_ids:
        - "DEC-001"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
      temporality: "ATEMPORAL"

  domain_invariants:
    - id: "INV_EXCLUSIVIDADE_TRECHO_MIDIA"
      statement: "O intervalo temporal de um Trecho Observado deve estar estritamente contido dentro da duração total do arquivo de Mídia Vídeo associado."
      affected_entity_ids:
        - "TRECHO_OBSERVADO"
        - "MIDIA_VIDEO"
      rule_ids:
        - "DEC-001"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"

    - id: "INV_INTEGRIDADE_REVISAO_OBSERVACAO"
      statement: "Toda Revisão da Observação deve ser executada por um Analista Observador qualificado e resulta obrigatoriamente em transição do Estado de Revisão."
      affected_entity_ids:
        - "REVISAO_DA_OBSERVACAO"
        - "ESTADO_DE_REVISAO"
        - "ANALISTA_OBSERVADOR"
      rule_ids:
        - "CON-006"
        - "DEC-001"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"

    - id: "INV_QUALIFICACAO_MINIMA_OBSERVADOR"
      statement: "Um Analista Observador só pode ter suas observações validadas se possuir registro ativo de Confiabilidade do Observador com acerto mínimo de 90% (18/20) e zero erro crítico."
      affected_entity_ids:
        - "CONFIABILIDADE_OBSERVADOR"
        - "ANALISTA_OBSERVADOR"
      rule_ids:
        - "CON-006"
      evidence_ref_ids:
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"

    - id: "INV_CONSISTENCIA_EVOLUCAO_PLACAR"
      statement: "Os registros de Evolução do Placar devem ser ordenados cronologicamente sem lacunas e ser derivados exclusivamente de ocorrências com valor de 1 ou 2 pontos."
      affected_entity_ids:
        - "EVOLUCAO_DO_PLACAR"
        - "PLACAR_JOGO"
        - "PARTIDA"
      rule_ids:
        - "REG-IHF-003"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_006"
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_026"

    - id: "INV_PROVENIENCIA_RASTREAVEL"
      statement: "Toda Observação de Scout deve possuir registro único e imutável de Proveniência da Observação que ateste a ferramenta, protocolo, autor e arquivo de vídeo fonte."
      affected_entity_ids:
        - "PROVENIENCIA_OBSERVACAO"
        - "OBSERVACAO_DE_SCOUT"
        - "PROTOCOLO_SCOUT"
        - "MIDIA_VIDEO"
      rule_ids:
        - "DEC-001"
      evidence_ref_ids:
        - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_005"
        - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"

    - id: "INV_TAXONOMIA_SISTEMA_DEFENSIVO"
      statement: "O atributo codigo_sistema_defensivo da entidade Sistema Defensivo deve obrigatoriamente pertencer ao domínio tático padronizado ('3:0', '2:1', '1:2') conforme TAX-001."
      affected_entity_ids:
        - "SISTEMA_DEFENSIVO"
        - "POSSE_DE_BOLA"
        - "EQUIPE"
      rule_ids:
        - "TAX-001"
      evidence_ref_ids:
        - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_006"
        - "EVID_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94_002"

    - id: "INV_INCREMENTO_PONTUACAO_IHF"
      statement: "Cada evento individual registrado na Evolução do Placar deve incrementar o placar da equipe em exatamente 1 ponto (gol simples) ou 2 pontos (gols espetaculares, 6m, gol de goleiro/especialista), vedado qualquer outro valor."
      affected_entity_ids:
        - "EVOLUCAO_DO_PLACAR"
        - "ESTADO_DO_PLACAR"
      rule_ids:
        - "REG-IHF-003"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_006"
        - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_009"

    - id: "INV_LIMITACAO_PLACAR_SETS"
      statement: "A contagem consolidada de sets no Placar do Jogo é estritamente limitada aos placares de 2:0 ou 0:2 (vitória direta em dois sets) ou 2:1 ou 1:2 (vitória via Shoot-out após empate em sets)."
      affected_entity_ids:
        - "PLACAR_JOGO"
        - "PARTIDA"
        - "PERIODO_SET"
      rule_ids:
        - "REG-IHF-003"
      evidence_ref_ids:
        - "EVID_IHF_RULES_2026_EN_002"
        - "EVID_IHF_RULES_2026_EN_004"
        - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_026"

  coverage_updates:
    promote_to_covered_concept_ids:
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
    remove_open_issue_ids:
      - "ISSUE_COVERAGE_SEGMENTO_OBSERVADO"
      - "ISSUE_COVERAGE_PLACAR_JOGO"
      - "ISSUE_COVERAGE_ESTADO_DO_PLACAR"
      - "ISSUE_COVERAGE_EVOLUCAO_DO_PLACAR"
      - "ISSUE_COVERAGE_SISTEMA_DEFENSIVO"
      - "ISSUE_COVERAGE_CONFIABILIDADE_OBSERVADOR"
      - "ISSUE_COVERAGE_REVISAO_DA_OBSERVACAO"
      - "ISSUE_COVERAGE_ESTADO_DE_REVISAO"
      - "ISSUE_COVERAGE_PROVENIENCIA_OBSERVACAO"
      - "ISSUE_COVERAGE_TRECHO_OBSERVADO"
    remaining_open_issues: []
```