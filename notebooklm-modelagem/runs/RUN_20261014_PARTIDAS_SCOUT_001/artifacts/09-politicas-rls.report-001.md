# Artefato SQL Candidato: 09-politicas-rls.candidate.sql

-- ==============================================================================
-- CABEÇALHO DE GOVERNANÇA E RASTREABILIDADE SQL
-- ==============================================================================
-- Identificação do Arquivo: 09-politicas-rls.candidate.sql
-- Identificador da Execução: RUN_20261014_PARTIDAS_SCOUT_001
-- Estágio e Decisão: STAGE_09 | Status: AUTHORIZED_WITH_RESTRICTIONS
-- Decisão do Operador: 78a6e2a4d1a6 (Registrada em 2026-10-16T01:36:28-03:00)
--
-- MAPEAMENTO DE FONTES PROMOVIDAS:
-- 1. ACCESS_REQUIREMENTS@0.1.0
--    SHA-256: bafce57a9d71ef3ea0ba54c79fac585f075d8d0efe5fe22967e62bde6c424c92
--    Promoted Source ID: c7f18856-d7c7-4b77-8feb-3266d60337c0
-- 2. POSTGRESQL_SCHEMA_CANDIDATE
--    SHA-256: f5224887f8dd85b82542e3645e0c68fbad77c336a5f0509c229a6f7867694828
--    Promoted Source ID: 1f69f4e5-f4f3-43fd-b8b0-87f19b8b2c8b
--
-- RESUMO DO ESCOPO DE SEGURANÇA:
-- - Recursos Públicos Expostos (Schema public): 9 tabelas expostas via Data API.
-- - Recursos Fechados/Internos/Restritos (Schema private): 23 tabelas isoladas.
--
-- AVISO DE INVARIANTE E NÃO-EXECUÇÃO:
-- Este arquivo representa uma composição de políticas RLS e concessões candidatas.
-- Trata-se de um artefato estritamente descritivo de segurança e NÃO uma migration
-- autônoma. Não se alega teste, execução, aplicação direta ou implantação em ambiente
-- de banco de dados neste estágio.
-- ==============================================================================

-- ==============================================================================
-- CONFIGURAÇÃO GLOBAL DE PERMISSÕES E REVOGAÇÃO PADRÃO DE GRANTS
-- ==============================================================================

-- Revogação total de acessos a nível de schema para garantir isolamento de perímetro
REVOKE ALL ON SCHEMA public FROM public, anon, authenticated;
REVOKE ALL ON SCHEMA private FROM public, anon, authenticated;

-- Permissão explícita de navegação (USAGE) apenas no schema public (exposição Data API)
GRANT USAGE ON SCHEMA public TO anon, authenticated;

-- Revogação preventiva de todos os privilégios em tabelas existentes nos schemas
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM public, anon, authenticated;
REVOKE ALL ON ALL TABLES IN SCHEMA private FROM public, anon, authenticated;

-- Defesa em Profundidade: Revogação explícita de privilégios padrão para futuros objetos
-- Garante que novos objetos criados nos schemas não herdem concessões públicas acidentais.
ALTER DEFAULT PRIVILEGES IN SCHEMA public REVOKE ALL ON TABLES FROM public, anon, authenticated;
ALTER DEFAULT PRIVILEGES IN SCHEMA private REVOKE ALL ON TABLES FROM public, anon, authenticated;
ALTER DEFAULT PRIVILEGES IN SCHEMA public REVOKE ALL ON SEQUENCES FROM public, anon, authenticated;
ALTER DEFAULT PRIVILEGES IN SCHEMA private REVOKE ALL ON SEQUENCES FROM public, anon, authenticated;
ALTER DEFAULT PRIVILEGES IN SCHEMA public REVOKE ALL ON ROUTINES FROM public, anon, authenticated;
ALTER DEFAULT PRIVILEGES IN SCHEMA private REVOKE ALL ON ROUTINES FROM public, anon, authenticated;

