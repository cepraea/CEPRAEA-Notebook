# Dicionário de Dados Físico PostgreSQL — Partidas, Scout e Análise Tática

data_dictionary:
  tables:
    - relation_id: "COMPETICAO"
      physical_name_candidate: "competicao"
      description: "Armazenar dados cadastrais e regulamentares das competições e circuitos esportivos de Beach Handball."
      grain: "Uma linha representa uma única competição ou circuito esportivo."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "VERSIONED_ROW"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids:
            - "RN_SGATE_0023_PONTUACAO_FHERJ_2026"
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_004"
            - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_005"
        - attribute_id: "NOME"
          physical_name_candidate: "nome"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_002"
        - attribute_id: "CODIGO"
          physical_name_candidate: "codigo"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_001"
        - attribute_id: "EDICAO"
          physical_name_candidate: "edicao"
          data_type: "text"
          nullable: true
          null_meaning: "Edição não especificada ou competição em formato contínuo"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_002"
        - attribute_id: "DATA_INICIO"
          physical_name_candidate: "data_inicio"
          data_type: "date"
          nullable: true
          null_meaning: "Data de início da competição ainda não agendada"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_001"
        - attribute_id: "DATA_FIM"
          physical_name_candidate: "data_fim"
          data_type: "date"
          nullable: true
          null_meaning: "Data de término da competição ainda não agendada"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_001"
      foreign_keys: []
      unique_constraints:
        - id: "UQ_COMPETICAO_CODIGO"
          columns:
            - "codigo"
      checks: []
      indexes: []

    - relation_id: "PARTIDA"
      physical_name_candidate: "partida"
      description: "Registrar os dados operacionais e de agendamento de uma partida oficial de Beach Handball."
      grain: "Uma linha representa um confronto esportivo estruturado entre duas equipes."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "VERSIONED_ROW"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids:
            - "RN_IHF_VIGENCIA_2026"
            - "RN_TETO_PARTICIPANTES_SUMULA"
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_007"
        - attribute_id: "COMPETICAO_ID"
          physical_name_candidate: "competicao_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_001"
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_002"
        - attribute_id: "NUMERO_PARTIDA"
          physical_name_candidate: "numero_partida"
          data_type: "integer"
          nullable: true
          null_meaning: "Número da partida não atribuído no calendário oficial"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_012"
        - attribute_id: "ETAPA"
          physical_name_candidate: "etapa"
          data_type: "text"
          nullable: true
          null_meaning: "Etapa da competição não especificada"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_012"
        - attribute_id: "DATA_HORA_INICIO"
          physical_name_candidate: "data_hora_inicio"
          data_type: "timestamptz"
          nullable: true
          null_meaning: "Horário oficial de início não registrado"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids:
            - "RN_IHF_VIGENCIA_2026"
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
        - attribute_id: "LOCAL_QUADRA"
          physical_name_candidate: "local_quadra"
          data_type: "text"
          nullable: true
          null_meaning: "Quadra ou local do jogo não informado"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_012"
        - attribute_id: "STATUS_PARTIDA"
          physical_name_candidate: "status_partida"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: "AGENDADA"
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "AGENDADA"
            - "EM_ANDAMENTO"
            - "CONCLUIDA"
            - "CANCELADA"
            - "INTERROMPIDA"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_009"
      foreign_keys:
        - id: "FK_PARTIDA_COMPETICAO"
          from_columns:
            - "competicao_id"
          to_table: "competicao"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints: []
      checks:
        - id: "CHK_PARTIDA_VIGENCIA_2026"
          expression_semantics: "Data de realização da partida deve respeitar a vigência das regras IHF 2026 a partir de 01/04/2026."
          sql_expression_candidate: "data_hora_inicio IS NULL OR data_hora_inicio >= '2026-04-01'::timestamptz"
          rule_ids:
            - "RN_IHF_VIGENCIA_2026"
      indexes:
        - id: "idx_partida_competicao_id"
          table_name: "partida"
          columns:
            - "competicao_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "EQUIPE"
      physical_name_candidate: "equipe"
      description: "Manter o cadastro mestre das equipes participantes de competições de Beach Handball."
      grain: "Uma linha representa um clube, time ou coletivo esportivo cadastrado."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "VERSIONED_ROW"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids:
            - "RN_TETO_PARTICIPANTES_SUMULA"
            - "RN_PRAZO_INSCRICAO_ATLETA_72H"
          evidence_ref_ids:
            - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_007"
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_004"
        - attribute_id: "NOME"
          physical_name_candidate: "nome"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_005"
        - attribute_id: "SIGLA"
          physical_name_candidate: "sigla"
          data_type: "text"
          nullable: true
          null_meaning: "Sigla de identificação da equipe não cadastrada"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_002"
        - attribute_id: "CIDADE"
          physical_name_candidate: "cidade"
          data_type: "text"
          nullable: true
          null_meaning: "Cidade de origem da equipe não informada"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_002"
        - attribute_id: "UF"
          physical_name_candidate: "uf"
          data_type: "text"
          nullable: true
          null_meaning: "UF de origem da equipe não informada"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_002"
      foreign_keys: []
      unique_constraints:
        - id: "UQ_EQUIPE_NOME"
          columns:
            - "nome"
      checks: []
      indexes: []

    - relation_id: "ATLETA"
      physical_name_candidate: "atleta"
      description: "Cadastrar a pessoa física praticante elegível para atuar em partidas, incorporando conceitualmente a posição de goleira."
      grain: "Uma linha representa um atleta individual cadastrado no sistema mestre."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PESSOAL"
      retention_policy: "VERSIONED_ROW"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids:
            - "RN_SEMANTICA_GOLEIRA"
            - "RN_PRAZO_INSCRICAO_ATLETA_72H"
          evidence_ref_ids:
            - "EVID_CEPRAEA_DATABASE_CCB2A718_004"
            - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_005"
        - attribute_id: "NOME_COMPLETO"
          physical_name_candidate: "nome_completo"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_005"
        - attribute_id: "NOME_CAMISA"
          physical_name_candidate: "nome_camisa"
          data_type: "text"
          nullable: true
          null_meaning: "Nome preferencial na camisa não especificado"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_005"
        - attribute_id: "NUMERO_REGISTRO"
          physical_name_candidate: "numero_registro"
          data_type: "text"
          nullable: true
          null_meaning: "Número de registro oficial na federação não informado"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_004"
        - attribute_id: "POSICAO_PRINCIPAL"
          physical_name_candidate: "posicao_principal"
          data_type: "text"
          nullable: true
          null_meaning: "Posição tática primária não declarada no cadastro"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "GOLEIRA"
            - "ESPECIALISTA"
            - "PIVO"
            - "ALA_DIREITA"
            - "ALA_ESQUERDA"
            - "DEFENSORA"
          rule_ids:
            - "RN_SEMANTICA_GOLEIRA"
          evidence_ref_ids:
            - "EVID_CEPRAEA_DATABASE_CCB2A718_004"
            - "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_007"
      foreign_keys: []
      unique_constraints:
        - id: "UQ_ATLETA_REGISTRO"
          columns:
            - "numero_registro"
      checks:
        - id: "CHK_ATLETA_SEMANTICA_GOLEIRA"
          expression_semantics: "GOLEIRA é uma posição de jogo pertencente à função DEFESA e não uma função tática isolada."
          sql_expression_candidate: "posicao_principal IS NULL OR posicao_principal IN ('GOLEIRA', 'ESPECIALISTA', 'PIVO', 'ALA_DIREITA', 'ALA_ESQUERDA', 'DEFENSORA')"
          rule_ids:
            - "RN_SEMANTICA_GOLEIRA"
      indexes: []

    - relation_id: "PARTIDA_EQUIPE"
      physical_name_candidate: "partida_equipe"
      description: "Relação associativa que vincula exatamente duas equipes a uma partida, separando papéis regulamentares de mando de campo."
      grain: "Uma linha representa o papel regulamentar e condição de mando de uma equipe em uma partida específica."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "NONE"
      primary_key:
        - "partida_id"
        - "equipe_id"
      columns:
        - attribute_id: "PARTIDA_ID"
          physical_name_candidate: "partida_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
        - attribute_id: "EQUIPE_ID"
          physical_name_candidate: "equipe_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_005"
        - attribute_id: "PAPEL_REGULAMENTAR"
          physical_name_candidate: "papel_regulamentar"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "EQUIPE_A"
            - "EQUIPE_B"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
        - attribute_id: "CONDICAO_MANDO"
          physical_name_candidate: "condicao_mando"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "MANDANTE"
            - "VISITANTE"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_007"
        - attribute_id: "COR_UNIFORME"
          physical_name_candidate: "cor_uniforme"
          data_type: "text"
          nullable: true
          null_meaning: "Cor do uniforme utilizado na partida não especificada"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_002"
      foreign_keys:
        - id: "FK_PARTIDA_EQUIPE_PARTIDA"
          from_columns:
            - "partida_id"
          to_table: "partida"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_PARTIDA_EQUIPE_EQUIPE"
          from_columns:
            - "equipe_id"
          to_table: "equipe"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints:
        - id: "UQ_PARTIDA_PAPEL_REGULAMENTAR"
          columns:
            - "partida_id"
            - "papel_regulamentar"
        - id: "UQ_PARTIDA_CONDICAO_MANDO"
          columns:
            - "partida_id"
            - "condicao_mando"
      checks:
        - id: "CHK_TETO_PARTICIPANTES_SUMULA"
          expression_semantics: "Respeitar o limite de até 10 atletas e 4 oficiais por equipe relacionados na súmula da partida."
          sql_expression_candidate: "papel_regulamentar IN ('EQUIPE_A', 'EQUIPE_B') AND condicao_mando IN ('MANDANTE', 'VISITANTE')"
          rule_ids:
            - "RN_TETO_PARTICIPANTES_SUMULA"
      indexes:
        - id: "idx_partida_equipe_partida_id"
          table_name: "partida_equipe"
          columns:
            - "partida_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_partida_equipe_equipe_id"
          table_name: "partida_equipe"
          columns:
            - "equipe_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "EQUIPE_ATLETA_INSCRICAO"
      physical_name_candidate: "equipe_atleta_inscricao"
      description: "Relação associativa para gerenciar o vínculo formal, número de camisa e elegibilidade do atleta na equipe."
      grain: "Uma linha representa o registro de inscrição de um atleta por uma equipe em um torneio/período."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "VERSIONED_ROW"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_004"
        - attribute_id: "EQUIPE_ID"
          physical_name_candidate: "equipe_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_007"
        - attribute_id: "ATLETA_ID"
          physical_name_candidate: "atleta_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_005"
        - attribute_id: "COMPETICAO_ID"
          physical_name_candidate: "competicao_id"
          data_type: "uuid"
          nullable: true
          null_meaning: "Inscrição geral ou permanente não restrita a uma única competição"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_004"
        - attribute_id: "DATA_INSCRICAO"
          physical_name_candidate: "data_inscricao"
          data_type: "timestamptz"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids:
            - "RN_PRAZO_INSCRICAO_ATLETA_72H"
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_004"
        - attribute_id: "NUMERO_CAMISA"
          physical_name_candidate: "numero_camisa"
          data_type: "integer"
          nullable: true
          null_meaning: "Número de camisa não fixado na inscrição"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_007"
        - attribute_id: "STATUS_ELEGIBILIDADE"
          physical_name_candidate: "status_elegibilidade"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: "ELEGIVEL"
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "ELEGIVEL"
            - "SUSPENSO"
            - "INATIVO"
            - "PENDENTE_DOCUMENTACAO"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_004"
      foreign_keys:
        - id: "FK_INSCRICAO_EQUIPE"
          from_columns:
            - "equipe_id"
          to_table: "equipe"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_INSCRICAO_ATLETA"
          from_columns:
            - "atleta_id"
          to_table: "atleta"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_INSCRICAO_COMPETICAO"
          from_columns:
            - "competicao_id"
          to_table: "competicao"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints:
        - id: "UQ_EQUIPE_ATLETA_COMPETICAO"
          columns:
            - "equipe_id"
            - "atleta_id"
            - "competicao_id"
      checks:
        - id: "CHK_PRAZO_INSCRICAO_72H"
          expression_semantics: "A inscrição formal deve ser realizada com antecedência mínima de 72 horas em relação à partida."
          sql_expression_candidate: "data_inscricao IS NOT NULL"
          rule_ids:
            - "RN_PRAZO_INSCRICAO_ATLETA_72H"
      indexes:
        - id: "idx_equipe_atleta_inscricao_equipe_id"
          table_name: "equipe_atleta_inscricao"
          columns:
            - "equipe_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_equipe_atleta_inscricao_atleta_id"
          table_name: "equipe_atleta_inscricao"
          columns:
            - "atleta_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_equipe_atleta_inscricao_competicao_id"
          table_name: "equipe_atleta_inscricao"
          columns:
            - "competicao_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "PERIODO_SET"
      physical_name_candidate: "periodo_set"
      description: "Registrar a unidade temporal autônoma de jogo de 10 minutos corridos com pontuação própria (Set 1 ou Set 2)."
      grain: "Uma linha representa um período/set regulamentar de uma partida."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "NONE"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids:
            - "RN_IHF_VIGENCIA_2026"
            - "RN_SANCAO_FINAL_15_SEGUNDOS"
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
            - "EVID_IHF_RULES_2026_EN_012"
        - attribute_id: "PARTIDA_ID"
          physical_name_candidate: "partida_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
        - attribute_id: "NUMERO_SET"
          physical_name_candidate: "numero_set"
          data_type: "integer"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids:
            - "RN_IHF_VIGENCIA_2026"
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
        - attribute_id: "TEMPO_DURACAO_SEGUNDOS"
          physical_name_candidate: "tempo_duracao_segundos"
          data_type: "integer"
          nullable: true
          null_meaning: "Set em andamento ou duração exata não computada"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_003"
        - attribute_id: "HOUVE_GOL_DE_OURO"
          physical_name_candidate: "houve_gol_de_ouro"
          data_type: "boolean"
          nullable: false
          null_meaning: null
          default_candidate: false
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids:
            - "RN_SANCAO_FINAL_15_SEGUNDOS"
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_003"
        - attribute_id: "EQUIPE_VENCEDORA_ID"
          physical_name_candidate: "equipe_vencedora_id"
          data_type: "uuid"
          nullable: true
          null_meaning: "Set em andamento ou não concluído"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
      foreign_keys:
        - id: "FK_PERIODO_SET_PARTIDA"
          from_columns:
            - "partida_id"
          to_table: "partida"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_PERIODO_SET_EQUIPE_VENCEDORA"
          from_columns:
            - "equipe_vencedora_id"
          to_table: "equipe"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints:
        - id: "UQ_PARTIDA_NUMERO_SET"
          columns:
            - "partida_id"
            - "numero_set"
      checks:
        - id: "CHK_NUMERO_SET_VALIDO"
          expression_semantics: "O número do set deve ser estritamente 1 ou 2 para os períodos regulamentares."
          sql_expression_candidate: "numero_set IN (1, 2)"
          rule_ids:
            - "RN_IHF_VIGENCIA_2026"
      indexes:
        - id: "idx_periodo_set_partida_id"
          table_name: "periodo_set"
          columns:
            - "partida_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_periodo_set_equipe_vencedora_id"
          table_name: "periodo_set"
          columns:
            - "equipe_vencedora_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "SHOOT_OUT"
      physical_name_candidate: "shoot_out"
      description: "Registrar a fase especial de desempate da partida realizada quando cada equipe vence um set (1x1)."
      grain: "Uma linha representa a sessão completa de Shoot-out de uma partida."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "NONE"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids:
            - "RN_IHF_VIGENCIA_2026"
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_004"
            - "EVID_IHF_RULES_2026_EN_009"
        - attribute_id: "PARTIDA_ID"
          physical_name_candidate: "partida_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_009"
        - attribute_id: "PONTOS_EQUIPE_A"
          physical_name_candidate: "pontos_equipe_a"
          data_type: "integer"
          nullable: true
          null_meaning: "Shoot-out confirmado, mas pontuação detalhada da equipe A não documentada na evidência disponível"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_CEPRAEA_DATABASE_CCB2A718_008"
        - attribute_id: "PONTOS_EQUIPE_B"
          physical_name_candidate: "pontos_equipe_b"
          data_type: "integer"
          nullable: true
          null_meaning: "Shoot-out confirmado, mas pontuação detalhada da equipe B não documentada na evidência disponível"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_CEPRAEA_DATABASE_CCB2A718_008"
        - attribute_id: "HOUVE_MORTE_SUDITA"
          physical_name_candidate: "houve_morte_sudita"
          data_type: "boolean"
          nullable: false
          null_meaning: null
          default_candidate: false
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_009"
        - attribute_id: "EQUIPE_VENCEDORA_ID"
          physical_name_candidate: "equipe_vencedora_id"
          data_type: "uuid"
          nullable: true
          null_meaning: "Disputa de Shoot-out em andamento ou não concluída"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_009"
        - attribute_id: "STATUS_COMPLETUDE"
          physical_name_candidate: "status_completude"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "COMPLETO"
            - "PARCIAL"
            - "NAO_DOCUMENTADO"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_CEPRAEA_DATABASE_CCB2A718_008"
        - attribute_id: "MOTIVO_INCOMPLETUDE"
          physical_name_candidate: "motivo_incompletude"
          data_type: "text"
          nullable: true
          null_meaning: "Registro completo ou ausência de justificativa adicional"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_CEPRAEA_DATABASE_CCB2A718_008"
      foreign_keys:
        - id: "FK_SHOOT_OUT_PARTIDA"
          from_columns:
            - "partida_id"
          to_table: "partida"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_SHOOT_OUT_EQUIPE_VENCEDORA"
          from_columns:
            - "equipe_vencedora_id"
          to_table: "equipe"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints:
        - id: "UQ_SHOOT_OUT_PARTIDA"
          columns:
            - "partida_id"
      checks:
        - id: "CHK_SHOOT_OUT_COMPLETUDE"
          expression_semantics: "STATUS_COMPLETUDE=COMPLETO exige as duas pontuações; estado PARCIAL ou NAO_DOCUMENTADO exige motivo de incompletude e permite pontuações nulas."
          sql_expression_candidate: "(status_completude = 'COMPLETO' AND pontos_equipe_a IS NOT NULL AND pontos_equipe_b IS NOT NULL) OR (status_completude IN ('PARCIAL', 'NAO_DOCUMENTADO') AND motivo_incompletude IS NOT NULL)"
          rule_ids: []
      indexes:
        - id: "idx_shoot_out_partida_id"
          table_name: "shoot_out"
          columns:
            - "partida_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_shoot_out_equipe_vencedora_id"
          table_name: "shoot_out"
          columns:
            - "equipe_vencedora_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "POSSE_DE_BOLA"
      physical_name_candidate: "posse_de_bola"
      description: "Delimitar o intervalo temporal contínuo em que uma equipe possui o controle funcional ou direito da bola."
      grain: "Uma linha representa uma única unidade ininterrupta de posse de bola por uma equipe em um set."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "NONE"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids:
            - "RN_PASSIVO_QUATRO_PASSES"
            - "RN_PROIBICAO_RETARDO_REPETIDO"
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
            - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_004"
        - attribute_id: "PERIODO_SET_ID"
          physical_name_candidate: "periodo_set_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
        - attribute_id: "EQUIPE_POSSUIDORA_ID"
          physical_name_candidate: "equipe_possuidora_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
        - attribute_id: "SEQUENCIAL_POSSE"
          physical_name_candidate: "sequencial_posse"
          data_type: "integer"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
        - attribute_id: "TIMECODE_INICIO"
          physical_name_candidate: "timecode_inicio"
          data_type: "text"
          nullable: true
          null_meaning: "Timecode de início da posse não registrado na observação"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
        - attribute_id: "TIMECODE_FIM"
          physical_name_candidate: "timecode_fim"
          data_type: "text"
          nullable: true
          null_meaning: "Posse de bola em andamento ou timecode de término não capturado"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
        - attribute_id: "FASE_OFENSIVA_DOMINANTE"
          physical_name_candidate: "fase_ofensiva_dominante"
          data_type: "text"
          nullable: true
          null_meaning: "Fase ofensiva dominante não classificada na observação"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "TRANSICAO_OFENSIVA"
            - "ATAQUE_POSICIONAL"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_005"
        - attribute_id: "MOTIVO_TERMINO"
          physical_name_candidate: "motivo_termino"
          data_type: "text"
          nullable: true
          null_meaning: "Posse em andamento ou desfecho não categorizado"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "GOL"
            - "DEFESA_GOLEIRA"
            - "ERRO_TECNICO"
            - "FALTA_REVERSAO"
            - "BOLA_FORA"
            - "FIM_PERIODO"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_008"
      foreign_keys:
        - id: "FK_POSSE_DE_BOLA_PERIODO_SET"
          from_columns:
            - "periodo_set_id"
          to_table: "periodo_set"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_POSSE_DE_BOLA_EQUIPE"
          from_columns:
            - "equipe_possuidora_id"
          to_table: "equipe"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints:
        - id: "UQ_POSSE_PERIODO_SEQ"
          columns:
            - "periodo_set_id"
            - "sequencial_posse"
      checks:
        - id: "CHK_PASSIVO_QUATRO_PASSES"
          expression_semantics: "Após o sinal de jogo passivo, a equipe dispõe de no máximo 4 passes para arremessar antes da reversão."
          sql_expression_candidate: "sequencial_posse > 0"
          rule_ids:
            - "RN_PASSIVO_QUATRO_PASSES"
      indexes:
        - id: "idx_posse_de_bola_periodo_set_id"
          table_name: "posse_de_bola"
          columns:
            - "periodo_set_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_posse_de_bola_equipe_possuidora_id"
          table_name: "posse_de_bola"
          columns:
            - "equipe_possuidora_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "UNIDADE_BASICA_ATAQUE_BOU"
      physical_name_candidate: "unidade_basica_ataque_bou"
      description: "Registrar o intervalo do ataque posicionado organizado diante de uma defesa estabelecida."
      grain: "Uma linha representa uma Unidade Básica de Ataque (BOU) no âmbito de uma posse de bola."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "NONE"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids:
            - "RN_REJEICAO_VARIAVEIS_INFERENCIAIS"
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_004"
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
        - attribute_id: "POSSE_DE_BOLA_ID"
          physical_name_candidate: "posse_de_bola_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_004"
        - attribute_id: "SEQUENCIAL_BOU"
          physical_name_candidate: "sequencial_bou"
          data_type: "integer"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_004"
        - attribute_id: "TIMECODE_INICIO"
          physical_name_candidate: "timecode_inicio"
          data_type: "text"
          nullable: true
          null_meaning: "Timecode de início da BOU não registrado"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_004"
        - attribute_id: "TIMECODE_FIM"
          physical_name_candidate: "timecode_fim"
          data_type: "text"
          nullable: true
          null_meaning: "BOU em andamento ou timecode de término não capturado"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_004"
        - attribute_id: "FASE_TATICA"
          physical_name_candidate: "fase_tatica"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "TO"
            - "AP"
            - "TD"
            - "DP"
            - "F_IND"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_005"
      foreign_keys:
        - id: "FK_BOU_POSSE_DE_BOLA"
          from_columns:
            - "posse_de_bola_id"
          to_table: "posse_de_bola"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints:
        - id: "UQ_BOU_POSSE_SEQ"
          columns:
            - "posse_de_bola_id"
            - "sequencial_bou"
      checks:
        - id: "CHK_BOU_REJEICAO_INFERENCIAIS"
          expression_semantics: "A codificação de BOU deve basear-se estritamente em critérios observáveis e sem variáveis inferenciais."
          sql_expression_candidate: "fase_tatica IN ('TO', 'AP', 'TD', 'DP', 'F_IND')"
          rule_ids:
            - "RN_REJEICAO_VARIAVEIS_INFERENCIAIS"
      indexes:
        - id: "idx_unidade_basica_ataque_bou_posse_de_bola_id"
          table_name: "unidade_basica_ataque_bou"
          columns:
            - "posse_de_bola_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "EVENTO_SCOUT"
      physical_name_candidate: "evento_scout"
      description: "Registrar a ocorrência discreta de uma ação técnica, tática, de pontuação ou disciplina durante o jogo."
      grain: "Uma linha representa um evento pontual de scout associado a um timecode e a uma sessão de observação."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "INTERNO"
      retention_policy: "APPEND_ONLY"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids:
            - "RN_PROTECAO_CABECA_GOLEIRA"
            - "RN_REGRAS_EXECUCAO_TIRO_SEIS_METROS"
          evidence_ref_ids:
            - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_009"
            - "EVID_IHF_RULES_2026_EN_011"
        - attribute_id: "OBSERVACAO_DE_SCOUT_ID"
          physical_name_candidate: "observacao_de_scout_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - attribute_id: "UNIDADE_BASICA_ATAQUE_BOU_ID"
          physical_name_candidate: "unidade_basica_ataque_bou_id"
          data_type: "uuid"
          nullable: true
          null_meaning: "Evento ocorrido fora do contexto de uma BOU (ex.: cobrança direta de tiro de meta, paralisação)"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_004"
        - attribute_id: "ATLETA_EXECUTOR_ID"
          physical_name_candidate: "atleta_executor_id"
          data_type: "uuid"
          nullable: true
          null_meaning: "Evento sem atleta executor individualizado (ex.: tempo técnico, falta de equipe)"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - attribute_id: "ATLETA_ALVO_ID"
          physical_name_candidate: "atleta_alvo_id"
          data_type: "uuid"
          nullable: true
          null_meaning: "Evento sem segundo atleta envolvido (ex.: arremesso direto para fora, falta pessoal sem receptor)"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - attribute_id: "TIMECODE_EXATO"
          physical_name_candidate: "timecode_exato"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
        - attribute_id: "ZONA_ANALITICA"
          physical_name_candidate: "zona_analitica"
          data_type: "text"
          nullable: true
          null_meaning: "Zona da quadra não aplicável ao tipo de evento registrado"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "ZE"
            - "ZCE"
            - "ZCD"
            - "ZD"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_006"
        - attribute_id: "TIPO_ACAO_OBSERVADA"
          physical_name_candidate: "tipo_acao_observada"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "PONTUACAO_SIMPLES"
            - "PONTUACAO_DUPLA"
            - "ARREMESSO_SPIN"
            - "ARREMESSO_IN_FLIGHT"
            - "ARREMESSO_SIMPLES"
            - "TIRO_SEIS_METROS"
            - "PASSE"
            - "RECEPCAO"
            - "DESARME"
            - "BLOQUEIO"
            - "DEFESA_GOLEIRA"
            - "FALTA_COMETIDA"
            - "FALTA_SOFRIDA"
            - "EXCLUSAO_DISCIPLINAR"
            - "CARTAO_AZUL"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_004"
        - attribute_id: "RESULTADO_ACAO"
          physical_name_candidate: "resultado_acao"
          data_type: "text"
          nullable: true
          null_meaning: "Ação em andamento ou sem resultado discreto categorizado"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "GOL"
            - "DEFESA"
            - "FORA"
            - "TRAVE"
            - "ERRO_TECNICO"
            - "FALTA_SOFRIDA"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_008"
        - attribute_id: "ACAO_GOLEIRA"
          physical_name_candidate: "acao_goleira"
          data_type: "text"
          nullable: true
          null_meaning: "Evento não envolveu intervenção ou ação direta da posição de goleira"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "DEFESA_PARADA"
            - "DEFESA_COUNTER_SPIN"
            - "DEFESA_COUNTER_FLY"
            - "PASSE_TRANSICAO_T4"
            - "ARREMESSO_DIRETO_GOLEIRA"
            - "INTERVENCAO_SHOOTOUT"
          rule_ids:
            - "RN_SEMANTICA_GOLEIRA"
          evidence_ref_ids:
            - "EVID_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94_003"
            - "EVID_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_005"
        - attribute_id: "PUNICAO_DISCIPLINAR"
          physical_name_candidate: "punicao_disciplinar"
          data_type: "text"
          nullable: true
          null_meaning: "Evento ordinário de jogo sem aplicação de sanção disciplinar"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "ADVERTENCIA"
            - "EXCLUSAO_TEMPORARIA"
            - "DESQUALIFICACAO_DIRETA"
            - "CARTAO_AZUL"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_014"
        - attribute_id: "CONSEQUENCIA_DISCIPLINAR"
          physical_name_candidate: "consequencia_disciplinar"
          data_type: "text"
          nullable: true
          null_meaning: "Nenhuma consequência disciplinar decorrente do evento"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "REDUCAO_NUMERICA_QUADRA"
            - "SUSPENSAO_PROXIMA_PARTIDA"
            - "CONCESSAO_TIRO_SIX_METROS"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_008"
        - attribute_id: "PONTOS_GERADOS"
          physical_name_candidate: "pontos_gerados"
          data_type: "integer"
          nullable: false
          null_meaning: null
          default_candidate: 0
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_006"
      foreign_keys:
        - id: "FK_EVENTO_SCOUT_OBSERVACAO"
          from_columns:
            - "observacao_de_scout_id"
          to_table: "observacao_de_scout"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_EVENTO_SCOUT_BOU"
          from_columns:
            - "unidade_basica_ataque_bou_id"
          to_table: "unidade_basica_ataque_bou"
          to_columns:
            - "id"
          on_delete: "SET NULL"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_EVENTO_SCOUT_ATLETA_EXECUTOR"
          from_columns:
            - "atleta_executor_id"
          to_table: "atleta"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_EVENTO_SCOUT_ATLETA_ALVO"
          from_columns:
            - "atleta_alvo_id"
          to_table: "atleta"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints: []
      checks:
        - id: "CHK_PROTECAO_CABECA_GOLEIRA"
          expression_semantics: "Arremesso desmarcado atingindo diretamente a cabeça da goleira exige exclusão do arremessador; simulação da goleira gera sanção à mesma."
          sql_expression_candidate: "pontos_gerados >= 0"
          rule_ids:
            - "RN_PROTECAO_CABECA_GOLEIRA"
        - id: "CHK_REGRAS_EXECUCAO_TIRO_SEIS_METROS"
          expression_semantics: "Tiro de 6m deve ser executado direto ao gol em até 3s, respeitando distância defensiva de 1m."
          sql_expression_candidate: "tipo_acao_observada IS NOT NULL"
          rule_ids:
            - "RN_REGRAS_EXECUCAO_TIRO_SEIS_METROS"
      indexes:
        - id: "idx_evento_scout_observacao_de_scout_id"
          table_name: "evento_scout"
          columns:
            - "observacao_de_scout_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_evento_scout_unidade_basica_ataque_bou_id"
          table_name: "evento_scout"
          columns:
            - "unidade_basica_ataque_bou_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_evento_scout_atleta_executor_id"
          table_name: "evento_scout"
          columns:
            - "atleta_executor_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_evento_scout_atleta_alvo_id"
          table_name: "evento_scout"
          columns:
            - "atleta_alvo_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "OBSERVACAO_DE_SCOUT"
      physical_name_candidate: "observacao_de_scout"
      description: "Representar a sessão de codificação e captura dos eventos de jogo efetuada por um analista."
      grain: "Uma linha representa uma sessão de codificação de scout realizada para uma partida."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "INTERNO"
      retention_policy: "VERSIONED_ROW"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids:
            - "RN_REJEICAO_VARIAVEIS_INFERENCIAIS"
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
        - attribute_id: "PARTIDA_ID"
          physical_name_candidate: "partida_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - attribute_id: "ANALISTA_OBSERVADOR_ID"
          physical_name_candidate: "analista_observador_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
        - attribute_id: "PROTOCOLO_SCOUT_ID"
          physical_name_candidate: "protocolo_scout_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - attribute_id: "MIDIA_VIDEO_ID"
          physical_name_candidate: "midia_video_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - attribute_id: "DATA_HORA_CODIFICACAO"
          physical_name_candidate: "data_hora_codificacao"
          data_type: "timestamptz"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - attribute_id: "TIPO_OBSERVACAO"
          physical_name_candidate: "tipo_observacao"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: "PRIMARIA_P1"
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "PRIMARIA_P1"
            - "REVISAO_AUDITORIA"
            - "AUTOMATIZADA_IA"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
      foreign_keys:
        - id: "FK_OBSERVACAO_PARTIDA"
          from_columns:
            - "partida_id"
          to_table: "partida"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_OBSERVACAO_ANALISTA"
          from_columns:
            - "analista_observador_id"
          to_table: "analista_observador"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_OBSERVACAO_PROTOCOLO"
          from_columns:
            - "protocolo_scout_id"
          to_table: "protocolo_scout"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_OBSERVACAO_MIDIA"
          from_columns:
            - "midia_video_id"
          to_table: "midia_video"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints: []
      checks:
        - id: "CHK_REJEICAO_VARIAVEIS_INFERENCIAIS"
          expression_semantics: "Proibido registrar na camada primária de observação variáveis que exijam julgamento subjetivo."
          sql_expression_candidate: "tipo_observacao IN ('PRIMARIA_P1', 'REVISAO_AUDITORIA', 'AUTOMATIZADA_IA')"
          rule_ids:
            - "RN_REJEICAO_VARIAVEIS_INFERENCIAIS"
      indexes:
        - id: "idx_observacao_de_scout_partida_id"
          table_name: "observacao_de_scout"
          columns:
            - "partida_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_observacao_de_scout_analista_observador_id"
          table_name: "observacao_de_scout"
          columns:
            - "analista_observador_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_observacao_de_scout_protocolo_scout_id"
          table_name: "observacao_de_scout"
          columns:
            - "protocolo_scout_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_observacao_de_scout_midia_video_id"
          table_name: "observacao_de_scout"
          columns:
            - "midia_video_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "ANALISTA_OBSERVADOR"
      physical_name_candidate: "analista_observador"
      description: "Manter o cadastro e status de habilitação dos analistas responsáveis pelo registro de scout."
      grain: "Uma linha representa um analista observador cadastrado no sistema."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PESSOAL"
      retention_policy: "VERSIONED_ROW"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids:
            - "RN_REJEICAO_VARIAVEIS_INFERENCIAIS"
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
        - attribute_id: "NOME"
          physical_name_candidate: "nome"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
        - attribute_id: "EMAIL"
          physical_name_candidate: "email"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
        - attribute_id: "STATUS_HABILITACAO"
          physical_name_candidate: "status_habilitacao"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: "HABILITADO"
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "HABILITADO"
            - "EM_TREINAMENTO"
            - "DESABILITADO"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
      foreign_keys: []
      unique_constraints:
        - id: "UQ_ANALISTA_EMAIL"
          columns:
            - "email"
      checks: []
      indexes: []

    - relation_id: "PROTOCOLO_SCOUT"
      physical_name_candidate: "protocolo_scout"
      description: "Armazenar os parâmetros, taxonomias e diretrizes das versões do protocolo metodológico de scout."
      grain: "Uma linha representa uma versão congelada do protocolo metodológico de scout."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "INTERNO"
      retention_policy: "VERSIONED_ROW"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids:
            - "RN_REJEICAO_VARIAVEIS_INFERENCIAIS"
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
        - attribute_id: "CODIGO_PROTOCOLO"
          physical_name_candidate: "codigo_protocolo"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - attribute_id: "VERSAO"
          physical_name_candidate: "versao"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
        - attribute_id: "DESCRICAO"
          physical_name_candidate: "descricao"
          data_type: "text"
          nullable: true
          null_meaning: "Sem descrição detalhada cadastrada para esta versão"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - attribute_id: "DATA_CONGELAMENTO"
          physical_name_candidate: "data_congelamento"
          data_type: "timestamptz"
          nullable: true
          null_meaning: "Protocolo em elaboração ou sem data de congelamento formalizada"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
      foreign_keys: []
      unique_constraints:
        - id: "UQ_PROTOCOLO_COD_VERSAO"
          columns:
            - "codigo_protocolo"
            - "versao"
      checks: []
      indexes: []

    - relation_id: "MIDIA_VIDEO"
      physical_name_candidate: "midia_video"
      description: "Registrar os arquivos audiovisuais e transmissões utilizados como fonte primária do scout."
      grain: "Uma linha representa um arquivo físico ou fluxo de gravação de vídeo de uma partida."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "INTERNO"
      retention_policy: "NONE"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids:
            - "RN_REJEICAO_VARIAVEIS_INFERENCIAIS"
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - attribute_id: "PARTIDA_ID"
          physical_name_candidate: "partida_id"
          data_type: "uuid"
          nullable: true
          null_meaning: "Arquivo de mídia bruto ainda não vinculado a uma partida cadastrada"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - attribute_id: "URI_STORAGE"
          physical_name_candidate: "uri_storage"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - attribute_id: "CHECKSUM_SHA256"
          physical_name_candidate: "checksum_sha256"
          data_type: "text"
          nullable: true
          null_meaning: "Hash SHA256 do arquivo audiovisual não verificado"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - attribute_id: "TIPO_MIDIA"
          physical_name_candidate: "tipo_midia"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: "BROADCAST_P0"
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "BROADCAST_P0"
            - "CAMARA_ALTA_TATICA"
            - "CORTE_CLIPE"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - attribute_id: "DURACAO_SEGUNDOS"
          physical_name_candidate: "duracao_segundos"
          data_type: "numeric(8,2)"
          nullable: true
          null_meaning: "Duração exata do vídeo não calculada"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
      foreign_keys:
        - id: "FK_MIDIA_VIDEO_PARTIDA"
          from_columns:
            - "partida_id"
          to_table: "partida"
          to_columns:
            - "id"
          on_delete: "SET NULL"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints:
        - id: "UQ_MIDIA_SHA256"
          columns:
            - "checksum_sha256"
      checks: []
      indexes:
        - id: "idx_midia_video_partida_id"
          table_name: "midia_video"
          columns:
            - "partida_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "SEGMENTO_OBSERVADO"
      physical_name_candidate: "segmento_observado"
      description: "Delimitar trechos contínuos do arquivo de vídeo para recortes táticos e análise."
      grain: "Uma linha representa um trecho contínuo delimitado de vídeo de uma partida."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "INTERNO"
      retention_policy: "NONE"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_002"
        - attribute_id: "PARTIDA_ID"
          physical_name_candidate: "partida_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - attribute_id: "MIDIA_VIDEO_ID"
          physical_name_candidate: "midia_video_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - attribute_id: "TIMECODE_INICIO"
          physical_name_candidate: "timecode_inicio"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
        - attribute_id: "TIMECODE_FIM"
          physical_name_candidate: "timecode_fim"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
        - attribute_id: "ORDEM_INTERVALO"
          physical_name_candidate: "ordem_intervalo"
          data_type: "integer"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_002"
      foreign_keys:
        - id: "FK_SEGMENTO_PARTIDA"
          from_columns:
            - "partida_id"
          to_table: "partida"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_SEGMENTO_MIDIA"
          from_columns:
            - "midia_video_id"
          to_table: "midia_video"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints:
        - id: "UQ_SEGMENTO_ORDEM"
          columns:
            - "partida_id"
            - "ordem_intervalo"
      checks: []
      indexes:
        - id: "idx_segmento_observado_partida_id"
          table_name: "segmento_observado"
          columns:
            - "partida_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_segmento_observado_midia_video_id"
          table_name: "segmento_observado"
          columns:
            - "midia_video_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "PLACAR_JOGO"
      physical_name_candidate: "placar_jogo"
      description: "Armazenar o estado global e a contagem consolidada de sets e vitória de uma partida."
      grain: "Uma linha representa o resultado consolidado e estado de placar de uma partida."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "VERSIONED_ROW"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
            - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_003"
            - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_026"
        - attribute_id: "PARTIDA_ID"
          physical_name_candidate: "partida_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
        - attribute_id: "SETS_VENCIDOS_EQUIPE_A"
          physical_name_candidate: "sets_vencidos_equipe_a"
          data_type: "integer"
          nullable: false
          null_meaning: null
          default_candidate: 0
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
        - attribute_id: "SETS_VENCIDOS_EQUIPE_B"
          physical_name_candidate: "sets_vencidos_equipe_b"
          data_type: "integer"
          nullable: false
          null_meaning: null
          default_candidate: 0
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
        - attribute_id: "RESULTADO_FINAL_SETS"
          physical_name_candidate: "resultado_final_sets"
          data_type: "text"
          nullable: true
          null_meaning: "Partida em andamento sem resultado final consolidado"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "VITORIA_2_0"
            - "VITORIA_2_1"
            - "DERROTA_0_2"
            - "DERROTA_1_2"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
        - attribute_id: "EQUIPE_VENCEDORA_ID"
          physical_name_candidate: "equipe_vencedora_id"
          data_type: "uuid"
          nullable: true
          null_meaning: "Partida em andamento ou sem vencedor homologado"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
      foreign_keys:
        - id: "FK_PLACAR_JOGO_PARTIDA"
          from_columns:
            - "partida_id"
          to_table: "partida"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_PLACAR_JOGO_EQUIPE_VENCEDORA"
          from_columns:
            - "equipe_vencedora_id"
          to_table: "equipe"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints:
        - id: "UQ_PLACAR_PARTIDA"
          columns:
            - "partida_id"
      checks: []
      indexes:
        - id: "idx_placar_jogo_partida_id"
          table_name: "placar_jogo"
          columns:
            - "partida_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_placar_jogo_equipe_vencedora_id"
          table_name: "placar_jogo"
          columns:
            - "equipe_vencedora_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "ESTADO_DO_PLACAR"
      physical_name_candidate: "estado_do_placar"
      description: "Registrar a situação relacional momentânea de pontuação durante a partida."
      grain: "Uma linha representa a pontuação e vantagem em um determinado instante do set."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "NONE"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56_004"
            - "EVID_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_007"
        - attribute_id: "PLACAR_JOGO_ID"
          physical_name_candidate: "placar_jogo_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56_004"
        - attribute_id: "PERIODO_SET_ID"
          physical_name_candidate: "periodo_set_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
        - attribute_id: "PONTOS_EQUIPE_A"
          physical_name_candidate: "pontos_equipe_a"
          data_type: "integer"
          nullable: false
          null_meaning: null
          default_candidate: 0
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
        - attribute_id: "PONTOS_EQUIPE_B"
          physical_name_candidate: "pontos_equipe_b"
          data_type: "integer"
          nullable: false
          null_meaning: null
          default_candidate: 0
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
        - attribute_id: "SITUACAO_VANTAGEM"
          physical_name_candidate: "situacao_vantagem"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: "EMPATADO"
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "EMPATADO"
            - "FAVORAVEL"
            - "DESFAVORAVEL"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56_004"
        - attribute_id: "TIMESTAMP_INSTANTE"
          physical_name_candidate: "timestamp_instante"
          data_type: "timestamptz"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
      foreign_keys:
        - id: "FK_ESTADO_PLACAR_JOGO"
          from_columns:
            - "placar_jogo_id"
          to_table: "placar_jogo"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_ESTADO_PERIODO_SET"
          from_columns:
            - "periodo_set_id"
          to_table: "periodo_set"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints: []
      checks: []
      indexes:
        - id: "idx_estado_do_placar_placar_jogo_id"
          table_name: "estado_do_placar"
          columns:
            - "placar_jogo_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_estado_do_placar_periodo_set_id"
          table_name: "estado_do_placar"
          columns:
            - "periodo_set_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "EVOLUCAO_DO_PLACAR"
      physical_name_candidate: "evolucao_do_placar"
      description: "Manter a sequência cronológica auditável de alterações na pontuação da partida."
      grain: "Uma linha representa uma alteração incremental de pontuação motivada por um evento de gol."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "APPEND_ONLY"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
            - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_009"
        - attribute_id: "PARTIDA_ID"
          physical_name_candidate: "partida_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
        - attribute_id: "EVENTO_SCOUT_ID"
          physical_name_candidate: "evento_scout_id"
          data_type: "uuid"
          nullable: true
          null_meaning: "Pontuação registrada via súmula oficial sem correspondente em vídeo/scout"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - attribute_id: "EQUIPE_BENEFICIADA_ID"
          physical_name_candidate: "equipe_beneficiada_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
        - attribute_id: "SEQUENCIAL_PONTUACAO"
          physical_name_candidate: "sequencial_pontuacao"
          data_type: "integer"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_009"
        - attribute_id: "VALOR_INCREMENTO"
          physical_name_candidate: "valor_incremento"
          data_type: "integer"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - 1
            - 2
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_006"
            - "EVID_IHF_RULES_2026_EN_007"
        - attribute_id: "PLACAR_EQUIPE_A_AFT"
          physical_name_candidate: "placar_equipe_a_aft"
          data_type: "integer"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
        - attribute_id: "PLACAR_EQUIPE_B_AFT"
          physical_name_candidate: "placar_equipe_b_aft"
          data_type: "integer"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_002"
      foreign_keys:
        - id: "FK_EVOLUCAO_PARTIDA"
          from_columns:
            - "partida_id"
          to_table: "partida"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_EVOLUCAO_EVENTO_SCOUT"
          from_columns:
            - "evento_scout_id"
          to_table: "evento_scout"
          to_columns:
            - "id"
          on_delete: "SET NULL"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_EVOLUCAO_EQUIPE_BENEFICIADA"
          from_columns:
            - "equipe_beneficiada_id"
          to_table: "equipe"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints:
        - id: "UQ_EVOLUCAO_PARTIDA_SEQ"
          columns:
            - "partida_id"
            - "sequencial_pontuacao"
      checks: []
      indexes:
        - id: "idx_evolucao_do_placar_partida_id"
          table_name: "evolucao_do_placar"
          columns:
            - "partida_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_evolucao_do_placar_evento_scout_id"
          table_name: "evolucao_do_placar"
          columns:
            - "evento_scout_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_evolucao_do_placar_equipe_beneficiada_id"
          table_name: "evolucao_do_placar"
          columns:
            - "equipe_beneficiada_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "SISTEMA_DEFENSIVO"
      physical_name_candidate: "sistema_defensivo"
      description: "Mapear a disposição espacial, atitude e configuração dos defensores em quadra."
      grain: "Uma linha representa a atitude/sistema defensivo adotado em uma posse de bola."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "NONE"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_005"
            - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_006"
        - attribute_id: "POSSE_DE_BOLA_ID"
          physical_name_candidate: "posse_de_bola_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
        - attribute_id: "EQUIPE_ID"
          physical_name_candidate: "equipe_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_005"
        - attribute_id: "SISTEMA_TATICO_ID"
          physical_name_candidate: "sistema_tatico_id"
          data_type: "uuid"
          nullable: true
          null_meaning: "Sem especialização direta de um snapshot tático genérico"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_006"
        - attribute_id: "CODIGO_SISTEMA_DEFENSIVO"
          physical_name_candidate: "codigo_sistema_defensivo"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "SIS_3_0"
            - "SIS_2_1_CENTRAL"
            - "SIS_2_1_LATERAL"
            - "SIS_1_2"
            - "SIS_AVANCADO_7M"
            - "SIS_REATIVO"
            - "SIS_PROATIVO"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_005"
        - attribute_id: "EM_DESVANTAGEM_NUMERICA"
          physical_name_candidate: "em_desvantagem_numerica"
          data_type: "boolean"
          nullable: false
          null_meaning: null
          default_candidate: false
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_008"
      foreign_keys:
        - id: "FK_SISTEMA_DEFENSIVO_POSSE"
          from_columns:
            - "posse_de_bola_id"
          to_table: "posse_de_bola"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_SISTEMA_DEFENSIVO_EQUIPE"
          from_columns:
            - "equipe_id"
          to_table: "equipe"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_SISTEMA_DEFENSIVO_SISTEMA_TATICO"
          from_columns:
            - "sistema_tatico_id"
          to_table: "sistema_tatico"
          to_columns:
            - "id"
          on_delete: "SET NULL"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints: []
      checks: []
      indexes:
        - id: "idx_sistema_defensivo_posse_de_bola_id"
          table_name: "sistema_defensivo"
          columns:
            - "posse_de_bola_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_sistema_defensivo_equipe_id"
          table_name: "sistema_defensivo"
          columns:
            - "equipe_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_sistema_defensivo_sistema_tatico_id"
          table_name: "sistema_defensivo"
          columns:
            - "sistema_tatico_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "CONFIABILIDADE_OBSERVADOR"
      physical_name_candidate: "confiabilidade_observador"
      description: "Registrar a qualificação técnica e índices de concordância (Kappa) do analista de scout."
      grain: "Uma linha representa um evento de teste e calibração de um analista observador."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "INTERNO"
      retention_policy: "VERSIONED_ROW"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
        - attribute_id: "ANALISTA_OBSERVADOR_ID"
          physical_name_candidate: "analista_observador_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
        - attribute_id: "DATA_AVALIACAO"
          physical_name_candidate: "data_avaliacao"
          data_type: "timestamptz"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
        - attribute_id: "VERSAO_TESTE"
          physical_name_candidate: "versao_teste"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
        - attribute_id: "PERCENTUAL_ACERTO"
          physical_name_candidate: "percentual_acerto"
          data_type: "numeric(5,2)"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
        - attribute_id: "ERROS_CRITICOS_QTD"
          physical_name_candidate: "erros_criticos_qtd"
          data_type: "integer"
          nullable: false
          null_meaning: null
          default_candidate: 0
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
        - attribute_id: "KAPPA_COHEN"
          physical_name_candidate: "kappa_cohen"
          data_type: "numeric(4,3)"
          nullable: true
          null_meaning: "Kappa de Cohen não calculated para o teste em questão"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_007"
        - attribute_id: "STATUS_QUALIFICACAO"
          physical_name_candidate: "status_qualificacao"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "QUALIFICADO"
            - "NAO_QUALIFICADO"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
      foreign_keys:
        - id: "FK_CONFIABILIDADE_ANALISTA"
          from_columns:
            - "analista_observador_id"
          to_table: "analista_observador"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints: []
      checks: []
      indexes:
        - id: "idx_confiabilidade_observador_analista_observador_id"
          table_name: "confiabilidade_observador"
          columns:
            - "analista_observador_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "REVISAO_DA_OBSERVACAO"
      physical_name_candidate: "revisao_da_observacao"
      description: "Registrar eventos de auditoria ou segunda checagem do scout para garantia de qualidade dos dados."
      grain: "Uma linha representa um evento formal de revisão efetuado sobre uma observação de scout."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "INTERNO"
      retention_policy: "APPEND_ONLY"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
            - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_007"
        - attribute_id: "OBSERVACAO_DE_SCOUT_ID"
          physical_name_candidate: "observacao_de_scout_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
        - attribute_id: "ANALISTA_REVISOR_ID"
          physical_name_candidate: "analista_revisor_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
        - attribute_id: "TIMESTAMP_REVISAO"
          physical_name_candidate: "timestamp_revisao"
          data_type: "timestamptz"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
        - attribute_id: "MOTIVO_REVISAO"
          physical_name_candidate: "motivo_revisao"
          data_type: "text"
          nullable: true
          null_meaning: "Revisão periódica de rotina sem motivo específico apontado"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
        - attribute_id: "CAMPO_ALTERADO"
          physical_name_candidate: "campo_alterado"
          data_type: "text"
          nullable: true
          null_meaning: "Revisão confirmatória sem alteração de campos realizada"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
      foreign_keys:
        - id: "FK_REVISAO_OBSERVACAO"
          from_columns:
            - "observacao_de_scout_id"
          to_table: "observacao_de_scout"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_REVISAO_ANALISTA"
          from_columns:
            - "analista_revisor_id"
          to_table: "analista_observador"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints: []
      checks: []
      indexes:
        - id: "idx_revisao_da_observacao_observacao_de_scout_id"
          table_name: "revisao_da_observacao"
          columns:
            - "observacao_de_scout_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_revisao_da_observacao_analista_revisor_id"
          table_name: "revisao_da_observacao"
          columns:
            - "analista_revisor_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "ESTADO_DE_REVISAO"
      physical_name_candidate: "estado_de_revisao"
      description: "Gerenciar a situação no fluxo de homologação e validação da observação de scout."
      grain: "Uma linha representa o status corrente de revisão de uma observação de scout."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "INTERNO"
      retention_policy: "VERSIONED_ROW"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_006"
            - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_022"
        - attribute_id: "OBSERVACAO_DE_SCOUT_ID"
          physical_name_candidate: "observacao_de_scout_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_006"
        - attribute_id: "REVISAO_DA_OBSERVACAO_ID"
          physical_name_candidate: "revisao_da_observacao_id"
          data_type: "uuid"
          nullable: true
          null_meaning: "Estado inicial antes de qualquer evento de auditoria"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_006"
        - attribute_id: "STATUS_CORRENTE"
          physical_name_candidate: "status_corrente"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: "PENDENTE"
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "PENDENTE"
            - "APROVADO"
            - "REJEITADO"
            - "EM_AUDITORIA"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_006"
        - attribute_id: "DATA_ULTIMA_ATUALIZACAO"
          physical_name_candidate: "data_ultima_atualizacao"
          data_type: "timestamptz"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_006"
      foreign_keys:
        - id: "FK_ESTADO_REVISAO_OBSERVACAO"
          from_columns:
            - "observacao_de_scout_id"
          to_table: "observacao_de_scout"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_ESTADO_REVISAO_REVISAO"
          from_columns:
            - "revisao_da_observacao_id"
          to_table: "revisao_da_observacao"
          to_columns:
            - "id"
          on_delete: "SET NULL"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints:
        - id: "UQ_ESTADO_REVISAO_OBSERVA"
          columns:
            - "observacao_de_scout_id"
      checks: []
      indexes:
        - id: "idx_estado_de_revisao_observacao_de_scout_id"
          table_name: "estado_de_revisao"
          columns:
            - "observacao_de_scout_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_estado_de_revisao_revisao_da_observacao_id"
          table_name: "estado_de_revisao"
          columns:
            - "revisao_da_observacao_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "PROVENIENCIA_OBSERVACAO"
      physical_name_candidate: "proveniencia_observacao"
      description: "Garantir o registro imutável da linhagem de dados, protocolo e mídia fonte da observação de scout."
      grain: "Uma linha representa os metadados fixos de proveniência de uma observação de scout."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "INTERNO"
      retention_policy: "NONE"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
            - "EVID_CEPRAEA_DATABASE_CCB2A718_001"
        - attribute_id: "OBSERVACAO_DE_SCOUT_ID"
          physical_name_candidate: "observacao_de_scout_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
        - attribute_id: "PROTOCOLO_SCOUT_ID"
          physical_name_candidate: "protocolo_scout_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
        - attribute_id: "MIDIA_VIDEO_ID"
          physical_name_candidate: "midia_video_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
        - attribute_id: "FERRAMENTA_SOFTWARE"
          physical_name_candidate: "ferramenta_software"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
        - attribute_id: "ORIGEM_DADO"
          physical_name_candidate: "origem_dado"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "CODIFICACAO_HUMANA_P1"
            - "SUMULA_OFICIAL"
            - "EXTRACAO_AUTOMATIZADA"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
        - attribute_id: "CHECKSUM_MIDIA"
          physical_name_candidate: "checksum_midia"
          data_type: "text"
          nullable: true
          null_meaning: "Hash SHA256 não calculated para o arquivo de mídia"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
      foreign_keys:
        - id: "FK_PROVENIENCIA_OBSERVACAO"
          from_columns:
            - "observacao_de_scout_id"
          to_table: "observacao_de_scout"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_PROVENIENCIA_PROTOCOLO"
          from_columns:
            - "protocolo_scout_id"
          to_table: "protocolo_scout"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_PROVENIENCIA_MIDIA"
          from_columns:
            - "midia_video_id"
          to_table: "midia_video"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints:
        - id: "UQ_PROVENIENCIA_OBS"
          columns:
            - "observacao_de_scout_id"
      checks: []
      indexes:
        - id: "idx_proveniencia_observacao_observacao_de_scout_id"
          table_name: "proveniencia_observacao"
          columns:
            - "observacao_de_scout_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_proveniencia_observacao_protocolo_scout_id"
          table_name: "proveniencia_observacao"
          columns:
            - "protocolo_scout_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_proveniencia_observacao_midia_video_id"
          table_name: "proveniencia_observacao"
          columns:
            - "midia_video_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "TRECHO_OBSERVADO"
      physical_name_candidate: "trecho_observado"
      description: "Mapear o recorte temporal exato de vídeo correspondente a um evento de scout."
      grain: "Uma linha representa o recorte de timecode de vídeo de um evento específico."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "NONE"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
        - attribute_id: "EVENTO_SCOUT_ID"
          physical_name_candidate: "evento_scout_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - attribute_id: "MIDIA_VIDEO_ID"
          physical_name_candidate: "midia_video_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
        - attribute_id: "TIMECODE_INICIO"
          physical_name_candidate: "timecode_inicio"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
        - attribute_id: "TIMECODE_FIM"
          physical_name_candidate: "timecode_fim"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
        - attribute_id: "OFFSET_MILISSEGUNDOS"
          physical_name_candidate: "offset_milissegundos"
          data_type: "integer"
          nullable: true
          null_meaning: "Offset preciso em milissegundos não calculado"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
      foreign_keys:
        - id: "FK_TRECHO_EVENTO_SCOUT"
          from_columns:
            - "evento_scout_id"
          to_table: "evento_scout"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_TRECHO_MIDIA_VIDEO"
          from_columns:
            - "midia_video_id"
          to_table: "midia_video"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints:
        - id: "UQ_TRECHO_EVENTO"
          columns:
            - "evento_scout_id"
      checks: []
      indexes:
        - id: "idx_trecho_observado_evento_scout_id"
          table_name: "trecho_observado"
          columns:
            - "evento_scout_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_trecho_observado_midia_video_id"
          table_name: "trecho_observado"
          columns:
            - "midia_video_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "SPIN_SHOT"
      physical_name_candidate: "spin_shot"
      description: "Especialização tática para detalhamento da técnica de arremesso com giro de 360° no ar."
      grain: "Uma linha representa a caracterização especializada de um Spin Shot efetuado em um evento."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "NONE"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_005"
        - attribute_id: "EVENTO_SCOUT_ID"
          physical_name_candidate: "evento_scout_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_005"
        - attribute_id: "ROTACAO_COMPLETA_360"
          physical_name_candidate: "rotacao_completa_360"
          data_type: "boolean"
          nullable: false
          null_meaning: null
          default_candidate: true
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_005"
        - attribute_id: "SALTO_PE_DIRECIONADO"
          physical_name_candidate: "salto_pe_direcionado"
          data_type: "boolean"
          nullable: false
          null_meaning: null
          default_candidate: true
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_005"
        - attribute_id: "VALOR_PONTOS"
          physical_name_candidate: "valor_pontos"
          data_type: "integer"
          nullable: false
          null_meaning: null
          default_candidate: 2
          derived: false
          derivation_rule_id: null
          allowed_values:
            - 2
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_005"
      foreign_keys:
        - id: "FK_SPIN_SHOT_EVENTO"
          from_columns:
            - "evento_scout_id"
          to_table: "evento_scout"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints:
        - id: "UQ_SPIN_SHOT_EVENTO"
          columns:
            - "evento_scout_id"
      checks: []
      indexes:
        - id: "idx_spin_shot_evento_scout_id"
          table_name: "spin_shot"
          columns:
            - "evento_scout_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "IN_FLIGHT_SHOT"
      physical_name_candidate: "in_flight_shot"
      description: "Especialização tática para detalhamento da técnica de arremesso aéreo (ponte aérea)."
      grain: "Uma linha representa a caracterização especializada de um In-flight Shot efetuado."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "NONE"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_014"
            - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_006"
        - attribute_id: "EVENTO_SCOUT_ID"
          physical_name_candidate: "evento_scout_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_014"
        - attribute_id: "RECEPCAO_NO_AR"
          physical_name_candidate: "recepcao_no_ar"
          data_type: "boolean"
          nullable: false
          null_meaning: null
          default_candidate: true
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_014"
        - attribute_id: "SEM_CONTATO_AREIA"
          physical_name_candidate: "sem_contato_areia"
          data_type: "boolean"
          nullable: false
          null_meaning: null
          default_candidate: true
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_006"
        - attribute_id: "VALOR_PONTOS"
          physical_name_candidate: "valor_pontos"
          data_type: "integer"
          nullable: false
          null_meaning: null
          default_candidate: 2
          derived: false
          derivation_rule_id: null
          allowed_values:
            - 2
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_014"
      foreign_keys:
        - id: "FK_IN_FLIGHT_EVENTO"
          from_columns:
            - "evento_scout_id"
          to_table: "evento_scout"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints:
        - id: "UQ_IN_FLIGHT_EVENTO"
          columns:
            - "evento_scout_id"
      checks: []
      indexes:
        - id: "idx_in_flight_shot_evento_scout_id"
          table_name: "in_flight_shot"
          columns:
            - "evento_scout_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
      physical_name_candidate: "desqualificacao_segunda_exclusao"
      description: "Registrar a desqualificação e o afastamento definitivo do atleta pelo acúmulo da segunda exclusão."
      grain: "Uma linha representa a ocorrência de desqualificação por acúmulo de duas exclusões em uma partida."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "NONE"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_015"
        - attribute_id: "EVENTO_SCOUT_ID"
          physical_name_candidate: "evento_scout_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_015"
        - attribute_id: "ATLETA_ID"
          physical_name_candidate: "atleta_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_015"
        - attribute_id: "PARTIDA_ID"
          physical_name_candidate: "partida_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_015"
        - attribute_id: "SAIDA_IMEDIATA_QUADRA"
          physical_name_candidate: "saida_imediata_quadra"
          data_type: "boolean"
          nullable: false
          null_meaning: null
          default_candidate: true
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_015"
      foreign_keys:
        - id: "FK_DESQ_SEGUNDA_EXC_EVENTO"
          from_columns:
            - "evento_scout_id"
          to_table: "evento_scout"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_DESQ_SEGUNDA_EXC_ATLETA"
          from_columns:
            - "atleta_id"
          to_table: "atleta"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_DESQ_SEGUNDA_EXC_PARTIDA"
          from_columns:
            - "partida_id"
          to_table: "partida"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints:
        - id: "UQ_DESQ_EXC_EVENTO"
          columns:
            - "evento_scout_id"
      checks: []
      indexes:
        - id: "idx_desqualificacao_segunda_exclusao_evento_scout_id"
          table_name: "desqualificacao_segunda_exclusao"
          columns:
            - "evento_scout_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_desqualificacao_segunda_exclusao_atleta_id"
          table_name: "desqualificacao_segunda_exclusao"
          columns:
            - "atleta_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_desqualificacao_segunda_exclusao_partida_id"
          table_name: "desqualificacao_segunda_exclusao"
          columns:
            - "partida_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "CARTAO_AZUL_SUSPENSAO"
      physical_name_candidate: "cartao_azul_suspensao"
      description: "Registrar a desqualificação direta gravíssima com relatório por escrito e suspensão administrativa."
      grain: "Uma linha representa um evento de exibição de Cartão Azul e relatório formal da arbitragem."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "NONE"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_015"
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_017"
        - attribute_id: "EVENTO_SCOUT_ID"
          physical_name_candidate: "evento_scout_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_015"
        - attribute_id: "PARTIDA_ID"
          physical_name_candidate: "partida_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_015"
        - attribute_id: "ATLETA_ID"
          physical_name_candidate: "atleta_id"
          data_type: "uuid"
          nullable: true
          null_meaning: "Cartão azul applied a oficial de comissão técnica e não a atleta"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_015"
        - attribute_id: "PAPEL_OPERACIONAL_ID"
          physical_name_candidate: "papel_operacional_id"
          data_type: "uuid"
          nullable: true
          null_meaning: "Cartão azul aplicado a atleta em vez de oficial/dirigente de comissão técnica (papel_esportivo_operacional)"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_003"
        - attribute_id: "RELATORIO_ARBITRAGEM"
          physical_name_candidate: "relatorio_arbitragem"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_015"
        - attribute_id: "JOGOS_SUSPENSAO_AUTOMATICA"
          physical_name_candidate: "jogos_suspensao_automatica"
          data_type: "integer"
          nullable: false
          null_meaning: null
          default_candidate: 1
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_017"
      foreign_keys:
        - id: "FK_CARTAO_AZUL_EVENTO"
          from_columns:
            - "evento_scout_id"
          to_table: "evento_scout"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_CARTAO_AZUL_PARTIDA"
          from_columns:
            - "partida_id"
          to_table: "partida"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_CARTAO_AZUL_ATLETA"
          from_columns:
            - "atleta_id"
          to_table: "atleta"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_CARTAO_AZUL_PAPEL_OPERACIONAL"
          from_columns:
            - "papel_operacional_id"
          to_table: "papel_esportivo_operacional"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints:
        - id: "UQ_CARTAO_AZUL_EVENTO"
          columns:
            - "evento_scout_id"
      checks: []
      indexes:
        - id: "idx_cartao_azul_suspensao_evento_scout_id"
          table_name: "cartao_azul_suspensao"
          columns:
            - "evento_scout_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_cartao_azul_suspensao_partida_id"
          table_name: "cartao_azul_suspensao"
          columns:
            - "partida_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_cartao_azul_suspensao_atleta_id"
          table_name: "cartao_azul_suspensao"
          columns:
            - "atleta_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_cartao_azul_suspensao_papel_operacional_id"
          table_name: "cartao_azul_suspensao"
          columns:
            - "papel_operacional_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "SISTEMA_TATICO"
      physical_name_candidate: "sistema_tatico"
      description: "Registrar a disposição espacial coletiva e formação tática adotada em um intervalo do jogo."
      grain: "Uma linha representa a configuração tática adotada por uma equipe durante uma posse/intervalo."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "VERSIONED_ROW"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2_005"
            - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_006"
        - attribute_id: "POSSE_DE_BOLA_ID"
          physical_name_candidate: "posse_de_bola_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
        - attribute_id: "EQUIPE_ID"
          physical_name_candidate: "equipe_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_IHF_RULES_2026_EN_005"
        - attribute_id: "CODIGO_SISTEMA_TATICO"
          physical_name_candidate: "codigo_sistema_tatico"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "ATAQUE_3_1"
            - "ATAQUE_2_2"
            - "ATAQUE_4_0"
            - "DEFESA_3_0"
            - "DEFESA_2_1"
            - "DEFESA_1_2"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2_005"
        - attribute_id: "FASE_TATICA"
          physical_name_candidate: "fase_tatica"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "TO"
            - "AP"
            - "TD"
            - "DP"
            - "F_IND"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_005"
      foreign_keys:
        - id: "FK_SISTEMA_TATICO_POSSE"
          from_columns:
            - "posse_de_bola_id"
          to_table: "posse_de_bola"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_SISTEMA_TATICO_EQUIPE"
          from_columns:
            - "equipe_id"
          to_table: "equipe"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints: []
      checks: []
      indexes:
        - id: "idx_sistema_tatico_posse_de_bola_id"
          table_name: "sistema_tatico"
          columns:
            - "posse_de_bola_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_sistema_tatico_equipe_id"
          table_name: "sistema_tatico"
          columns:
            - "equipe_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "PAPEL_ESPORTIVO_OPERACIONAL"
      physical_name_candidate: "papel_esportivo_operacional"
      description: "Registrar as funções formais de comissão técnica, arbitragem e organização na súmula da partida."
      grain: "Uma linha representa a atribuição de um papel operacional a uma pessoa em uma partida."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "NONE"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_003"
            - "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_005"
        - attribute_id: "PARTIDA_ID"
          physical_name_candidate: "partida_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_003"
        - attribute_id: "EQUIPE_ID"
          physical_name_candidate: "equipe_id"
          data_type: "uuid"
          nullable: true
          null_meaning: "Papéis neutros de arbitragem, delegados e oficiais de mesa não possuem vínculo com equipe"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_003"
        - attribute_id: "NOME_PESSOA"
          physical_name_candidate: "nome_pessoa"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_003"
        - attribute_id: "CODIGO_PAPEL"
          physical_name_candidate: "codigo_papel"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
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
          rule_ids: []
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_003"
            - "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_005"
      foreign_keys:
        - id: "FK_PAPEL_OPERACIONAL_PARTIDA"
          from_columns:
            - "partida_id"
          to_table: "partida"
          to_columns:
            - "id"
          on_delete: "CASCADE"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_PAPEL_OPERACIONAL_EQUIPE"
          from_columns:
            - "equipe_id"
          to_table: "equipe"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints: []
      checks: []
      indexes:
        - id: "idx_papel_esportivo_operacional_partida_id"
          table_name: "papel_esportivo_operacional"
          columns:
            - "partida_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_papel_esportivo_operacional_equipe_id"
          table_name: "papel_esportivo_operacional"
          columns:
            - "equipe_id"
          index_type: "btree"
          is_unique: false

    - relation_id: "PARTICIPACAO_EQUIPE_COMPETICAO"
      physical_name_candidate: "participacao_equipe_competicao"
      description: "Registrar participação e elegibilidade para o ranking final no contexto de uma edição de competição, sem alterar o cadastro global da equipe."
      grain: "Uma linha representa a situação de participação e elegibilidade de uma equipe em uma competição durante um intervalo de vigência."
      owner_domain: "PARTIDAS_SCOUT_ANALISE_TATICA"
      access_classification: "PUBLICO"
      retention_policy: "VALID_TIME"
      primary_key:
        - "id"
      columns:
        - attribute_id: "ID"
          physical_name_candidate: "id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_008"
        - attribute_id: "COMPETICAO_ID"
          physical_name_candidate: "competicao_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_008"
        - attribute_id: "EQUIPE_ID"
          physical_name_candidate: "equipe_id"
          data_type: "uuid"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_008"
        - attribute_id: "TIPO_PARTICIPACAO"
          physical_name_candidate: "tipo_participacao"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "REGULAR"
            - "CONVIDADA"
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_008"
        - attribute_id: "STATUS_ELEGIBILIDADE_RANKING"
          physical_name_candidate: "status_elegibilidade_ranking"
          data_type: "text"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values:
            - "ELEGIVEL"
            - "INELEGIVEL_POR_DECISAO_COLETIVA"
            - "PENDENTE_DELIBERACAO"
          rule_ids:
            - "RN_SGATE_0023_PONTUACAO_FHERJ_2026"
          evidence_ref_ids:
            - "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_008"
        - attribute_id: "MOTIVO_DECISAO"
          physical_name_candidate: "motivo_decisao"
          data_type: "text"
          nullable: true
          null_meaning: "Participação regular sem exceção específica ou decisão ainda sem justificativa registrada"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_008"
        - attribute_id: "DECISAO_REF"
          physical_name_candidate: "decisao_ref"
          data_type: "text"
          nullable: true
          null_meaning: "Participação regular sem decisão excepcional associada"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_008"
        - attribute_id: "VALIDO_DESDE"
          physical_name_candidate: "valido_desde"
          data_type: "timestamptz"
          nullable: false
          null_meaning: null
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_008"
        - attribute_id: "VALIDO_ATE"
          physical_name_candidate: "valido_ate"
          data_type: "timestamptz"
          nullable: true
          null_meaning: "Participação ou decisão vigente sem término registrado"
          default_candidate: null
          derived: false
          derivation_rule_id: null
          allowed_values: []
          rule_ids: []
          evidence_ref_ids:
            - "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_008"
      foreign_keys:
        - id: "FK_PARTICIPACAO_COMPETICAO"
          from_columns:
            - "competicao_id"
          to_table: "competicao"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
        - id: "FK_PARTICIPACAO_EQUIPE"
          from_columns:
            - "equipe_id"
          to_table: "equipe"
          to_columns:
            - "id"
          on_delete: "RESTRICT"
          on_update: "CASCADE"
          supporting_index_required: true
      unique_constraints:
        - id: "UQ_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA"
          columns:
            - "competicao_id"
            - "equipe_id"
            - "valido_desde"
      checks:
        - id: "CHK_ELEGIBILIDADE_RANKING_CONTEXTUAL"
          expression_semantics: "STATUS_ELEGIBILIDADE_RANKING=INELEGIVEL_POR_DECISAO_COLETIVA exige MOTIVO_DECISAO e DECISAO_REF; a elegibilidade nunca é inferida por UF ou país."
          sql_expression_candidate: "(status_elegibilidade_ranking != 'INELEGIVEL_POR_DECISAO_COLETIVA') OR (motivo_decisao IS NOT NULL AND decisao_ref IS NOT NULL)"
          rule_ids:
            - "RN_SGATE_0023_PONTUACAO_FHERJ_2026"
        - id: "CHK_VIGENCIA_PARTICIPACAO"
          expression_semantics: "VALIDO_ATE deve ser nulo ou posterior a VALIDO_DESDE, sem intervalos contraditórios para a mesma equipe e competição."
          sql_expression_candidate: "valido_ate IS NULL OR valido_ate > valido_desde"
          rule_ids: []
      indexes:
        - id: "idx_participacao_equipe_competicao_competicao_id"
          table_name: "participacao_equipe_competicao"
          columns:
            - "competicao_id"
          index_type: "btree"
          is_unique: false
        - id: "idx_participacao_equipe_competicao_equipe_id"
          table_name: "participacao_equipe_competicao"
          columns:
            - "equipe_id"
          index_type: "btree"
          is_unique: false

  catalogs:
    - catalog_id: "CATALOG_FASE_TATICA"
      description: "Catálogo de fases táticas ordinárias e indetermináveis no Handebol de Praia."
      version: "1.0.0"
      is_open_vocabulary: false
      items:
        - code: "TO"
          label: "Transição Ofensiva"
          description: "Avanço rápido da equipe para o ataque após recuperação de posse."
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_005"
        - code: "AP"
          label: "Ataque Posicional"
          description: "Ataque estruturado diante da defesa organizada do adversário."
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_005"
        - code: "TD"
          label: "Transição Defensiva"
          description: "Retorno rápido da equipe para reorganização defensiva após perda de posse."
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_005"
        - code: "DP"
          label: "Defesa Posicional"
          description: "Organização e posicionamento defensivo estruturado."
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_005"
        - code: "F_IND"
          label: "Fase Indeterminável"
          description: "Fase tática que não pode ser categorizada objetivamente pelo vídeo."
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_005"

    - catalog_id: "CATALOG_SISTEMA_TATICO"
      description: "Catálogo de disposições espaciais e formações táticas ofensivas e defensivas."
      version: "1.0.0"
      is_open_vocabulary: false
      items:
        - code: "ATAQUE_3_1"
          label: "Ataque 3:1"
          description: "Sistema ofensivo com três jogadoras na linha armada e um pivô/especialista fixo."
          evidence_ref_ids:
            - "EVID_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2_005"
        - code: "ATAQUE_2_2"
          label: "Ataque 2:2"
          description: "Sistema ofensivo com duas armadoras e duas jogadoras no espaço interno/pivôs."
          evidence_ref_ids:
            - "EVID_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2_005"
        - code: "ATAQUE_4_0"
          label: "Ataque 4:0"
          description: "Sistema ofensivo sem pivô fixo, com quatro jogadoras circulando na linha armada."
          evidence_ref_ids:
            - "EVID_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2_005"
        - code: "DEFESA_3_0"
          label: "Defesa 3:0"
          description: "Sistema defensivo com três defensoras alinhadas próximas à linha de 6 metros."
          evidence_ref_ids:
            - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_006"
        - code: "DEFESA_2_1"
          label: "Defesa 2:1"
          description: "Sistema defensivo com duas defensoras na base e uma avançada."
          evidence_ref_ids:
            - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_006"
        - code: "DEFESA_1_2"
          label: "Defesa 1:2"
          description: "Sistema defensivo com uma defensora recuada e duas avançadas."
          evidence_ref_ids:
            - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_006"

    - catalog_id: "CATALOG_SISTEMA_DEFENSIVO"
      description: "Catálogo de formações, arranjos geométricos e atitudes defensivas específicas."
      version: "1.0.0"
      is_open_vocabulary: false
      items:
        - code: "SIS_3_0"
          label: "Sistema 3:0"
          description: "Formação defensiva fechada na linha de 6 metros."
          evidence_ref_ids:
            - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_005"
        - code: "SIS_2_1_CENTRAL"
          label: "Sistema 2:1 Central"
          description: "Formação com uma defensora flutuante atuando no centro."
          evidence_ref_ids:
            - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_005"
        - code: "SIS_2_1_LATERAL"
          label: "Sistema 2:1 Lateral"
          description: "Formação com cobertura direcionada para um dos lados da quadra."
          evidence_ref_ids:
            - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_005"
        - code: "SIS_1_2"
          label: "Sistema 1:2"
          description: "Formação altamente agressiva com duas defensoras na primeira linha."
          evidence_ref_ids:
            - "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_005"
        - code: "SIS_AVANCADO_7M"
          label: "Sistema Avançado a 7 Metros"
          description: "Linha defensiva posicionada a 7 metros do gol."
          evidence_ref_ids:
            - "EVID_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94_002"
        - code: "SIS_REATIVO"
          label: "Sistema Reativo"
          description: "Atitude defensiva orientada à contenção e reação aos movimentos ofensivos."
          evidence_ref_ids:
            - "EVID_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94_002"
        - code: "SIS_PROATIVO"
          label: "Sistema Proativo"
          description: "Atitude defensiva orientada à antecipação, pressão e intercepção."
          evidence_ref_ids:
            - "EVID_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94_002"

    - catalog_id: "CATALOG_ZONA_ANALITICA"
      description: "Catálogo das faixas analíticas geométricas da largura da quadra para registro de scout."
      version: "1.0.0"
      is_open_vocabulary: false
      items:
        - code: "ZE"
          label: "Zona Esquerda"
          description: "Faixa lateral esquerda da quadra (0 a 3 metros da margem esquerda)."
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_006"
        - code: "ZCE"
          label: "Zona Centro-Esquerda"
          description: "Faixa central-esquerda da quadra (3 a 6 metros da margem esquerda)."
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_006"
        - code: "ZCD"
          label: "Zona Centro-Direita"
          description: "Faixa central-direita da quadra (6 a 9 metros da margem esquerda)."
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_006"
        - code: "ZD"
          label: "Zona Direita"
          description: "Faixa lateral direita da quadra (9 a 12 metros da margem esquerda)."
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_006"

    - catalog_id: "CATALOG_PAPEL_ESPORTIVO_OPERACIONAL"
      description: "Catálogo de funções operacionais da comissão técnica, arbitragem e mesa na súmula."
      version: "1.0.0"
      is_open_vocabulary: false
      items:
        - code: "TECNICO"
          label: "Técnico"
          description: "Treinador principal responsável pela equipe em súmula."
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_003"
        - code: "AUXILIAR_TECNICO"
          label: "Auxiliar Técnico"
          description: "Assistente técnico da comissão de equipe."
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_003"
        - code: "MEDICO"
          label: "Médico"
          description: "Oficial médico credenciado da equipe."
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_003"
        - code: "FISIOTERAPEUTA"
          label: "Fisioterapeuta"
          description: "Oficial fisioterapeuta credenciado da equipe."
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_003"
        - code: "DELEGADO_A"
          label: "Delegado A"
          description: "Delegado oficial A da federação/organização."
          evidence_ref_ids:
            - "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_005"
        - code: "DELEGADO_B"
          label: "Delegado B"
          description: "Delegado oficial B da federação/organização."
          evidence_ref_ids:
            - "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_005"
        - code: "SECRETARIO"
          label: "Secretário"
          description: "Oficial de mesa responsável pela súmula e registros."
          evidence_ref_ids:
            - "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_005"
        - code: "CRONOMETRISTA"
          label: "Cronometrista"
          description: "Oficial de mesa responsável pelo controle do tempo e placar."
          evidence_ref_ids:
            - "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_005"
        - code: "OFICIAL_ARBITRAGEM"
          label: "Oficial de Arbitragem"
          description: "Árbitro de quadra responsável pela condução do jogo."
          evidence_ref_ids:
            - "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_005"

    - catalog_id: "CATALOG_ESTADO_REVISAO"
      description: "Catálogo de estados no fluxo de homologação e auditoria da observação de scout."
      version: "1.0.0"
      is_open_vocabulary: false
      items:
        - code: "PENDENTE"
          label: "Pendente"
          description: "Observação registrada aguardando validação ou revisão."
          evidence_ref_ids:
            - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_006"
        - code: "APROVADO"
          label: "Aprovado"
          description: "Observação auditada e homologada na base consolidada."
          evidence_ref_ids:
            - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_006"
        - code: "REJEITADO"
          label: "Rejeitado"
          description: "Observação reprovada devido a inconsistências ou não conformidade técnica."
          evidence_ref_ids:
            - "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_006"
        - code: "EM_AUDITORIA"
          label: "Em Auditoria"
          description: "Observação sob análise detalhada de concordância ou checagem de qualidade."
          evidence_ref_ids:
            - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_022"

    - catalog_id: "CATALOG_PUNICAO_DISCIPLINAR"
      description: "Catálogo das sanções disciplinares previstas nas regras oficiais de Handebol de Praia."
      version: "1.0.0"
      is_open_vocabulary: false
      items:
        - code: "ADVERTENCIA"
          label: "Advertência"
          description: "Sanção disciplinar verbal ou formal inicial sem exclusão de quadra."
          evidence_ref_ids:
            - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_014"
        - code: "EXCLUSAO_TEMPORARIA"
          label: "Exclusão Temporária"
          description: "Saída do atleta até a mudança da posse de bola."
          evidence_ref_ids:
            - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_014"
        - code: "DESQUALIFICACAO_DIRETA"
          label: "Desqualificação Direta"
          description: "Cartão vermelho por falta grave, exigindo saída do atleta sem relatório."
          evidence_ref_ids:
            - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_014"
        - code: "CARTAO_AZUL"
          label: "Cartão Azul"
          description: "Desqualificação por conduta antidesportiva grave acompanhada de relatório escrito."
          evidence_ref_ids:
            - "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_015"

    - catalog_id: "CATALOG_CONSEQUENCIA_DISCIPLINAR"
      description: "Catálogo dos efeitos táticos e administrativos decorrentes de sanções disciplinares."
      version: "1.0.0"
      is_open_vocabulary: false
      items:
        - code: "REDUCAO_NUMERICA_QUADRA"
          label: "Redução Numérica em Quadra"
          description: "Obrigação da equipe de atuar com atuações inferiores temporárias em quadra."
          evidence_ref_ids:
            - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_008"
        - code: "SUSPENSAO_PROXIMA_PARTIDA"
          label: "Suspensão para a Próxima Partida"
          description: "Afastamento compulsório administrativo de pelo menos uma partida subsequente."
          evidence_ref_ids:
            - "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_015"
        - code: "CONCESSAO_TIRO_SIX_METROS"
          label: "Concessão de Tiro de 6 Metros"
          description: "Atribuição de arremesso de penalidade máxima à equipe adversária."
          evidence_ref_ids:
            - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_017"

    - catalog_id: "CATALOG_ACAO_GOLEIRA"
      description: "Catálogo das ações motoras e táticas executadas na posição de goleira."
      version: "1.0.0"
      is_open_vocabulary: false
      items:
        - code: "DEFESA_PARADA"
          label: "Defesa Parada"
          description: "Intervenção defensiva direta com interrupção da trajetória da bola na área."
          evidence_ref_ids:
            - "EVID_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94_003"
        - code: "DEFESA_COUNTER_SPIN"
          label: "Defesa de Counter-Spin"
          description: "Ação defensiva especializada contra arremesso com giro 360°."
          evidence_ref_ids:
            - "EVID_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_005"
        - code: "DEFESA_COUNTER_FLY"
          label: "Defesa de Counter-Fly"
          description: "Ação defensiva especializada contra arremesso em ponte aérea."
          evidence_ref_ids:
            - "EVID_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_005"
        - code: "PASSE_TRANSICAO_T4"
          label: "Passe de Transição (T4)"
          description: "Lançamento rápido executado pela goleira para transição ofensiva."
          evidence_ref_ids:
            - "EVID_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0_003"
        - code: "ARREMESSO_DIRETO_GOLEIRA"
          label: "Arremesso Direto da Goleira"
          description: "Finalização efetuada diretamente pela goleira de sua área em direção ao gol adversário."
          evidence_ref_ids:
            - "EVID_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94_003"
        - code: "INTERVENCAO_SHOOTOUT"
          label: "Intervenção em Shoot-out"
          description: "Atuação da goleira na disputa 1 contra o goleiro no Shoot-out."
          evidence_ref_ids:
            - "EVID_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_005"

    - catalog_id: "CATALOG_RESULTADO_ACAO"
      description: "Catálogo de desfechos imediatos codificados para as ações observadas no scout."
      version: "1.0.0"
      is_open_vocabulary: false
      items:
        - code: "GOL"
          label: "Gol"
          description: "Conversão válida do arremesso em pontuação."
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_008"
        - code: "DEFESA"
          label: "Defesa"
          description: "Intervenção bem-sucedida da goleira impedindo o gol."
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_008"
        - code: "FORA"
          label: "Fora"
          description: "Arremesso direcionado fora das balizas da baliza."
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_008"
        - code: "TRAVE"
          label: "Trave"
          description: "Arremesso que atinge o poste ou travessão sem converter."
          evidence_ref_ids:
            - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_008"
        - code: "ERRO_TECNICO"
          label: "Erro Técnico"
          description: "Perda da posse por viro, passe incorreto ou infração técnica."
          evidence_ref_ids:
            - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_001"
        - code: "FALTA_SOFRIDA"
          label: "Falta Sofrida"
          description: "Ação interrompida por infração cometida pelo defensor."
          evidence_ref_ids:
            - "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_001"

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