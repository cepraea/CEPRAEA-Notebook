-- ==============================================================================
-- FILE METADATA, GOVERNANCE & TRACEABILITY
-- ==============================================================================
-- Nome do arquivo: 08-schema-postgresql.candidate.sql
-- RUN_ID: RUN_20261014_PARTIDAS_SCOUT_001
-- Domínio de Negócio: PARTIDAS_SCOUT_ANALISE_TATICA
-- Estado do Artefato: CANDIDATO
-- Banco de Dados Alvo: PostgreSQL 15+ (Versão do ambiente: NAO_VERIFICADA)
-- Estado de Governança: Gate READY_WITH_RESTRICTIONS | Decisão APPROVED_WITH_RESTRICTIONS
-- Status da Execução: Implementação NAO_INICIADO | Verificação NAO_EXECUTADO
-- Escopo Autorizado: Exatamente 32 relações físicas.
-- Nota de Distribuição de Schemas: A lista explicativa de atribuição de tabelas do escopo
-- especifica 9 tabelas no schema public (competicao, partida, equipe, partida_equipe,
-- periodo_set, shoot_out, placar_jogo, estado_do_placar, evolucao_do_placar) e 23 tabelas no
-- schema private (atleta, equipe_atleta_inscricao, posse_de_bola, unidade_basica_ataque_bou,
-- evento_scout, observacao_de_scout, analista_observador, protocolo_scout, midia_video,
-- segmento_observado, sistema_defensivo, confiabilidade_observador, revisao_da_observacao,
-- estado_de_revisao, proveniencia_observacao, trecho_observado, spin_shot, in_flight_shot,
-- desqualificacao_segunda_exclusao, cartao_azul_suspensao, sistema_tatico,
-- papel_esportivo_operacional, participacao_equipe_competicao), totalizando exatamente 32 relações físicas.
-- MAPEAMENTO DE FONTES SELECIONADAS:
-- 1. LOGICAL_MODEL@0.1.2
--    sha256: 7a82bd2235897e67338036ba5be67f222ac3fdcf19a05bb919ecb1787824b1cb
--    source_id: 1689f311-fd8c-420e-bf53-593d7d90cd1d
-- 2. DATA_DICTIONARY@0.1.1
--    sha256: 82ed6eb37a7872bb1eb66c6d853dd3e9d96b53f5a93b4670b67bd489a44c348e
--    source_id: 0f1d2800-6195-4758-be73-a61da4546429
-- 3. TRACEABILITY_MATRIX@0.1.1
--    sha256: e2d497b0f96bcc74e9287561a2432d821a0dbd5349b01699acb2d2b50042959e
--    source_id: 8b83dda5-dc87-4562-a1d0-ea2e89558b10
-- 4. ACCESS_REQUIREMENTS@0.1.0
--    sha256: bafce57a9d71ef3ea0ba54c79fac585f075d8d0efe5fe22967e62bde6c424c92
--    source_id: c7f18856-d7c7-4b77-8feb-3266d60337c0
-- 5. STOP_GATE_PARTIDAS_SCOUT_ANALISE_TATICA@0.2.0
--    sha256: 8034fc8290a814a2cb63d7d43138c8552ea087d787f44566b94393449a2d09f0
--    source_id: 8347d2e6-f0fd-4872-a5f6-b23adae009f3
-- 6. Decisão Externa do Operador do STAGE_07
--    sha256: 95861272d84e896a0ba82793b63788d8ec070efa284d4100da47b773e1657c66
--    source_id: 167b105a-d750-4d7e-bc53-3da5d56e10f4
-- 7. STAGE_08_ENFORCEMENT_REVIEW@1.0.0
--    sha256: 8931793affb327caf64a69d6508d97a6e9cee0c178b756c59e82837e704d1d75
--    source_id: 4761f1cf-bf81-463f-bd36-a78ab24786de
-- ==============================================================================

-- ==============================================================================
-- PREPARAÇÃO DE AMBIENTE DE BANCO DE DADOS E SCHEMAS
-- ==============================================================================
CREATE EXTENSION IF NOT EXISTS btree_gist;

CREATE SCHEMA private;

-- ==============================================================================
-- CRIAÇÃO DAS TABELAS (32 RELAÇÕES FÍSICAS / 9 PUBLIC, 23 PRIVATE)
-- ==============================================================================

-- Logical ID: COMPETICAO
CREATE TABLE public.competicao (
    id uuid NOT NULL,
    nome text NOT NULL,
    codigo text NOT NULL,
    edicao text NULL,
    data_inicio timestamptz NULL,
    data_fim timestamptz NULL,
    CONSTRAINT pk_competicao PRIMARY KEY (id)
);

-- Logical ID: PARTIDA
CREATE TABLE public.partida (
    id uuid NOT NULL,
    competicao_id uuid NOT NULL,
    numero_partida integer NULL,
    etapa text NULL,
    data_hora_inicio timestamptz NULL,
    local_quadra text NULL,
    status_partida text NOT NULL DEFAULT 'AGENDADA',
    CONSTRAINT pk_partida PRIMARY KEY (id),
    CONSTRAINT CHK_PARTIDA_VIGENCIA_2026 CHECK (data_hora_inicio IS NULL OR data_hora_inicio >= '2026-04-01 00:00:00+00'),
    CONSTRAINT chk_partida_status_partida CHECK (status_partida IN ('AGENDADA', 'EM_ANDAMENTO', 'CONCLUIDA', 'CANCELADA', 'INTERROMPIDA'))
);

-- Logical ID: EQUIPE
CREATE TABLE public.equipe (
    id uuid NOT NULL,
    nome text NOT NULL,
    sigla text NULL,
    cidade text NULL,
    uf text NULL,
    CONSTRAINT pk_equipe PRIMARY KEY (id)
);

-- Logical ID: ATLETA (Schema privado)
CREATE TABLE private.atleta (
    id uuid NOT NULL,
    nome_completo text NOT NULL,
    nome_camisa text NULL,
    numero_registro text NULL,
    posicao_principal text NULL,
    CONSTRAINT pk_atleta PRIMARY KEY (id),
    CONSTRAINT chk_atleta_posicao_principal CHECK (posicao_principal IS NULL OR posicao_principal IN ('GOLEIRA', 'ESPECIALISTA', 'PIVO', 'ALA_DIREITA', 'ALA_ESQUERDA', 'DEFENSORA'))
);

-- Logical ID: PARTIDA_EQUIPE
CREATE TABLE public.partida_equipe (
    partida_id uuid NOT NULL,
    equipe_id uuid NOT NULL,
    papel_regulamentar text NOT NULL,
    condicao_mando text NOT NULL,
    cor_uniforme text NULL,
    CONSTRAINT pk_partida_equipe PRIMARY KEY (partida_id, equipe_id),
    CONSTRAINT uq_partida_papel_regulamentar UNIQUE (partida_id, papel_regulamentar),
    CONSTRAINT uq_partida_condicao_mando UNIQUE (partida_id, condicao_mando),
    CONSTRAINT chk_partida_equipe_papel_regulamentar CHECK (papel_regulamentar IN ('EQUIPE_A', 'EQUIPE_B')),
    CONSTRAINT chk_partida_equipe_condicao_mando CHECK (condicao_mando IN ('MANDANTE', 'VISITANTE'))
);

