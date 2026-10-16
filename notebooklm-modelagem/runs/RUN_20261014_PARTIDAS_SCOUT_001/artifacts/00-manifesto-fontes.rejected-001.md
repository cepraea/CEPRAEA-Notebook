# Plano de Execução do Manifesto de Reconciliação de Fontes (`00-manifesto-fontes.yaml`)

run_id: "RUN_20261014_PARTIDAS_SCOUT_001"
domain_id: "PARTIDAS_SCOUT_ANALISE_TATICA"
reference_date: "2026-10-14"
status: "PROPOSTO"

escopo_incluido:
  - "Partida, sets, segmentos e shoot-out"
  - "Placar e eventos de pontuação"
  - "Gols de um e dois pontos, spin shot, in-flight e tiro de seis metros"
  - "Punições e exclusões"
  - "Posses de bola, fases ofensivas e sistemas defensivos"
  - "Ações da goleira e zonas da quadra (origem e alvo)"
  - "Resultado das ações técnicas e táticas"
  - "Scout observacional, protocolo, observador, revisão e confiabilidade"
  - "Mídia observacional, trecho de vídeo e timecode (exclusivamente como proveniência)"
  - "Modelos e SQL existentes (classificados estritamente como propostas históricas a reconciliar)"

escopo_excluido:
  - "Carga e planejamento de treinamento"
  - "Saúde, prontuário ou avaliação médica de atletas"
  - "Gestão financeira, orçamentária ou administrativa"
  - "Mídia institucional, marketing e acervo fotográfico público"
  - "Infraestrutura de TI e autenticação fora do enquadramento dos artefatos históricos"