-- ==============================================================================
-- SEGURANÇA E POLÍTICAS RLS PARA RECURSOS PÚBLICOS EXPOSTOS (SCHEMA public)
-- ==============================================================================
-- NOTA DE ARQUITETURA DE SEGURANÇA:
-- Para os 9 recursos do schema public expostos via Data API conforme DEC_ACCESS_004,
-- aplica-se a habilitação forçada de RLS (FORCE ROW LEVEL SECURITY), revogação total
-- e concessão explícita de GRANT SELECT aos papéis 'anon' e 'authenticated'.
-- As políticas de leitura pública utilizam a expressão incondicional USING (true)
-- em conformidade com as permissões PERM_001, PERM_003, PERM_005-PERM_011.
--
-- Observação sobre permissões administrativas em recursos públicos:
-- Somente PERM_002 (competicao) e PERM_004 (partida) possuem regras atreladas ao
-- ROLE_ADMIN_DADOS sob ACCESS_REQUIREMENTS@0.1.0, gerando os respectivos blocos
-- GENERATION_BLOCKED. As demais 7 tabelas públicas não possuem mapeamento de papel
-- administrativo definido na especificação de acesso promovida.
-- ==============================================================================

--------------------------------------------------------------------------------
-- 1. Tabela: public.competicao (Recurso: RES_COMPETICAO)
--------------------------------------------------------------------------------
ALTER TABLE public.competicao ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.competicao FORCE ROW LEVEL SECURITY;

REVOKE ALL ON public.competicao FROM public, anon, authenticated;

GRANT SELECT ON public.competicao TO anon, authenticated;

CREATE POLICY p_select_competicao_publica ON public.competicao
  FOR SELECT
  TO anon, authenticated
  USING (true);

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_002
-- Recurso: RES_COMPETICAO (public.competicao)
-- Papel Exigido: ROLE_ADMIN_DADOS
-- Operação: SELECT
-- Requisito de Acesso: Todas as linhas, somente enquanto houver atribuição administrativa vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo GLOBAL.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

--------------------------------------------------------------------------------
-- 2. Tabela: public.partida (Recurso: RES_PARTIDA)
--------------------------------------------------------------------------------
ALTER TABLE public.partida ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.partida FORCE ROW LEVEL SECURITY;

REVOKE ALL ON public.partida FROM public, anon, authenticated;

GRANT SELECT ON public.partida TO anon, authenticated;

CREATE POLICY p_select_partida_publica ON public.partida
  FOR SELECT
  TO anon, authenticated
  USING (true);

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_004
-- Recurso: RES_PARTIDA (public.partida)
-- Papel Exigido: ROLE_ADMIN_DADOS
-- Operação: SELECT
-- Requisito de Acesso: Todas as linhas, somente enquanto houver atribuição administrativa vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo GLOBAL.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

--------------------------------------------------------------------------------
-- 3. Tabela: public.equipe (Recurso: RES_EQUIPE)
--------------------------------------------------------------------------------
ALTER TABLE public.equipe ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.equipe FORCE ROW LEVEL SECURITY;

REVOKE ALL ON public.equipe FROM public, anon, authenticated;

GRANT SELECT ON public.equipe TO anon, authenticated;

CREATE POLICY p_select_equipe_publica ON public.equipe
  FOR SELECT
  TO anon, authenticated
  USING (true);

--------------------------------------------------------------------------------
-- 4. Tabela: public.partida_equipe (Recurso: RES_PARTIDA_EQUIPE)
--------------------------------------------------------------------------------
ALTER TABLE public.partida_equipe ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.partida_equipe FORCE ROW LEVEL SECURITY;

REVOKE ALL ON public.partida_equipe FROM public, anon, authenticated;

GRANT SELECT ON public.partida_equipe TO anon, authenticated;