-- Logical ID: EQUIPE_ATLETA_INSCRICAO
CREATE TABLE private.equipe_atleta_inscricao (
    id uuid NOT NULL,
    equipe_id uuid NOT NULL,
    atleta_id uuid NOT NULL,
    competicao_id uuid NULL,
    data_inscricao timestamptz NOT NULL,
    numero_camisa integer NULL,
    status_elegibilidade text NOT NULL DEFAULT 'ELEGIVEL',
    CONSTRAINT pk_equipe_atleta_inscricao PRIMARY KEY (id),
    CONSTRAINT uq_equipe_atleta_competicao UNIQUE (equipe_id, atleta_id, competicao_id),
    CONSTRAINT chk_equipe_atleta_inscricao_status_elegibilidade CHECK (status_elegibilidade IN ('ELEGIVEL', 'SUSPENSO', 'INATIVO', 'PENDENTE_DOCUMENTACAO')),
    CONSTRAINT chk_equipe_atleta_inscricao_numero_camisa CHECK (numero_camisa IS NULL OR (numero_camisa >= 1 AND numero_camisa <= 99))
);

-- Logical ID: PERIODO_SET
CREATE TABLE public.periodo_set (
    id uuid NOT NULL,
    partida_id uuid NOT NULL,
    numero_set integer NOT NULL,
    tempo_duracao_segundos integer NULL,
    houve_gol_de_ouro boolean NOT NULL DEFAULT false,
    equipe_vencedora_id uuid NULL,
    CONSTRAINT pk_periodo_set PRIMARY KEY (id),
    CONSTRAINT uq_partida_numero_set UNIQUE (partida_id, numero_set),
    CONSTRAINT CHK_NUMERO_SET_VALIDO CHECK (numero_set IN (1, 2))
);

-- Logical ID: SHOOT_OUT
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
    CONSTRAINT uq_shoot_out_partida UNIQUE (partida_id),
    CONSTRAINT CHK_SHOOT_OUT_COMPLETUDE CHECK ((status_completude = 'COMPLETO' AND pontos_equipe_a IS NOT NULL AND pontos_equipe_b IS NOT NULL) OR (status_completude IN ('PARCIAL', 'NAO_DOCUMENTADO') AND motivo_incompletude IS NOT NULL AND length(trim(motivo_incompletude)) > 0)),
    CONSTRAINT chk_shoot_out_status_completude CHECK (status_completude IN ('COMPLETO', 'PARCIAL', 'NAO_DOCUMENTADO'))
);

-- Logical ID: POSSE_DE_BOLA
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
    CONSTRAINT uq_posse_periodo_seq UNIQUE (periodo_set_id, sequencial_posse),
    CONSTRAINT chk_posse_de_bola_fase_ofensiva_dominante CHECK (fase_ofensiva_dominante IS NULL OR fase_ofensiva_dominante IN ('TRANSICAO_OFENSIVA', 'ATAQUE_POSICIONAL')),
    CONSTRAINT chk_posse_de_bola_motivo_termino CHECK (motivo_termino IS NULL OR motivo_termino IN ('GOL', 'DEFESA_GOLEIRA', 'ERRO_TECNICO', 'FALTA_REVERSAO', 'BOLA_FORA', 'FIM_PERIODO'))
);

-- Logical ID: UNIDADE_BASICA_ATAQUE_BOU
CREATE TABLE private.unidade_basica_ataque_bou (
    id uuid NOT NULL,
    posse_de_bola_id uuid NOT NULL,
    sequencial_bou integer NOT NULL,
    timecode_inicio text NULL,
    timecode_fim text NULL,
    fase_tatica text NOT NULL,
    CONSTRAINT pk_unidade_basica_ataque_bou PRIMARY KEY (id),
    CONSTRAINT uq_bou_posse_seq UNIQUE (posse_de_bola_id, sequencial_bou),
    CONSTRAINT chk_unidade_basica_ataque_bou_fase_tatica CHECK (fase_tatica IN ('TO', 'AP', 'TD', 'DP', 'F_IND'))
);

-- Logical ID: EVENTO_SCOUT
CREATE TABLE private.evento_scout (
    id uuid NOT NULL,
    observacao_de_scout_id uuid NOT NULL,
    unidade_basica_ataque_bou_id uuid NULL,
    atleta_executor_id uuid NULL,
    atleta_alvo_id uuid NULL,
    timecode_exato text NOT NULL,
    zona_analitica text NULL,
    tipo_acao_observada text NOT NULL,
    resultado_acao text NULL,
    acao_goleira text NULL,
    punicao_disciplinar text NULL,
    consequencia_disciplinar text NULL,
    pontos_gerados integer NOT NULL DEFAULT 0,
    CONSTRAINT pk_evento_scout PRIMARY KEY (id),
    CONSTRAINT chk_evento_scout_zona_analitica CHECK (zona_analitica IS NULL OR zona_analitica IN ('ZE', 'ZCE', 'ZCD', 'ZD')),
    CONSTRAINT chk_evento_scout_tipo_acao_observada CHECK (tipo_acao_observada IN ('PONTUACAO_SIMPLES', 'PONTUACAO_DUPLA', 'ARREMESSO_SPIN', 'ARREMESSO_IN_FLIGHT', 'ARREMESSO_SIMPLES', 'TIRO_SEIS_METROS', 'PASSE', 'RECEPCAO', 'DESARME', 'BLOQUEIO', 'DEFESA_GOLEIRA', 'FALTA_COMETIDA', 'FALTA_SOFRIDA', 'EXCLUSAO_DISCIPLINAR', 'CARTAO_AZUL')),
    CONSTRAINT chk_evento_scout_resultado_acao CHECK (resultado_acao IS NULL OR resultado_acao IN ('GOL', 'DEFESA', 'FORA', 'TRAVE', 'ERRO_TECNICO', 'FALTA_SOFRIDA')),
    CONSTRAINT chk_evento_scout_acao_goleira CHECK (acao_goleira IS NULL OR acao_goleira IN ('DEFESA_PARADA', 'DEFESA_COUNTER_SPIN', 'DEFESA_COUNTER_FLY', 'PASSE_TRANSICAO_T4', 'ARREMESSO_DIRETO_GOLEIRA', 'INTERVENCAO_SHOOTOUT')),
    CONSTRAINT chk_evento_scout_punicao_disciplinar CHECK (punicao_disciplinar IS NULL OR punicao_disciplinar IN ('ADVERTENCIA', 'EXCLUSAO_TEMPORARIA', 'DESQUALIFICACAO_DIRETA', 'CARTAO_AZUL')),
    CONSTRAINT chk_evento_scout_consequencia_disciplinar CHECK (consequencia_disciplinar IS NULL OR consequencia_disciplinar IN ('REDUCAO_NUMERICA_QUADRA', 'SUSPENSAO_PROXIMA_PARTIDA', 'CONCESSAO_TIRO_SIX_METROS'))
);

