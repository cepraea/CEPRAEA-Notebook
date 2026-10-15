# Schema PostgreSQL Candidato (08-schema-postgresql.candidate.sql)

/*
==============================================================================
Arquivo: 08-schema-postgresql.candidate.sql
RUN_ID: RUN_20261014_PARTIDAS_SCOUT_001
Domínio: PARTIDAS_SCOUT_ANALISE_TATICA
Estado: CANDIDATO
Alvo de Compatibilidade: PostgreSQL 15+ (A versão do ambiente de produção ainda não foi verificada)

Entradas Promovidas Selecionadas:
  - LOGICAL_MODEL@0.1.1 (sha256: aebdbd4c7b725a25ce1b89d632ae56e94ee25d5529e8ce7c82ab87387ef2e492, source_id: e2ba2453-a22f-4784-b90d-34173898d6ed)
  - DATA_DICTIONARY@0.1.0 (sha256: 969b7479813c97f5b2da95631b185211495b509cf86147a0337a53dcbb909c2f, source_id: 1c227cde-1ffd-472f-b0ab-92594c05ec2b)
  - TRACEABILITY_MATRIX@0.1.0 (sha256: 3e36cfb319571923d213c8527eda511bd6cba0f193e75dfbb795b94e839e66d1, source_id: 5b4b8ee3-c08d-40b5-bc0d-705f68f2e0dd)
  - ACCESS_REQUIREMENTS@0.1.0 (sha256: bafce57a9d71ef3ea0ba54c79fac585f075d8d0efe5fe22967e62bde6c424c92, source_id: c7f18856-d7c7-4b77-8feb-3266d60337c0)
  - STOP_GATE_PARTIDAS_SCOUT_ANALISE_TATICA@0.2.0 (sha256: 8034fc8290a814a2cb63d7d43138c8552ea087d787f44566b94393449a2d09f0, source_id: 8347d2e6-f0fd-4872-a5f6-b23adae009f3)
  - Decisão Externa do Operador STAGE_07 (sha256: 95861272d84e896a0ba82793b63788d8ec070efa284d4100da47b773e1657c66, source_id: 167b105a-d750-4d7e-bc53-3da5d56e10f4)

Gate Status: READY_WITH_RESTRICTIONS
Decisão: APPROVED_WITH_RESTRICTIONS
Escopo Autorizado: 32 relações
Status de Implementação: NAO_INICIADO
Status de Verificação: NAO_EXECUTADO

Arquitetura de Isolamento & Qualificação de Objetos:
  - Manipulação da variável `search_path` é intencionalmente omitida para garantir isolamento estrito da Data API.
  - Todos os objetos são integralmente qualificados pelos seus respectivos schemas (public.nome_tabela, private.nome_tabela).

Aviso Estrutural: Este arquivo é um candidato de composição e não deve ser aplicado de forma isolada sem validação Pré-DDL do ambiente.
==============================================================================
*/

-- ==============================================================================
-- DEFINIÇÃO DE ESPAÇOS DE NOMES (SCHEMAS) E EXTENSÕES CANDIDATAS
-- ==============================================================================

CREATE SCHEMA public;
CREATE SCHEMA private;

-- Dependência não verificada no ambiente de produção:
-- Extensão Candidata: btree_gist
-- Finalidade: Suporte a restrições de exclusão temporal (EXCLUDE USING gist) para validação de não sobreposição de janelas de vigência.


-- ==============================================================================
-- DDL DAS TABELAS DO SCHEMA PUBLIC (9 RELAÇÕES PÚBLICAS - DATA API EXPOSED)
-- ==============================================================================

-- Relação Lógica 1: COMPETICAO (Acesso: PUBLICO)
-- Trace ID: TRACE_RN_SGATE_0023_PONTUACAO_FHERJ_2026_COMPETICAO
CREATE TABLE public.competicao (
    id uuid NOT NULL,
    nome text NOT NULL,
    codigo text NOT NULL,
    edicao text NULL,
    data_inicio timestamptz NULL,
    data_fim timestamptz NULL,
    CONSTRAINT pk_competicao PRIMARY KEY (id)
);

-- Relação Lógica 2: PARTIDA (Acesso: PUBLICO)
-- Trace ID: TRACE_RN_IHF_VIGENCIA_2026_PARTIDA | TRACE_RN_TETO_PARTICIPANTES_SUMULA_PARTIDA
CREATE TABLE public.partida (
    id uuid NOT NULL,
    competicao_id uuid NOT NULL,
    numero_partida integer NULL,
    etapa text NULL,
    data_hora_inicio timestamptz NULL,
    local_quadra text NULL,
    status_partida text NOT NULL DEFAULT 'AGENDADA',
    CONSTRAINT pk_partida PRIMARY KEY (id),
    CONSTRAINT fk_partida_competicao FOREIGN KEY (competicao_id) REFERENCES public.competicao(id),
    CONSTRAINT chk_partida_status_partida CHECK (status_partida IN ('AGENDADA', 'EM_ANDAMENTO', 'CONCLUIDA', 'CANCELADA', 'INTERROMPIDA'))
);

-- Relação Lógica 3: EQUIPE (Acesso: PUBLICO)
-- Trace ID: TRACE_RN_TETO_PARTICIPANTES_SUMULA_EQUIPE
CREATE TABLE public.equipe (
    id uuid NOT NULL,
    nome text NOT NULL,
    sigla text NULL,
    cidade text NULL,
    uf text NULL,
    CONSTRAINT pk_equipe PRIMARY KEY (id)
);

-- Relação Lógica 4: PARTIDA_EQUIPE (Acesso: PUBLICO)
-- Trace ID: TRACE_RN_TETO_PARTICIPANTES_SUMULA_PARTIDA_EQUIPE
CREATE TABLE public.partida_equipe (
    partida_id uuid NOT NULL,
    equipe_id uuid NOT NULL,
    papel_regulamentar text NOT NULL,
    condicao_mando text NOT NULL,
    cor_uniforme text NULL,
    CONSTRAINT pk_partida_equipe PRIMARY KEY (partida_id, equipe_id),
    CONSTRAINT fk_partida_equipe_partida FOREIGN KEY (partida_id) REFERENCES public.partida(id),
    CONSTRAINT fk_partida_equipe_equipe FOREIGN KEY (equipe_id) REFERENCES public.equipe(id),
    CONSTRAINT uq_partida_papel_regulamentar UNIQUE (partida_id, papel_regulamentar),
    CONSTRAINT uq_partida_condicao_mando UNIQUE (partida_id, condicao_mando),
    CONSTRAINT chk_partida_equipe_papel CHECK (papel_regulamentar IN ('EQUIPE_A', 'EQUIPE_B')),
    CONSTRAINT chk_partida_equipe_mando CHECK (condicao_mando IN ('MANDANTE', 'VISITANTE'))
);

