roles:
  - id: "ROLE_ADMIN"
    name: "Administrador do Sistema"
    description: "Administrador responsável pela governança de dados, gestão de acessos e segurança."
    authentication_required: true
    assignment_scope: "GLOBAL"
    authorization_claim_source: "DATABASE_MEMBERSHIP"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_002"
  - id: "ROLE_TREINADOR"
    name: "Treinador e Comissão Técnica"
    description: "Autoridade técnica responsável por confirmação de presenças, convocações e homologação de dados."
    authentication_required: true
    assignment_scope: "GLOBAL"
    authorization_claim_source: "DATABASE_MEMBERSHIP"
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_003"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_022"
  - id: "ROLE_ANALISTA_OBSERVADOR"
    name: "Analista de Scout e Observador"
    description: "Responsável pela coleta, codificação e revisão de eventos de scout e análise tática."
    authentication_required: true
    assignment_scope: "GLOBAL"
    authorization_claim_source: "DATABASE_MEMBERSHIP"
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
  - id: "ROLE_ATLETA"
    name: "Atleta do Elenco"
    description: "Atleta participante do elenco com acesso a declarações de disponibilidade e relatórios pessoais."
    authentication_required: true
    assignment_scope: "GLOBAL"
    authorization_claim_source: "DATABASE_MEMBERSHIP"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_003"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_005"
  - id: "ROLE_PUBLICO_LEITOR"
    name: "Usuário Público / Leitor"
    description: "Acesso de leitura para dados públicos de competições, partidas e placares."
    authentication_required: true
    assignment_scope: "GLOBAL"
    authorization_claim_source: "DATABASE_MEMBERSHIP"
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_002"
resources:
  - id: "RES_COMPETICAO"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "COMPETICAO"
    classification: "PUBLICO"
    exposed_via_data_api: true
    owner_rule: "Sem restrição de propriedade individual; leitura pública e escrita restrita à comissão e administradores."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_PARTIDA"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "PARTIDA"
    classification: "PUBLICO"
    exposed_via_data_api: true
    owner_rule: "Sem restrição de propriedade individual; leitura pública e escrita restrita à comissão e administradores."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_EQUIPE"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "EQUIPE"
    classification: "PUBLICO"
    exposed_via_data_api: true
    owner_rule: "Sem restrição de propriedade individual; leitura pública e escrita restrita à comissão e administradores."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_PARTIDA_EQUIPE"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "PARTIDA_EQUIPE"
    classification: "PUBLICO"
    exposed_via_data_api: true
    owner_rule: "Sem restrição de propriedade individual; leitura pública e escrita restrita à comissão e administradores."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_PERIODO_SET"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "PERIODO_SET"
    classification: "PUBLICO"
    exposed_via_data_api: true
    owner_rule: "Sem restrição de propriedade individual; leitura pública e escrita restrita à comissão e administradores."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_SHOOT_OUT"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "SHOOT_OUT"
    classification: "PUBLICO"
    exposed_via_data_api: true
    owner_rule: "Sem restrição de propriedade individual; leitura pública e escrita restrita à comissão e administradores."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_PLACAR_JOGO"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "PLACAR_JOGO"
    classification: "PUBLICO"
    exposed_via_data_api: true
    owner_rule: "Sem restrição de propriedade individual; leitura pública e escrita restrita à comissão e administradores."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_ESTADO_DO_PLACAR"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "ESTADO_DO_PLACAR"
    classification: "PUBLICO"
    exposed_via_data_api: true
    owner_rule: "Sem restrição de propriedade individual; leitura pública e escrita restrita à comissão e administradores."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_EVOLUCAO_DO_PLACAR"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "EVOLUCAO_DO_PLACAR"
    classification: "PUBLICO"
    exposed_via_data_api: true
    owner_rule: "Sem restrição de propriedade individual; leitura pública e escrita restrita à comissão e administradores."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_EQUIPE_ATLETA_INSCRICAO"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "EQUIPE_ATLETA_INSCRICAO"
    classification: "INTERNO"
    exposed_via_data_api: true
    owner_rule: "Acesso restrito aos membros autenticados da comissão técnica, atletas e analistas."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_POSSE_DE_BOLA"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "POSSE_DE_BOLA"
    classification: "INTERNO"
    exposed_via_data_api: true
    owner_rule: "Acesso restrito aos membros autenticados da comissão técnica e analistas de scout."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_UNIDADE_BASICA_ATAQUE_BOU"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "UNIDADE_BASICA_ATAQUE_BOU"
    classification: "INTERNO"
    exposed_via_data_api: true
    owner_rule: "Acesso restrito aos membros autenticados da comissão técnica e analistas de scout."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_EVENTO_SCOUT"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "EVENTO_SCOUT"
    classification: "INTERNO"
    exposed_via_data_api: true
    owner_rule: "Acesso restrito aos membros autenticados da comissão técnica e analistas de scout."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_OBSERVACAO_DE_SCOUT"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "OBSERVACAO_DE_SCOUT"
    classification: "INTERNO"
    exposed_via_data_api: true
    owner_rule: "Acesso restrito aos membros autenticados da comissão técnica e analistas de scout."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_PROTOCOLO_SCOUT"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "PROTOCOLO_SCOUT"
    classification: "INTERNO"
    exposed_via_data_api: true
    owner_rule: "Acesso restrito aos membros autenticados da comissão técnica e analistas de scout."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_MIDIA_VIDEO"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "MIDIA_VIDEO"
    classification: "INTERNO"
    exposed_via_data_api: true
    owner_rule: "Acesso restrito aos membros autenticados da comissão técnica e analistas de scout."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_SEGMENTO_OBSERVADO"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "SEGMENTO_OBSERVADO"
    classification: "INTERNO"
    exposed_via_data_api: true
    owner_rule: "Acesso restrito aos membros autenticados da comissão técnica e analistas de scout."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_SISTEMA_DEFENSIVO"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "SISTEMA_DEFENSIVO"
    classification: "INTERNO"
    exposed_via_data_api: true
    owner_rule: "Acesso restrito aos membros autenticados da comissão técnica e analistas de scout."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_CONFIABILIDADE_OBSERVADOR"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "CONFIABILIDADE_OBSERVADOR"
    classification: "INTERNO"
    exposed_via_data_api: true
    owner_rule: "Acesso restrito aos membros autenticados da comissão técnica e analistas de scout."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_REVISAO_DA_OBSERVACAO"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "REVISAO_DA_OBSERVACAO"
    classification: "INTERNO"
    exposed_via_data_api: true
    owner_rule: "Acesso restrito aos membros autenticados da comissão técnica e analistas de scout."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_ESTADO_DE_REVISAO"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "ESTADO_DE_REVISAO"
    classification: "INTERNO"
    exposed_via_data_api: true
    owner_rule: "Acesso restrito aos membros autenticados da comissão técnica e analistas de scout."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_PROVENIENCIA_OBSERVACAO"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "PROVENIENCIA_OBSERVACAO"
    classification: "INTERNO"
    exposed_via_data_api: true
    owner_rule: "Acesso restrito aos membros autenticados da comissão técnica e analistas de scout."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_TRECHO_OBSERVADO"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "TRECHO_OBSERVADO"
    classification: "INTERNO"
    exposed_via_data_api: true
    owner_rule: "Acesso restrito aos membros autenticados da comissão técnica e analistas de scout."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_SPIN_SHOT"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "SPIN_SHOT"
    classification: "INTERNO"
    exposed_via_data_api: true
    owner_rule: "Acesso restrito aos membros autenticados da comissão técnica e analistas de scout."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_IN_FLIGHT_SHOT"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "IN_FLIGHT_SHOT"
    classification: "INTERNO"
    exposed_via_data_api: true
    owner_rule: "Acesso restrito aos membros autenticados da comissão técnica e analistas de scout."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_SISTEMA_TATICO"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "SISTEMA_TATICO"
    classification: "INTERNO"
    exposed_via_data_api: true
    owner_rule: "Acesso restrito aos membros autenticados da comissão técnica e analistas de scout."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_PAPEL_ESPORTIVO_OPERACIONAL"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "PAPEL_ESPORTIVO_OPERACIONAL"
    classification: "INTERNO"
    exposed_via_data_api: true
    owner_rule: "Acesso restrito aos membros autenticados da comissão técnica e analistas de scout."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_PARTICIPACAO_EQUIPE_COMPETICAO"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "PARTICIPACAO_EQUIPE_COMPETICAO"
    classification: "INTERNO"
    exposed_via_data_api: true
    owner_rule: "Acesso restrito aos membros autenticados da comissão técnica e analistas de scout."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_ATLETA"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "ATLETA"
    classification: "RESTRITO"
    exposed_via_data_api: true
    owner_rule: "Acesso estritamente restrito com base na identidade individual da atleta, comissão técnica e administradores."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_ANALISTA_OBSERVADOR"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "ANALISTA_OBSERVADOR"
    classification: "RESTRITO"
    exposed_via_data_api: true
    owner_rule: "Acesso estritamente restrito com base na identidade do analista e administradores."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
    classification: "RESTRITO"
    exposed_via_data_api: true
    owner_rule: "Acesso estritamente restrito à comissão técnica e administradores."
    view_security_mode: "NOT_APPLICABLE"
  - id: "RES_CARTAO_AZUL_SUSPENSAO"
    resource_kind: "TABLE"
    logical_relation_ids:
      - "CARTAO_AZUL_SUSPENSAO"
    classification: "RESTRITO"
    exposed_via_data_api: true
    owner_rule: "Acesso estritamente restrito à comissão técnica e administradores."
    view_security_mode: "NOT_APPLICABLE"