-- Logical ID: OBSERVACAO_DE_SCOUT
CREATE TABLE private.observacao_de_scout (
    id uuid NOT NULL,
    partida_id uuid NOT NULL,
    analista_observador_id uuid NOT NULL,
    protocolo_scout_id uuid NOT NULL,
    midia_video_id uuid NOT NULL,
    data_hora_codificacao timestamptz NOT NULL,
    tipo_observacao text NOT NULL DEFAULT 'PRIMARIA_P1',
    CONSTRAINT pk_observacao_de_scout PRIMARY KEY (id),
    CONSTRAINT chk_observacao_de_scout_tipo_observacao CHECK (tipo_observacao IN ('PRIMARIA_P1', 'REVISAO_AUDITORIA', 'AUTOMATIZADA_IA'))
);

-- Logical ID: ANALISTA_OBSERVADOR
CREATE TABLE private.analista_observador (
    id uuid NOT NULL,
    nome text NOT NULL,
    email text NOT NULL,
    status_habilitacao text NOT NULL DEFAULT 'HABILITADO',
    CONSTRAINT pk_analista_observador PRIMARY KEY (id),
    CONSTRAINT chk_analista_observador_status_habilitacao CHECK (status_habilitacao IN ('HABILITADO', 'EM_TREINAMENTO', 'DESABILITADO'))
);

-- Logical ID: PROTOCOLO_SCOUT
CREATE TABLE private.protocolo_scout (
    id uuid NOT NULL,
    codigo_protocolo text NOT NULL,
    versao text NOT NULL,
    descricao text NULL,
    data_congelamento timestamptz NULL,
    CONSTRAINT pk_protocolo_scout PRIMARY KEY (id)
);

-- Logical ID: MIDIA_VIDEO
CREATE TABLE private.midia_video (
    id uuid NOT NULL,
    partida_id uuid NULL,
    uri_storage text NOT NULL,
    checksum_sha256 text NULL,
    tipo_midia text NOT NULL DEFAULT 'BROADCAST_P0',
    duracao_segundos numeric NULL,
    CONSTRAINT pk_midia_video PRIMARY KEY (id),
    CONSTRAINT chk_midia_video_tipo_midia CHECK (tipo_midia IN ('BROADCAST_P0', 'CAMARA_ALTA_TATICA', 'CORTE_CLIPE'))
);

-- Logical ID: SEGMENTO_OBSERVADO
CREATE TABLE private.segmento_observado (
    id uuid NOT NULL,
    partida_id uuid NOT NULL,
    midia_video_id uuid NOT NULL,
    timecode_inicio text NOT NULL,
    timecode_fim text NOT NULL,
    ordem_intervalo integer NOT NULL,
    CONSTRAINT pk_segmento_observado PRIMARY KEY (id),
    CONSTRAINT uq_segmento_ordem UNIQUE (partida_id, midia_video_id, ordem_intervalo)
);

-- Logical ID: PLACAR_JOGO
CREATE TABLE public.placar_jogo (
    id uuid NOT NULL,
    partida_id uuid NOT NULL,
    sets_vencidos_equipe_a integer NOT NULL DEFAULT 0,
    sets_vencidos_equipe_b integer NOT NULL DEFAULT 0,
    resultado_final_sets text NULL,
    equipe_vencedora_id uuid NULL,
    CONSTRAINT pk_placar_jogo PRIMARY KEY (id),
    CONSTRAINT uq_placar_partida UNIQUE (partida_id),
    CONSTRAINT chk_placar_jogo_resultado_final_sets CHECK (resultado_final_sets IS NULL OR resultado_final_sets IN ('VITORIA_2_0', 'VITORIA_2_1', 'DERROTA_0_2', 'DERROTA_1_2'))
);

-- Logical ID: ESTADO_DO_PLACAR
CREATE TABLE public.estado_do_placar (
    id uuid NOT NULL,
    placar_jogo_id uuid NOT NULL,
    periodo_set_id uuid NOT NULL,
    pontos_equipe_a integer NOT NULL DEFAULT 0,
    pontos_equipe_b integer NOT NULL DEFAULT 0,
    situacao_vantagem text NOT NULL DEFAULT 'EMPATADO',
    timestamp_instante timestamptz NOT NULL,
    CONSTRAINT pk_estado_do_placar PRIMARY KEY (id),
    CONSTRAINT chk_estado_do_placar_situacao_vantagem CHECK (situacao_vantagem IN ('EMPATADO', 'FAVORAVEL', 'DESFAVORAVEL'))
);

-- Logical ID: EVOLUCAO_DO_PLACAR
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
    CONSTRAINT uq_evolucao_partida_seq UNIQUE (partida_id, sequencial_pontuacao),
    CONSTRAINT chk_evolucao_do_placar_valor_incremento CHECK (valor_incremento IN (1, 2))
);

-- Logical ID: SISTEMA_DEFENSIVO
CREATE TABLE private.sistema_defensivo (
    id uuid NOT NULL,
    posse_de_bola_id uuid NOT NULL,
    equipe_id uuid NOT NULL,
    sistema_tatico_id uuid NULL,
    codigo_sistema_defensivo text NOT NULL,
    em_desvantagem_numerica boolean NOT NULL DEFAULT false,
    CONSTRAINT pk_sistema_defensivo PRIMARY KEY (id),
    CONSTRAINT chk_sistema_defensivo_codigo_sistema_defensivo CHECK (codigo_sistema_defensivo IN ('SIS_3_0', 'SIS_2_1_CENTRAL', 'SIS_2_1_LATERAL', 'SIS_1_2', 'SIS_AVANCADO_7M', 'SIS_REATIVO', 'SIS_PROATIVO'))
);

-- Logical ID: CONFIABILIDADE_OBSERVADOR
CREATE TABLE private.confiabilidade_observador (
    id uuid NOT NULL,
    analista_observador_id uuid NOT NULL,
    data_avaliacao timestamptz NOT NULL,
    versao_teste text NOT NULL,
    percentual_acerto numeric NOT NULL,
    erros_criticos_qtd integer NOT NULL DEFAULT 0,
    kappa_cohen numeric NULL,
    status_qualificacao text NOT NULL,
    CONSTRAINT pk_confiabilidade_observador PRIMARY KEY (id),
    CONSTRAINT chk_confiabilidade_observador_status_qualificacao CHECK (status_qualificacao IN ('QUALIFICADO', 'NAO_QUALIFICADO'))
);