-- Relação Lógica 5: PERIODO_SET (Acesso: PUBLICO)
-- Trace ID: TRACE_RN_IHF_VIGENCIA_2026_PERIODO_SET
CREATE TABLE public.periodo_set (
    id uuid NOT NULL,
    partida_id uuid NOT NULL,
    numero_set integer NOT NULL,
    tempo_duracao_segundos integer NULL,
    houve_gol_de_ouro boolean NOT NULL DEFAULT false,
    equipe_vencedora_id uuid NULL,
    CONSTRAINT pk_periodo_set PRIMARY KEY (id),
    CONSTRAINT fk_periodo_set_partida FOREIGN KEY (partida_id) REFERENCES public.partida(id),
    CONSTRAINT fk_periodo_set_equipe_vencedora FOREIGN KEY (equipe_vencedora_id) REFERENCES public.equipe(id),
    CONSTRAINT uq_partida_numero_set UNIQUE (partida_id, numero_set),
    CONSTRAINT chk_numero_set_valido CHECK (numero_set IN (1, 2))
);

-- Relação Lógica 6: SHOOT_OUT (Acesso: PUBLICO)
-- Trace ID: TRACE_RN_IHF_VIGENCIA_2026_SHOOT_OUT
CREATE TABLE public.shoot_out (
    id uuid NOT NULL,
    partida_id uuid NOT NULL,
    pontos_equipe_a integer NULL,
    pontos_equipe_b integer NULL,
    houve_morte_sudita boolean NOT NULL DEFAULT false,
    equipe_vencedora_id uuid NULL,
    status_completude text NOT NULL,
    motivo_incompletude text NULL,
    CONSTRAINT pk_shoot_out PRIMARY KEY (id),
    CONSTRAINT fk_shoot_out_partida FOREIGN KEY (partida_id) REFERENCES public.partida(id),
    CONSTRAINT fk_shoot_out_equipe_vencedora FOREIGN KEY (equipe_vencedora_id) REFERENCES public.equipe(id),
    CONSTRAINT uq_shoot_out_partida UNIQUE (partida_id),
    CONSTRAINT chk_shoot_out_status_completude CHECK (status_completude IN ('COMPLETO', 'PARCIAL', 'NAO_DOCUMENTADO'))
);

-- Relação Lógica 7: PLACAR_JOGO (Acesso: PUBLICO)
-- Evidence Ref: EVID_IHF_RULES_2026_EN_002
CREATE TABLE public.placar_jogo (
    id uuid NOT NULL,
    partida_id uuid NOT NULL,
    sets_vencidos_equipe_a integer NOT NULL DEFAULT 0,
    sets_vencidos_equipe_b integer NOT NULL DEFAULT 0,
    resultado_final_sets text NULL,
    equipe_vencedora_id uuid NULL,
    CONSTRAINT pk_placar_jogo PRIMARY KEY (id),
    CONSTRAINT fk_placar_jogo_partida FOREIGN KEY (partida_id) REFERENCES public.partida(id),
    CONSTRAINT fk_placar_jogo_equipe_vencedora FOREIGN KEY (equipe_vencedora_id) REFERENCES public.equipe(id),
    CONSTRAINT uq_placar_partida UNIQUE (partida_id),
    CONSTRAINT chk_placar_jogo_resultado CHECK (resultado_final_sets IS NULL OR resultado_final_sets IN ('VITORIA_2_0', 'VITORIA_2_1', 'DERROTA_0_2', 'DERROTA_1_2'))
);

-- Relação Lógica 8: ESTADO_DO_PLACAR (Acesso: PUBLICO)
-- Evidence Ref: EVID_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56_004
CREATE TABLE public.estado_do_placar (
    id uuid NOT NULL,
    placar_jogo_id uuid NOT NULL,
    periodo_set_id uuid NOT NULL,
    pontos_equipe_a integer NOT NULL DEFAULT 0,
    pontos_equipe_b integer NOT NULL DEFAULT 0,
    situacao_vantagem text NOT NULL DEFAULT 'EMPATADO',
    timestamp_instante timestamptz NOT NULL,
    CONSTRAINT pk_estado_do_placar PRIMARY KEY (id),
    CONSTRAINT fk_estado_placar_placar_jogo FOREIGN KEY (placar_jogo_id) REFERENCES public.placar_jogo(id),
    CONSTRAINT fk_estado_placar_periodo_set FOREIGN KEY (periodo_set_id) REFERENCES public.periodo_set(id),
    CONSTRAINT chk_estado_placar_situacao CHECK (situacao_vantagem IN ('EMPATADO', 'FAVORAVEL', 'DESFAVORAVEL'))
);

-- Relação Lógica 9: EVOLUCAO_DO_PLACAR (Acesso: PUBLICO)
-- Observação: A FK evento_scout_id para a tabela private.evento_scout é declarada via ALTER TABLE após a criação do schema private.
CREATE TABLE public.evolucao_do_placar (
    id uuid NOT NULL,
    partida_id uuid NOT NULL,
    evento_scout_id uuid NULL,
    equipe_beneficiada_id uuid NOT NULL,
    sequencial_pontuacao integer NOT NULL,
    valor_incremento integer NOT NULL,
    placar_equipe_a_aft integer NOT NULL,
    placar_equipe_b_aft integer NOT NULL,
    CONSTRAINT pk_evolucao_do_placar PRIMARY KEY (id),
    CONSTRAINT fk_evolucao_placar_partida FOREIGN KEY (partida_id) REFERENCES public.partida(id),
    CONSTRAINT fk_evolucao_placar_equipe FOREIGN KEY (equipe_beneficiada_id) REFERENCES public.equipe(id),
    CONSTRAINT uq_evolucao_partida_seq UNIQUE (partida_id, sequencial_pontuacao),
    CONSTRAINT chk_evolucao_placar_valor_incremento CHECK (valor_incremento IN (1, 2))
);


-- ==============================================================================
-- DDL DAS TABELAS DO SCHEMA PRIVATE (23 RELAÇÕES INTERNAS / RESTRITAS)
-- ==============================================================================

-- Relação Lógica 10: ATLETA (Acesso: RESTRITO)
-- Trace ID: TRACE_RN_SEMANTICA_GOLEIRA_ATLETA
CREATE TABLE private.atleta (
    id uuid NOT NULL,
    nome_completo text NOT NULL, -- PII: Classified under Data Protection Rules
    nome_camisa text NULL, -- PII: Classified under Data Protection Rules
    numero_registro text NULL, -- PII: Classified under Data Protection Rules
    posicao_principal text NULL,
    CONSTRAINT pk_atleta PRIMARY KEY (id),
    CONSTRAINT chk_atleta_semantica_goleira CHECK (
        posicao_principal IS NULL OR 
        posicao_principal IN ('GOLEIRA', 'ESPECIALISTA', 'PIVO', 'ALA_DIREITA', 'ALA_ESQUERDA', 'DEFENSORA')
    )
);