CREATE POLICY p_select_partida_equipe_publica ON public.partida_equipe
  FOR SELECT
  TO anon, authenticated
  USING (true);

--------------------------------------------------------------------------------
-- 5. Tabela: public.periodo_set (Recurso: RES_PERIODO_SET)
--------------------------------------------------------------------------------
ALTER TABLE public.periodo_set ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.periodo_set FORCE ROW LEVEL SECURITY;

REVOKE ALL ON public.periodo_set FROM public, anon, authenticated;

GRANT SELECT ON public.periodo_set TO anon, authenticated;

CREATE POLICY p_select_periodo_set_publico ON public.periodo_set
  FOR SELECT
  TO anon, authenticated
  USING (true);

--------------------------------------------------------------------------------
-- 6. Tabela: public.shoot_out (Recurso: RES_SHOOT_OUT)
--------------------------------------------------------------------------------
ALTER TABLE public.shoot_out ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.shoot_out FORCE ROW LEVEL SECURITY;

REVOKE ALL ON public.shoot_out FROM public, anon, authenticated;

GRANT SELECT ON public.shoot_out TO anon, authenticated;

CREATE POLICY p_select_shoot_out_publico ON public.shoot_out
  FOR SELECT
  TO anon, authenticated
  USING (true);

--------------------------------------------------------------------------------
-- 7. Tabela: public.placar_jogo (Recurso: RES_PLACAR_JOGO)
--------------------------------------------------------------------------------
ALTER TABLE public.placar_jogo ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.placar_jogo FORCE ROW LEVEL SECURITY;

REVOKE ALL ON public.placar_jogo FROM public, anon, authenticated;

GRANT SELECT ON public.placar_jogo TO anon, authenticated;

CREATE POLICY p_select_placar_jogo_publico ON public.placar_jogo
  FOR SELECT
  TO anon, authenticated
  USING (true);

--------------------------------------------------------------------------------
-- 8. Tabela: public.estado_do_placar (Recurso: RES_ESTADO_DO_PLACAR)
--------------------------------------------------------------------------------
ALTER TABLE public.estado_do_placar ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.estado_do_placar FORCE ROW LEVEL SECURITY;

REVOKE ALL ON public.estado_do_placar FROM public, anon, authenticated;

GRANT SELECT ON public.estado_do_placar TO anon, authenticated;

CREATE POLICY p_select_estado_do_placar_publico ON public.estado_do_placar
  FOR SELECT
  TO anon, authenticated
  USING (true);

--------------------------------------------------------------------------------
-- 9. Tabela: public.evolucao_do_placar (Recurso: RES_EVOLUCAO_DO_PLACAR)
--------------------------------------------------------------------------------
ALTER TABLE public.evolucao_do_placar ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.evolucao_do_placar FORCE ROW LEVEL SECURITY;

REVOKE ALL ON public.evolucao_do_placar FROM public, anon, authenticated;

GRANT SELECT ON public.evolucao_do_placar TO anon, authenticated;

CREATE POLICY p_select_evolucao_do_placar_publica ON public.evolucao_do_placar
  FOR SELECT
  TO anon, authenticated
  USING (true);

-- ==============================================================================
-- SEGURANÇA E BLOQUEIOS EM RECURSOS FECHADOS (SCHEMA private)
-- ==============================================================================
-- NOTA DE ENFORCEMENT DE PERÍMETRO:
-- Em observância às decisões DEC_ACCESS_001 e DEC_ACCESS_004, todas as 23 tabelas do
-- schema 'private' são totalmente bloqueadas para a Data API e papéis não privilegiados.
-- O enforçamento é realizado através de FORCE ROW LEVEL SECURITY e revogação total de
-- privilégios. Nenhuma política permissiva é criada.
--
-- Para cada permissão mapeada em ACCESS_REQUIREMENTS (PERM_012 a PERM_056, excluindo
-- a PERM_047 revogada por DEC_ACCESS_001), emite-se um bloco GENERATION_BLOCKED formal.
-- ==============================================================================