permissions:
  - id: "PERM_001"
    role_id: "ROLE_PUBLICO_LEITOR"
    resource_id: "RES_COMPETICAO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "true"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_001"
    positive_test_ids:
      - "TEST_ACCESS_POS_001"
  - id: "PERM_002"
    role_id: "ROLE_ADMIN"
    resource_id: "RES_COMPETICAO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_ADMIN'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_002"
    positive_test_ids:
      - "TEST_ACCESS_POS_002"
  - id: "PERM_003"
    role_id: "ROLE_PUBLICO_LEITOR"
    resource_id: "RES_PARTIDA"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "true"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_003"
    positive_test_ids:
      - "TEST_ACCESS_POS_003"
  - id: "PERM_004"
    role_id: "ROLE_ADMIN"
    resource_id: "RES_PARTIDA"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_ADMIN'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_004"
    positive_test_ids:
      - "TEST_ACCESS_POS_004"
  - id: "PERM_005"
    role_id: "ROLE_PUBLICO_LEITOR"
    resource_id: "RES_EQUIPE"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "true"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_005"
    positive_test_ids:
      - "TEST_ACCESS_POS_005"
  - id: "PERM_006"
    role_id: "ROLE_PUBLICO_LEITOR"
    resource_id: "RES_PARTIDA_EQUIPE"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "true"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_006"
    positive_test_ids:
      - "TEST_ACCESS_POS_006"
  - id: "PERM_007"
    role_id: "ROLE_PUBLICO_LEITOR"
    resource_id: "RES_PERIODO_SET"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "true"
    column_scope: []
    conditions: []
    rule_ids:
      - "REG-IHF-003"
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_007"
    positive_test_ids:
      - "TEST_ACCESS_POS_007"
  - id: "PERM_008"
    role_id: "ROLE_PUBLICO_LEITOR"
    resource_id: "RES_SHOOT_OUT"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "true"
    column_scope: []
    conditions: []
    rule_ids:
      - "REG-IHF-003"
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_008"
    positive_test_ids:
      - "TEST_ACCESS_POS_008"
  - id: "PERM_009"
    role_id: "ROLE_PUBLICO_LEITOR"
    resource_id: "RES_PLACAR_JOGO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "true"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_009"
    positive_test_ids:
      - "TEST_ACCESS_POS_009"
  - id: "PERM_010"
    role_id: "ROLE_PUBLICO_LEITOR"
    resource_id: "RES_ESTADO_DO_PLACAR"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "true"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_010"
    positive_test_ids:
      - "TEST_ACCESS_POS_010"
  - id: "PERM_011"
    role_id: "ROLE_PUBLICO_LEITOR"
    resource_id: "RES_EVOLUCAO_DO_PLACAR"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "true"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_011"
    positive_test_ids:
      - "TEST_ACCESS_POS_011"
  - id: "PERM_012"
    role_id: "ROLE_TREINADOR"
    resource_id: "RES_EQUIPE_ATLETA_INSCRICAO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids:
      - "REG-IHF-001"
      - "REG-IHF-002"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_024"
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_025"
    negative_test_ids:
      - "TEST_ACCESS_NEG_012"
    positive_test_ids:
      - "TEST_ACCESS_POS_012"
  - id: "PERM_013"
    role_id: "ROLE_TREINADOR"
    resource_id: "RES_EQUIPE_ATLETA_INSCRICAO"
    operation: "INSERT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_TREINADOR'"
    column_scope: []
    conditions: []
    rule_ids:
      - "REG-IHF-001"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_024"
    negative_test_ids:
      - "TEST_ACCESS_NEG_013"
    positive_test_ids:
      - "TEST_ACCESS_POS_013"
  - id: "PERM_014"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_POSSE_DE_BOLA"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
    negative_test_ids:
      - "TEST_ACCESS_NEG_014"
    positive_test_ids:
      - "TEST_ACCESS_POS_014"
  - id: "PERM_015"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_POSSE_DE_BOLA"
    operation: "INSERT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_ANALISTA_OBSERVADOR'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
    negative_test_ids:
      - "TEST_ACCESS_NEG_015"
    positive_test_ids:
      - "TEST_ACCESS_POS_015"
  - id: "PERM_016"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_UNIDADE_BASICA_ATAQUE_BOU"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_004"
    negative_test_ids:
      - "TEST_ACCESS_NEG_016"
    positive_test_ids:
      - "TEST_ACCESS_POS_016"
  - id: "PERM_017"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_UNIDADE_BASICA_ATAQUE_BOU"
    operation: "INSERT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_ANALISTA_OBSERVADOR'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_004"
    negative_test_ids:
      - "TEST_ACCESS_NEG_017"
    positive_test_ids:
      - "TEST_ACCESS_POS_017"
  - id: "PERM_018"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_EVENTO_SCOUT"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    negative_test_ids:
      - "TEST_ACCESS_NEG_018"
    positive_test_ids:
      - "TEST_ACCESS_POS_018"
  - id: "PERM_019"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_EVENTO_SCOUT"
    operation: "INSERT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_ANALISTA_OBSERVADOR'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
    negative_test_ids:
      - "TEST_ACCESS_NEG_019"
    positive_test_ids:
      - "TEST_ACCESS_POS_019"
  - id: "PERM_020"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_OBSERVACAO_DE_SCOUT"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    negative_test_ids:
      - "TEST_ACCESS_NEG_020"
    positive_test_ids:
      - "TEST_ACCESS_POS_020"
  - id: "PERM_021"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_OBSERVACAO_DE_SCOUT"
    operation: "INSERT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_ANALISTA_OBSERVADOR'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    negative_test_ids:
      - "TEST_ACCESS_NEG_021"
    positive_test_ids:
      - "TEST_ACCESS_POS_021"
  - id: "PERM_022"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_PROTOCOLO_SCOUT"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    negative_test_ids:
      - "TEST_ACCESS_NEG_022"
    positive_test_ids:
      - "TEST_ACCESS_POS_022"
  - id: "PERM_023"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_MIDIA_VIDEO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    negative_test_ids:
      - "TEST_ACCESS_NEG_023"
    positive_test_ids:
      - "TEST_ACCESS_POS_023"
  - id: "PERM_024"
    role_id: "ROLE_TREINADOR"
    resource_id: "RES_MIDIA_VIDEO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    negative_test_ids:
      - "TEST_ACCESS_NEG_024"
    positive_test_ids:
      - "TEST_ACCESS_POS_024"
  - id: "PERM_025"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_SEGMENTO_OBSERVADO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    negative_test_ids:
      - "TEST_ACCESS_NEG_025"
    positive_test_ids:
      - "TEST_ACCESS_POS_025"
  - id: "PERM_026"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_SEGMENTO_OBSERVADO"
    operation: "INSERT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_ANALISTA_OBSERVADOR'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    negative_test_ids:
      - "TEST_ACCESS_NEG_026"
    positive_test_ids:
      - "TEST_ACCESS_POS_026"
  - id: "PERM_027"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_SISTEMA_DEFENSIVO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    negative_test_ids:
      - "TEST_ACCESS_NEG_027"
    positive_test_ids:
      - "TEST_ACCESS_POS_027"
  - id: "PERM_028"
    role_id: "ROLE_TREINADOR"
    resource_id: "RES_SISTEMA_DEFENSIVO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    negative_test_ids:
      - "TEST_ACCESS_NEG_028"
    positive_test_ids:
      - "TEST_ACCESS_POS_028"
  - id: "PERM_029"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_CONFIABILIDADE_OBSERVADOR"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "analyst_id = auth.uid() OR auth.jwt() ->> 'role' = 'ROLE_ADMIN'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
    negative_test_ids:
      - "TEST_ACCESS_NEG_029"
    positive_test_ids:
      - "TEST_ACCESS_POS_029"
  - id: "PERM_030"
    role_id: "ROLE_ADMIN"
    resource_id: "RES_CONFIABILIDADE_OBSERVADOR"
    operation: "UPDATE"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_ADMIN'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
    negative_test_ids:
      - "TEST_ACCESS_NEG_030"
    positive_test_ids:
      - "TEST_ACCESS_POS_030"
  - id: "PERM_031"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_REVISAO_DA_OBSERVACAO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    negative_test_ids:
      - "TEST_ACCESS_NEG_031"
    positive_test_ids:
      - "TEST_ACCESS_POS_031"
  - id: "PERM_032"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_REVISAO_DA_OBSERVACAO"
    operation: "INSERT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_ANALISTA_OBSERVADOR'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    negative_test_ids:
      - "TEST_ACCESS_NEG_032"
    positive_test_ids:
      - "TEST_ACCESS_POS_032"
  - id: "PERM_033"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_ESTADO_DE_REVISAO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    negative_test_ids:
      - "TEST_ACCESS_NEG_033"
    positive_test_ids:
      - "TEST_ACCESS_POS_033"
  - id: "PERM_034"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_PROVENIENCIA_OBSERVACAO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    negative_test_ids:
      - "TEST_ACCESS_NEG_034"
    positive_test_ids:
      - "TEST_ACCESS_POS_034"
  - id: "PERM_035"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_TRECHO_OBSERVADO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    negative_test_ids:
      - "TEST_ACCESS_NEG_035"
    positive_test_ids:
      - "TEST_ACCESS_POS_035"
  - id: "PERM_036"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_TRECHO_OBSERVADO"
    operation: "INSERT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_ANALISTA_OBSERVADOR'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    negative_test_ids:
      - "TEST_ACCESS_NEG_036"
    positive_test_ids:
      - "TEST_ACCESS_POS_036"
  - id: "PERM_037"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_SPIN_SHOT"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_005"
    negative_test_ids:
      - "TEST_ACCESS_NEG_037"
    positive_test_ids:
      - "TEST_ACCESS_POS_037"
  - id: "PERM_038"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_SPIN_SHOT"
    operation: "INSERT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_ANALISTA_OBSERVADOR'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_005"
    negative_test_ids:
      - "TEST_ACCESS_NEG_038"
    positive_test_ids:
      - "TEST_ACCESS_POS_038"
  - id: "PERM_039"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_IN_FLIGHT_SHOT"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_006"
    negative_test_ids:
      - "TEST_ACCESS_NEG_039"
    positive_test_ids:
      - "TEST_ACCESS_POS_039"
  - id: "PERM_040"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_IN_FLIGHT_SHOT"
    operation: "INSERT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_ANALISTA_OBSERVADOR'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_006"
    negative_test_ids:
      - "TEST_ACCESS_NEG_040"
    positive_test_ids:
      - "TEST_ACCESS_POS_040"
  - id: "PERM_041"
    role_id: "ROLE_TREINADOR"
    resource_id: "RES_SISTEMA_TATICO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_041"
    positive_test_ids:
      - "TEST_ACCESS_POS_041"
  - id: "PERM_042"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_SISTEMA_TATICO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    negative_test_ids:
      - "TEST_ACCESS_NEG_042"
    positive_test_ids:
      - "TEST_ACCESS_POS_042"
  - id: "PERM_043"
    role_id: "ROLE_TREINADOR"
    resource_id: "RES_PAPEL_ESPORTIVO_OPERACIONAL"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_043"
    positive_test_ids:
      - "TEST_ACCESS_POS_043"
  - id: "PERM_044"
    role_id: "ROLE_ADMIN"
    resource_id: "RES_PAPEL_ESPORTIVO_OPERACIONAL"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_ADMIN'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_044"
    positive_test_ids:
      - "TEST_ACCESS_POS_044"
  - id: "PERM_045"
    role_id: "ROLE_TREINADOR"
    resource_id: "RES_PARTICIPACAO_EQUIPE_COMPETICAO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_045"
    positive_test_ids:
      - "TEST_ACCESS_POS_045"
  - id: "PERM_046"
    role_id: "ROLE_TREINADOR"
    resource_id: "RES_PARTICIPACAO_EQUIPE_COMPETICAO"
    operation: "INSERT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_TREINADOR'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_CEPRAEA_DATABASE_CCB2A718_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_046"
    positive_test_ids:
      - "TEST_ACCESS_POS_046"
  - id: "PERM_047"
    role_id: "ROLE_ATLETA"
    resource_id: "RES_ATLETA"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.uid() = user_id"
    column_scope: []
    conditions: []
    rule_ids:
      - "RN-DISP-003"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_005"
    negative_test_ids:
      - "TEST_ACCESS_NEG_047"
    positive_test_ids:
      - "TEST_ACCESS_POS_047"
  - id: "PERM_048"
    role_id: "ROLE_TREINADOR"
    resource_id: "RES_ATLETA"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids:
      - "RN-DISP-003"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_005"
    negative_test_ids:
      - "TEST_ACCESS_NEG_048"
    positive_test_ids:
      - "TEST_ACCESS_POS_048"
  - id: "PERM_049"
    role_id: "ROLE_ADMIN"
    resource_id: "RES_ATLETA"
    operation: "UPDATE"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_ADMIN'"
    column_scope: []
    conditions: []
    rule_ids:
      - "RN-DISP-003"
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_049"
    positive_test_ids:
      - "TEST_ACCESS_POS_049"
  - id: "PERM_050"
    role_id: "ROLE_ANALISTA_OBSERVADOR"
    resource_id: "RES_ANALISTA_OBSERVADOR"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.uid() = user_id"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    negative_test_ids:
      - "TEST_ACCESS_NEG_050"
    positive_test_ids:
      - "TEST_ACCESS_POS_050"
  - id: "PERM_051"
    role_id: "ROLE_ADMIN"
    resource_id: "RES_ANALISTA_OBSERVADOR"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_ADMIN'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_051"
    positive_test_ids:
      - "TEST_ACCESS_POS_051"
  - id: "PERM_052"
    role_id: "ROLE_ADMIN"
    resource_id: "RES_ANALISTA_OBSERVADOR"
    operation: "UPDATE"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_ADMIN'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_052"
    positive_test_ids:
      - "TEST_ACCESS_POS_052"
  - id: "PERM_053"
    role_id: "ROLE_TREINADOR"
    resource_id: "RES_DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_015"
    negative_test_ids:
      - "TEST_ACCESS_NEG_053"
    positive_test_ids:
      - "TEST_ACCESS_POS_053"
  - id: "PERM_054"
    role_id: "ROLE_ADMIN"
    resource_id: "RES_DESQUALIFICACAO_SEGUNDA_EXCLUSAO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_ADMIN'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_054"
    positive_test_ids:
      - "TEST_ACCESS_POS_054"
  - id: "PERM_055"
    role_id: "ROLE_TREINADOR"
    resource_id: "RES_CARTAO_AZUL_SUSPENSAO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.role() = 'authenticated'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_017"
    negative_test_ids:
      - "TEST_ACCESS_NEG_055"
    positive_test_ids:
      - "TEST_ACCESS_POS_055"
  - id: "PERM_056"
    role_id: "ROLE_ADMIN"
    resource_id: "RES_CARTAO_AZUL_SUSPENSAO"
    operation: "SELECT"
    effect: "ALLOW"
    grant_required: true
    row_scope: "auth.jwt() ->> 'role' = 'ROLE_ADMIN'"
    column_scope: []
    conditions: []
    rule_ids: []
    evidence_ref_ids:
      - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_002"
    negative_test_ids:
      - "TEST_ACCESS_NEG_056"
    positive_test_ids:
      - "TEST_ACCESS_POS_056"