-- Relação Lógica 11: ANALISTA_OBSERVADOR (Acesso: RESTRITO)
-- Trace ID: TRACE_RN_REJEICAO_VARIAVEIS_INFERENCIAIS_OBSERVACAO_DE_SCOUT
CREATE TABLE private.analista_observador (
    id uuid NOT NULL,
    nome text NOT NULL, -- PII: Classified under Data Protection Rules
    email text NOT NULL, -- PII: Classified under Data Protection Rules
    status_habilitacao text NOT NULL DEFAULT 'HABILITADO',
    CONSTRAINT pk_analista_observador PRIMARY KEY (id),
    CONSTRAINT chk_analista_status_habilitacao CHECK (status_habilitacao IN ('HABILITADO', 'EM_TREINAMENTO', 'DESABILITADO'))
);

-- Relação Lógica 12: PROTOCOLO_SCOUT (Acesso: INTERNO)
-- Evidence Ref: EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001
CREATE TABLE private.protocolo_scout (
    id uuid NOT NULL,
    codigo_protocolo text NOT NULL,
    versao text NOT NULL,
    descricao text NULL,
    data_congelamento timestamptz NULL,
    CONSTRAINT pk_protocolo_scout PRIMARY KEY (id)
);

-- Relação Lógica 13: MIDIA_VIDEO (Acesso: INTERNO)
-- Evidence Ref: EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001
CREATE TABLE private.midia_video (
    id uuid NOT NULL,
    partida_id uuid NULL,
    uri_storage text NOT NULL,
    checksum_sha256 text NULL,
    tipo_midia text NOT NULL DEFAULT 'BROADCAST_P0',
    duracao_segundos numeric NULL,
    CONSTRAINT pk_midia_video PRIMARY KEY (id),
    CONSTRAINT fk_midia_video_partida FOREIGN KEY (partida_id) REFERENCES public.partida(id),
    CONSTRAINT chk_midia_video_tipo CHECK (tipo_midia IN ('BROADCAST_P0', 'CAMARA_ALTA_TATICA', 'CORTE_CLIPE'))
);

-- Relação Lógica 14: EQUIPE_ATLETA_INSCRICAO (Acesso: INTERNO)
-- Rule Ref: RN_PRAZO_INSCRICAO_ATLETA_72H
CREATE TABLE private.equipe_atleta_inscricao (
    id uuid NOT NULL,
    equipe_id uuid NOT NULL,
    atleta_id uuid NOT NULL, -- PII: References PII Entity
    competicao_id uuid NULL,
    data_inscricao timestamptz NOT NULL,
    numero_camisa integer NULL,
    status_elegibilidade text NOT NULL DEFAULT 'ELEGIVEL',
    CONSTRAINT pk_equipe_atleta_inscricao PRIMARY KEY (id),
    CONSTRAINT fk_inscricao_equipe FOREIGN KEY (equipe_id) REFERENCES public.equipe(id),
    CONSTRAINT fk_inscricao_atleta FOREIGN KEY (atleta_id) REFERENCES private.atleta(id),
    CONSTRAINT fk_inscricao_competicao FOREIGN KEY (competicao_id) REFERENCES public.competicao(id),
    CONSTRAINT uq_equipe_atleta_competicao UNIQUE (equipe_id, atleta_id, competicao_id),
    CONSTRAINT chk_equipe_atleta_inscricao_status CHECK (status_elegibilidade IN ('ELEGIVEL', 'SUSPENSO', 'INATIVO', 'PENDENTE_DOCUMENTACAO'))
);

-- Relação Lógica 15: POSSE_DE_BOLA (Acesso: INTERNO)
-- Evidence Ref: EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003
CREATE TABLE private.posse_de_bola (
    id uuid NOT NULL,
    periodo_set_id uuid NOT NULL,
    equipe_possuidora_id uuid NOT NULL,
    sequencial_posse integer NOT NULL,
    timecode_inicio text NULL,
    timecode_fim text NULL,
    fase_ofensiva_dominante text NULL,
    motivo_termino text NULL,
    CONSTRAINT pk_posse_de_bola PRIMARY KEY (id),
    CONSTRAINT fk_posse_de_bola_periodo_set FOREIGN KEY (periodo_set_id) REFERENCES public.periodo_set(id),
    CONSTRAINT fk_posse_de_bola_equipe FOREIGN KEY (equipe_possuidora_id) REFERENCES public.equipe(id),
    CONSTRAINT uq_posse_periodo_seq UNIQUE (periodo_set_id, sequencial_posse),
    CONSTRAINT chk_posse_fase_ofensiva CHECK (fase_ofensiva_dominante IS NULL OR fase_ofensiva_dominante IN ('TRANSICAO_OFENSIVA', 'ATAQUE_POSICIONAL')),
    CONSTRAINT chk_posse_motivo_termino CHECK (motivo_termino IS NULL OR motivo_termino IN ('GOL', 'DEFESA_GOLEIRA', 'ERRO_TECNICO', 'FALTA_REVERSAO', 'BOLA_FORA', 'FIM_PERIODO'))
);

-- Relação Lógica 16: UNIDADE_BASICA_ATAQUE_BOU (Acesso: INTERNO)
-- Trace ID: TRACE_RN_REJEICAO_VARIAVEIS_INFERENCIAIS_UNIDADE_BASICA_ATAQUE_BOU
CREATE TABLE private.unidade_basica_ataque_bou (
    id uuid NOT NULL,
    posse_de_bola_id uuid NOT NULL,
    sequencial_bou integer NOT NULL,
    timecode_inicio text NULL,
    timecode_fim text NULL,
    fase_tatica text NOT NULL,
    CONSTRAINT pk_unidade_basica_ataque_bou PRIMARY KEY (id),
    CONSTRAINT fk_bou_posse_de_bola FOREIGN KEY (posse_de_bola_id) REFERENCES private.posse_de_bola(id),
    CONSTRAINT uq_bou_posse_seq UNIQUE (posse_de_bola_id, sequencial_bou),
    CONSTRAINT chk_bou_fase_tatica CHECK (fase_tatica IN ('TO', 'AP', 'TD', 'DP', 'F_IND'))
);