--------------------------------------------------------------------------------
-- Habilitação de FORCE RLS e Revogação Total nas 23 Tabelas Privadas
--------------------------------------------------------------------------------
ALTER TABLE private.equipe_atleta_inscricao ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.equipe_atleta_inscricao FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.equipe_atleta_inscricao FROM public, anon, authenticated;

ALTER TABLE private.posse_de_bola ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.posse_de_bola FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.posse_de_bola FROM public, anon, authenticated;

ALTER TABLE private.unidade_basica_ataque_bou ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.unidade_basica_ataque_bou FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.unidade_basica_ataque_bou FROM public, anon, authenticated;

ALTER TABLE private.evento_scout ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.evento_scout FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.evento_scout FROM public, anon, authenticated;

ALTER TABLE private.observacao_de_scout ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.observacao_de_scout FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.observacao_de_scout FROM public, anon, authenticated;

ALTER TABLE private.protocolo_scout ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.protocolo_scout FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.protocolo_scout FROM public, anon, authenticated;

ALTER TABLE private.midia_video ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.midia_video FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.midia_video FROM public, anon, authenticated;

ALTER TABLE private.segmento_observado ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.segmento_observado FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.segmento_observado FROM public, anon, authenticated;

ALTER TABLE private.sistema_defensivo ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.sistema_defensivo FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.sistema_defensivo FROM public, anon, authenticated;

ALTER TABLE private.confiabilidade_observador ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.confiabilidade_observador FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.confiabilidade_observador FROM public, anon, authenticated;

ALTER TABLE private.revisao_da_observacao ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.revisao_da_observacao FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.revisao_da_observacao FROM public, anon, authenticated;

ALTER TABLE private.estado_de_revisao ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.estado_de_revisao FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.estado_de_revisao FROM public, anon, authenticated;

ALTER TABLE private.proveniencia_observacao ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.proveniencia_observacao FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.proveniencia_observacao FROM public, anon, authenticated;

ALTER TABLE private.trecho_observado ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.trecho_observado FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.trecho_observado FROM public, anon, authenticated;

ALTER TABLE private.spin_shot ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.spin_shot FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.spin_shot FROM public, anon, authenticated;

ALTER TABLE private.in_flight_shot ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.in_flight_shot FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.in_flight_shot FROM public, anon, authenticated;

ALTER TABLE private.sistema_tatico ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.sistema_tatico FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.sistema_tatico FROM public, anon, authenticated;

ALTER TABLE private.papel_esportivo_operacional ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.papel_esportivo_operacional FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.papel_esportivo_operacional FROM public, anon, authenticated;

ALTER TABLE private.participacao_equipe_competicao ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.participacao_equipe_competicao FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.participacao_equipe_competicao FROM public, anon, authenticated;

ALTER TABLE private.atleta ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.atleta FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.atleta FROM public, anon, authenticated;

ALTER TABLE private.analista_observador ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.analista_observador FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.analista_observador FROM public, anon, authenticated;

ALTER TABLE private.desqualificacao_segunda_exclusao ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.desqualificacao_segunda_exclusao FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.desqualificacao_segunda_exclusao FROM public, anon, authenticated;

ALTER TABLE private.cartao_azul_suspensao ENABLE ROW LEVEL SECURITY;
ALTER TABLE private.cartao_azul_suspensao FORCE ROW LEVEL SECURITY;
REVOKE ALL ON private.cartao_azul_suspensao FROM public, anon, authenticated;