fontes_selecionadas:
  - source_id: "ARQ-001"
    notebook_source_id: "04A-MODELO-CONCEITUAL.md"
    titulo_canonical: "04A — Modelo Conceitual — CEPRAEA Beach Pro"
    categoria_autoridade: "historica"
    vigencia_e_data: "2026-08-07T15:02:00-03:00"
    escopo_coberto: "Objetos de negócio, estruturas táticas, relações conceituais, lifecycles e diretrizes formais de governança."
    status_revisao: "APPROVED"
    limitacoes: "Modelo conceitual da fase de reconciliação; modelo predecessor 04-MODELO-CONCEITUAL-E-LOGICO preservado apenas como baseline histórico."
    hash: null

  - source_id: "ARQ-002"
    notebook_source_id: "04B-MODELO-LOGICO.md"
    titulo_canonical: "04B — MODELO LÓGICO — CEPRAEA BEACH PRO"
    categoria_autoridade: "historica"
    vigencia_e_data: "2026-10-12"
    escopo_coberto: "Tipagem abstrata de objetos (ATHLETE, TACTICAL_ASSIGNMENT, MATCH, MATCH_SEGMENT, CARIOCA_2026_SCORING_RULE), cardinalidades e restrições declarativas."
    status_revisao: "APPROVED"
    limitacoes: "Não introduz escolhas físicas de SGBD; mantém tipos abstratos e referências genéricas sob Stop Gate físico."
    hash: null

  - source_id: "04C"
    notebook_source_id: "04C-DICIONARIO-DE-DADOS.md"
    titulo_canonical: "04C — DICIONÁRIO DE DADOS CANÔNICO — CEPRAEA BEACH HANDBALL PRO"
    categoria_autoridade: "historica"
    vigencia_e_data: null
    escopo_coberto: "Documentação da camada física e relacional no PostgreSQL 15+/Supabase (athletes, calendar_events, availability_declarations, factual_presences, competitions, convocations, matches, match_appearances) e classes epistemológicas."
    status_revisao: "APPROVED"
    limitacoes: "Detalhamento estrito do schema de tabelas operacionais; tabelas especializadas de scout detalhado são suplementadas pelo DDL 05."
    hash: null

  - source_id: "05"
    notebook_source_id: "05-schema-postgresql.sql"
    titulo_canonical: "05 — MODELO FÍSICO POSTGRESQL / SUPABASE — CEPRAEA BEACH HANDBALL PRO"
    categoria_autoridade: "historica"
    vigencia_e_data: null
    escopo_coberto: "Estrutura DDL física em PostgreSQL: enums canônicos, governança, cadastro de elenco, eventos, presença, competições, convocações, partidas e tabelas de scout observacional (possessions, bous, tactical_events, finalizations, goalkeeper_actions)."
    status_revisao: "APPROVED"
    limitacoes: "Classificado estritamente como proposta histórica sujeita à validação no novo domínio tático."
    hash: null

  - source_id: "06"
    notebook_source_id: "06-migrations-rollback.sql.md"
    titulo_canonical: "06 — MIGRATIONS VERSIONADAS E ROLLBACK — CEPRAEA BEACH HANDBALL PRO"
    categoria_autoridade: "historica"
    vigencia_e_data: "2026-10-13"
    escopo_coberto: "Scripts de migração versionada (20261013000001) e instrução de rollback (UP/DOWN) para o ecossistema Supabase/PostgreSQL."
    status_revisao: "ACTIVE"
    limitacoes: "Script operacional de infraestrutura condicionado ao pipeline de execução do banco."
    hash: null

  - source_id: "07"
    notebook_source_id: "07-matriz-rbac-e-politicas-rls"
    titulo_canonical: "07 — MATRIZ RBAC E POLÍTICAS RLS (SUPABASE) — CEPRAEA BEACH HANDBALL PRO"
    categoria_autoridade: "historica"
    vigencia_e_data: null
    escopo_coberto: "Controle de acesso por linha (Row Level Security), princípio default-deny, permissões para perfis anon/authenticated e funções privadas helper."
    status_revisao: "ACTIVE"
    limitacoes: "Proposta de segurança em nível de banco que requer alinhamento com a matriz de autorização das novas entidades de scout."
    hash: null

  - source_id: "IHF-RULES-2PT"
    notebook_source_id: "2-point goals (spin and in-flight shots)-min.pdf"
    titulo_canonical: "IHF Online Education Weeks 2023 — 2-point Goals, Spin and In-flight"
    categoria_autoridade: "regramento_tecnico"
    vigencia_e_data: "2023"
    escopo_coberto: "Regras oficiais da IHF para valoração de gols (1 e 2 pontos), definições técnicas e ângulos de Spin Shots, In-flight shots, gols de goleira/especialista e tiro de 6 metros."
    status_revisao: "APPROVED"
    limitacoes: "Material educacional oficial IHF focalizado nas especificidades técnicas dos arremessos espetaculares."
    hash: null

  - source_id: "IHF-RULES-6M"
    notebook_source_id: "6-metre throw + punishments.pdf"
    titulo_canonical: "IHF Online Education Weeks 2023 — 6-Metre Throw + Punishment"
    categoria_autoridade: "regramento_tecnico"
    vigencia_e_data: "2023"
    escopo_coberto: "Regras oficiais da IHF sobre marcação e execução de tiro de 6 metros, destruição de clara chance de gol, e critérios de punição disciplinar para faltas contra o corpo."
    status_revisao: "APPROVED"
    limitacoes: "Apresentação técnica focada na tomada de decisão da arbitragem e aplicação de sanções em quadra."
    hash: null

  - source_id: "CEPRAEA-DB"
    notebook_source_id: "CEPRAEA DATABASE"
    titulo_canonical: "CEPRAEA DATABASE — SSOT OPERACIONAL (DB_CONFIG, DB_ATLETAS, DB_PRESENCA, DB_JOGOS, DB_SISTEMAS_POSICOES, DB_ATLETA_POSICOES_TATICAS)"
    categoria_autoridade: "operacional"
    vigencia_e_data: "2026-09-09"
    escopo_coberto: "Parâmetros de governança, cadastro oficial de atletas, posições táticas primárias e secundárias, presenças factuais (DEC-DATA-045), regras de disponibilidade (RN-DISP-001 a 017), registros de jogos e validações de regressão."
    status_revisao: "APPROVED"
    limitacoes: "Base de dados operacional ativa contendo marcas de desatualização normativa mapeadas (ex.: Art. 25º FHERJ como STALE_FOR_SCORING)."
    hash: null

  - source_id: "LIT-001"
    notebook_source_id: "Contextual_Factors_and_Decision-Making_in_the_Behavior_of_Finalization_in_the_Positional_Attack_in_Beach_Handball.pdf"
    titulo_canonical: "Frontiers in Psychology — Contextual Factors and Decision-Making in the Behavior of Finalization in the Positional Attack in Beach Handball"
    categoria_autoridade: "regramento_tecnico"
    vigencia_e_data: "2019-06"
    escopo_coberto: "Estudo científico observacional sobre tomada de decisão e fatores contextuais na finalização do ataque posicionado."
    status_revisao: null
    limitacoes: "Excerto de metadados publicado no volume 10, artigo 1386 da revista Frontiers in Psychology."
    hash: null

  - source_id: "LIT-002"
    notebook_source_id: "Estudo das ações do guarda redes de andebol de praia através da análise.pdf"
    titulo_canonical: "Cuadernos de Psicología del Deporte — Estudo das ações do guarda redes de andebol de praia através da análise"
    categoria_autoridade: "regramento_tecnico"
    vigencia_e_data: "2019-09"
    escopo_coberto: "Análise técnica do comportamento defensivo e intervenções do guarda-redes de andebol de praia."
    status_revisao: null
    limitacoes: "Excerto pontual (p. 155) da publicação Cuadernos de Psicología del Deporte."
    hash: null

  - source_id: "LIT-003"
    notebook_source_id: "Tempos de defesa do goleiro de handebol de praia.pdf"
    titulo_canonical: "Tempos de defesa do goleiro de handebol de praia"
    categoria_autoridade: "regramento_tecnico"
    vigencia_e_data: null
    escopo_coberto: "Métricas temporais de reação e eficácia das ações defensivas do goleiro."
    status_revisao: null
    limitacoes: "Excerto de pesquisa técnica focado em tempos de defesa."
    hash: null