-- Logical ID: REVISAO_DA_OBSERVACAO
CREATE TABLE private.revisao_da_observacao (
    id uuid NOT NULL,
    observacao_de_scout_id uuid NOT NULL,
    analista_revisor_id uuid NOT NULL,
    timestamp_revisao timestamptz NOT NULL,
    motivo_revisao text NULL,
    campo_alterado text NULL,
    CONSTRAINT pk_revisao_da_observacao PRIMARY KEY (id)
);

-- Logical ID: ESTADO_DE_REVISAO
CREATE TABLE private.estado_de_revisao (
    id uuid NOT NULL,
    observacao_de_scout_id uuid NOT NULL,
    revisao_da_observacao_id uuid NULL,
    status_corrente text NOT NULL DEFAULT 'PENDENTE',
    data_ultima_atualizacao timestamptz NOT NULL,
    CONSTRAINT pk_estado_de_revisao PRIMARY KEY (id),
    CONSTRAINT uq_estado_revisao_observa UNIQUE (observacao_de_scout_id),
    CONSTRAINT chk_estado_de_revisao_status_corrente CHECK (status_corrente IN ('PENDENTE', 'APROVADO', 'REJEITADO', 'EM_AUDITORIA'))
);

-- Logical ID: PROVENIENCIA_OBSERVACAO
CREATE TABLE private.proveniencia_observacao (
    id uuid NOT NULL,
    observacao_de_scout_id uuid NOT NULL,
    protocolo_scout_id uuid NOT NULL,
    midia_video_id uuid NOT NULL,
    ferramenta_software text NOT NULL,
    origem_dado text NOT NULL,
    checksum_midia text NULL,
    CONSTRAINT pk_proveniencia_observacao PRIMARY KEY (id),
    CONSTRAINT uq_proveniencia_obs UNIQUE (observacao_de_scout_id),
    CONSTRAINT chk_proveniencia_observacao_origem_dado CHECK (origem_dado IN ('CODIFICACAO_HUMANA_P1', 'SUMULA_OFICIAL', 'EXTRACAO_AUTOMATIZADA'))
);

-- Logical ID: TRECHO_OBSERVADO
CREATE TABLE private.trecho_observado (
    id uuid NOT NULL,
    evento_scout_id uuid NOT NULL,
    midia_video_id uuid NOT NULL,
    timecode_inicio text NOT NULL,
    timecode_fim text NOT NULL,
    offset_milissegundos integer NULL,
    CONSTRAINT pk_trecho_observado PRIMARY KEY (id)
);

-- Logical ID: SPIN_SHOT
CREATE TABLE private.spin_shot (
    id uuid NOT NULL,
    evento_scout_id uuid NOT NULL,
    rotacao_completa_360 boolean NOT NULL DEFAULT true,
    salto_pe_direcionado boolean NOT NULL DEFAULT true,
    valor_pontos integer NOT NULL DEFAULT 2,
    CONSTRAINT pk_spin_shot PRIMARY KEY (id),
    CONSTRAINT uq_spin_shot_evento UNIQUE (evento_scout_id),
    CONSTRAINT chk_spin_shot_valor_pontos CHECK (valor_pontos = 2)
);

-- Logical ID: IN_FLIGHT_SHOT
CREATE TABLE private.in_flight_shot (
    id uuid NOT NULL,
    evento_scout_id uuid NOT NULL,
    recepcao_no_ar boolean NOT NULL DEFAULT true,
    sem_contato_areia boolean NOT NULL DEFAULT true,
    valor_pontos integer NOT NULL DEFAULT 2,
    CONSTRAINT pk_in_flight_shot PRIMARY KEY (id),
    CONSTRAINT uq_in_flight_evento UNIQUE (evento_scout_id),
    CONSTRAINT chk_in_flight_shot_valor_pontos CHECK (valor_pontos = 2)
);

-- Logical ID: DESQUALIFICACAO_SEGUNDA_EXCLUSAO
CREATE TABLE private.desqualificacao_segunda_exclusao (
    id uuid NOT NULL,
    evento_scout_id uuid NOT NULL,
    atleta_id uuid NOT NULL,
    partida_id uuid NOT NULL,
    saida_imediata_quadra boolean NOT NULL DEFAULT true,
    CONSTRAINT pk_desqualificacao_segunda_exclusao PRIMARY KEY (id),
    CONSTRAINT uq_desq_exc_evento UNIQUE (evento_scout_id)
);

-- Logical ID: CARTAO_AZUL_SUSPENSAO
CREATE TABLE private.cartao_azul_suspensao (
    id uuid NOT NULL,
    evento_scout_id uuid NOT NULL,
    partida_id uuid NOT NULL,
    atleta_id uuid NULL,
    papel_operacional_id uuid NULL,
    relatorio_arbitragem text NOT NULL,
    jogos_suspensao_automatica integer NOT NULL DEFAULT 1,
    CONSTRAINT pk_cartao_azul_suspensao PRIMARY KEY (id),
    CONSTRAINT uq_cartao_azul_evento UNIQUE (evento_scout_id)
);

-- Logical ID: SISTEMA_TATICO
CREATE TABLE private.sistema_tatico (
    id uuid NOT NULL,
    posse_de_bola_id uuid NOT NULL,
    equipe_id uuid NOT NULL,
    codigo_sistema_tatico text NOT NULL,
    fase_tatica text NOT NULL,
    CONSTRAINT pk_sistema_tatico PRIMARY KEY (id),
    CONSTRAINT chk_sistema_tatico_codigo_sistema_tatico CHECK (codigo_sistema_tatico IN ('ATAQUE_3_1', 'ATAQUE_2_2', 'ATAQUE_4_0', 'DEFESA_3_0', 'DEFESA_2_1', 'DEFESA_1_2')),
    CONSTRAINT chk_sistema_tatico_fase_tatica CHECK (fase_tatica IN ('TO', 'AP', 'TD', 'DP', 'F_IND'))
);

-- Logical ID: PAPEL_ESPORTIVO_OPERACIONAL
CREATE TABLE private.papel_esportivo_operacional (
    id uuid NOT NULL,
    partida_id uuid NOT NULL,
    equipe_id uuid NULL,
    nome_pessoa text NOT NULL,
    codigo_papel text NOT NULL,
    CONSTRAINT pk_papel_esportivo_operacional PRIMARY KEY (id),
    CONSTRAINT chk_papel_esportivo_operacional_codigo_papel CHECK (codigo_papel IN ('TECNICO', 'AUXILIAR_TECNICO', 'MEDICO', 'FISIOTERAPEUTA', 'DELEGADO_A', 'DELEGADO_B', 'SECRETARIO', 'CRONOMETRISTA', 'OFICIAL_ARBITRAGEM'))
);