--------------------------------------------------------------------------------
-- Emissão Formal de Blocos GENERATION_BLOCKED para Permissões Restritas
--------------------------------------------------------------------------------

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_012
-- Recurso: RES_EQUIPE_ATLETA_INSCRICAO (private.equipe_atleta_inscricao)
-- Papel Exigido: ROLE_TREINADOR
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às equipes, competições e partidas atribuídas ao papel por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo TEAM.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_013
-- Recurso: RES_EQUIPE_ATLETA_INSCRICAO (private.equipe_atleta_inscricao)
-- Papel Exigido: ROLE_TREINADOR
-- Operação: INSERT
-- Requisito de Acesso: Somente linhas vinculadas às equipes, competições e partidas atribuídas ao papel por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo TEAM.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_014
-- Recurso: RES_POSSE_DE_BOLA (private.posse_de_bola)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_015
-- Recurso: RES_POSSE_DE_BOLA (private.posse_de_bola)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: INSERT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_016
-- Recurso: RES_UNIDADE_BASICA_ATAQUE_BOU (private.unidade_basica_ataque_bou)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_017
-- Recurso: RES_UNIDADE_BASICA_ATAQUE_BOU (private.unidade_basica_ataque_bou)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: INSERT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_018
-- Recurso: RES_EVENTO_SCOUT (private.evento_scout)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_019
-- Recurso: RES_EVENTO_SCOUT (private.evento_scout)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: INSERT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_020
-- Recurso: RES_OBSERVACAO_DE_SCOUT (private.observacao_de_scout)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_021
-- Recurso: RES_OBSERVACAO_DE_SCOUT (private.observacao_de_scout)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: INSERT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_022
-- Recurso: RES_PROTOCOLO_SCOUT (private.protocolo_scout)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_023
-- Recurso: RES_MIDIA_VIDEO (private.midia_video)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_024
-- Recurso: RES_MIDIA_VIDEO (private.midia_video)
-- Papel Exigido: ROLE_TREINADOR
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às equipes, competições e partidas atribuídas ao papel por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo TEAM.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_025
-- Recurso: RES_SEGMENTO_OBSERVADO (private.segmento_observado)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_026
-- Recurso: RES_SEGMENTO_OBSERVADO (private.segmento_observado)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: INSERT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_027
-- Recurso: RES_SISTEMA_DEFENSIVO (private.sistema_defensivo)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_028
-- Recurso: RES_SISTEMA_DEFENSIVO (private.sistema_defensivo)
-- Papel Exigido: ROLE_TREINADOR
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às equipes, competições e partidas atribuídas ao papel por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo TEAM.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_029
-- Recurso: RES_CONFIABILIDADE_OBSERVADOR (private.confiabilidade_observador)
-- Papel Exigido: ROLE_REVISOR_SCOUT
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao revisor por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo REVISION.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_030
-- Recurso: RES_CONFIABILIDADE_OBSERVADOR (private.confiabilidade_observador)
-- Papel Exigido: ROLE_ADMIN_DADOS
-- Operação: UPDATE
-- Requisito de Acesso: Todas as linhas, somente enquanto houver atribuição administrativa vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo GLOBAL.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_031
-- Recurso: RES_REVISAO_DA_OBSERVACAO (private.revisao_da_observacao)
-- Papel Exigido: ROLE_REVISOR_SCOUT
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao revisor por associação vigente no banco, respeitada a invariante de segregação de funções.
-- Invariante de Negócio Exigida: DEC_ACCESS_003 (REVISOR_DIFERENTE_DO_ANALISTA_ORIGINAL: revisor_id <> analista_observador_id).
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física de atribuição de revisão e vínculo de conta para mapear auth.uid() ao escopo REVISION com validação de segregação.
-- Ação de Mitigação: Criar modelo de atribuição auditável e implementar checagem funcional antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_032
-- Recurso: RES_REVISAO_DA_OBSERVACAO (private.revisao_da_observacao)
-- Papel Exigido: ROLE_REVISOR_SCOUT
-- Operação: INSERT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao revisor por associação vigente no banco, respeitada a invariante de segregação de funções.
-- Invariante de Negócio Exigida: DEC_ACCESS_003 (REVISOR_DIFERENTE_DO_ANALISTA_ORIGINAL: revisor_id <> analista_observador_id).
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física de atribuição de revisão e vínculo de conta para mapear auth.uid() ao escopo REVISION com validação de segregação.
-- Ação de Mitigação: Criar modelo de atribuição auditável e implementar checagem funcional antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_033
-- Recurso: RES_ESTADO_DE_REVISAO (private.estado_de_revisao)
-- Papel Exigido: ROLE_REVISOR_SCOUT
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao revisor por associação vigente no banco, respeitada a invariante de segregação de funções.
-- Invariante de Negócio Exigida: DEC_ACCESS_003 (REVISOR_DIFERENTE_DO_ANALISTA_ORIGINAL: revisor_id <> analista_observador_id).
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física de atribuição de revisão e vínculo de conta para mapear auth.uid() ao escopo REVISION com validação de segregação.
-- Ação de Mitigação: Criar modelo de atribuição auditável e implementar checagem funcional antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_034
-- Recurso: RES_PROVENIENCIA_OBSERVACAO (private.proveniencia_observacao)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_035
-- Recurso: RES_TRECHO_OBSERVADO (private.trecho_observado)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_036
-- Recurso: RES_TRECHO_OBSERVADO (private.trecho_observado)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: INSERT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_037
-- Recurso: RES_SPIN_SHOT (private.spin_shot)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_038
-- Recurso: RES_SPIN_SHOT (private.spin_shot)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: INSERT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_039
-- Recurso: RES_IN_FLIGHT_SHOT (private.in_flight_shot)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_040
-- Recurso: RES_IN_FLIGHT_SHOT (private.in_flight_shot)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: INSERT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_041
-- Recurso: RES_SISTEMA_TATICO (private.sistema_tatico)
-- Papel Exigido: ROLE_TREINADOR
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às equipes, competições e partidas atribuídas ao papel por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo TEAM.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_042
-- Recurso: RES_SISTEMA_TATICO (private.sistema_tatico)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_043
-- Recurso: RES_PAPEL_ESPORTIVO_OPERACIONAL (private.papel_esportivo_operacional)
-- Papel Exigido: ROLE_TREINADOR
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às equipes, competições e partidas atribuídas ao papel por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo TEAM.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_044
-- Recurso: RES_PAPEL_ESPORTIVO_OPERACIONAL (private.papel_esportivo_operacional)
-- Papel Exigido: ROLE_ADMIN_DADOS
-- Operação: SELECT
-- Requisito de Acesso: Todas as linhas, somente enquanto houver atribuição administrativa vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo GLOBAL.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_045
-- Recurso: RES_PARTICIPACAO_EQUIPE_COMPETICAO (private.participacao_equipe_competicao)
-- Papel Exigido: ROLE_TREINADOR
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às equipes, competições e partidas atribuídas ao papel por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo TEAM.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_046
-- Recurso: RES_PARTICIPACAO_EQUIPE_COMPETICAO (private.participacao_equipe_competicao)
-- Papel Exigido: ROLE_TREINADOR
-- Operação: INSERT
-- Requisito de Acesso: Somente linhas vinculadas às equipes, competições e partidas atribuídas ao papel por associação vigente no banco.
-- Escopo de Colunas: [] (Todas as colunas)
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo TEAM.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_048
-- Recurso: RES_ATLETA (private.atleta)
-- Papel Exigido: ROLE_TREINADOR
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às equipes, competições e partidas atribuídas ao papel por associação vigente no banco.
-- Restrição de Escopo de Colunas (Column Scope): [ID, NOME_COMPLETO, NOME_CAMISA, NUMERO_REGISTRO, POSICAO_PRINCIPAL]
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo TEAM.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) e aplicar visão/GRANT de colunas antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_049
-- Recurso: RES_ATLETA (private.atleta)
-- Papel Exigido: ROLE_ADMIN_DADOS
-- Operação: UPDATE
-- Requisito de Acesso: Todas as linhas, somente enquanto houver atribuição administrativa vigente no banco.
-- Restrição de Escopo de Colunas (Column Scope): [ID, NOME_COMPLETO, NOME_CAMISA, NUMERO_REGISTRO, POSICAO_PRINCIPAL]
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo GLOBAL.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) e aplicar concessão restrita de colunas antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_050
-- Recurso: RES_ANALISTA_OBSERVADOR (private.analista_observador)
-- Papel Exigido: ROLE_ANALISTA_SCOUT
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às partidas atribuídas ao analista por associação vigente no banco.
-- Restrição de Escopo de Colunas (Column Scope): [ID, NOME, EMAIL, STATUS_HABILITACAO]
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo MATCH.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_051
-- Recurso: RES_ANALISTA_OBSERVADOR (private.analista_observador)
-- Papel Exigido: ROLE_ADMIN_DADOS
-- Operação: SELECT
-- Requisito de Acesso: Todas as linhas, somente enquanto houver atribuição administrativa vigente no banco.
-- Restrição de Escopo de Colunas (Column Scope): [ID, NOME, EMAIL, STATUS_HABILITACAO]
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo GLOBAL.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_052
-- Recurso: RES_ANALISTA_OBSERVADOR (private.analista_observador)
-- Papel Exigido: ROLE_ADMIN_DADOS
-- Operação: UPDATE
-- Requisito de Acesso: Todas as linhas, somente enquanto houver atribuição administrativa vigente no banco.
-- Restrição de Escopo de Colunas (Column Scope): [ID, NOME, EMAIL, STATUS_HABILITACAO]
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo GLOBAL.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_053
-- Recurso: RES_DESQUALIFICACAO_SEGUNDA_EXCLUSAO (private.desqualificacao_segunda_exclusao)
-- Papel Exigido: ROLE_TREINADOR
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às equipes, competições e partidas atribuídas ao papel por associação vigente no banco.
-- Restrição de Escopo de Colunas (Column Scope): [ID, EVENTO_SCOUT_ID, ATLETA_ID, PARTIDA_ID, SAIDA_IMEDIATA_QUADRA]
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo TEAM.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_054
-- Recurso: RES_DESQUALIFICACAO_SEGUNDA_EXCLUSAO (private.desqualificacao_segunda_exclusao)
-- Papel Exigido: ROLE_ADMIN_DADOS
-- Operação: SELECT
-- Requisito de Acesso: Todas as linhas, somente enquanto houver atribuição administrativa vigente no banco.
-- Restrição de Escopo de Colunas (Column Scope): [ID, EVENTO_SCOUT_ID, ATLETA_ID, PARTIDA_ID, SAIDA_IMEDIATA_QUADRA]
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo GLOBAL.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_055
-- Recurso: RES_CARTAO_AZUL_SUSPENSAO (private.cartao_azul_suspensao)
-- Papel Exigido: ROLE_TREINADOR
-- Operação: SELECT
-- Requisito de Acesso: Somente linhas vinculadas às equipes, competições e partidas atribuídas ao papel por associação vigente no banco.
-- Restrição de Escopo de Colunas (Column Scope): [ID, EVENTO_SCOUT_ID, PARTIDA_ID, ATLETA_ID, PAPEL_OPERACIONAL_ID, RELATORIO_ARBITRAGEM, JOGOS_SUSPENSAO_AUTOMATICA]
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo TEAM.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- GENERATION_BLOCKED: PERM_056
-- Recurso: RES_CARTAO_AZUL_SUSPENSAO (private.cartao_azul_suspensao)
-- Papel Exigido: ROLE_ADMIN_DADOS
-- Operação: SELECT
-- Requisito de Acesso: Todas as linhas, somente enquanto houver atribuição administrativa vigente no banco.
-- Restrição de Escopo de Colunas (Column Scope): [ID, EVENTO_SCOUT_ID, PARTIDA_ID, ATLETA_ID, PAPEL_OPERACIONAL_ID, RELATORIO_ARBITRAGEM, JOGOS_SUSPENSAO_AUTOMATICA]
-- Dependência Ausente: Ausência de tabela/coluna física no schema promovido para mapear auth.uid() ao escopo GLOBAL.
-- Ação de Mitigação: Criar modelo de atribuição auditável (downstream requirement) antes da liberação de RLS.
-- ==============================================================================