-- Relação Lógica 17: OBSERVACAO_DE_SCOUT (Acesso: INTERNO)
-- Trace ID: TRACE_RN_REJEICAO_VARIAVEIS_INFERENCIAIS_OBSERVACAO_DE_SCOUT
CREATE TABLE private.observacao_de_scout (
    id uuid NOT NULL,
    partida_id uuid NOT NULL,
    analista_observador_id uuid NOT NULL, -- PII: References PII Entity
    protocolo_scout_id uuid NOT NULL,
    midia_video_id uuid NOT NULL,
    data_hora_codificacao timestamptz NOT NULL,
    tipo_observacao text NOT NULL DEFAULT 'PRIMARIA_P1',
    CONSTRAINT pk_observacao_de_scout PRIMARY KEY (id),
    CONSTRAINT fk_observacao_scout_partida FOREIGN KEY (partida_id) REFERENCES public.partida(id),
    CONSTRAINT fk_observacao_scout_analista FOREIGN KEY (analista_observador_id) REFERENCES private.analista_observador(id),
    CONSTRAINT fk_observacao_scout_protocolo FOREIGN KEY (protocolo_scout_id) REFERENCES private.protocolo_scout(id),
    CONSTRAINT fk_observacao_scout_midia FOREIGN KEY (midia_video_id) REFERENCES private.midia_video(id),
    CONSTRAINT chk_observacao_scout_tipo CHECK (tipo_observacao IN ('PRIMARIA_P1', 'REVISAO_AUDITORIA', 'AUTOMATIZADA_IA'))
);

-- Relação Lógica 18: EVENTO_SCOUT (Acesso: INTERNO)
-- Trace ID: TRACE_RN_SEMANTICA_GOLEIRA_EVENTO_SCOUT
CREATE TABLE private.evento_scout (
    id uuid NOT NULL,
    observacao_de_scout_id uuid NOT NULL,
    unidade_basica_ataque_bou_id uuid NULL,
    atleta_executor_id uuid NULL, -- PII: References PII Entity
    atleta_alvo_id uuid NULL, -- PII: References PII Entity
    timecode_exato text NOT NULL,
    zona_analitica text NULL,
    tipo_acao_observada text NOT NULL,
    resultado_acao text NULL,
    acao_goleira text NULL,
    punicao_disciplinar text NULL,
    consequencia_disciplinar text NULL,
    pontos_gerados integer NOT NULL DEFAULT 0,
    CONSTRAINT pk_evento_scout PRIMARY KEY (id),
    CONSTRAINT fk_evento_scout_observacao FOREIGN KEY (observacao_de_scout_id) REFERENCES private.observacao_de_scout(id),
    CONSTRAINT fk_evento_scout_bou FOREIGN KEY (unidade_basica_ataque_bou_id) REFERENCES private.unidade_basica_ataque_bou(id),
    CONSTRAINT fk_evento_scout_atleta_exec FOREIGN KEY (atleta_executor_id) REFERENCES private.atleta(id),
    CONSTRAINT fk_evento_scout_atleta_alvo FOREIGN KEY (atleta_alvo_id) REFERENCES private.atleta(id),
    CONSTRAINT chk_evento_scout_zona CHECK (zona_analitica IS NULL OR zona_analitica IN ('ZE', 'ZCE', 'ZCD', 'ZD')),
    CONSTRAINT chk_evento_scout_tipo_acao CHECK (tipo_acao_observada IN ('PONTUACAO_SIMPLES', 'PONTUACAO_DUPLA', 'ARREMESSO_SPIN', 'ARREMESSO_IN_FLIGHT', 'ARREMESSO_SIMPLES', 'TIRO_SEIS_METROS', 'PASSE', 'RECEPCAO', 'DESARME', 'BLOQUEIO', 'DEFESA_GOLEIRA', 'FALTA_COMETIDA', 'FALTA_SOFRIDA', 'EXCLUSAO_DISCIPLINAR', 'CARTAO_AZUL')),
    CONSTRAINT chk_evento_scout_resultado CHECK (resultado_acao IS NULL OR resultado_acao IN ('GOL', 'DEFESA', 'FORA', 'TRAVE', 'ERRO_TECNICO', 'FALTA_SOFRIDA')),
    CONSTRAINT chk_evento_scout_acao_goleira CHECK (acao_goleira IS NULL OR acao_goleira IN ('DEFESA_PARADA', 'DEFESA_COUNTER_SPIN', 'DEFESA_COUNTER_FLY', 'PASSE_TRANSICAO_T4', 'ARREMESSO_DIRETO_GOLEIRA', 'INTERVENCAO_SHOOTOUT')),
    CONSTRAINT chk_evento_scout_punicao CHECK (punicao_disciplinar IS NULL OR punicao_disciplinar IN ('ADVERTENCIA', 'EXCLUSAO_TEMPORARIA', 'DESQUALIFICACAO_DIRETA', 'CARTAO_AZUL')),
    CONSTRAINT chk_evento_scout_consequencia CHECK (consequencia_disciplinar IS NULL OR consequencia_disciplinar IN ('REDUCAO_NUMERICA_QUADRA', 'SUSPENSAO_PROXIMA_PARTIDA', 'CONCESSAO_TIRO_SIX_METROS'))
);

-- Conexão Cruzada de Schema: Adicionar FK pendente de public.evolucao_do_placar para private.evento_scout
ALTER TABLE public.evolucao_do_placar 
    ADD CONSTRAINT fk_evolucao_placar_evento_scout 
    FOREIGN KEY (evento_scout_id) REFERENCES private.evento_scout(id);

-- Relação Lógica 19: SEGMENTO_OBSERVADO (Acesso: INTERNO)
-- Evidence Ref: EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001
CREATE TABLE private.segmento_observado (
    id uuid NOT NULL,
    partida_id uuid NOT NULL,
    midia_video_id uuid NOT NULL,
    timecode_inicio text NOT NULL,
    timecode_fim text NOT NULL,
    ordem_intervalo integer NOT NULL,
    CONSTRAINT pk_segmento_observado PRIMARY KEY (id),
    CONSTRAINT fk_segmento_observado_partida FOREIGN KEY (partida_id) REFERENCES public.partida(id),
    CONSTRAINT fk_segmento_observado_midia FOREIGN KEY (midia_video_id) REFERENCES private.midia_video(id),
    CONSTRAINT uq_segmento_ordem UNIQUE (partida_id, midia_video_id, ordem_intervalo)
);

-- Relação Lógica 20: SISTEMA_TATICO (Acesso: INTERNO)
-- Evidence Ref: EVID_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2_005
CREATE TABLE private.sistema_tatico (
    id uuid NOT NULL,
    posse_de_bola_id uuid NOT NULL,
    equipe_id uuid NOT NULL,
    codigo_sistema_tatico text NOT NULL,
    fase_tatica text NOT NULL,
    CONSTRAINT pk_sistema_tatico PRIMARY KEY (id),
    CONSTRAINT fk_sistema_tatico_posse FOREIGN KEY (posse_de_bola_id) REFERENCES private.posse_de_bola(id),
    CONSTRAINT fk_sistema_tatico_equipe FOREIGN KEY (equipe_id) REFERENCES public.equipe(id),
    CONSTRAINT chk_sistema_tatico_codigo CHECK (codigo_sistema_tatico IN ('ATAQUE_3_1', 'ATAQUE_2_2', 'ATAQUE_4_0', 'DEFESA_3_0', 'DEFESA_2_1', 'DEFESA_1_2')),
    CONSTRAINT chk_sistema_tatico_fase CHECK (fase_tatica IN ('TO', 'AP', 'TD', 'DP', 'F_IND'))
);