-- Logical ID: PARTICIPACAO_EQUIPE_COMPETICAO
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
    CONSTRAINT uq_participacao_equipe_competicao_vigencia UNIQUE (competicao_id, equipe_id, valido_desde),
    CONSTRAINT CHK_ELEGIBILIDADE_RANKING_CONTEXTUAL CHECK (status_elegibilidade_ranking IN ('ELEGIVEL', 'INELEGIVEL_POR_DECISAO_COLETIVA', 'PENDENTE_DELIBERACAO')),
    CONSTRAINT CHK_INTERVALO_VIGENCIA_PARTICIPACAO CHECK (valido_ate IS NULL OR valido_ate > valido_desde),
    CONSTRAINT chk_participacao_equipe_competicao_tipo_participacao CHECK (tipo_participacao IN ('REGULAR', 'CONVIDADA'))
);

-- EXCLUSÃO TEMPORAL DE SOBREPOSIÇÃO
ALTER TABLE private.participacao_equipe_competicao
    ADD CONSTRAINT ex_participacao_equipe_competicao_no_overlap
    EXCLUDE USING gist (
        competicao_id WITH =,
        equipe_id WITH =,
        tstzrange(valido_desde, valido_ate, '[)') WITH &&
    );

-- ==============================================================================
-- CHAVES ESTRANGEIRAS E AÇÕES REFERENCIAIS (59 RELAÇÕES REFERENCIAIS)
-- ==============================================================================

-- 1. FK_PARTIDA_COMPETICAO (Alvo da diretriz cirúrgica: ON DELETE RESTRICT ON UPDATE CASCADE)
ALTER TABLE public.partida
    ADD CONSTRAINT fk_partida_competicao
    FOREIGN KEY (competicao_id) REFERENCES public.competicao(id)
    ON DELETE RESTRICT ON UPDATE CASCADE;

-- 2. FK_PARTIDA_EQUIPE_PARTIDA
ALTER TABLE public.partida_equipe
    ADD CONSTRAINT fk_partida_equipe_partida
    FOREIGN KEY (partida_id) REFERENCES public.partida(id)
    ON UPDATE CASCADE;

-- 3. FK_PARTIDA_EQUIPE_EQUIPE
ALTER TABLE public.partida_equipe
    ADD CONSTRAINT fk_partida_equipe_equipe
    FOREIGN KEY (equipe_id) REFERENCES public.equipe(id)
    ON UPDATE CASCADE;

-- 4. FK_INSCRICAO_EQUIPE (Alvo da diretriz cirúrgica: ON DELETE CASCADE ON UPDATE CASCADE)
ALTER TABLE private.equipe_atleta_inscricao
    ADD CONSTRAINT fk_inscricao_equipe
    FOREIGN KEY (equipe_id) REFERENCES public.equipe(id)
    ON DELETE CASCADE ON UPDATE CASCADE;

-- 5. FK_INSCRICAO_ATLETA (Redirecionada para private.atleta)
ALTER TABLE private.equipe_atleta_inscricao
    ADD CONSTRAINT fk_inscricao_atleta
    FOREIGN KEY (atleta_id) REFERENCES private.atleta(id)
    ON UPDATE CASCADE;

-- 6. FK_INSCRICAO_COMPETICAO
ALTER TABLE private.equipe_atleta_inscricao
    ADD CONSTRAINT fk_inscricao_competicao
    FOREIGN KEY (competicao_id) REFERENCES public.competicao(id)
    ON UPDATE CASCADE;

-- 7. FK_PERIODO_SET_PARTIDA
ALTER TABLE public.periodo_set
    ADD CONSTRAINT fk_periodo_set_partida
    FOREIGN KEY (partida_id) REFERENCES public.partida(id)
    ON UPDATE CASCADE;

-- 8. FK_PERIODO_SET_EQUIPE_VENCEDORA (Alvo da diretriz cirúrgica: ON DELETE RESTRICT ON UPDATE CASCADE)
ALTER TABLE public.periodo_set
    ADD CONSTRAINT fk_periodo_set_equipe_vencedora
    FOREIGN KEY (equipe_vencedora_id) REFERENCES public.equipe(id)
    ON DELETE RESTRICT ON UPDATE CASCADE;

-- 9. FK_SHOOT_OUT_PARTIDA
ALTER TABLE public.shoot_out
    ADD CONSTRAINT fk_shoot_out_partida
    FOREIGN KEY (partida_id) REFERENCES public.partida(id)
    ON UPDATE CASCADE;

-- 10. FK_SHOOT_OUT_EQUIPE_VENCEDORA (Alvo da diretriz cirúrgica: ON DELETE RESTRICT ON UPDATE CASCADE)
ALTER TABLE public.shoot_out
    ADD CONSTRAINT fk_shoot_out_equipe_vencedora
    FOREIGN KEY (equipe_vencedora_id) REFERENCES public.equipe(id)
    ON DELETE RESTRICT ON UPDATE CASCADE;

-- 11. FK_POSSE_DE_BOLA_PERIODO_SET
ALTER TABLE private.posse_de_bola
    ADD CONSTRAINT fk_posse_de_bola_periodo_set
    FOREIGN KEY (periodo_set_id) REFERENCES public.periodo_set(id)
    ON UPDATE CASCADE;

-- 12. FK_POSSE_DE_BOLA_EQUIPE
ALTER TABLE private.posse_de_bola
    ADD CONSTRAINT fk_posse_de_bola_equipe
    FOREIGN KEY (equipe_possuidora_id) REFERENCES public.equipe(id)
    ON UPDATE CASCADE;

-- 13. FK_BOU_POSSE_DE_BOLA
ALTER TABLE private.unidade_basica_ataque_bou
    ADD CONSTRAINT fk_bou_posse_de_bola
    FOREIGN KEY (posse_de_bola_id) REFERENCES private.posse_de_bola(id)
    ON UPDATE CASCADE;

-- 14. FK_EVENTO_SCOUT_OBSERVACAO
ALTER TABLE private.evento_scout
    ADD CONSTRAINT fk_evento_scout_observacao
    FOREIGN KEY (observacao_de_scout_id) REFERENCES private.observacao_de_scout(id)
    ON UPDATE CASCADE;

-- 15. FK_EVENTO_SCOUT_BOU
ALTER TABLE private.evento_scout
    ADD CONSTRAINT fk_evento_scout_bou
    FOREIGN KEY (unidade_basica_ataque_bou_id) REFERENCES private.unidade_basica_ataque_bou(id)
    ON UPDATE CASCADE;

-- 16. FK_EVENTO_SCOUT_ATLETA_EXEC (Redirecionada para private.atleta; Alvo: ON DELETE RESTRICT ON UPDATE CASCADE)
ALTER TABLE private.evento_scout
    ADD CONSTRAINT fk_evento_scout_atleta_exec
    FOREIGN KEY (atleta_executor_id) REFERENCES private.atleta(id)
    ON DELETE RESTRICT ON UPDATE CASCADE;

-- 17. FK_EVENTO_SCOUT_ATLETA_ALVO (Redirecionada para private.atleta; Alvo: ON DELETE RESTRICT ON UPDATE CASCADE)
ALTER TABLE private.evento_scout
    ADD CONSTRAINT fk_evento_scout_atleta_alvo
    FOREIGN KEY (atleta_alvo_id) REFERENCES private.atleta(id)
    ON DELETE RESTRICT ON UPDATE CASCADE;