default_policy:
  effect: "DENY"
  unauthenticated_access: "DENY"
  fallback_rule: "Negação padrão implícita para qualquer requisição, papel ou recurso sem permissão explícita concedida."
  audit_unmatched_requests: true
  evidence_ref_ids:
    - "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_012"
    - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
open_issues:
  - id: "ISSUE_REQUISITOS_ACESSO_STAGE_06"
    status: "ABERTA"
    question: "Necessidade de revisão formal e aprovação humana das matrizes de permissões e políticas de segurança RLS para entrada em produção."
    affected_ids:
      - "ROLE_ADMIN"
      - "ROLE_TREINADOR"
      - "ROLE_ANALISTA_OBSERVADOR"
      - "ROLE_ATLETA"
      - "ROLE_PUBLICO_LEITOR"
    impact: "A especificação permanece em estado de verificação pendente de validação pelo operador do sistema."
    required_evidence: "Termo de homologação assinado pelo responsável pela governança de dados."
    owner: "OPERADOR"
  - id: "ISSUE_SOURCE_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919_001"
    status: "ABERTA"
    question: "As tabelas secondary_positions, calendar_events, competitions, convocations, convocation_athletes, matches, match_appearances, possessions, bous, tactical_events, finalizations e goalkeeper_actions têm RLS habilitado na Seção 1, mas não possuem diretivas CREATE POLICY declaradas no documento."
    affected_ids:
      - "SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
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