-- Relação Lógica 21: SISTEMA_DEFENSIVO (Acesso: INTERNO)
-- Evidence Ref: EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_005
CREATE TABLE private.sistema_defensivo (
    id uuid NOT NULL,
    posse_de_bola_id uuid NOT NULL,
    equipe_id uuid NOT NULL,
    sistema_tatico_id uuid NULL,
    codigo_sistema_defensivo text NOT NULL,
    em_desvantagem_numerica boolean NOT NULL DEFAULT false,
    CONSTRAINT pk_sistema_defensivo PRIMARY KEY (id),
    CONSTRAINT fk_sistema_defensivo_posse FOREIGN KEY (posse_de_bola_id) REFERENCES private.posse_de_bola(id),
    CONSTRAINT fk_sistema_defensivo_equipe FOREIGN KEY (equipe_id) REFERENCES public.equipe(id),
    CONSTRAINT fk_sistema_defensivo_sistema_tatico FOREIGN KEY (sistema_tatico_id) REFERENCES private.sistema_tatico(id),
    CONSTRAINT chk_sistema_defensivo_codigo CHECK (codigo_sistema_defensivo IN ('SIS_3_0', 'SIS_2_1_CENTRAL', 'SIS_2_1_LATERAL', 'SIS_1_2', 'SIS_AVANCADO_7M', 'SIS_REATIVO', 'SIS_PROATIVO'))
);

-- Relação Lógica 22: CONFIABILIDADE_OBSERVADOR (Acesso: INTERNO)
-- Evidence Ref: EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009
CREATE TABLE private.confiabilidade_observador (
    id uuid NOT NULL,
    analista_observador_id uuid NOT NULL, -- PII: References PII Entity
    data_avaliacao timestamptz NOT NULL,
    versao_teste text NOT NULL,
    percentual_acerto numeric NOT NULL,
    erros_criticos_qtd integer NOT NULL DEFAULT 0,
    kappa_cohen numeric NULL,
    status_qualificacao text NOT NULL,
    CONSTRAINT pk_confiabilidade_observador PRIMARY KEY (id),
    CONSTRAINT fk_confiabilidade_analista FOREIGN KEY (analista_observador_id) REFERENCES private.analista_observador(id),
    CONSTRAINT chk_confiabilidade_status CHECK (status_qualificacao IN ('QUALIFICADO', 'NAO_QUALIFICADO'))
);

-- Relação Lógica 23: REVISAO_DA_OBSERVACAO (Acesso: INTERNO)
-- Evidence Ref: EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_007
CREATE TABLE private.revisao_da_observacao (
    id uuid NOT NULL,
    observacao_de_scout_id uuid NOT NULL,
    analista_revisor_id uuid NOT NULL, -- PII: References PII Entity
    timestamp_revisao timestamptz NOT NULL,
    motivo_revisao text NULL,
    campo_alterado text NULL,
    CONSTRAINT pk_revisao_da_observacao PRIMARY KEY (id),
    CONSTRAINT fk_revisao_observacao_obs FOREIGN KEY (observacao_de_scout_id) REFERENCES private.observacao_de_scout(id),
    CONSTRAINT fk_revisao_observacao_analista FOREIGN KEY (analista_revisor_id) REFERENCES private.analista_observador(id)
);

-- Relação Lógica 24: ESTADO_DE_REVISAO (Acesso: INTERNO)
-- Evidence Ref: EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_022
CREATE TABLE private.estado_de_revisao (
    id uuid NOT NULL,
    observacao_de_scout_id uuid NOT NULL,
    revisao_da_observacao_id uuid NULL,
    status_corrente text NOT NULL DEFAULT 'PENDENTE',
    data_ultima_atualizacao timestamptz NOT NULL,
    CONSTRAINT pk_estado_de_revisao PRIMARY KEY (id),
    CONSTRAINT fk_estado_revisao_observacao FOREIGN KEY (observacao_de_scout_id) REFERENCES private.observacao_de_scout(id),
    CONSTRAINT fk_estado_revisao_revisao FOREIGN KEY (revisao_da_observacao_id) REFERENCES private.revisao_da_observacao(id),
    CONSTRAINT uq_estado_revisao_observa UNIQUE (observacao_de_scout_id),
    CONSTRAINT chk_estado_revisao_status CHECK (status_corrente IN ('PENDENTE', 'APROVADO', 'REJEITADO', 'EM_AUDITORIA'))
);

-- Relação Lógica 25: PROVENIENCIA_OBSERVACAO (Acesso: INTERNO)
-- Evidence Ref: EVID_CEPRAEA_DATABASE_CCB2A718_001
CREATE TABLE private.proveniencia_observacao (
    id uuid NOT NULL,
    observacao_de_scout_id uuid NOT NULL,
    protocolo_scout_id uuid NOT NULL,
    midia_video_id uuid NOT NULL,
    ferramenta_software text NOT NULL,
    origem_dado text NOT NULL,
    checksum_midia text NULL,
    CONSTRAINT pk_proveniencia_observacao PRIMARY KEY (id),
    CONSTRAINT fk_proveniencia_observacao_obs FOREIGN KEY (observacao_de_scout_id) REFERENCES private.observacao_de_scout(id),
    CONSTRAINT fk_proveniencia_protocolo FOREIGN KEY (protocolo_scout_id) REFERENCES private.protocolo_scout(id),
    CONSTRAINT fk_proveniencia_midia FOREIGN KEY (midia_video_id) REFERENCES private.midia_video(id),
    CONSTRAINT uq_proveniencia_obs UNIQUE (observacao_de_scout_id),
    CONSTRAINT chk_proveniencia_origem CHECK (origem_dado IN ('CODIFICACAO_HUMANA_P1', 'SUMULA_OFICIAL', 'EXTRACAO_AUTOMATIZADA'))
);

-- Relação Lógica 26: TRECHO_OBSERVADO (Acesso: INTERNO)
-- RECONCILIAÇÃO EXPLICITA (DIVERGÊNCIA 1): A restrição UQ_TRECHO_EVENTO foi OMITIDA intencionalmente conforme Decisão do Operador STAGE_07 para preservar a cardinalidade de 0..N trechos observados por evento de scout.
CREATE TABLE private.trecho_observado (
    id uuid NOT NULL,
    evento_scout_id uuid NOT NULL,
    midia_video_id uuid NOT NULL,
    timecode_inicio text NOT NULL,
    timecode_fim text NOT NULL,
    offset_milissegundos integer NULL,
    CONSTRAINT pk_trecho_observado PRIMARY KEY (id),
    CONSTRAINT fk_trecho_observado_evento FOREIGN KEY (evento_scout_id) REFERENCES private.evento_scout(id),
    CONSTRAINT fk_trecho_observado_midia FOREIGN KEY (midia_video_id) REFERENCES private.midia_video(id)
);