-- 18. FK_OBSERVACAO_SCOUT_PARTIDA
ALTER TABLE private.observacao_de_scout
    ADD CONSTRAINT fk_observacao_scout_partida
    FOREIGN KEY (partida_id) REFERENCES public.partida(id)
    ON UPDATE CASCADE;

-- 19. FK_OBSERVACAO_SCOUT_ANALISTA
ALTER TABLE private.observacao_de_scout
    ADD CONSTRAINT fk_observacao_scout_analista
    FOREIGN KEY (analista_observador_id) REFERENCES private.analista_observador(id)
    ON UPDATE CASCADE;

-- 20. FK_OBSERVACAO_SCOUT_PROTOCOLO
ALTER TABLE private.observacao_de_scout
    ADD CONSTRAINT fk_observacao_scout_protocolo
    FOREIGN KEY (protocolo_scout_id) REFERENCES private.protocolo_scout(id)
    ON UPDATE CASCADE;

-- 21. FK_OBSERVACAO_SCOUT_MIDIA
ALTER TABLE private.observacao_de_scout
    ADD CONSTRAINT fk_observacao_scout_midia
    FOREIGN KEY (midia_video_id) REFERENCES private.midia_video(id)
    ON UPDATE CASCADE;

-- 22. FK_MIDIA_VIDEO_PARTIDA
ALTER TABLE private.midia_video
    ADD CONSTRAINT fk_midia_video_partida
    FOREIGN KEY (partida_id) REFERENCES public.partida(id)
    ON UPDATE CASCADE;

-- 23. FK_SEGMENTO_OBSERVADO_PARTIDA
ALTER TABLE private.segmento_observado
    ADD CONSTRAINT fk_segmento_observado_partida
    FOREIGN KEY (partida_id) REFERENCES public.partida(id)
    ON UPDATE CASCADE;

-- 24. FK_SEGMENTO_OBSERVADO_MIDIA (Alvo da diretriz cirúrgica: ON DELETE RESTRICT ON UPDATE CASCADE)
ALTER TABLE private.segmento_observado
    ADD CONSTRAINT fk_segmento_observado_midia
    FOREIGN KEY (midia_video_id) REFERENCES private.midia_video(id)
    ON DELETE RESTRICT ON UPDATE CASCADE;

-- 25. FK_PLACAR_JOGO_PARTIDA
ALTER TABLE public.placar_jogo
    ADD CONSTRAINT fk_placar_jogo_partida
    FOREIGN KEY (partida_id) REFERENCES public.partida(id)
    ON UPDATE CASCADE;

-- 26. FK_PLACAR_JOGO_EQUIPE_VENCEDORA (Alvo da diretriz cirúrgica: ON DELETE RESTRICT ON UPDATE CASCADE)
ALTER TABLE public.placar_jogo
    ADD CONSTRAINT fk_placar_jogo_equipe_vencedora
    FOREIGN KEY (equipe_vencedora_id) REFERENCES public.equipe(id)
    ON DELETE RESTRICT ON UPDATE CASCADE;

-- 27. FK_ESTADO_PLACAR_PLACAR_JOGO
ALTER TABLE public.estado_do_placar
    ADD CONSTRAINT fk_estado_placar_placar_jogo
    FOREIGN KEY (placar_jogo_id) REFERENCES public.placar_jogo(id)
    ON UPDATE CASCADE;

-- 28. FK_ESTADO_PLACAR_PERIODO_SET
ALTER TABLE public.estado_do_placar
    ADD CONSTRAINT fk_estado_placar_periodo_set
    FOREIGN KEY (periodo_set_id) REFERENCES public.periodo_set(id)
    ON UPDATE CASCADE;

-- 29. FK_EVOLUCAO_PLACAR_PARTIDA
ALTER TABLE public.evolucao_do_placar
    ADD CONSTRAINT fk_evolucao_placar_partida
    FOREIGN KEY (partida_id) REFERENCES public.partida(id)
    ON UPDATE CASCADE;

-- 30. FK_EVOLUCAO_PLACAR_EVENTO_SCOUT
ALTER TABLE public.evolucao_do_placar
    ADD CONSTRAINT fk_evolucao_placar_evento_scout
    FOREIGN KEY (evento_scout_id) REFERENCES private.evento_scout(id)
    ON UPDATE CASCADE;

-- 31. FK_EVOLUCAO_PLACAR_EQUIPE
ALTER TABLE public.evolucao_do_placar
    ADD CONSTRAINT fk_evolucao_placar_equipe
    FOREIGN KEY (equipe_beneficiada_id) REFERENCES public.equipe(id)
    ON UPDATE CASCADE;

-- 32. FK_SISTEMA_DEFENSIVO_POSSE
ALTER TABLE private.sistema_defensivo
    ADD CONSTRAINT fk_sistema_defensivo_posse
    FOREIGN KEY (posse_de_bola_id) REFERENCES private.posse_de_bola(id)
    ON UPDATE CASCADE;

-- 33. FK_SISTEMA_DEFENSIVO_EQUIPE
ALTER TABLE private.sistema_defensivo
    ADD CONSTRAINT fk_sistema_defensivo_equipe
    FOREIGN KEY (equipe_id) REFERENCES public.equipe(id)
    ON UPDATE CASCADE;

-- 34. FK_SISTEMA_DEFENSIVO_SISTEMA_TATICO
ALTER TABLE private.sistema_defensivo
    ADD CONSTRAINT fk_sistema_defensivo_sistema_tatico
    FOREIGN KEY (sistema_tatico_id) REFERENCES private.sistema_tatico(id)
    ON UPDATE CASCADE;

-- 35. FK_CONFIABILIDADE_ANALISTA
ALTER TABLE private.confiabilidade_observador
    ADD CONSTRAINT fk_confiabilidade_analista
    FOREIGN KEY (analista_observador_id) REFERENCES private.analista_observador(id)
    ON UPDATE CASCADE;

-- 36. FK_REVISAO_OBSERVACAO_OBS
ALTER TABLE private.revisao_da_observacao
    ADD CONSTRAINT fk_revisao_observacao_obs
    FOREIGN KEY (observacao_de_scout_id) REFERENCES private.observacao_de_scout(id)
    ON UPDATE CASCADE;

-- 37. FK_REVISAO_OBSERVACAO_ANALISTA
ALTER TABLE private.revisao_da_observacao
    ADD CONSTRAINT fk_revisao_observacao_analista
    FOREIGN KEY (analista_revisor_id) REFERENCES private.analista_observador(id)
    ON UPDATE CASCADE;

-- 38. FK_ESTADO_REVISAO_OBSERVACAO
ALTER TABLE private.estado_de_revisao
    ADD CONSTRAINT fk_estado_revisao_observacao
    FOREIGN KEY (observacao_de_scout_id) REFERENCES private.observacao_de_scout(id)
    ON UPDATE CASCADE;