analise_relacional:
  duplicidades_e_sobreposicoes:
    - descricao: "Convergência na valoração de gols de 2 pontos (spin shot, in-flight, goleira/especialista e tiro de 6 metros) entre as apresentações da IHF e a restrição da tabela de finalizações no DDL 05."
      artefatos_envolvidos:
        - "IHF-RULES-2PT"
        - "IHF-RULES-6M"
        - "05-schema-postgresql.sql (tabela public.finalizations, coluna points_awarded)"
      resolucao_mecanismo: "A regra técnica da IHF valida o constraint CHECK (points_awarded IN (0, 1, 2)) presente no banco físico."

    - descricao: "Mapeamento de posições táticas e funções entre os modelos conceituais, lógicos, dicionário de dados e tabelas ativas do banco de dados operacional."
      artefatos_envolvidos:
        - "04A-MODELO-CONCEITUAL.md"
        - "04B-MODELO-LOGICO.md"
        - "04C-DICIONARIO-DE-DADOS.md"
        - "CEPRAEA DATABASE (DB_ATLETAS, DB_POSICOES, DB_SISTEMAS_POSICOES, DB_ATLETA_POSICOES_TATICAS)"
      resolucao_mecanismo: "Alinhamento normativo garantindo que GOLEIRA pertença à função DEFESA e que posições secundárias permaneçam sob autoridade restrita de governança."

  traducoes_e_conversoes:
    - termo_origem_ingles: "Spin shot"
      taxonomia_pt_cepraea: "Giro / Arremesso com rotação completa de 360 graus no ar"
      regra_valoracao: "Concede 2 pontos se executado com rotação completa e salto correto com pés direcionados ao gol no momento da impulsão."

    - termo_origem_ingles: "In-flight shot"
      taxonomia_pt_cepraea: "Ponte aérea / Finalização em suspensão aérea"
      regra_valoracao: "Concede 2 pontos se o atleta dominar a bola e arremessar enquanto estiver no ar. O ato de apenas empurrar ou dar um tapinha na bola ('pushing/slapping') concede apenas 1 ponto."

    - termo_origem_ingles: "6-metre throw"
      taxonomia_pt_cepraea: "Tiro de 6 metros"
      regra_valoracao: "Penalidade máxima decorrente da destruição de clara chance de gol; se convertido, concede obrigatoriamente 2 pontos."

    - termo_origem_ingles: "Specialist / Goalkeeper goal"
      taxonomia_pt_cepraea: "Gol da Especialista / Gol da Goleira"
      regra_valoracao: "Qualquer gol assinalado diretamente pela goleira da sua área de gol ou pela especialista em jogo regular concede 2 pontos."

  substituicoes_e_sucessoes:
    - artefato_obsoleto: "04-MODELO-CONCEITUAL-E-LOGICO.md"
      artefato_sucessor: "04A-MODELO-CONCEITUAL.md e 04B-MODELO-LOGICO.md"
      motivo_governanca: "Separação formal entre projeção conceitual e projeção lógica homologadas pelo Steward em 2026-08-07."

    - artefato_obsoleto: "public.DB_PRESENCA_FATUAL (tabela/aba transitória)"
      artefato_sucessor: "public.factual_presences / DB_PRESENCA"
      motivo_governanca: "Implementação da decisão DEC-DATA-045 e homologação da SSOT canônica de presença factual em 2026-08-14."

    - artefato_obsoleto: "Artigo 25º do Regulamento FHERJ armazenado no acervo"
      artefato_sucessor: "Tabela Operacional FHERJ 2026 (SGATE-0023)"
      motivo_governanca: "O Art. 25º armazenado foi classificado como STALE_FOR_SCORING, prevalecendo a publicação operacional oficial FHERJ 2026 para as posições de 1 a 7."

  propostas_historicas:
    - artefato: "05-schema-postgresql.sql"
      status_enquadramento: "Proposta histórica DDL pendente de reconciliação de atributos táticos."
    - artefato: "04C-DICIONARIO-DE-DADOS.md"
      status_enquadramento: "Proposta histórica de mapeamento físico pendente de inclusão exaustiva de componentes de scout."
    - artefato: "06-migrations-rollback.sql.md"
      status_enquadramento: "Proposta histórica de script de migração versionada (versão 20261013000001); a implantação física do pipeline de migração está estritamente sujeita ao mecanismo de Stop Gate até a aprovação formal da reconciliação do schema tático."
    - artefato: "07-matriz-rbac-e-politicas-rls"
      status_enquadramento: "Proposta histórica de políticas RLS sujeita à revisão conforme os escopos de visibilidade dos dados observacionais."