-- Relação Lógica 27: SPIN_SHOT (Acesso: INTERNO)
-- Evidence Ref: EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_005
CREATE TABLE private.spin_shot (
    id uuid NOT NULL,
    evento_scout_id uuid NOT NULL,
    rotacao_completa_360 boolean NOT NULL DEFAULT true,
    salto_pe_direcionado boolean NOT NULL DEFAULT true,
    valor_pontos integer NOT NULL DEFAULT 2,
    CONSTRAINT pk_spin_shot PRIMARY KEY (id),
    CONSTRAINT fk_spin_shot_evento FOREIGN KEY (evento_scout_id) REFERENCES private.evento_scout(id),
    CONSTRAINT uq_spin_shot_evento UNIQUE (evento_scout_id),
    CONSTRAINT chk_spin_shot_valor_pontos CHECK (valor_pontos = 2)
);

-- Relação Lógica 28: IN_FLIGHT_SHOT (Acesso: INTERNO)
-- Evidence Ref: EVID_IHF_RULES_2026_EN_014
CREATE TABLE private.in_flight_shot (
    id uuid NOT NULL,
    evento_scout_id uuid NOT NULL,
    recepcao_no_ar boolean NOT NULL DEFAULT true,
    sem_contato_areia boolean NOT NULL DEFAULT true,
    valor_pontos integer NOT NULL DEFAULT 2,
    CONSTRAINT pk_in_flight_shot PRIMARY KEY (id),
    CONSTRAINT fk_in_flight_shot_evento FOREIGN KEY (evento_scout_id) REFERENCES private.evento_scout(id),
    CONSTRAINT uq_in_flight_evento UNIQUE (evento_scout_id),
    CONSTRAINT chk_in_flight_valor_pontos CHECK (valor_pontos = 2)
);

-- Relação Lógica 29: DESQUALIFICACAO_SEGUNDA_EXCLUSAO (Acesso: RESTRITO)
-- Evidence Ref: EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_015
CREATE TABLE private.desqualificacao_segunda_exclusao (
    id uuid NOT NULL,
    evento_scout_id uuid NOT NULL,
    atleta_id uuid NOT NULL, -- PII: References PII Entity
    partida_id uuid NOT NULL,
    saida_imediata_quadra boolean NOT NULL DEFAULT true,
    CONSTRAINT pk_desqualificacao_segunda_exclusao PRIMARY KEY (id),
    CONSTRAINT fk_desqualificacao_evento FOREIGN KEY (evento_scout_id) REFERENCES private.evento_scout(id),
    CONSTRAINT fk_desqualificacao_atleta FOREIGN KEY (atleta_id) REFERENCES private.atleta(id),
    CONSTRAINT fk_desqualificacao_partida FOREIGN KEY (partida_id) REFERENCES public.partida(id),
    CONSTRAINT uq_desq_exc_evento UNIQUE (evento_scout_id)
);

-- Relação Lógica 30: PAPEL_ESPORTIVO_OPERACIONAL (Acesso: INTERNO)
-- Evidence Ref: EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_003
CREATE TABLE private.papel_esportivo_operacional (
    id uuid NOT NULL,
    partida_id uuid NOT NULL,
    equipe_id uuid NULL,
    nome_pessoa text NOT NULL, -- PII: Classified under Data Protection Rules
    codigo_papel text NOT NULL,
    CONSTRAINT pk_papel_esportivo_operacional PRIMARY KEY (id),
    CONSTRAINT fk_papel_operacional_partida FOREIGN KEY (partida_id) REFERENCES public.partida(id),
    CONSTRAINT fk_papel_operacional_equipe FOREIGN KEY (equipe_id) REFERENCES public.equipe(id),
    CONSTRAINT chk_papel_operacional_codigo CHECK (codigo_papel IN ('TECNICO', 'AUXILIAR_TECNICO', 'MEDICO', 'FISIOTERAPEUTA', 'DELEGADO_A', 'DELEGADO_B', 'SECRETARIO', 'CRONOMETRISTA', 'OFICIAL_ARBITRAGEM'))
);

-- Relação Lógica 31: CARTAO_AZUL_SUSPENSAO (Acesso: RESTRITO)
-- Evidence Ref: EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_015
CREATE TABLE private.cartao_azul_suspensao (
    id uuid NOT NULL,
    evento_scout_id uuid NOT NULL,
    partida_id uuid NOT NULL,
    atleta_id uuid NULL, -- PII: References PII Entity
    papel_operacional_id uuid NULL,
    relatorio_arbitragem text NOT NULL,
    jogos_suspensao_automatica integer NOT NULL DEFAULT 1,
    CONSTRAINT pk_cartao_azul_suspensao PRIMARY KEY (id),
    CONSTRAINT fk_cartao_azul_evento FOREIGN KEY (evento_scout_id) REFERENCES private.evento_scout(id),
    CONSTRAINT fk_cartao_azul_partida FOREIGN KEY (partida_id) REFERENCES public.partida(id),
    CONSTRAINT fk_cartao_azul_atleta FOREIGN KEY (atleta_id) REFERENCES private.atleta(id),
    CONSTRAINT fk_cartao_azul_papel_operacional FOREIGN KEY (papel_operacional_id) REFERENCES private.papel_esportivo_operacional(id),
    CONSTRAINT uq_cartao_azul_evento UNIQUE (evento_scout_id)
);