-- ==============================================================================
-- AVALIAÇÃO E CRIAÇÃO DE ÍNDICES PARA FILTROS RLS
-- ==============================================================================
--
-- 1. AVALIAÇÃO DE COBERTURA DE ÍNDICES NO SCHEMA PUBLIC:
--    Os índices já criados no candidato físico do STAGE_08 cobrem integralmente as
--    chaves estrangeiras e relacionamentos das 9 tabelas públicas:
--    - idx_partida_competicao ON public.partida (competicao_id)
--    - idx_partida_equipe_equipe ON public.partida_equipe (equipe_id)
--    - idx_periodo_set_equipe_vencedora ON public.periodo_set (equipe_vencedora_id)
--    - idx_shoot_out_equipe_vencedora ON public.shoot_out (equipe_vencedora_id)
--    - idx_placar_jogo_equipe_vencedora ON public.placar_jogo (equipe_vencedora_id)
--    - idx_estado_placar_placar_jogo ON public.estado_do_placar (placar_jogo_id)
--    - idx_estado_placar_periodo_set ON public.estado_do_placar (periodo_set_id)
--    - idx_evolucao_placar_evento_scout ON public.evolucao_do_placar (evento_scout_id)
--    - idx_evolucao_placar_equipe ON public.evolucao_do_placar (equipe_beneficiada_id)
--
--    Dado que as 9 políticas de leitura pública ativas utilizam a expressão incondicional
--    USING (true), não há exigência de criação de novos índices no schema public neste estágio.
--
-- 2. SÍNTESE E PRONTIDÃO PARA RECURSOS FECHADOS (SCHEMA PRIVATE):
--    Em alinhamento com a diretriz downstream STAGE_06_OPERATOR_REVIEW_001 ("Criar índices
--    nas colunas usadas pelos escopos RLS e validar os planos das consultas"), confirma-se
--    que os 50 índices de chave estrangeira criados no STAGE_08 (como idx_observacao_scout_analista,
--    idx_evento_scout_observacao, idx_sistema_defensivo_posse, idx_confiabilidade_analista,
--    idx_revisao_observacao_obs, etc.) constituirão a base estrutural para a execução de subconsultas
--    de escopo (ex: auth.uid() = analista_observador_id) quando os recursos privados forem
--    desbloqueados em estágios futuros.
-- ==============================================================================

-- ==============================================================================
-- DECLARAÇÕES E SALVAGUARDAS FINAIS
-- ==============================================================================
--
-- 1. ISOLAMENTO DE CREDENCIAIS E SEGREDOS:
--    Nenhuma credencial privilegiada (como service_role), chave secreta ou parâmetro
--    sensível de ambiente foi exposto ou incorporado neste artefato SQL.
--
-- 2. ORIGEM DA AUTORIZAÇÃO:
--    Confirma-se expressamente que nenhuma regra de autorização baseia-se em
--    user_metadata ou dados autodeclarados pelo cliente no token JWT. A autorização
--    dependerá estritamente de tabelas de associação persistidas e auditáveis no banco.
--
-- 3. GOVERNANÇA DE IMPLANTAÇÃO:
--    Este arquivo possui caráter exclusivamente candidato. Qualquer criação de migration,
--    execução física ou aplicação em banco de dados depende de nova aprovação humana
--    e da conclusão rigorosa dos estágios subsequentes (STAGE_10 a STAGE_15).
-- ==============================================================================