evidence_refs:
  - id: "EV-001"
    descricao: "Critérios de execução e pontuação de Spin Shots (rotação de 360 graus)."
    fonte_id: "IHF-RULES-2PT"
    localizador_preciso: "Slides 11 a 35 (Seção 04 — Spin Shots)"
    fato_tatico: "Para concessão de 2 pontos, o atleta deve realizar rotação completa do corpo no ar. Deficiências técnicas ou rotações incompletas resultam em gol de apenas 1 ponto."

  - id: "EV-002"
    descricao: "Critérios de execução de In-flight Shots (ponte aérea)."
    fonte_id: "IHF-RULES-2PT"
    localizador_preciso: "Slides 36 a 43 (Seção 05 — In-flight)"
    fato_tatico: "Gols de 2 pontos exigem controle da bola e arremesso durante a suspensão. Tapas ou empurrões na bola sem controle concedem apenas 1 ponto."

  - id: "EV-003"
    descricao: "Valoração de gols marcados por Goleira, Especialista e Tiro de 6 Metros."
    fonte_id: "IHF-RULES-2PT"
    localizador_preciso: "Slides 44 a 47 (6-metre throw) e Slides 48 a 51 (Scoring by Goalkeeper/Specialist)"
    fato_tatico: "Todos os gols convertidos a partir de tiro de 6m e todas as finalizações efetuadas por goleira ou especialista valem obrigatoriamente 2 pontos."

  - id: "EV-004"
    descricao: "Diretrizes para marcação de Tiro de 6 Metros e Punições Disciplinares."
    fonte_id: "IHF-RULES-6M"
    localizador_preciso: "Slides 3 a 6 (Clear Chance of Scoring) e Slides 10 a 16 (Criteria & Punishments)"
    fato_tatico: "O tiro de 6m deve ser assinalado na destruição de clara chance de gol em qualquer local da quadra. Faltas diretas contra o corpo sofrem punições disciplinares adequadas."

  - id: "EV-005"
    descricao: "Estrutura do Scout Observacional na Camada Física."
    fonte_id: "05"
    localizador_preciso: "Seção 7 (Tabelas possessions, bous, tactical_events, finalizations, goalkeeper_actions)"
    fato_tatico: "O modelo DDL 05-schema-postgresql.sql estabelece uma cadeia relacional estrita para a progressão dos eventos observacionais do scout: possessions (1:N) -> bous (1:N) -> tactical_events (1:1) -> finalizations (1:1) -> goalkeeper_actions."

  - id: "EV-006"
    descricao: "Mapeamento de Sistemas Defensivos e Posições Táticas."
    fonte_id:
      - "ARQ-001"
      - "CEPRAEA-DB"
    localizador_preciso: "ARQ-001 (04A-MODELO-CONCEITUAL.md, Seção 3.C) e CEPRAEA DATABASE (Tabelas DB_SISTEMAS_POSICOES e DB_ATLETA_POSICOES_TATICAS)"
    fato_tatico: "Define a estrutura tática por atribuições de função (ATAQUE, DEFESA), sistemas (ATAQUE→3X1|4X0; DEFESA→3X0|2X1) e posições táticas específicas em slots mapeados (Base, Solta, Cobertura, Avançada; Lateral Esquerda/Direita, Central, Pivô, Central Esquerda/Direita)."

  - id: "EV-007"
    descricao: "Fatores Contextuais e Tomada de Decisão no Ataque Posicionado."
    fonte_id: "LIT-001"
    localizador_preciso: "Frontiers in Psychology, Vol. 10, Art. 1386 (Junho 2019)"
    fato_tatico: "Estudo científico observacional fundamentando os fatores contextuais e a tomada de decisão no comportamento de finalização do ataque posicionado no handebol de praia."

  - id: "EV-008"
    descricao: "Análise Observacional das Ações Defensivas da Goleira."
    fonte_id: "LIT-002"
    localizador_preciso: "Cuadernos de Psicología del Deporte, Vol. 19, Nº 3, p. 155 (Setembro 2019)"
    fato_tatico: "Análise técnica observacional das intervenções e do comportamento defensivo da goleira de handebol de praia."

  - id: "EV-009"
    descricao: "Métricas Temporais e Eficiência de Defesa da Goleira."
    fonte_id: "LIT-003"
    localizador_preciso: "Tempos de defesa do goleiro de handebol de praia, p. 7"
    fato_tatico: "Pesquisa técnica fundamentando as métricas temporais de reação e a eficiência defensiva nas ações da goleira."