-- Relação Lógica 32: PARTICIPACAO_EQUIPE_COMPETICAO (Acesso: INTERNO)
-- Trace ID: TRACE_RN_SGATE_0023_PONTUACAO_FHERJ_2026_PARTICIPACAO_EQUIPE_COMPETICAO
-- RECONCILIAÇÃO EXPLICITA (DIVERGÊNCIA 2):
-- 1. A restrição CHK_VIGENCIA_PARTICIPACAO foi OMITIDA conforme Decisão do Operador STAGE_07.
-- 2. Foi criada unicamente a restrição CHK_INTERVALO_VIGENCIA_PARTICIPACAO para validação da coerência da linha (valido_ate IS NULL OR valido_ate >= valido_desde).
-- 3. A não sobreposição temporal de janelas é uma constraint candidata dependente da extensão btree_gist (ainda não verificada no ambiente):
--    Sintaxe para ativação futura: EXCLUDE USING gist (competicao_id WITH =, equipe_id WITH =, tstzrange(valido_desde, valido_ate, '[]') WITH &&)
CREATE TABLE private.participacao_equipe_competicao (
    id uuid NOT NULL,
    competicao_id uuid NOT NULL,
    equipe_id uuid NOT NULL,
    tipo_participacao text NOT NULL,
    status_elegibilidade_ranking text NOT NULL,
    motivo_decisao text NULL,
    decisao_ref text NULL,
    valido_desde timestamptz NOT NULL,
    valido_ate timestamptz NULL,
    CONSTRAINT pk_participacao_equipe_competicao PRIMARY KEY (id),
    CONSTRAINT fk_participacao_equipe_competicao_competicao FOREIGN KEY (competicao_id) REFERENCES public.competicao(id),
    CONSTRAINT fk_participacao_equipe_competicao_equipe FOREIGN KEY (equipe_id) REFERENCES public.equipe(id),
    CONSTRAINT chk_intervalo_vigencia_participacao CHECK (valido_ate IS NULL OR valido_ate >= valido_desde),
    CONSTRAINT chk_participacao_tipo CHECK (tipo_participacao IN ('REGULAR', 'CONVIDADA')),
    CONSTRAINT chk_participacao_status_ranking CHECK (status_elegibilidade_ranking IN ('ELEGIVEL', 'INELEGIVEL_POR_DECISAO_COLETIVA', 'PENDENTE_DELIBERACAO'))
);


-- ==============================================================================
-- ÍNDICES DE SUPORTE OBRIGATÓRIOS PARA AS 59 CHAVES ESTRANGEIRAS (FKS)
-- ==============================================================================

-- 1. FK: public.partida(competicao_id)
CREATE INDEX idx_partida_competicao ON public.partida (competicao_id);

-- 2. FK: public.partida_equipe(partida_id)
-- Índice Omitido: Coberto como prefixo esquerdo da CHAVE PRIMÁRIA pk_partida_equipe(partida_id, equipe_id).

-- 3. FK: public.partida_equipe(equipe_id)
CREATE INDEX idx_partida_equipe_equipe ON public.partida_equipe (equipe_id);

-- 4. FK: public.periodo_set(partida_id)
CREATE INDEX idx_periodo_set_partida ON public.periodo_set (partida_id);

-- 5. FK: public.periodo_set(equipe_vencedora_id)
CREATE INDEX idx_periodo_set_equipe_vencedora ON public.periodo_set (equipe_vencedora_id);

-- 6. FK: public.shoot_out(partida_id)
-- Índice Omitido: Coberto pela restrição UNIQUE uq_shoot_out_partida(partida_id).

-- 7. FK: public.shoot_out(equipe_vencedora_id)
CREATE INDEX idx_shoot_out_equipe_vencedora ON public.shoot_out (equipe_vencedora_id);

-- 8. FK: public.placar_jogo(partida_id)
-- Índice Omitido: Coberto pela restrição UNIQUE uq_placar_partida(partida_id).

-- 9. FK: public.placar_jogo(equipe_vencedora_id)
CREATE INDEX idx_placar_jogo_equipe_vencedora ON public.placar_jogo (equipe_vencedora_id);

-- 10. FK: public.estado_do_placar(placar_jogo_id)
CREATE INDEX idx_estado_placar_placar_jogo ON public.estado_do_placar (placar_jogo_id);

-- 11. FK: public.estado_do_placar(periodo_set_id)
CREATE INDEX idx_estado_placar_periodo_set ON public.estado_do_placar (periodo_set_id);

-- 12. FK: public.evolucao_do_placar(partida_id)
CREATE INDEX idx_evolucao_placar_partida ON public.evolucao_do_placar (partida_id);

-- 13. FK: public.evolucao_do_placar(evento_scout_id)
CREATE INDEX idx_evolucao_placar_evento_scout ON public.evolucao_do_placar (evento_scout_id);

-- 14. FK: public.evolucao_do_placar(equipe_beneficiada_id)
CREATE INDEX idx_evolucao_placar_equipe ON public.evolucao_do_placar (equipe_beneficiada_id);

-- 15. FK: private.equipe_atleta_inscricao(equipe_id)
CREATE INDEX idx_inscricao_equipe ON private.equipe_atleta_inscricao (equipe_id);

-- 16. FK: private.equipe_atleta_inscricao(atleta_id)
CREATE INDEX idx_inscricao_atleta ON private.equipe_atleta_inscricao (atleta_id);

-- 17. FK: private.equipe_atleta_inscricao(competicao_id)
CREATE INDEX idx_inscricao_competicao ON private.equipe_atleta_inscricao (competicao_id);

-- 18. FK: private.posse_de_bola(periodo_set_id)
CREATE INDEX idx_posse_de_bola_periodo_set ON private.posse_de_bola (periodo_set_id);

-- 19. FK: private.posse_de_bola(equipe_possuidora_id)
CREATE INDEX idx_posse_de_bola_equipe ON private.posse_de_bola (equipe_possuidora_id);

-- 20. FK: private.unidade_basica_ataque_bou(posse_de_bola_id)
CREATE INDEX idx_bou_posse_de_bola ON private.unidade_basica_ataque_bou (posse_de_bola_id);

-- 21. FK: private.observacao_de_scout(partida_id)
CREATE INDEX idx_observacao_scout_partida ON private.observacao_de_scout (partida_id);

-- 22. FK: private.observacao_de_scout(analista_observador_id)
CREATE INDEX idx_observacao_scout_analista ON private.observacao_de_scout (analista_observador_id);

-- 23. FK: private.observacao_de_scout(protocolo_scout_id)
CREATE INDEX idx_observacao_scout_protocolo ON private.observacao_de_scout (protocolo_scout_id);

-- 24. FK: private.observacao_de_scout(midia_video_id)
CREATE INDEX idx_observacao_scout_midia ON private.observacao_de_scout (midia_video_id);

-- 25. FK: private.evento_scout(observacao_de_scout_id)
CREATE INDEX idx_evento_scout_observacao ON private.evento_scout (observacao_de_scout_id);

-- 26. FK: private.evento_scout(unidade_basica_ataque_bou_id)
CREATE INDEX idx_evento_scout_bou ON private.evento_scout (unidade_basica_ataque_bou_id);

-- 27. FK: private.evento_scout(atleta_executor_id)
CREATE INDEX idx_evento_scout_atleta_exec ON private.evento_scout (atleta_executor_id);

-- 28. FK: private.evento_scout(atleta_alvo_id)
CREATE INDEX idx_evento_scout_atleta_alvo ON private.evento_scout (atleta_alvo_id);

-- 29. FK: private.midia_video(partida_id)
CREATE INDEX idx_midia_video_partida ON private.midia_video (partida_id);

-- 30. FK: private.segmento_observado(partida_id)
CREATE INDEX idx_segmento_observado_partida ON private.segmento_observado (partida_id);

-- 31. FK: private.segmento_observado(midia_video_id)
CREATE INDEX idx_segmento_observado_midia ON private.segmento_observado (midia_video_id);