-- 39. FK_ESTADO_REVISAO_REVISAO
ALTER TABLE private.estado_de_revisao
    ADD CONSTRAINT fk_estado_revisao_revisao
    FOREIGN KEY (revisao_da_observacao_id) REFERENCES private.revisao_da_observacao(id)
    ON UPDATE CASCADE;

-- 40. FK_PROVENIENCIA_OBSERVACAO_OBS
ALTER TABLE private.proveniencia_observacao
    ADD CONSTRAINT fk_proveniencia_observacao_obs
    FOREIGN KEY (observacao_de_scout_id) REFERENCES private.observacao_de_scout(id)
    ON UPDATE CASCADE;

-- 41. FK_PROVENIENCIA_PROTOCOLO
ALTER TABLE private.proveniencia_observacao
    ADD CONSTRAINT fk_proveniencia_protocolo
    FOREIGN KEY (protocolo_scout_id) REFERENCES private.protocolo_scout(id)
    ON UPDATE CASCADE;

-- 42. FK_PROVENIENCIA_MIDIA
ALTER TABLE private.proveniencia_observacao
    ADD CONSTRAINT fk_proveniencia_midia
    FOREIGN KEY (midia_video_id) REFERENCES private.midia_video(id)
    ON UPDATE CASCADE;

-- 43. FK_TRECHO_OBSERVADO_EVENTO
ALTER TABLE private.trecho_observado
    ADD CONSTRAINT fk_trecho_observado_evento
    FOREIGN KEY (evento_scout_id) REFERENCES private.evento_scout(id)
    ON UPDATE CASCADE;

-- 44. FK_TRECHO_OBSERVADO_MIDIA (Alvo da diretriz cirúrgica: ON DELETE RESTRICT ON UPDATE CASCADE)
ALTER TABLE private.trecho_observado
    ADD CONSTRAINT fk_trecho_observado_midia
    FOREIGN KEY (midia_video_id) REFERENCES private.midia_video(id)
    ON DELETE RESTRICT ON UPDATE CASCADE;

-- 45. FK_SPIN_SHOT_EVENTO
ALTER TABLE private.spin_shot
    ADD CONSTRAINT fk_spin_shot_evento
    FOREIGN KEY (evento_scout_id) REFERENCES private.evento_scout(id)
    ON UPDATE CASCADE;

-- 46. FK_IN_FLIGHT_SHOT_EVENTO
ALTER TABLE private.in_flight_shot
    ADD CONSTRAINT fk_in_flight_shot_evento
    FOREIGN KEY (evento_scout_id) REFERENCES private.evento_scout(id)
    ON UPDATE CASCADE;

-- 47. FK_DESQUALIFICACAO_EVENTO
ALTER TABLE private.desqualificacao_segunda_exclusao
    ADD CONSTRAINT fk_desqualificacao_evento
    FOREIGN KEY (evento_scout_id) REFERENCES private.evento_scout(id)
    ON UPDATE CASCADE;

-- 48. FK_DESQUALIFICACAO_ATLETA (Redirecionada para private.atleta)
ALTER TABLE private.desqualificacao_segunda_exclusao
    ADD CONSTRAINT fk_desqualificacao_atleta
    FOREIGN KEY (atleta_id) REFERENCES private.atleta(id)
    ON UPDATE CASCADE;

-- 49. FK_DESQUALIFICACAO_PARTIDA
ALTER TABLE private.desqualificacao_segunda_exclusao
    ADD CONSTRAINT fk_desqualificacao_partida
    FOREIGN KEY (partida_id) REFERENCES public.partida(id)
    ON UPDATE CASCADE;

-- 50. FK_CARTAO_AZUL_EVENTO
ALTER TABLE private.cartao_azul_suspensao
    ADD CONSTRAINT fk_cartao_azul_evento
    FOREIGN KEY (evento_scout_id) REFERENCES private.evento_scout(id)
    ON UPDATE CASCADE;

-- 51. FK_CARTAO_AZUL_PARTIDA
ALTER TABLE private.cartao_azul_suspensao
    ADD CONSTRAINT fk_cartao_azul_partida
    FOREIGN KEY (partida_id) REFERENCES public.partida(id)
    ON UPDATE CASCADE;

-- 52. FK_CARTAO_AZUL_ATLETA (Redirecionada para private.atleta; Alvo: ON DELETE RESTRICT ON UPDATE CASCADE)
ALTER TABLE private.cartao_azul_suspensao
    ADD CONSTRAINT fk_cartao_azul_atleta
    FOREIGN KEY (atleta_id) REFERENCES private.atleta(id)
    ON DELETE RESTRICT ON UPDATE CASCADE;

-- 53. FK_CARTAO_AZUL_PAPEL_OPERACIONAL (Alvo da diretriz cirúrgica: ON DELETE RESTRICT ON UPDATE CASCADE)
ALTER TABLE private.cartao_azul_suspensao
    ADD CONSTRAINT fk_cartao_azul_papel_operacional
    FOREIGN KEY (papel_operacional_id) REFERENCES private.papel_esportivo_operacional(id)
    ON DELETE RESTRICT ON UPDATE CASCADE;

-- 54. FK_SISTEMA_TATICO_POSSE
ALTER TABLE private.sistema_tatico
    ADD CONSTRAINT fk_sistema_tatico_posse
    FOREIGN KEY (posse_de_bola_id) REFERENCES private.posse_de_bola(id)
    ON UPDATE CASCADE;

-- 55. FK_SISTEMA_TATICO_EQUIPE
ALTER TABLE private.sistema_tatico
    ADD CONSTRAINT fk_sistema_tatico_equipe
    FOREIGN KEY (equipe_id) REFERENCES public.equipe(id)
    ON UPDATE CASCADE;

-- 56. FK_PAPEL_OPERACIONAL_PARTIDA
ALTER TABLE private.papel_esportivo_operacional
    ADD CONSTRAINT fk_papel_operacional_partida
    FOREIGN KEY (partida_id) REFERENCES public.partida(id)
    ON UPDATE CASCADE;

-- 57. FK_PAPEL_OPERACIONAL_EQUIPE
ALTER TABLE private.papel_esportivo_operacional
    ADD CONSTRAINT fk_papel_operacional_equipe
    FOREIGN KEY (equipe_id) REFERENCES public.equipe(id)
    ON UPDATE CASCADE;

-- 58. FK_PARTICIPACAO_EQUIPE_COMPETICAO_COMPETICAO (Alvo da diretriz cirúrgica: ON DELETE RESTRICT ON UPDATE CASCADE)
ALTER TABLE private.participacao_equipe_competicao
    ADD CONSTRAINT fk_participacao_equipe_competicao_competicao
    FOREIGN KEY (competicao_id) REFERENCES public.competicao(id)
    ON DELETE RESTRICT ON UPDATE CASCADE;