governanca_e_conflitos:
  precedencias_demonstraveis:
    - ordem: 1
      escopo: "Interpretação do Fato Esportivo em Quadra"
      autoridade_precedente: "Diretrizes e Regras Oficiais da IHF (IHF Online Education Weeks / Regras de Beach Handball)"
      regra: "Prevalece de forma absoluta sobre qualquer modelo de dados interno para definir a natureza do fato tático, pontuação do gol, faltas e sanções."

    - ordem: 2
      escopo: "Regulamento Competitivo Local e Tabela de Pontuação"
      autoridade_precedente: "Publicações Operacionais Oficiais da FHERJ / CBHb"
      regra: "Prevalece sobre documentos de acervo histórico para homologação de classificações, colocações de etapa e atribuição de pontos no circuito corrente."

    - ordem: 3
      escopo: "Governança Semântica e Arquitetura de Dados Interna"
      autoridade_precedente: "Decisões do Steward (DEC-DATA-XXX), Stop Gates (SGATE-XXX) e DB_CONFIG"
      regra: "Prevalece sobre propostas DDL e dicionários de dados legados no tocante à estrutura do banco, controle de presença e lineage de dados."

  conflitos_nao_resolvidos:
    - conflito_id: "CONF-001"
      descricao: "Divergência entre a tabela de pontuação do Artigo 25º do Regulamento FHERJ armazenado e a tabela praticada na publicação operacional de 2026."
      status: "STALE_FOR_SCORING"
      impacto: "A pontuação FHERJ 2026 para as posições 1..7 foi validada pelo SGATE-0023 em {16, 13, 11, 10, 9, 8, 7}. Posições 8 ou superiores permanecem como NOT_VERIFIED_BY_CURRENT_OPERATIONAL_PUBLICATION, devendo retornar INDETERMINATE quando requisitadas."

  pendencias_rastreaveis:
    - pendencia_id: "PEND-001"
      descricao: "Ausência de hashes criptográficos SHA-256 e timestamps exatos de homologação nos artefatos DDL (05) e apresentações normativas PDF."
      impacto: "A validação de imutabilidade estrita dos arquivos físicos exige o registro manual de hash: null e datas com o valor null no inventário até nova auditoria de segurança."

    - pendencia_id: "PEND-002"
      descricao: "Inexistência de especificação para vinculação do timecode de vídeo ao acervo de mídia física no DDL 05."
      impacto: "Apesar de a tabela public.possessions prever start_timecode e end_timecode, a proveniência detalhada do arquivo de vídeo (hash da mídia, url do repositório) necessita ser incorporada como metadado de rastreabilidade."