-- 32. FK: private.sistema_defensivo(posse_de_bola_id)
CREATE INDEX idx_sistema_defensivo_posse ON private.sistema_defensivo (posse_de_bola_id);

-- 33. FK: private.sistema_defensivo(equipe_id)
CREATE INDEX idx_sistema_defensivo_equipe ON private.sistema_defensivo (equipe_id);

-- 34. FK: private.sistema_defensivo(sistema_tatico_id)
CREATE INDEX idx_sistema_defensivo_sistema_tatico ON private.sistema_defensivo (sistema_tatico_id);

-- 35. FK: private.confiabilidade_observador(analista_observador_id)
CREATE INDEX idx_confiabilidade_analista ON private.confiabilidade_observador (analista_observador_id);

-- 36. FK: private.revisao_da_observacao(observacao_de_scout_id)
CREATE INDEX idx_revisao_observacao_obs ON private.revisao_da_observacao (observacao_de_scout_id);

-- 37. FK: private.revisao_da_observacao(analista_revisor_id)
CREATE INDEX idx_revisao_observacao_analista ON private.revisao_da_observacao (analista_revisor_id);

-- 38. FK: private.estado_de_revisao(observacao_de_scout_id)
-- Índice Omitido: Coberto pela restrição UNIQUE uq_estado_revisao_observa(observacao_de_scout_id).

-- 39. FK: private.estado_de_revisao(revisao_da_observacao_id)
CREATE INDEX idx_estado_revisao_revisao ON private.estado_de_revisao (revisao_da_observacao_id);

-- 40. FK: private.proveniencia_observacao(observacao_de_scout_id)
-- Índice Omitido: Coberto pela restrição UNIQUE uq_proveniencia_obs(observacao_de_scout_id).

-- 41. FK: private.proveniencia_observacao(protocolo_scout_id)
CREATE INDEX idx_proveniencia_protocolo ON private.proveniencia_observacao (protocolo_scout_id);

-- 42. FK: private.proveniencia_observacao(midia_video_id)
CREATE INDEX idx_proveniencia_midia ON private.proveniencia_observacao (midia_video_id);

-- 43. FK: private.trecho_observado(evento_scout_id)
CREATE INDEX idx_trecho_observado_evento ON private.trecho_observado (evento_scout_id);

-- 44. FK: private.trecho_observado(midia_video_id)
CREATE INDEX idx_trecho_observado_midia ON private.trecho_observado (midia_video_id);

-- 45. FK: private.spin_shot(evento_scout_id)
-- Índice Omitido: Coberto pela restrição UNIQUE uq_spin_shot_evento(evento_scout_id).

-- 46. FK: private.in_flight_shot(evento_scout_id)
-- Índice Omitido: Coberto pela restrição UNIQUE uq_in_flight_evento(evento_scout_id).

-- 47. FK: private.desqualificacao_segunda_exclusao(evento_scout_id)
-- Índice Omitido: Coberto pela restrição UNIQUE uq_desq_exc_evento(evento_scout_id).

-- 48. FK: private.desqualificacao_segunda_exclusao(atleta_id)
CREATE INDEX idx_desqualificacao_atleta ON private.desqualificacao_segunda_exclusao (atleta_id);

-- 49. FK: private.desqualificacao_segunda_exclusao(partida_id)
CREATE INDEX idx_desqualificacao_partida ON private.desqualificacao_segunda_exclusao (partida_id);

-- 50. FK: private.cartao_azul_suspensao(evento_scout_id)
-- Índice Omitido: Coberto pela restrição UNIQUE uq_cartao_azul_evento(evento_scout_id).

-- 51. FK: private.cartao_azul_suspensao(partida_id)
CREATE INDEX idx_cartao_azul_partida ON private.cartao_azul_suspensao (partida_id);

-- 52. FK: private.cartao_azul_suspensao(atleta_id)
CREATE INDEX idx_cartao_azul_atleta ON private.cartao_azul_suspensao (atleta_id);

-- 53. FK: private.cartao_azul_suspensao(papel_operacional_id)
CREATE INDEX idx_cartao_azul_papel_operacional ON private.cartao_azul_suspensao (papel_operacional_id);

-- 54. FK: private.sistema_tatico(posse_de_bola_id)
CREATE INDEX idx_sistema_tatico_posse ON private.sistema_tatico (posse_de_bola_id);

-- 55. FK: private.sistema_tatico(equipe_id)
CREATE INDEX idx_sistema_tatico_equipe ON private.sistema_tatico (equipe_id);

-- 56. FK: private.papel_esportivo_operacional(partida_id)
CREATE INDEX idx_papel_operacional_partida ON private.papel_esportivo_operacional (partida_id);

-- 57. FK: private.papel_esportivo_operacional(equipe_id)
CREATE INDEX idx_papel_operacional_equipe ON private.papel_esportivo_operacional (equipe_id);

-- 58. FK: private.participacao_equipe_competicao(competicao_id)
CREATE INDEX idx_participacao_equipe_competicao_competicao ON private.participacao_equipe_competicao (competicao_id);

-- 59. FK: private.participacao_equipe_competicao(equipe_id)
CREATE INDEX idx_participacao_equipe_competicao_equipe ON private.participacao_equipe_competicao (equipe_id);


-- ==============================================================================
-- ÍNDICES CANDIDATOS COMPOSITOS PARA CONSULTAS E FILTROS FUTUROS / RLS (STAGE_09)
-- ==============================================================================

-- AVISO: Esta seção especifica índices compostos candidatos dependentes dos padrões de consulta analítica de scout e políticas de RLS a serem homologadas no STAGE_09.

-- Candidate Index 1: Filtro sequencial de eventos por observação e tipo de ação técnica
-- CREATE INDEX idx_candidato_evento_scout_busca ON private.evento_scout (observacao_de_scout_id, tipo_acao_observada, timecode_exato);

-- Candidate Index 2: Busca por estado do placar em ordem cronológica de instância
-- CREATE INDEX idx_candidato_estado_placar_timeline ON public.estado_do_placar (placar_jogo_id, timestamp_instante);

-- Candidate Index 3: Filtro de sessões de observação por partida e tipo de observação (P1 vs Auditoria)
-- CREATE INDEX idx_candidato_observacao_scout_partida_tipo ON private.observacao_de_scout (partida_id, tipo_observacao);

-- Candidate Index 4: Consulta de histórico de posses de bola por período/set e ordem sequencial
-- CREATE INDEX idx_candidato_posse_de_bola_ordem ON private.posse_de_bola (periodo_set_id, sequencial_posse);

-- Candidate Index 5: Acesso rápido às revisões pendentes por status de auditoria
-- CREATE INDEX idx_candidato_estado_revisao_status ON private.estado_de_revisao (status_corrente, data_ultima_atualizacao);