-- 59. FK_PARTICIPACAO_EQUIPE_COMPETICAO_EQUIPE
ALTER TABLE private.participacao_equipe_competicao
    ADD CONSTRAINT fk_participacao_equipe_competicao_equipe
    FOREIGN KEY (equipe_id) REFERENCES public.equipe(id)
    ON UPDATE CASCADE;

-- ==============================================================================
-- ÍNDICES EXPLÍCITOS E COBERTURA REFERENCIAL (59 ÍNDICES)
-- ==============================================================================

CREATE INDEX idx_partida_competicao ON public.partida(competicao_id);
CREATE INDEX idx_partida_equipe_partida ON public.partida_equipe(partida_id);
CREATE INDEX idx_partida_equipe_equipe ON public.partida_equipe(equipe_id);
CREATE INDEX idx_inscricao_equipe ON private.equipe_atleta_inscricao(equipe_id);
CREATE INDEX idx_inscricao_atleta ON private.equipe_atleta_inscricao(atleta_id);
CREATE INDEX idx_inscricao_competicao ON private.equipe_atleta_inscricao(competicao_id);
CREATE INDEX idx_periodo_set_partida ON public.periodo_set(partida_id);
CREATE INDEX idx_periodo_set_equipe_vencedora ON public.periodo_set(equipe_vencedora_id);
CREATE INDEX idx_shoot_out_partida ON public.shoot_out(partida_id);
CREATE INDEX idx_shoot_out_equipe_vencedora ON public.shoot_out(equipe_vencedora_id);
CREATE INDEX idx_posse_de_bola_periodo_set ON private.posse_de_bola(periodo_set_id);
CREATE INDEX idx_posse_de_bola_equipe ON private.posse_de_bola(equipe_possuidora_id);
CREATE INDEX idx_bou_posse_de_bola ON private.unidade_basica_ataque_bou(posse_de_bola_id);
CREATE INDEX idx_evento_scout_observacao ON private.evento_scout(observacao_de_scout_id);
CREATE INDEX idx_evento_scout_bou ON private.evento_scout(unidade_basica_ataque_bou_id);
CREATE INDEX idx_evento_scout_atleta_exec ON private.evento_scout(atleta_executor_id);
CREATE INDEX idx_evento_scout_atleta_alvo ON private.evento_scout(atleta_alvo_id);
CREATE INDEX idx_observacao_scout_partida ON private.observacao_de_scout(partida_id);
CREATE INDEX idx_observacao_scout_analista ON private.observacao_de_scout(analista_observador_id);
CREATE INDEX idx_observacao_scout_protocolo ON private.observacao_de_scout(protocolo_scout_id);
CREATE INDEX idx_observacao_scout_midia ON private.observacao_de_scout(midia_video_id);
CREATE INDEX idx_midia_video_partida ON private.midia_video(partida_id);
CREATE INDEX idx_segmento_observado_partida ON private.segmento_observado(partida_id);
CREATE INDEX idx_segmento_observado_midia ON private.segmento_observado(midia_video_id);
CREATE INDEX idx_placar_jogo_partida ON public.placar_jogo(partida_id);
CREATE INDEX idx_placar_jogo_equipe_vencedora ON public.placar_jogo(equipe_vencedora_id);
CREATE INDEX idx_estado_placar_placar_jogo ON public.estado_do_placar(placar_jogo_id);
CREATE INDEX idx_estado_placar_periodo_set ON public.estado_do_placar(periodo_set_id);
CREATE INDEX idx_evolucao_placar_partida ON public.evolucao_do_placar(partida_id);
CREATE INDEX idx_evolucao_placar_evento_scout ON public.evolucao_do_placar(evento_scout_id);
CREATE INDEX idx_evolucao_placar_equipe ON public.evolucao_do_placar(equipe_beneficiada_id);
CREATE INDEX idx_sistema_defensivo_posse ON private.sistema_defensivo(posse_de_bola_id);
CREATE INDEX idx_sistema_defensivo_equipe ON private.sistema_defensivo(equipe_id);
CREATE INDEX idx_sistema_defensivo_sistema_tatico ON private.sistema_defensivo(sistema_tatico_id);
CREATE INDEX idx_confiabilidade_analista ON private.confiabilidade_observador(analista_observador_id);
CREATE INDEX idx_revisao_observacao_obs ON private.revisao_da_observacao(observacao_de_scout_id);
CREATE INDEX idx_revisao_observacao_analista ON private.revisao_da_observacao(analista_revisor_id);
CREATE INDEX idx_estado_revisao_observacao ON private.estado_de_revisao(observacao_de_scout_id);
CREATE INDEX idx_estado_revisao_revisao ON private.estado_de_revisao(revisao_da_observacao_id);
CREATE INDEX idx_proveniencia_observacao_obs ON private.proveniencia_observacao(observacao_de_scout_id);
CREATE INDEX idx_proveniencia_protocolo ON private.proveniencia_observacao(protocolo_scout_id);
CREATE INDEX idx_proveniencia_midia ON private.proveniencia_observacao(midia_video_id);
CREATE INDEX idx_trecho_observado_evento ON private.trecho_observado(evento_scout_id);
CREATE INDEX idx_trecho_observado_midia ON private.trecho_observado(midia_video_id);
CREATE INDEX idx_spin_shot_evento ON private.spin_shot(evento_scout_id);
CREATE INDEX idx_in_flight_shot_evento ON private.in_flight_shot(evento_scout_id);
CREATE INDEX idx_desqualificacao_evento ON private.desqualificacao_segunda_exclusao(evento_scout_id);
CREATE INDEX idx_desqualificacao_atleta ON private.desqualificacao_segunda_exclusao(atleta_id);
CREATE INDEX idx_desqualificacao_partida ON private.desqualificacao_segunda_exclusao(partida_id);
CREATE INDEX idx_cartao_azul_evento ON private.cartao_azul_suspensao(evento_scout_id);
CREATE INDEX idx_cartao_azul_partida ON private.cartao_azul_suspensao(partida_id);
CREATE INDEX idx_cartao_azul_atleta ON private.cartao_azul_suspensao(atleta_id);
CREATE INDEX idx_cartao_azul_papel_operacional ON private.cartao_azul_suspensao(papel_operacional_id);
CREATE INDEX idx_sistema_tatico_posse ON private.sistema_tatico(posse_de_bola_id);
CREATE INDEX idx_sistema_tatico_equipe ON private.sistema_tatico(equipe_id);
CREATE INDEX idx_papel_operacional_partida ON private.papel_esportivo_operacional(partida_id);
CREATE INDEX idx_papel_operacional_equipe ON private.papel_esportivo_operacional(equipe_id);
CREATE INDEX idx_participacao_equipe_competicao_competicao ON private.participacao_equipe_competicao(competicao_id);
CREATE INDEX idx_participacao_equipe_competicao_equipe ON private.participacao_equipe_competicao(equipe_id);