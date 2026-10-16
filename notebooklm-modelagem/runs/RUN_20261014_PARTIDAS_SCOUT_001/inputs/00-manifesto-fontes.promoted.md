# Fontes YAML consolidadas

## Arquivo: `notebooklm-modelagem/runs/RUN_20261014_PARTIDAS_SCOUT_001/artifacts/00-manifesto-fontes.candidate.yaml`

```yaml
schema_version: "1.1"
document:
  id: "SOURCE_MANIFEST"
  artifact_kind: "SOURCE_MANIFEST"
  title: "Manifesto de fontes"
  version: "0.1.0"
  status: "PROPOSTO"
  run_id: "RUN_20261014_PARTIDAS_SCOUT_001"
  domain_id: "PARTIDAS_SCOUT_ANALISE_TATICA"
  notebook_id: "93446a17-55bf-4cd8-b9f9-18c52c8f4c1d"
  generated_at: null
  supersedes: null
  input_artifacts: []
scope:
  included:
    - "Partida, sets, segmentos, shoot-out, placar, pontuação e finalizações."
    - "Tiro de seis metros, punições, posses, fases ofensivas e sistemas defensivos."
    - "Ações da goleira, zonas, resultado, scout, protocolo, revisão, confiabilidade, vídeo, trecho e timecode."
    - "Modelos e SQL existentes somente como propostas históricas a reconciliar."
  excluded:
    - "Carga e planejamento de treinamento."
    - "Saúde, prontuário ou avaliação médica."
    - "Gestão financeira ou administrativa."
    - "Mídia institucional e acervo fotográfico."
    - "Infraestrutura fora do necessário para classificar os artefatos históricos."
  reference_date: "2026-10-14"
sources:
  - id: "SRC_CTRL_FLUXO_MODELAGEM_ACF6AFA2AAB0_C17B2843"
    canonical_title: "CTRL — Fluxo_Modelagem — acf6afa2aab0"
    notebook_source_id: "965f27f8-7475-43d0-a5b3-0fc985debf80"
    drive_file_id: null
    source_type: "OTHER"
    publisher: null
    source_revision: null
    publication_date: null
    retrieved_at: null
    content_sha256: "acf6afa2aab04d625d4d01d989d139c801b87358750e72f9f10c76f8d1c151fa"
    language: null
    authority_class: "DECISAO_HUMANA"
    lifecycle_status: "EM_VERIFICACAO"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations: []
  - id: "SRC_CTRL_INSTRUCOES_NOTEBOOK_A6EDE74B1BAA_63B2FA9E"
    canonical_title: "CTRL — Instrucoes_Notebook — a6ede74b1baa"
    notebook_source_id: "991b26f0-0d26-4cfe-935d-81b92dee7c76"
    drive_file_id: null
    source_type: "OTHER"
    publisher: null
    source_revision: null
    publication_date: null
    retrieved_at: null
    content_sha256: "a6ede74b1baabc872bde3c5c800a0ef91d065de377633a33d5d57947b2c2c94f"
    language: null
    authority_class: "DECISAO_HUMANA"
    lifecycle_status: "EM_VERIFICACAO"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations: []
  - id: "SRC_CTRL_CONTRATO_ARTEFATOS_DB2D64DA9680_5CDE0B19"
    canonical_title: "CTRL — Contrato_Artefatos — db2d64da9680"
    notebook_source_id: "cf663fd6-cb2a-4c03-82a0-a31023023f1c"
    drive_file_id: null
    source_type: "OTHER"
    publisher: null
    source_revision: null
    publication_date: null
    retrieved_at: null
    content_sha256: "db2d64da96802b51a7ed3d231a60f0f4efc20f32762902aecbdd1ebb8a4d163d"
    language: null
    authority_class: "DECISAO_HUMANA"
    lifecycle_status: "EM_VERIFICACAO"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations: []
  - id: "SRC_00_MANIFESTO_FONTES_TEMPLATE_8F26F1D8"
    canonical_title: "00-manifesto-fontes.template"
    notebook_source_id: "718459c6-32df-46cc-bfb8-15b981a2b01e"
    drive_file_id: null
    source_type: "OTHER"
    publisher: null
    source_revision: null
    publication_date: null
    retrieved_at: null
    content_sha256: null
    language: null
    authority_class: "DECISAO_HUMANA"
    lifecycle_status: "EM_VERIFICACAO"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations: []
  - id: "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    canonical_title: "IX. Rules of the Game for Beach Handball"
    notebook_source_id: "d7ebb4e2-04f1-43f8-b2a0-152b98e5a226"
    drive_file_id: null
    source_type: "PDF"
    publisher: "International Handball Federation (IHF)"
    source_revision: "Edition: 1 March 2026"
    publication_date: "2026-03-01"
    retrieved_at: null
    content_sha256: null
    language: "en"
    authority_class: "AUTORITATIVA"
    lifecycle_status: "VIGENTE"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "A extração de texto em formato plano não preserva a cor de destaque em amarelo mencionada na nota da página 1, impossibilitando\
        \ a identificação puramente textual das disposições que entram em vigor em 1º de julho de 2026."
      - "Trata-se do texto oficial em língua inglesa que requer reconciliação com eventuais traduções (ex.: versão em português\
        \ de 29 de maio de 2026) e regulamentos de federações estaduais/nacionais (ex.: CBHb e Campeonato Carioca)."
  - id: "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    canonical_title: "Regras de Jogo - Handebol de Praia (IHF 2026)"
    notebook_source_id: "236e788c-9c85-4133-93c8-4650a26e867a"
    drive_file_id: null
    source_type: "PDF"
    publisher: "International Handball Federation (IHF) / Tradução: Prof. Luiz Filipe Galvão da Silva Caldas"
    source_revision: "Edição de 01 de março de 2026 (Tradução de 29 de maio de 2026)"
    publication_date: "2026-05-29"
    retrieved_at: null
    content_sha256: null
    language: "pt-BR"
    authority_class: "SUPORTE"
    lifecycle_status: "COMPLEMENTAR"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Documento em língua portuguesa decorrente de tradução; em caso de divergência conceitual ou de redação, prevalece\
        \ o texto oficial em língua inglesa da IHF."
      - "Contém adaptações gráficas e de diagramação da versão em português."
  - id: "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    canonical_title: "New rules for beach handball and wheelchair handball to be observed from 1 April and 1 July"
    notebook_source_id: "0d48291e-32ab-449e-8f86-ea43244c921c"
    drive_file_id: null
    source_type: "MARKDOWN"
    publisher: "International Handball Federation (IHF)"
    source_revision: null
    publication_date: "2026-03-13"
    retrieved_at: null
    content_sha256: null
    language: "en"
    authority_class: "AUTORITATIVA"
    lifecycle_status: "EM_VERIFICACAO"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Documento do tipo comunicado/notícia resumida que apresenta os destaques e esclarecimentos das alterações, sem transcrever\
        \ a íntegra codificada de todas as regras do jogo."
      - "Combina no mesmo texto informativo atualizações do Handebol de Praia e do Handebol em Cadeira de Rodas (4x4 e 6x6)."
  - id: "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    canonical_title: "Esclarecimentos à Regra de Jogo - Handebol de Praia"
    notebook_source_id: "9c553f24-6f99-4a21-b63c-9cbfda6552c1"
    drive_file_id: null
    source_type: "PDF"
    publisher: "Federação de Handebol do Estado do Rio de Janeiro (FHERJ)"
    source_revision: null
    publication_date: "2025-04-23"
    retrieved_at: null
    content_sha256: null
    language: "pt-BR"
    authority_class: "AUTORITATIVA"
    lifecycle_status: "EM_VERIFICACAO"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Aplica-se diretamente às competições do Circuito Estadual da FHERJ."
      - "Foca em tópicos específicos de esclarecimento e uniformização, não constituindo a totalidade do livro de regras da\
        \ modalidade."
  - id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    canonical_title: "Regulamento Geral — Circuito Estadual de Handebol de Praia 2026"
    notebook_source_id: "e593c4e6-903a-4169-a1c5-7f551bbe5b9d"
    drive_file_id: null
    source_type: "PDF"
    publisher: "Federação de Handebol do Estado do Rio de Janeiro (FHERJ)"
    source_revision: "Rev.01"
    publication_date: "2026-03-01"
    retrieved_at: null
    content_sha256: null
    language: "pt-BR"
    authority_class: "AUTORITATIVA"
    lifecycle_status: "EM_VERIFICACAO"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Datas, locais e tabelas específicas de jogos não estão detalhadas no texto, dependendo do Calendário Oficial e do\
        \ Congresso Técnico de 2026."
      - "A desobrigação de registro no CREF para dirigentes e técnicos é restrita ao Circuito Estadual da FHERJ, não sendo\
        \ extensiva ao Circuito Brasileiro ou outras praças."
      - "Em caso de divergência formal quanto às regras do jogo, a Regra Oficial de Handebol de Praia da IHF/CBHb prevalece\
        \ sobre o presente regulamento (conforme Art. 39, § 2º)."
  - id: "SRC_REGULAMENTO_CBHB_2026_PDF_818BCC8B"
    canonical_title: "CIRCUITO BRASILEIRO ADULTO DE HANDEBOL DE PRAIA - REGULAMENTO 2026"
    notebook_source_id: "bb8b9ba4-cd24-452a-aa2b-2a3a3854e0a0"
    drive_file_id: null
    source_type: "PDF"
    publisher: "Confederação Brasileira de Handebol - CBHb"
    source_revision: null
    publication_date: "2026"
    retrieved_at: null
    content_sha256: null
    language: "pt-BR"
    authority_class: "AUTORITATIVA"
    lifecycle_status: "EM_VERIFICACAO"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Contém anotações editoriais internas pendentes de edição final (ex.: solicitações de inserção de links e envio para\
        \ avaliação jurídica)."
      - "Documento focado na organização e regulamentação da competição nacional, remetendo casos omissos às regras gerais\
        \ da CBHb e da IHF."
  - id: "SRC_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5"
    canonical_title: "2-point Goals, Spin and In-flight"
    notebook_source_id: "f68c1687-7153-4283-a6a0-5e33b814fe00"
    drive_file_id: null
    source_type: "PDF"
    publisher: "IHF - International Handball Federation (IHF Virtual Academy)"
    source_revision: null
    publication_date: "2023"
    retrieved_at: null
    content_sha256: null
    language: "en"
    authority_class: "SUPORTE"
    lifecycle_status: "COMPLEMENTAR"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Apresentação em slides com tópicos sintéticos e capturas visuais de partidas (ex.: Campeonato Mundial de Kazan 2018),\
        \ sem apresentar o texto regulamentar completo da IHF."
      - "Foco temático restrito aos critérios de validação e valoração de arremessos espetaculares e situações especiais de\
        \ pontuação, sem cobrir todo o regulamento do jogo."
  - id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    canonical_title: "6-Metre Throw + Punishment"
    notebook_source_id: "049d2bf2-ac90-44f8-951a-ae9a32c0cc64"
    drive_file_id: null
    source_type: "PDF"
    publisher: "IHF Virtual Academy / International Handball Federation"
    source_revision: null
    publication_date: "2023"
    retrieved_at: null
    content_sha256: null
    language: "en"
    authority_class: "SUPORTE"
    lifecycle_status: "COMPLEMENTAR"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Trata-se de uma apresentação de slides sintética orientada para treinamento e reciclagem de arbitragem, sem o texto\
        \ regulamentar integral de um livro oficial de regras."
      - "Depende do contexto visual de clipes de vídeo que foram originalmente exibidos durante a palestra explicativa (evidenciados\
        \ pelos placares, tempos e times do circuito internacional nos slides)."
  - id: "SRC_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2"
    canonical_title: "Protocolo de Scout — Beach Handball"
    notebook_source_id: "a44eece7-56e3-407c-9348-23b35ab0efa4"
    drive_file_id: null
    source_type: "OTHER"
    publisher: null
    source_revision: "v0.9.2"
    publication_date: "2026-08-26"
    retrieved_at: null
    content_sha256: null
    language: "pt-BR"
    authority_class: "OPERACIONAL_PRIMARIA"
    lifecycle_status: "EM_VERIFICACAO"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Documento composto por guias vigentes e guias históricas/substituídas preservadas para rastreabilidade de decisões\
        \ passadas."
      - "Versão v0.9.2 congelada apenas como candidata ao piloto, sem validação empírica concluída ou autorização de uso em\
        \ produção."
      - "Orientado a vídeo de broadcast e codificação humana, não substituindo medições de carga física ou cinemática obtidas\
        \ por sensores (LPS/IMU)."
      - "Depende do cumprimento do procedimento de qualificação do observador (CON-006) e da confirmação de autorização da\
        \ mídia P0 para início da coleta."
  - id: "SRC_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC"
    canonical_title: "DEVELOPMENT OF AN INSTRUMENT FOR THE OBSERVATION OF COLLECTIVE TACTICAL PROCEDURES OF POSITIONAL ATTACK\
      \ IN BEACH HANDBALL"
    notebook_source_id: "162256e7-41bf-40ac-b77f-7b892250771f"
    drive_file_id: null
    source_type: "OTHER"
    publisher: "[suspicious link removed]: Revista de Ciencias del Deporte - Journal of Sport Science (Universidad de Extremadura\
      \ & Federación Extremeña de Balonmano)"
    source_revision: "Vol. 21, N° 4, pp. 495-514, DOI: 10.17398/1885-7019.21.495"
    publication_date: "2025-12-30"
    retrieved_at: null
    content_sha256: null
    language: "en"
    authority_class: "SUPORTE"
    lifecycle_status: "COMPLEMENTAR"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "A amostragem de validação de campo restringe-se a duas partidas de alto nível (as finais masculina e feminina do\
        \ Campeonato Mundial de Handebol de Praia de 2022 em Heraklion, Grécia)."
      - "O escopo de observação foca no ataque posicional organizado (BOU - Basic Attack Unit) e seus procedimentos táticos\
        \ coletivos, não cobrindo o jogo de transição, contra-ataque ou aspectos administrativos e físicos."
  - id: "SRC_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56"
    canonical_title: "Contextual Factors and Decision-Making in the Behavior of Finalization in the Positional Attack in Beach\
      \ Handball: Differences by Gender Through Polar Coordinates Analysis"
    notebook_source_id: "605ea05f-b931-405d-984f-4773065aa6c8"
    drive_file_id: null
    source_type: "OTHER"
    publisher: "Frontiers Media S.A."
    source_revision: null
    publication_date: "2019-06-13"
    retrieved_at: null
    content_sha256: null
    language: "en"
    authority_class: "SUPORTE"
    lifecycle_status: "COMPLEMENTAR"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Amostra limitada a 12 partidas (24 sessões de observação) da Copa de Espanha Sênior de 2016 com atletas exclusivamente\
        \ espanhóis."
      - "A análise baseia-se em comportamentos motores perceptíveis registrados por observação sistemática, sem mensuração\
        \ direta de variáveis cognitivas internas."
      - "Escassez de literatura científica anterior focada especificamente em tomada de decisão e coordenadas polares no handebol\
        \ de praia para comparação direta dos achados."
  - id: "SRC_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2"
    canonical_title: "O jogo ofensivo do handebol de areia: estrutura e aspectos técnico-táticos do ataque posicionado [1]."
    notebook_source_id: "74cb7983-decc-42de-86eb-f691d8e00d53"
    drive_file_id: null
    source_type: "OTHER"
    publisher: "Servicio de Publicaciones de la Universidad de Murcia / Cuadernos de Psicología del Deporte [1]."
    source_revision: "Vol. 18, N. 3 [1]."
    publication_date: "2018-10-10 [1]."
    retrieved_at: null
    content_sha256: null
    language: "pt-BR [1, 2]."
    authority_class: "SUPORTE"
    lifecycle_status: "COMPLEMENTAR"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Entrevistou cinco treinadores de equipes que disputaram o circuito paulista de handebol de areia de 2015 [2, 3]."
      - "A amostragem é restrita ao estado de São Paulo, o que impede a generalização direta dos resultados para outros contextos\
        \ [4]."
  - id: "SRC_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A"
    canonical_title: "Latest Trends in Defence"
    notebook_source_id: "d8076ca2-b651-48af-be4e-b14dd524c377"
    drive_file_id: null
    source_type: "PDF"
    publisher: "International Handball Federation (IHF) / IHF Virtual Academy"
    source_revision: null
    publication_date: "2023"
    retrieved_at: null
    content_sha256: null
    language: "en"
    authority_class: "SUPORTE"
    lifecycle_status: "COMPLEMENTAR"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Documento composto por slides sintéticos de apresentação, sem detalhamento textual extenso para todos os tópicos\
        \ abordados."
      - "Conteúdo audiovisual de partidas de alto nível citado nos slides (ex.: Dinamarca vs Brasil, Dinamarca vs Espanha\
        \ EURO 2021) não está transcrito na fonte documental."
  - id: "SRC_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94"
    canonical_title: "The structuring of the defensive phase of beach handball"
    notebook_source_id: "de6241bc-cad8-42a5-80db-015ef2c1a780"
    drive_file_id: null
    source_type: "PDF"
    publisher: "Motriz: Journal of Physical Education (UNESP)"
    source_revision: null
    publication_date: "2021"
    retrieved_at: null
    content_sha256: null
    language: "en"
    authority_class: "SUPORTE"
    lifecycle_status: "COMPLEMENTAR"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Amostra qualitativa restrita a cinco treinadores de equipes adultas do Campeonato Paulista de Handebol de Praia."
      - "Coleta de dados fundamentada em entrevistas e percepções subjetivas dos treinadores (Discurso do Sujeito Coletivo),\
        \ sem observação quantitativa direta de partidas."
      - "Refere-se ao livro de regras da IHF de 2014 (referência 11 do artigo), devendo suas menções de regras ser verificadas\
        \ frente a regulamentos mais recentes."
  - id: "SRC_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E"
    canonical_title: "Estudio de las acciones del portero en balonmano playa a través del análisis de coordenadas polares:\
      \ diferencias por género"
    notebook_source_id: "a3068def-bef6-49bd-b063-c8593116298f"
    drive_file_id: null
    source_type: "PDF"
    publisher: "Servicio de Publicaciones de la Universidad de Murcia / Sociedad Iberoamericana de Psicología del Deporte\
      \ (Cuadernos de Psicología del Deporte)"
    source_revision: null
    publication_date: "2019-09-08"
    retrieved_at: null
    content_sha256: null
    language: "es"
    authority_class: "SUPORTE"
    lifecycle_status: "COMPLEMENTAR"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Amostra observacional limitada a 12 partidas (6 masculinas e 6 femininas) entre 3 equipes selecionadas na Copa de\
        \ España sénior de 2016."
      - "Resultados restritos às condutas focais de finalização e às ações do goleiro no ataque posicional."
      - "Análise baseada em ambiente competitivo específico do circuito espanhol de clubes de 2016."
  - id: "SRC_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0"
    canonical_title: "Tempos de defesa do goleiro de handebol de praia"
    notebook_source_id: "9b742f2e-0d21-4fb1-bca9-33411d6c6ec2"
    drive_file_id: null
    source_type: "PDF"
    publisher: "Research, Society and Development"
    source_revision: null
    publication_date: "2022-11-06"
    retrieved_at: null
    content_sha256: null
    language: "pt-BR"
    authority_class: "SUPORTE"
    lifecycle_status: "COMPLEMENTAR"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Estudo de revisão de escopo sem validação empírica de campo ou dados de eficácia observacional em competição."
      - "Não constitui norma ou regulamento oficial emitido por órgãos regentes da modalidade (IHF ou CBHb)."
  - id: "SRC_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533"
    canonical_title: "UNDERSTANDING PSYCHOLOGICAL PRESSURE IN BEACH HANDBALL SHOOTOUTS"
    notebook_source_id: "36d92b57-69c1-4563-a2a4-71a7bd357dc7"
    drive_file_id: null
    source_type: "PDF"
    publisher: "EHF Beach Handball"
    source_revision: null
    publication_date: null
    retrieved_at: null
    content_sha256: null
    language: "en"
    authority_class: "SUPORTE"
    lifecycle_status: "COMPLEMENTAR"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Documento não apresenta data explícita de publicação nem número de revisão no cabeçalho ou folha de rosto."
      - "Aborda exclusivamente a dimensão psicológica e de treinamento mental do shoot-out, sem definir regras formais de\
        \ arbitragem ou normas disciplinares de jogo."
  - id: "SRC_CEPRAEA_DATABASE_CCB2A718"
    canonical_title: "CEPRAEA DATABASE"
    notebook_source_id: "569f2d66-ba38-41fc-aa84-d854bb6d0df9"
    drive_file_id: null
    source_type: "OTHER"
    publisher: "CEPRAEA"
    source_revision: "2026-09-27T21:10:00-03:00"
    publication_date: "2026-09-27"
    retrieved_at: null
    content_sha256: null
    language: "pt-BR"
    authority_class: "OPERACIONAL_PRIMARIA"
    lifecycle_status: "EM_VERIFICACAO"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Exige portão de confirmação humana autorizada do treinador para homologação de presenças factuais e convocações."
      - "Apresenta pendências de dados de parciais de sets em jogos específicos (ex.: 4ª Etapa Estadual) e omissão de placar\
        \ de shoot-out no boletim oficial da Etapa Final (J71)."
      - "Contém registros e abas históricas que foram supersedidos ou migrados (ex.: DB_PRESENCA_FATUAL e DB_PRESENCA_LEGADO),\
        \ necessitando de controle de vigência."
  - id: "SRC_04A_MODELO_CONCEITUAL_MD_D7C900D7"
    canonical_title: "04A — Modelo Conceitual — CEPRAEA Beach Pro"
    notebook_source_id: "3bb0c332-947d-494f-a6fa-85493b579464"
    drive_file_id: null
    source_type: "MARKDOWN"
    publisher: "Davi Sermenho (davisermenho@handballtrack.app)"
    source_revision: "v1.0.0"
    publication_date: "2026-08-07"
    retrieved_at: null
    content_sha256: null
    language: "pt-BR"
    authority_class: "HISTORICA"
    lifecycle_status: "HISTORICA"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Trata-se de uma especificação conceitual e de arquitetura técnica de dados para o software CEPRAEA Beach Pro, não\
        \ constituindo um regulamento esportivo oficial de federação."
      - "Declarações relativas a regulamentos e pontuações externas (ex.: Circuito FHERJ 2026, SGATE-0023) refletem mapeamentos\
        \ de regras de negócio para implementação no banco de dados e requerem reconciliação contínua com os documentos oficiais\
        \ emitidos pelas entidades esportivas."
  - id: "SRC_04B_MODELO_LOGICO_MD_FFCFA1B3"
    canonical_title: "04B — MODELO LÓGICO — CEPRAEA BEACH PRO"
    notebook_source_id: "aef04d7f-4e75-4597-8f96-acc3b87f945d"
    drive_file_id: null
    source_type: "MARKDOWN"
    publisher: "Davi Sermenho"
    source_revision: "v1.0.0"
    publication_date: "2026-10-12"
    retrieved_at: null
    content_sha256: null
    language: "pt-BR"
    authority_class: "HISTORICA"
    lifecycle_status: "HISTORICA"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Especifica apenas tipos abstratos e restrições lógicas, estando estritamente bloqueado contra conversão para DDL\
        \ ou tipos físicos PostgreSQL (STOP GATE físico)."
      - "Bloqueia a materialização e persistência dos objetos SESSION_SEGMENT e PLANNED_TRAINING_LOAD nesta versão."
      - "Trata-se de proposta histórica de modelagem a reconciliar no âmbito da execução corrente."
  - id: "SRC_04C_DICIONARIO_DE_DADOS_MD_6B0D9716"
    canonical_title: "04C — DICIONÁRIO DE DADOS CANÔNICO — CEPRAEA BEACH HANDBALL PRO"
    notebook_source_id: "fef688f6-d141-475d-87c0-abbeaffe46fb"
    drive_file_id: null
    source_type: "MARKDOWN"
    publisher: "Davi Sermenho (ROLE-CEPRAEA-DATA-GOVERNANCE-STEWARD)"
    source_revision: "v1.0.0"
    publication_date: null
    retrieved_at: null
    content_sha256: null
    language: "pt-BR"
    authority_class: "HISTORICA"
    lifecycle_status: "HISTORICA"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Ausência de data de publicação formal no cabeçalho do documento."
      - "Trata-se de documentação técnica de banco de dados do sistema interno, não constituindo regra oficial da modalidade\
        \ esportiva (IHF/CBHb) nem regulamento de competição."
      - "O estado de aprovação declarada no cabeçalho ('APPROVED') é uma alegação histórica interna e requer homologação no\
        \ manifesto de reconciliação pelo operador."
  - id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    canonical_title: "CATÁLOGO DE REGRAS DE NEGÓCIO E INVARIANTES — CEPRAEA BEACH HANDBALL PRO"
    notebook_source_id: "475ce51f-f4bd-44ca-8194-31d42ea308e8"
    drive_file_id: null
    source_type: "MARKDOWN"
    publisher: "Davi Sermenho (ROLE-CEPRAEA-DATA-GOVERNANCE-STEWARD)"
    source_revision: "v1.0.0"
    publication_date: null
    retrieved_at: null
    content_sha256: null
    language: "pt-BR"
    authority_class: "HISTORICA"
    lifecycle_status: "HISTORICA"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Trata-se de um catálogo interno de regras de negócio e restrições de arquitetura de dados; não substitui o texto\
        \ integral oficial das regras de jogo da IHF ou dos regulamentos da CBHb e FHERJ."
      - "Não apresenta data explícita de publicação ou emissão no cabeçalho do documento."
      - "A regra de pontuação de etapa da FHERJ (SGATE-0023 / DEC-DATA-042) é parcial, cobrindo apenas as posições 1ª a 7ª,\
        \ retornando INDETERMINATE para a 8ª posição em diante e sinalizando o Artigo 25º como STALE_FOR_SCORING."
  - id: "SRC_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB"
    canonical_title: "MATRIZ CONSOLIDADA DE RELAÇÕES E CARDINALIDADES — CEPRAEA BEACH HANDBALL PRO"
    notebook_source_id: "2cea376b-08be-4969-b2e4-d66189ca0935"
    drive_file_id: null
    source_type: "MARKDOWN"
    publisher: "Davi Sermenho (ROLE-CEPRAEA-DATA-GOVERNANCE-STEWARD)"
    source_revision: "v1.0.0"
    publication_date: null
    retrieved_at: null
    content_sha256: null
    language: "pt-BR"
    authority_class: "HISTORICA"
    lifecycle_status: "HISTORICA"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Trata-se de uma especificação técnica de modelagem de banco de dados e não de uma regra oficial do esporte emitida\
        \ pela IHF nem de um regulamento de competição."
      - "Não apresenta data explícita de publicação ou emissão no texto do documento."
      - "Aprovações ('APPROVED') e alegações de alinhamento com 04A e 04B referem-se ao histórico interno do projeto, necessitando\
        \ de reconciliação e validação formal no manifesto de governança do ambiente de execução."
  - id: "SRC_05_SCHEMA_POSTGRESQL_SQL_B7F68C42"
    canonical_title: "05 — Modelo Físico PostgreSQL / Supabase — CEPRAEA Beach Handball Pro"
    notebook_source_id: "c30b6966-654c-4682-84d5-41b0d15febb0"
    drive_file_id: null
    source_type: "SQL"
    publisher: "CEPRAEA Beach Handball Pro"
    source_revision: null
    publication_date: null
    retrieved_at: null
    content_sha256: null
    language: "pt-BR"
    authority_class: "HISTORICA"
    lifecycle_status: "HISTORICA"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "O cabeçalho do arquivo omite a data de publicação e o identificador explícito de revisão."
      - "A indicação 'Estado: APPROVED' constante no cabeçalho representa uma alegação histórica e não reflete status de aprovação\
        \ na presente execução."
      - "Inconsistência lógica identificada na fórmula SQL calculada para a coluna gerada `sets_won_opponent` na tabela `public.matches`."
  - id: "SRC_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E"
    canonical_title: "06 — MIGRATIONS VERSIONADAS E ROLLBACK — CEPRAEA BEACH HANDBALL PRO"
    notebook_source_id: "e9e4272e-d302-4ce3-bf80-b1c9bdc84060"
    drive_file_id: null
    source_type: "SQL"
    publisher: "CEPRAEA Beach Handball Pro"
    source_revision: "20261013000001"
    publication_date: null
    retrieved_at: null
    content_sha256: null
    language: "pt-BR"
    authority_class: "HISTORICA"
    lifecycle_status: "HISTORICA"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "O bloco UP MIGRATION 001 restringe-se à criação da tabela public.schema_migrations e à inserção da versão '20261013000001'."
      - "Não inclui as instruções DDL de criação para as 20 tabelas e 9 ENUMs referenciados na seção de rollback."
      - "As instruções de rollback (DOWN MIGRATION 001) encontram-se inativas por estarem dentro de um bloco de comentário\
        \ SQL."
      - "Ausência de metadados formais de aprovação, autoria individual ou logs de execução em banco de dados no corpo do\
        \ arquivo."
  - id: "SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919"
    canonical_title: "07 — MATRIZ RBAC E POLÍTICAS RLS (SUPABASE) — CEPRAEA BEACH HANDBALL PRO"
    notebook_source_id: "49ceb0ca-9160-4d36-a8ac-b58470c73f80"
    drive_file_id: null
    source_type: "OTHER"
    publisher: "CEPRAEA"
    source_revision: null
    publication_date: null
    retrieved_at: null
    content_sha256: null
    language: "pt-BR"
    authority_class: "HISTORICA"
    lifecycle_status: "HISTORICA"
    notebook_status: "READY"
    valid_from: null
    valid_to: null
    supersedes_source_id: null
    duplicate_of_source_id: null
    supported_domain_ids:
      - "PARTIDAS_SCOUT_ANALISE_TATICA"
    limitations:
      - "Documento não inclui data de publicação, autor individual nem número de revisão formal."
      - "Declara políticas RLS específicas para apenas um subconjunto de tabelas (athletes, availability_declarations, factual_presences,\
        \ presence_proposals), omitindo a declaração explicita de políticas para outras tabelas habilitadas na Seção 1."
evidence_refs:
  - id: "EVID_IHF_RULES_2026_EN_001"
    source_id: "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    locator: "p. 1, Note"
    evidence_type: "REGRA"
    excerpt: "The provisions highlighted in yellow will come into force on 1 July 2026. The provisions related to the uniform\
      \ for female athletes will come into force on 1 January 2022."
    interpretation: "Estabelece o marco de vigência temporal das atualizações das regras da IHF, definindo que trechos específicos\
      \ entram em vigor em 1º de julho de 2026."
  - id: "EVID_IHF_RULES_2026_EN_002"
    source_id: "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    locator: "p. 8, Rule 2:4"
    evidence_type: "REGRA"
    excerpt: "The game consists of two periods, which are scored separately. Each period lasts 10 minutes (but see Rules 2:6,\
      \ 2:8 and 4:2). The intermission lasts 5 minutes."
    interpretation: "Define a estrutura temporal básica da partida: dois períodos independentes de 10 minutos com intervalo\
      \ de 5 minutos entre eles."
  - id: "EVID_IHF_RULES_2026_EN_003"
    source_id: "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    locator: "p. 8, Rule 2:6, 2:8"
    evidence_type: "REGRA"
    excerpt: "If the score is even at the end of a period, the 'Golden Goal' is used, (Rule 9:7)"
    interpretation: "Especifica o critério de desempate de períodos (Gol de Ouro) e o método para decidir a partida em caso\
      \ de empate em períodos (Shoot-out)."
  - id: "EVID_IHF_RULES_2026_EN_004"
    source_id: "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    locator: "p. 8, Rule 2:6, 2:8"
    evidence_type: "REGRA"
    excerpt: ". If each team wins a period, the result is a tie. As there must always be a winner, the 'Shoot-out' is used\
      \ (Rule 9)."
    interpretation: "Especifica o critério de desempate de períodos (Gol de Ouro) e o método para decidir a partida em caso\
      \ de empate em períodos (Shoot-out)."
  - id: "EVID_IHF_RULES_2026_EN_005"
    source_id: "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    locator: "p. 12, Rule 4:3"
    evidence_type: "REGRA"
    excerpt: "A maximum of 4 players per team (3 court players and 1 goalkeeper) may be on the playing court."
    interpretation: "Regula o limite de atletas em quadra por equipe durante o jogo: máximo de 4 jogadores (3 de linha e 1\
      \ goleiro/goleira)."
  - id: "EVID_IHF_RULES_2026_EN_006"
    source_id: "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    locator: "p. 22, Rule 9:2, 9:3, 9:6"
    evidence_type: "REGRA"
    excerpt: "Creative or spectacular goals are awarded with two points"
    interpretation: "Consolida as hipóteses de pontuação dobrada (2 pontos): gols criativos/espetaculares, tiros de 6 metros\
      \ e gols marcados pelo goleiro."
  - id: "EVID_IHF_RULES_2026_EN_007"
    source_id: "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    locator: "p. 22, Rule 9:2, 9:3, 9:6"
    evidence_type: "REGRA"
    excerpt: ". A goal scored by a 6-metre throw is awarded with two points"
    interpretation: "Consolida as hipóteses de pontuação dobrada (2 pontos): gols criativos/espetaculares, tiros de 6 metros\
      \ e gols marcados pelo goleiro."
  - id: "EVID_IHF_RULES_2026_EN_008"
    source_id: "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    locator: "p. 22, Rule 9:2, 9:3, 9:6"
    evidence_type: "REGRA"
    excerpt: ". Two points are awarded when a goal is scored by the goalkeeper."
    interpretation: "Consolida as hipóteses de pontuação dobrada (2 pontos): gols criativos/espetaculares, tiros de 6 metros\
      \ e gols marcados pelo goleiro."
  - id: "EVID_IHF_RULES_2026_EN_009"
    source_id: "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    locator: "p. 22-23, Rule 9:8"
    evidence_type: "REGRA"
    excerpt: "Five players who are eligible to play take throws alternating with the opposing team"
    interpretation: "Define a estrutura do Shoot-out como uma série de 5 cobranças alternadas para cada equipe por atletas\
      \ elegíveis."
  - id: "EVID_IHF_RULES_2026_EN_010"
    source_id: "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    locator: "p. 22-23, Rule 9:8"
    evidence_type: "REGRA"
    excerpt: ". The winner is the team that has scored more points after five throws."
    interpretation: "Define a estrutura do Shoot-out como uma série de 5 cobranças alternadas para cada equipe por atletas\
      \ elegíveis."
  - id: "EVID_IHF_RULES_2026_EN_011"
    source_id: "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    locator: "p. 27, Rule 14:1"
    evidence_type: "REGRA"
    excerpt: "A 6-metre throw is awarded when: a. A clear chance of scoring is destroyed anywhere on the court by a player\
      \ or a team official of the opposing team"
    interpretation: "Estipula a concessão de tiro de 6 metros quando uma oportunidade clara de gol for impedida ilicitamente\
      \ por adversário ou oficial."
  - id: "EVID_IHF_RULES_2026_EN_012"
    source_id: "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    locator: "p. 21, Rule 8:11a, 8:11b"
    evidence_type: "REGRA"
    excerpt: "If during the last 15 seconds of both periods and during 'Golden Goal' the ball is out of play, and a player\
      \ or team official prevents or delays the execution of a throw for the opponents"
    interpretation: "Regra especial do trecho final (últimos 15 segundos e Gol de Ouro) punindo a obstrução de reinício de\
      \ jogo com desqualificação direta e tiro de 6m."
  - id: "EVID_IHF_RULES_2026_EN_013"
    source_id: "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    locator: "p. 21, Rule 8:11a, 8:11b"
    evidence_type: "REGRA"
    excerpt: "the guilty player / official is to be disqualified and a 6-metre throw is to be granted to the opponents."
    interpretation: "Regra especial do trecho final (últimos 15 segundos e Gol de Ouro) punindo a obstrução de reinício de\
      \ jogo com desqualificação direta e tiro de 6m."
  - id: "EVID_IHF_RULES_2026_EN_014"
    source_id: "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    locator: "p. 47, Clarification 1"
    evidence_type: "REGRA"
    excerpt: "Also in the following scoring situation two points are awarded: A goal scored in 'in-flight' (Rule 9:2). Two\
      \ points are awarded only if the player who is in-flight controls the ball and shots on goal while in the air"
    interpretation: "Esclarece que o gol de in-flight vale 2 pontos desde que haja controle da bola e arremesso efetuados\
      \ no ar."
  - id: "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_001"
    source_id: "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    locator: "pág. 1, Seção IX.b"
    evidence_type: "FATO"
    excerpt: "IX. Regras de Jogo b) Handebol de Praia. Edição: 01 de março de 2026. Tradução: Prof. Luiz Filipe Galvão da\
      \ Silva Caldas, Árbitro Internacional (IHF), Delegado Técnico da Federação Internacional de Handebol (IHF)."
    interpretation: "Identificação formal da edição das regras da IHF de 01/03/2026 e da autoria da tradução em 29/05/2026."
  - id: "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_002"
    source_id: "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    locator: "pág. 4, Regra 1:1"
    evidence_type: "REGRA"
    excerpt: "A quadra de jogo (Diagrama N°1) é um retângulo de 27 metros de comprimento por 12 metros de largura, que consiste\
      \ em uma Área de Jogo e duas Áreas de Gol."
    interpretation: "Definição das dimensões oficiais da quadra de Handebol de Praia (27m x 12m)."
  - id: "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_003"
    source_id: "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    locator: "pág. 7, Regra 2:4"
    evidence_type: "REGRA"
    excerpt: "O jogo consiste em dois períodos, que são pontuados separadamente. Cada período dura 10 minutos"
    interpretation: "Estrutura temporal da partida em dois períodos independentes de 10 minutos."
  - id: "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_004"
    source_id: "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    locator: "pág. 7, Regra 2:4"
    evidence_type: "REGRA"
    excerpt: ". O intervalo dura 5 minutos."
    interpretation: "Estrutura temporal da partida em dois períodos independentes de 10 minutos."
  - id: "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_005"
    source_id: "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    locator: "pág. 7, Regra 2:6, 2:8"
    evidence_type: "REGRA"
    excerpt: "Se o placar estiver empatado no final de um período, o Gol de Ouro é usado"
    interpretation: "Regulamentação do Gol de Ouro para encerramento de períodos empatados e do Shoot-out para desempate da\
      \ partida."
  - id: "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_006"
    source_id: "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    locator: "pág. 7, Regra 2:6, 2:8"
    evidence_type: "REGRA"
    excerpt: ". Se cada equipe vencer um período, o resultado é um empate. Como deve haver sempre um vencedor, o 'Shoot out'\
      \ é usado."
    interpretation: "Regulamentação do Gol de Ouro para encerramento de períodos empatados e do Shoot-out para desempate da\
      \ partida."
  - id: "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_007"
    source_id: "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    locator: "pág. 11, Regra 4:2, 4:3"
    evidence_type: "REGRA"
    excerpt: "Em princípio uma equipe consiste em até 10 (dez) jogadores. Pelo menos 6 (seis) jogadores devem estar presentes\
      \ no início do jogo."
    interpretation: "Composição numérica das equipes: até 10 inscritos, mínimo de 6 para iniciar e 4 simultâneos em quadra."
  - id: "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_008"
    source_id: "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    locator: "pág. 11, Regra 4:2, 4:3"
    evidence_type: "REGRA"
    excerpt: "Um máximo 4 (quatro) jogadores por equipe, (3 jogadores de linha e 1 goleiro), podem estar na quadra de jogo."
    interpretation: "Composição numérica das equipes: até 10 inscritos, mínimo de 6 para iniciar e 4 simultâneos em quadra."
  - id: "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_009"
    source_id: "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    locator: "pág. 21, Regra 9:2, 9:3, 9:6"
    evidence_type: "REGRA"
    excerpt: "Gols criativos ou espetaculares são premiados com dois pontos"
    interpretation: "Critérios de valorização de gols de 2 pontos (gols criativos/espetaculares, tiros de 6 metros e gols\
      \ do goleiro)."
  - id: "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_010"
    source_id: "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    locator: "pág. 21, Regra 9:2, 9:3, 9:6"
    evidence_type: "REGRA"
    excerpt: ". Um gol marcado em um tiro de 6 metros é premiado com dois pontos."
    interpretation: "Critérios de valorização de gols de 2 pontos (gols criativos/espetaculares, tiros de 6 metros e gols\
      \ do goleiro)."
  - id: "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_011"
    source_id: "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    locator: "pág. 21, Regra 9:2, 9:3, 9:6"
    evidence_type: "REGRA"
    excerpt: "Dois pontos são concedidos quando um gol é marcado pelo goleiro."
    interpretation: "Critérios de valorização de gols de 2 pontos (gols criativos/espetaculares, tiros de 6 metros e gols\
      \ do goleiro)."
  - id: "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_012"
    source_id: "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    locator: "pág. 21-22, Regra 9:8"
    evidence_type: "REGRA"
    excerpt: "Cinco jogadores que estejam aptos a jogar executarão os arremessos alternadamente com a equipe adversária. Se\
      \ um goleiro for um dos arremessadores, ele conta como um jogador de linha ao realizar seu arremesso."
    interpretation: "Regramento do Shoot-out com rodada inicial de 5 cobranças alternadas por equipe."
  - id: "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_013"
    source_id: "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    locator: "pág. 28, Regra 14:1"
    evidence_type: "REGRA"
    excerpt: "Um tiro de 6 metros é assinalado quando: a) uma clara chance de marcar um gol é destruída qualquer lugar da\
      \ quadra por um jogador ou oficial de equipe da equipe adversária"
    interpretation: "Requisitos para assinalação de tiro de 6 metros por destruição de clara chance de gol."
  - id: "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_014"
    source_id: "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    locator: "pág. 30, Regra 16:1, 16:2, 16:5"
    evidence_type: "REGRA"
    excerpt: "Uma exclusão pode ser dada por:"
    interpretation: "Regra de acúmulo disciplinar onde a 2ª exclusão do mesmo atleta implica desqualificação automática."
  - id: "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_015"
    source_id: "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    locator: "pág. 30, Regra 16:1, 16:2, 16:5"
    evidence_type: "REGRA"
    excerpt: "A segunda exclusão de um jogador resulta em sua desqualificação."
    interpretation: "Regra de acúmulo disciplinar onde a 2ª exclusão do mesmo atleta implica desqualificação automática."
  - id: "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_016"
    source_id: "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    locator: "pág. 48, Esclarecimento 10"
    evidence_type: "REGRA"
    excerpt: ". Se, durante os últimos 15 segundos de ambos os períodos e durante o 'Gol de Ouro'"
    interpretation: "Penalização severa (desqualificação + tiro de 6m) por obstrução nos últimos 15 segundos do período ou\
      \ no Gol de Ouro."
  - id: "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_017"
    source_id: "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    locator: "pág. 48, Esclarecimento 10"
    evidence_type: "REGRA"
    excerpt: "impedir ou atrasar a execução de um tiro"
    interpretation: "Penalização severa (desqualificação + tiro de 6m) por obstrução nos últimos 15 segundos do período ou\
      \ no Gol de Ouro."
  - id: "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_018"
    source_id: "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    locator: "pág. 48, Esclarecimento 10"
    evidence_type: "REGRA"
    excerpt: "o jogador/oficial culpado deve ser desqualificado e um tiro de 6 metros deve ser concedido aos adversários."
    interpretation: "Penalização severa (desqualificação + tiro de 6m) por obstrução nos últimos 15 segundos do período ou\
      \ no Gol de Ouro."
  - id: "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_001"
    source_id: "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    locator: "Parágrafos 1 e 3"
    evidence_type: "DECISAO"
    excerpt: "As part of this ongoing evolution, amendments to the Rules of the Game for Beach Handball will come into effect\
      \ on 1 April 2026 and the ones for Wheelchair Handball will come into effect on 1 July 2026"
    interpretation: "Aprovação unânime das alterações pelo Conselho da IHF em 04/06/2025 e antecipação da data de vigência\
      \ para o Handebol de Praia de 01/07/2026 para 01/04/2026 por decisão do Congresso da IHF de 2025 no Cairo."
  - id: "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_002"
    source_id: "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    locator: "Parágrafos 1 e 3"
    evidence_type: "DECISAO"
    excerpt: "Following a decision of the 2025 Ordinary IHF Congress in Cairo, Egypt, and as approved by the IHF Beach Handball\
      \ Working Group in accordance with the new Article 21.3 of the IHF Statutes, the amendments to the Rules of the Game\
      \ for Beach Handball outlined in this article will come into force on 1 April 2026, three months earlier than the previously\
      \ announced date of 1 July 2026."
    interpretation: "Aprovação unânime das alterações pelo Conselho da IHF em 04/06/2025 e antecipação da data de vigência\
      \ para o Handebol de Praia de 01/07/2026 para 01/04/2026 por decisão do Congresso da IHF de 2025 no Cairo."
  - id: "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_003"
    source_id: "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    locator: "Parágrafo 4"
    evidence_type: "REGRA"
    excerpt: "A new provision has been set in the rules (Rule 7, Article 10), which states that 'it is not allowed to delay\
      \ repeatedly the execution of free throw, throw-in or goalkeeper throw for one team'."
    interpretation: "Regra 7, Artigo 10: Inclusão de proibição explícita contra o retardo repetido da execução de tiro livre,\
      \ tiro lateral (throw-in) ou tiro de goleiro por uma equipe."
  - id: "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_004"
    source_id: "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    locator: "Parágrafos 4 e 5"
    evidence_type: "REGRA"
    excerpt: "When referees detect a possible tendency toward passive play, they will display the forewarning signal (Hand\
      \ Signal No. 16), giving the attacking team one last chance to adjust their play. From this point, the team has a maximum\
      \ of four passes to attempt a shot on goal."
    interpretation: "Detalhamento de jogo passivo: Após o sinal de advertência (Gesto nº 16), a equipe atacante dispõe de\
      \ no máximo 4 passes para realizar um arremesso a gol antes que a posse de bola seja revertida."
  - id: "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_005"
    source_id: "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    locator: "Parágrafos 6 e 7"
    evidence_type: "REGRA"
    excerpt: "If the ball is out of play and a player or team official deliberately interferes with or delays the execution\
      \ of a throw by the opposing team"
    interpretation: "Sanções nos últimos 15 segundos do período e no Golden Goal: Interferência deliberada na execução de\
      \ tiro (bola fora) ou faltas das Regras 8:5/8:6/8:7/8:10 para evitar oportunidade de gol (bola em jogo) acarretam desqualificação\
      \ direta do infrator e tiro de 6 metros para o adversário."
  - id: "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_006"
    source_id: "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    locator: "Parágrafos 6 e 7"
    evidence_type: "REGRA"
    excerpt: "the offender must be disqualified, and the opponents are awarded a 6‑metre throw"
    interpretation: "Sanções nos últimos 15 segundos do período e no Golden Goal: Interferência deliberada na execução de\
      \ tiro (bola fora) ou faltas das Regras 8:5/8:6/8:7/8:10 para evitar oportunidade de gol (bola em jogo) acarretam desqualificação\
      \ direta do infrator e tiro de 6 metros para o adversário."
  - id: "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_007"
    source_id: "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    locator: "Parágrafos 6 e 7"
    evidence_type: "REGRA"
    excerpt: "If the ball is in play during these final 15 seconds"
    interpretation: "Sanções nos últimos 15 segundos do período e no Golden Goal: Interferência deliberada na execução de\
      \ tiro (bola fora) ou faltas das Regras 8:5/8:6/8:7/8:10 para evitar oportunidade de gol (bola em jogo) acarretam desqualificação\
      \ direta do infrator e tiro de 6 metros para o adversário."
  - id: "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_008"
    source_id: "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    locator: "Parágrafos 6 e 7"
    evidence_type: "REGRA"
    excerpt: "and a player or team official violates Rules 8:5, 8:6, 8:7, or 8:10 to prevent a scoring opportunity, the same\
      \ sanction applies: automatic disqualification for the offender and a 6‑metre throw for the opponents."
    interpretation: "Sanções nos últimos 15 segundos do período e no Golden Goal: Interferência deliberada na execução de\
      \ tiro (bola fora) ou faltas das Regras 8:5/8:6/8:7/8:10 para evitar oportunidade de gol (bola em jogo) acarretam desqualificação\
      \ direta do infrator e tiro de 6 metros para o adversário."
  - id: "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_009"
    source_id: "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    locator: "Parágrafo 7"
    evidence_type: "REGRA"
    excerpt: "A suspension is mandatory when an unhindered player, in an open-play situation with no defender between the\
      \ shooter and goalkeeper, throws a shot that strikes the goalkeeper’s head first. This applies only to open-play scenarios\
      \ where the head is the initial contact point"
    interpretation: "Proteção da integridade da/do goleira(o): Suspensão obrigatória para arremessador sem marcação em jogo\
      \ aberto cujo arremesso atinja diretamente a cabeça do goleiro. Punição ao goleiro caso simule lesão."
  - id: "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_010"
    source_id: "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    locator: "Parágrafo 7"
    evidence_type: "REGRA"
    excerpt: "Conversely, if the goalkeeper feigns injury to provoke a call, such as after chest contact, they face punishment\
      \ instead."
    interpretation: "Proteção da integridade da/do goleira(o): Suspensão obrigatória para arremessador sem marcação em jogo\
      \ aberto cujo arremesso atinja diretamente a cabeça do goleiro. Punição ao goleiro caso simule lesão."
  - id: "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_011"
    source_id: "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    locator: "Parágrafos 8 e 9"
    evidence_type: "REGRA"
    excerpt: "Each player must wear a clearly visible number between 1 and 99, measuring at least 12 x 10 centimetres"
    interpretation: "Padronização de uniformes e acessórios no Handebol de Praia: Números de 1 a 99 (mínimo 12x10 cm); obrigatoriedade\
      \ de jogar descalço, sendo permitidas meias esportivas comuns de tecido (de cor idêntica se usadas por mais de um jogador);\
      \ proibição estrita de meias de areia e calçados sintéticos/borracha."
  - id: "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_012"
    source_id: "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    locator: "Parágrafos 8 e 9"
    evidence_type: "REGRA"
    excerpt: "All players are required to play barefoot; however, they may wear regular, cloth-made sport socks or support\
      \ bandages"
    interpretation: "Padronização de uniformes e acessórios no Handebol de Praia: Números de 1 a 99 (mínimo 12x10 cm); obrigatoriedade\
      \ de jogar descalço, sendo permitidas meias esportivas comuns de tecido (de cor idêntica se usadas por mais de um jogador);\
      \ proibição estrita de meias de areia e calçados sintéticos/borracha."
  - id: "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_013"
    source_id: "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    locator: "Parágrafos 8 e 9"
    evidence_type: "REGRA"
    excerpt: "Sand socks or any form of synthetic or rubber footwear remain prohibited."
    interpretation: "Padronização de uniformes e acessórios no Handebol de Praia: Números de 1 a 99 (mínimo 12x10 cm); obrigatoriedade\
      \ de jogar descalço, sendo permitidas meias esportivas comuns de tecido (de cor idêntica se usadas por mais de um jogador);\
      \ proibição estrita de meias de areia e calçados sintéticos/borracha."
  - id: "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_014"
    source_id: "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    locator: "Parágrafo 10"
    evidence_type: "REGRA"
    excerpt: "If no female player can continue playing due to injuries or disqualifications, the affected team must operate\
      \ with one fewer player for the remainder of the match. Additionally, their maximum team points total is capped at 8"
    interpretation: "Handebol em Cadeira de Rodas 4x4: Caso não haja atleta feminina disponível por lesão ou desqualificação,\
      \ a equipe atua com um atleta a menos em quadra e seu teto de pontuação de classificação é limitado a 8 pontos."
  - id: "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_015"
    source_id: "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    locator: "Parágrafo 12"
    evidence_type: "REGRA"
    excerpt: "A two-point goal is awarded for: A complete 360° spin turn executed with one hand only, without touching the\
      \ wheelchair wheel during rotation"
    interpretation: "Handebol em Cadeira de Rodas 4x4: Condições para validação de gol de 2 pontos (giro 360° com uma mão\
      \ sem tocar na roda durante o giro, gol de goleiro de sua área, tiro de 7 metros e gols espetaculares em shoot-out)."
  - id: "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_016"
    source_id: "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    locator: "Parágrafo 12"
    evidence_type: "REGRA"
    excerpt: "A goal scored by the goalkeeper from their own goal area. Any goal from a 7-metre throw. Spectacular goals during\
      \ shoot-outs, per Rule 8:4a criteria."
    interpretation: "Handebol em Cadeira de Rodas 4x4: Condições para validação de gol de 2 pontos (giro 360° com uma mão\
      \ sem tocar na roda durante o giro, gol de goleiro de sua área, tiro de 7 metros e gols espetaculares em shoot-out)."
  - id: "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_001"
    source_id: "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    locator: "Página 1, Cabeçalho e Apresentação"
    evidence_type: "DECISAO"
    excerpt: "apresentamos abaixo os esclarecimentos às regras do jogo com base no último campeonato mundial realizado e que\
      \ passarão a ser utilizados em nosso Circuito Estadual a partir da presente Etapa, tendo todas as partidas disputadas\
      \ em de acordo com as atuais Leis do Jogo de Handebol de Praia da IHF."
    interpretation: "Adoção oficial das diretrizes e interpretações de arbitragem do último Mundial da IHF para todas as partidas\
      \ do Circuito Estadual da FHERJ a partir de 23/04/2025."
  - id: "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_002"
    source_id: "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    locator: "Página 1, Seção EQUIPE, Item 1"
    evidence_type: "REGRA"
    excerpt: "É permitido usar meias esportivas regulares (feitas de tecido) ou bandagens de apoio. Todos os outros tipos\
      \ de calçado (sintético, borracha, etc.) não são permitidos;"
    interpretation: "Autorização de meias esportivas de tecido e bandagens de apoio, com proibição expressa de qualquer outro\
      \ tipo de calçado sintético ou de borracha."
  - id: "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_003"
    source_id: "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    locator: "Página 1, Seção EQUIPE, Item 2"
    evidence_type: "REGRA"
    excerpt: "Em caso de utilização das meias esportivas comuns (feitas de tecido), elas devem ser curtas. Se mais de um jogador\
      \ do mesmo time estiver usando meias, todas devem ser da mesma cor;"
    interpretation: "Exigência de que meias esportivas sejam curtas e apresentem cor idêntica entre todos os atletas da mesma\
      \ equipe que as utilizem."
  - id: "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_004"
    source_id: "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    locator: "Página 1, Seção EQUIPE, Item 3"
    evidence_type: "REGRA"
    excerpt: "Está autorizado a cobrir qualquer parte do corpo por razões médicas com fitas Kinesiotape e bandagens da mesma\
      \ cor. Caso seja usado por mais de um jogador, a cor deve ser a mesma para todos;"
    interpretation: "Permissão de kinesiotape e bandagens para fins médicos com obrigatoriedade de cor uniforme entre os atletas\
      \ da equipe."
  - id: "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_005"
    source_id: "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    locator: "Página 1, Seção EQUIPE, Item 4"
    evidence_type: "REGRA"
    excerpt: "Peças duras (plástico ou metal) não são permitidas dentro de equipamentos de proteção;"
    interpretation: "Proibição estrita de inserções rígidas de plástico ou metal em equipamentos de proteção."
  - id: "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_006"
    source_id: "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    locator: "Página 1, Seção EQUIPE, Item 5"
    evidence_type: "REGRA"
    excerpt: "Compressão, mangas para braços e pernas são permitidas, mas a cor deve ser a mesma para todos do time;"
    interpretation: "Autorização do uso de mangas de compressão para braços e pernas, sujeita à padronização de cor na equipe."
  - id: "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_007"
    source_id: "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    locator: "Página 1, Seção EQUIPE, Item 6"
    evidence_type: "REGRA"
    excerpt: "Bonés ou chapéus e bandanas usados pelos atletas devem ser da mesma cor. Isso também se aplica a qualquer implemento\
      \ (bonés ou chapéus e bandanas) usado pelos oficiais da equipe;"
    interpretation: "Exigência de cor única para acessórios de cabeça (bonés, chapéus, bandanas) tanto para atletas quanto\
      \ para oficiais da comissão técnica."
  - id: "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_008"
    source_id: "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    locator: "Página 1, Seção EQUIPE, Item 7"
    evidence_type: "REGRA"
    excerpt: "Não é permitido prender com fita mais de dois dedos por mão;"
    interpretation: "Restrição do uso de fita (taping) a no máximo dois dedos unidos por mão."
  - id: "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_009"
    source_id: "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    locator: "Página 1, Seção EQUIPE, Item 8"
    evidence_type: "REGRA"
    excerpt: "Os quatro (4) oficiais da equipe devem usar camisas (uniforme) em uma cor diferente das camisas de seus próprios\
      \ jogadores e dos jogadores da equipe adversária;"
    interpretation: "Obrigatoriedade de uniforme dos oficiais da equipe em cor distinta dos atletas de ambas as equipes em\
      \ quadra."
  - id: "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_010"
    source_id: "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    locator: "Página 1, Seção TIRO DE ÁRBITRO, Item 9"
    evidence_type: "REGRA"
    excerpt: "A bola só pode ser jogada depois de atingir seu ponto mais alto. Não é permitido que os dois jogadores que estão\
      \ pulando para a bola a segurem durante o tiro de árbitro;"
    interpretation: "Regulamentação do tiro de árbitro: o toque na bola é permitido apenas no ápice do salto e proíbe-se a\
      \ posse simultânea por ambos os saltadores."
  - id: "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_011"
    source_id: "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    locator: "Página 1, Seção JOGO PASSIVO, Item 10"
    evidence_type: "REGRA"
    excerpt: "Quando um jogador se abstém intencionalmente de tentar usar uma oportunidade clara de gol passando a bola para\
      \ um companheiro de equipe, o companheiro de equipe que recebe a bola deve chutar a gol, caso contrário, um tiro livre\
      \ é marcado contra seu time;"
    interpretation: "Caracterização de jogo passivo com punição de tiro livre contra a equipe caso o recebedor não arremesse\
      \ imediatamente após rejeição intencional de oportunidade clara de gol."
  - id: "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_012"
    source_id: "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    locator: "Página 2, Seção SHOOT OUT, Item 11"
    evidence_type: "REGRA"
    excerpt: "Todos os jogadores em campo e goleiros devem permanecer em sua área de substituição;"
    interpretation: "Obrigatoriedade de permanência dos atletas e goleiros na respectiva área de substituição durante a fase\
      \ de Shoot Out."
  - id: "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_013"
    source_id: "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    locator: "Página 2, Seção SHOOT OUT, Item 12"
    evidence_type: "REGRA"
    excerpt: "A equipe atacante (goleiro e jogador de campo (arremessador)) assume sua posição na quadra PRIMEIRO;"
    interpretation: "Definição do fluxo de posicionamento no Shoot Out: a dupla atacante (goleiro e arremessador) deve se\
      \ posicionar antes da equipe defensora."
  - id: "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_014"
    source_id: "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    locator: "Página 2, Seção SHOOT OUT, Item 13"
    evidence_type: "REGRA"
    excerpt: "Os arremessos devem ser executados com a mesma bola para ambas as equipes;"
    interpretation: "Exigência do uso de bola única e idêntica para as execuções de Shoot Out de ambas as equipes."
  - id: "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_015"
    source_id: "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    locator: "Página 2, Seção PUNIÇÕES, Item 14"
    evidence_type: "REGRA"
    excerpt: "Uma desqualificação (a menos que seja uma desqualificação após uma segunda suspensão) deve ser explicada pelos\
      \ árbitros às autoridades no relatório da partida e leva a uma suspensão (mínima) de uma partida para o jogador/oficial\
      \ da equipe infrator;"
    interpretation: "Regra de desqualificação direta: exige justificativa no relatório de partida e acarreta suspensão automática\
      \ mínima de uma partida ao infrator."
  - id: "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_016"
    source_id: "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    locator: "Página 2, Encerramento"
    evidence_type: "FATO"
    excerpt: "Luiz Filipe Caldas - Diretor de Árbitros de Handebol de Praia da FHERJ, Chefe de Árbitros de Handebol de Praia\
      \ da COSCABAL, Delegado Técnico de Handebol de Praia e Instrutor da IHF"
    interpretation: "Identificação da autoridade técnica responsável pela emissão das diretrizes regulamentares."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_001"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo I, Cabeçalho"
    evidence_type: "FATO"
    excerpt: "Rev.00 - Revisado em 20/01/2026 | Rev.01 - Revisado em 01/03/2026"
    interpretation: "Registra o histórico de revisões do documento oficial da FHERJ, estabelecendo a vigência da versão Rev.01\
      \ em 01/03/2026."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_002"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo II, Art. 1º, Parágrafo 2º"
    evidence_type: "REGRA"
    excerpt: "Em todas as competições nominadas no presente artigo, deverão ser observadas as normas constantes deste regulamento\
      \ geral, conjuntamente com as normas nacionais e internacionais aceitas pelo Handebol, as normas da CBHb, e a legislação\
      \ federal aplicável."
    interpretation: "Define a articulação e submissão hierárquica do regulamento estadual às normas nacionais da CBHb, internacionais\
      \ da IHF e legislação federal."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_003"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo III, Seção III, Art. 5º"
    evidence_type: "REGRA"
    excerpt: "a equipe para cada jogo composta, no mínimo, por 6(seis) membros oficiais de arbitragens assim divididos: 2\
      \ (dois) Oficiais de Arbitragem, 1 (um) Delegado A, 1 (um) Delegado B, 1 (um) Secretário e 1(um) Cronometrista."
    interpretation: "Fixa a exigência da estrutura mínima de arbitragem necessária para a realização de partidas do Circuito\
      \ Estadual."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_004"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo IV, Seção I, Art. 10º, Parágrafo 7º"
    evidence_type: "REGRA"
    excerpt: "Para que um(a) jogador(a) novo(a) atue, o(a) mesmo(a) precisa ser inscrito(a) até três dias antecessores à partida,\
      \ entenda-se como 72 horas anteriores ao respectivo jogo na rodada."
    interpretation: "Estipula o prazo limite de antecedência de 72 horas para a inscrição válida de novos atletas na fase\
      \ classificatória."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_005"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo IV, Seção I, Art. 10º, Parágrafo 9º"
    evidence_type: "REGRA"
    excerpt: "uma vez que os atletas estejam inscritos por uma equipe"
    interpretation: "Determina a janela máxima temporal para transferência estadual de atletas fixada no cumprimento de 50%\
      \ do total de etapas."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_006"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo IV, Seção I, Art. 10º, Parágrafo 9º"
    evidence_type: "REGRA"
    excerpt: "somente poderão se transferir de equipe até antes do início da Etapa equivalente a 50% (cinquenta por cento)\
      \ do total de Etapas do Campeonato do Ano Vigente."
    interpretation: "Determina a janela máxima temporal para transferência estadual de atletas fixada no cumprimento de 50%\
      \ do total de etapas."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_007"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo IV, Seção I, Art. 10º, Parágrafos 14º e 15º"
    evidence_type: "REGRA"
    excerpt: "Só poderão ser relacionadas para um jogo, 14 (quatorze) pessoas, sendo no máximo 10 (dez) atletas e 04 (quatro)\
      \ dirigentes"
    interpretation: "Regulamenta o teto de 10 atletas e 4 dirigentes por súmula, limitando a permanência a no máximo 2 dirigentes\
      \ na área de substituição."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_008"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo IV, Seção I, Art. 10º, Parágrafos 14º e 15º"
    evidence_type: "REGRA"
    excerpt: "Durante o Jogo, somente poderão ficar na área de substituição 02 (dois) Dirigentes."
    interpretation: "Regulamenta o teto de 10 atletas e 4 dirigentes por súmula, limitando a permanência a no máximo 2 dirigentes\
      \ na área de substituição."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_009"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo IV, Seção I, Art. 10º, Parágrafo 20º"
    evidence_type: "REGRA"
    excerpt: "ficam as Equipes desobrigadas a apresentar Dirigentes com CREF ou o Certificado do Curso Nacional de Técnicos\
      \ de Handebol emitido pela CBHb"
    interpretation: "Estabelece exceção local de dispensa do CREF e curso da CBHb para técnicos/dirigentes atuantes no estado\
      \ do Rio de Janeiro."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_010"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo IV, Seção I, Art. 10º, Parágrafo 20º"
    evidence_type: "REGRA"
    excerpt: "A presente desobrigação"
    interpretation: "Estabelece exceção local de dispensa do CREF e curso da CBHb para técnicos/dirigentes atuantes no estado\
      \ do Rio de Janeiro."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_011"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo IV, Seção I, Art. 10º, Parágrafo 20º"
    evidence_type: "REGRA"
    excerpt: "somente é válido para o Circuito Estadual de Handebol de Praia do Rio de Janeiro"
    interpretation: "Estabelece exceção local de dispensa do CREF e curso da CBHb para técnicos/dirigentes atuantes no estado\
      \ do Rio de Janeiro."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_012"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo VI, Seção I, Art. 20º, Parágrafos 1º a 4º"
    evidence_type: "REGRA"
    excerpt: "O jogo consiste em dois períodos, que são pontuados separadamente. Cada período tem duração de 10 minutos"
    interpretation: "Normatiza a estrutura da partida: 2 períodos de 10 minutos, decisão por Gol de Ouro em empate no set\
      \ e Shoot-out em desempate de sets."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_013"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo VI, Seção I, Art. 20º, Parágrafos 1º a 4º"
    evidence_type: "REGRA"
    excerpt: "Se o placar estiver empatado no final de um período, o Gol de Ouro (Golden Gol) é precedido"
    interpretation: "Normatiza a estrutura da partida: 2 períodos de 10 minutos, decisão por Gol de Ouro em empate no set\
      \ e Shoot-out em desempate de sets."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_014"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo VI, Seção I, Art. 20º, Parágrafos 1º a 4º"
    evidence_type: "REGRA"
    excerpt: "Se cada equipe vencer um set"
    interpretation: "Normatiza a estrutura da partida: 2 períodos de 10 minutos, decisão por Gol de Ouro em empate no set\
      \ e Shoot-out em desempate de sets."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_015"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo VI, Seção I, Art. 20º, Parágrafos 1º a 4º"
    evidence_type: "REGRA"
    excerpt: "o 1 contra o Goleiro ('Shoot out') será precedido como forma de desempate."
    interpretation: "Normatiza a estrutura da partida: 2 períodos de 10 minutos, decisão por Gol de Ouro em empate no set\
      \ e Shoot-out em desempate de sets."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_016"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo IX, Art. 29º"
    evidence_type: "REGRA"
    excerpt: "As equipes vencedoras por W.O terão a seu favor a pontuação correspondente a 01 (uma) vitória, 02 (dois) pontos,\
      \ e para efeito de contagem de gols, as mesmas receberão um saldo de 20 gols e a equipe que não compareceu, não pontuará."
    interpretation: "Estabelece os efeitos esportivos e o saldo de gols padrão (20x0) em partidas decididas por W.O."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_017"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo XI, Art. 34º, Parágrafos 1º e 2º"
    evidence_type: "REGRA"
    excerpt: "Toda Desqualificação acompanhada do Cartão Azul, está inclusa nas Medidas Disciplinares automáticas e o Jogador\
      \ desqualificado"
    interpretation: "Institui suspensão automática de uma partida para punição com cartão azul e fixa a composição tripartite\
      \ da Comissão Especial Disciplinar."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_018"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo XI, Art. 34º, Parágrafos 1º e 2º"
    evidence_type: "REGRA"
    excerpt: "está automaticamente suspenso do próximo jogo"
    interpretation: "Institui suspensão automática de uma partida para punição com cartão azul e fixa a composição tripartite\
      \ da Comissão Especial Disciplinar."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_019"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo XI, Art. 34º, Parágrafos 1º e 2º"
    evidence_type: "REGRA"
    excerpt: "A Comissão Especial Disciplinar"
    interpretation: "Institui suspensão automática de uma partida para punição com cartão azul e fixa a composição tripartite\
      \ da Comissão Especial Disciplinar."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_020"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo XI, Art. 34º, Parágrafos 1º e 2º"
    evidence_type: "REGRA"
    excerpt: "será constituída por 3 (três) membros da Diretoria"
    interpretation: "Institui suspensão automática de uma partida para punição com cartão azul e fixa a composição tripartite\
      \ da Comissão Especial Disciplinar."
  - id: "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_021"
    source_id: "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    locator: "Capítulo XII, Art. 39º, Parágrafo 2º"
    evidence_type: "REGRA"
    excerpt: "Estando algum item deste Regulamento em desacordo com a Regra Oficial de Handebol, prevalece a Regra Oficial\
      \ e não o Regulamento da competição."
    interpretation: "Define a cláusula geral de prevalência da Regra Oficial IHF/CBHb sobre os dispositivos deste regulamento\
      \ em caso de antinomia."
  - id: "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_001"
    source_id: "SRC_REGULAMENTO_CBHB_2026_PDF_818BCC8B"
    locator: "Capítulo I, Art. 1º"
    evidence_type: "REGRA"
    excerpt: "Art. 1º Com a realização do CIRCUITO BRASILEIRO DE HANDEBOL DE PRAIA, a Confederação Brasileira de Handebol\
      \ - CBHb têm como objetivo principal agregar e incentivar a prática desta modalidade como forma sadia de competição\
      \ e entretenimento, ao mesmo tempo, estabelecer maior intercâmbio sócio esportivo entre os praticantes, promovendo o\
      \ surgimento de novos valores no cenário desportivo nacional."
    interpretation: "Define a finalidade e os objetivos institucionais do Circuito Brasileiro promovido pela CBHb."
  - id: "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_002"
    source_id: "SRC_REGULAMENTO_CBHB_2026_PDF_818BCC8B"
    locator: "Capítulo II, Art. 3º"
    evidence_type: "REGRA"
    excerpt: "Art. 3º - Para todos os fins, os participantes do CIRCUITO BRASILEIRO DE HANDEBOL DE PRAIA serão conhecedores\
      \ das regras oficiais da modalidade, das normas da Confederação Brasileira de Handebol e da International Handball Federation\
      \ - IHF, deste regulamento, bem como da legislação esportiva vigente no país. Colocar aqui o link das regras oficiais."
    interpretation: "Estabelece a presunção de conhecimento e obrigatoriedade das regras oficiais da IHF, normas da CBHb e\
      \ legislação desportiva nacional."
  - id: "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_003"
    source_id: "SRC_REGULAMENTO_CBHB_2026_PDF_818BCC8B"
    locator: "Capítulo VI, Art. 7º"
    evidence_type: "REGRA"
    excerpt: "Art. 7° - O CIRCUITO BRASILEIRO DE HANDEBOL DE PRAIA permitirá a inscrição de até 18 atletas (lista Larga).\
      \ A lista larga será finalizada e entregue até o último dia previsto para inscrição da terceira etapa classificatória,\
      \ que será disputada em final de junho. Esse número pode chegar a 20 atletas na fase final, com a inscrição de mais\
      \ dois atletas, entre emprestados, estrangeiros ou inadimplentes (não inscritos na lista larga)."
    interpretation: "Regulamenta o tamanho e os prazos da lista larga de atletas inscritos (18 atletas até a 3ª etapa, podendo\
      \ expandir para 20 na fase final)."
  - id: "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_004"
    source_id: "SRC_REGULAMENTO_CBHB_2026_PDF_818BCC8B"
    locator: "Capítulo VI, Art. 7º, § 9º"
    evidence_type: "REGRA"
    excerpt: "§9° - Para cada etapa da fase de classificação, ou final, serão inscritos até 12 (doze) atletas e 4 dirigentes.\
      \ Entretanto, somente 10 jogarão por jogo."
    interpretation: "Define os limites de inscritos por etapa (12 atletas e 4 dirigentes) e o número de atletas participantes\
      \ por partida (10 atletas)."
  - id: "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_005"
    source_id: "SRC_REGULAMENTO_CBHB_2026_PDF_818BCC8B"
    locator: "Capítulo VI, Art. 8º"
    evidence_type: "REGRA"
    excerpt: "Art. 8° Durante a competição os profissionais que compõem uma equipe são: técnico (bacharel em educação física,\
      \ obrigatoriamente), auxiliar, médico e fisioterapeuta. Todos deverão cumprir exigências legais, junto aos fiscais de\
      \ seus respectivos conselhos. Levar esse parágrafo para os advogados da CBHb."
    interpretation: "Fixa a composição da comissão técnica e exige formação em Educação Física para o técnico principal."
  - id: "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_006"
    source_id: "SRC_REGULAMENTO_CBHB_2026_PDF_818BCC8B"
    locator: "Capítulo VII, Art. 11"
    evidence_type: "REGRA"
    excerpt: "Art. 11. - O CIRCUITO BRASILEIRO DE HANDEBOL DE PRAIA será realizado em duas (02)) fases: classificatória e\
      \ final. A fase classificatória terá três (03) etapas mais Copa Brasil."
    interpretation: "Define a estrutura geral do campeonato dividida em fase classificatória (3 etapas e Copa Brasil) e fase\
      \ final."
  - id: "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_007"
    source_id: "SRC_REGULAMENTO_CBHB_2026_PDF_818BCC8B"
    locator: "Capítulo VII, Art. 11, § 1º"
    evidence_type: "REGRA"
    excerpt: "§ 1º - A fase final do CIRCUITO BRASILEIRO DE HANDEBOL DE PRAIA será realizada em etapa única, com dez (10)\
      \ equipes por naipe."
    interpretation: "Especifica o formato da etapa final única com 10 equipes qualificadas em cada naipe."
  - id: "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_008"
    source_id: "SRC_REGULAMENTO_CBHB_2026_PDF_818BCC8B"
    locator: "Capítulo VII, Art. 19"
    evidence_type: "REGRA"
    excerpt: "Art. 19. Os jogos serão regidos pelo sistema de pontos ganhos e perdidos, obedecendo aos seguintes critérios:\n\
      \nDois pontos por vitória\n\nZero ponto por derrota"
    interpretation: "Define a pontuação atribuída por jogo (2 pontos por vitória, 0 ponto por derrota)."
  - id: "EVID_REGULAMENTO_CBHB_2026_PDF_818BCC8B_009"
    source_id: "SRC_REGULAMENTO_CBHB_2026_PDF_818BCC8B"
    locator: "Capítulo VIII, Art. 22"
    evidence_type: "REGRA"
    excerpt: "Art. 22. - Na fase final do CIRCUITO BRASILEIRO DE HANDEBOL DE PRAIA as equipes serão divididas em duas chaves\
      \ A e B, com cinco (05) equipes em cada chave. A designação das equipes, excetuando a sede e a última colocada na fase\
      \ de classificação, será através dos resultados obtidos na fase anterior. A sede terá o direito de escolher a chave,\
      \ sendo a última colocada designada para a chave contrária a essa escolha."
    interpretation: "Estabelece a formação dos grupos A e B com 5 equipes na fase final e as prerrogativas do clube sede."
  - id: "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_001"
    source_id: "SRC_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5"
    locator: "Slide 04"
    evidence_type: "REGRA"
    excerpt: "When the entire ball has crossed the entire width of the goal line."
    interpretation: "Requisito básico para a validação de gol: a bola deve ultrapassar totalmente a linha de gol."
  - id: "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_002"
    source_id: "SRC_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5"
    locator: "Slide 04"
    evidence_type: "REGRA"
    excerpt: "A goal shall be allowed, if there is a violation of the rules by a defender but the ball still goes into the\
      \ goal."
    interpretation: "Aplicação de vantagem: o gol é concedido se houver infração do defensor, mas a bola ainda assim entrar\
      \ no gol."
  - id: "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_003"
    source_id: "SRC_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5"
    locator: "Slide 04"
    evidence_type: "REGRA"
    excerpt: "A goal shall be awarded to the opponents, if a player plays the ball into his own goal, except in the situation\
      \ where a goalkeeper is executing a goalkeeper throw and the ball does not cross the goal-area line (Rules 12:2, 2nd\
      \ paragraph). An own goal scored by any player is awarded with one point."
    interpretation: "Gol contra é concedido à equipe adversária valendo um ponto, exceto quando o goleiro executa o tiro de\
      \ meta e a bola não sai da área de gol."
  - id: "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_004"
    source_id: "SRC_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5"
    locator: "Slide 05"
    evidence_type: "REGRA"
    excerpt: "Regular goal One point Normal goal scored by a court player"
    interpretation: "Gol regular arremessado por jogador de linha vale um ponto."
  - id: "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_005"
    source_id: "SRC_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5"
    locator: "Slide 12"
    evidence_type: "REGRA"
    excerpt: "A shot taken with full turn of the body in the air. Correct (\"complete ) spin shot - when the jumping feet\
      \ of the player are pointing directly towards the goal at the point of take-off."
    interpretation: "Definição técnica do spin shot correto: giro completo do corpo no ar com os pés de impulsão direcionados\
      \ ao gol no momento da saída do solo."
  - id: "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_006"
    source_id: "SRC_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5"
    locator: "Slide 36"
    evidence_type: "REGRA"
    excerpt: "Two points are awarded only if the player who is in-flight controls the ball and shoots at goal while in the\
      \ air."
    interpretation: "Ponte-aérea (in-flight) concede dois pontos apenas se o atleta dominar a bola e arremessar enquanto estiver\
      \ suspenso no ar."
  - id: "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_007"
    source_id: "SRC_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5"
    locator: "Slide 41"
    evidence_type: "REGRA"
    excerpt: "\"Slapping the ball or just “pushing\" the ball into the goal is worth one point."
    interpretation: "Tapas ou empurrões na bola em jogadas aéreas valem apenas um ponto."
  - id: "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_008"
    source_id: "SRC_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5"
    locator: "Slide 45"
    evidence_type: "REGRA"
    excerpt: "A goal scored by a 6-metre throw is awarded with two points."
    interpretation: "Gol resultante de tiro de 6 metros vale dois pontos."
  - id: "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_009"
    source_id: "SRC_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5"
    locator: "Slide 45"
    evidence_type: "REGRA"
    excerpt: "A clear chance of scoring is destroyed anywhere on the court by a player or a team official of the opposing\
      \ team;"
    interpretation: "Configuração de tiro de 6 metros pela interrupção de clara ocasião de gol cometida por jogador ou oficial\
      \ adversário."
  - id: "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_010"
    source_id: "SRC_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5"
    locator: "Slide 49"
    evidence_type: "REGRA"
    excerpt: "Two points are awarded when a goal is scored by the goalkeeper."
    interpretation: "Gol marcado pelo goleiro vale dois pontos."
  - id: "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_011"
    source_id: "SRC_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5"
    locator: "Slide 49"
    evidence_type: "REGRA"
    excerpt: "The goalkeeper can shoot directly from the own goal area (without leaving it) at the opponents goal."
    interpretation: "O goleiro pode arremessar diretamente de dentro da sua própria área de gol."
  - id: "EVID_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_012"
    source_id: "SRC_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5"
    locator: "Slide 49"
    evidence_type: "REGRA"
    excerpt: "Every goal made by a goalkeeper or specialist is awarded two points. They wear differently coloured shirts."
    interpretation: "Qualquer gol marcado por goleiro ou especialista (identificado por camiseta de cor diferente) vale dois\
      \ pontos."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_001"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 1"
    evidence_type: "FATO"
    excerpt: "6-Metre Throw + Punishment By Luiz Filipe Caldas (BRA), Luis Monico (URU) & Pablo Martinez (URU)"
    interpretation: "Identificação do título do módulo pedagógico, autoria e vinculo com a IHF Virtual Academy."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_002"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 4"
    evidence_type: "REGRA"
    excerpt: "Clear chance of scoring is destroyed Anywhere on the court by the opposing team"
    interpretation: "Condição primária para assinalar o tiro de 6 metros: destruição de clara ocasião de gol em qualquer parte\
      \ da quadra pela equipe adversária."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_003"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 5"
    evidence_type: "REGRA"
    excerpt: "Unwarranted whistle signal"
    interpretation: "Sinal de apito injustificado que interrompe uma clara ocasião de gol enseja tiro de 6m."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_004"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 5"
    evidence_type: "REGRA"
    excerpt: "Interference of someone outside of the game"
    interpretation: "Interferência externa ao jogo que impede uma clara ocasião de gol."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_005"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 6"
    evidence_type: "REGRA"
    excerpt: "Ball and body control to shoot on goal"
    interpretation: "Critério para caracterizar clara ocasião de gol com posse e controle do corpo para arremesso à baliza."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_006"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 6"
    evidence_type: "REGRA"
    excerpt: "Without ball but referees convinced player is going to receive it"
    interpretation: "Caracterização de clara ocasião de gol sem posse direta, fundamentada na convicção dos árbitros de recepção\
      \ iminente."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_007"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 6"
    evidence_type: "REGRA"
    excerpt: "Counterattack or fast break against GK"
    interpretation: "Situação de contra-ataque ou transição rápida em duelo isolado contra o goleiro como clara ocasião de\
      \ gol."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_008"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 6"
    evidence_type: "REGRA"
    excerpt: "GK left the goal area empty goal"
    interpretation: "Situação de gol desprotegido em razão da saída do goleiro da área de gol."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_009"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 8"
    evidence_type: "REGRA"
    excerpt: "14.5 - Direct shot on goal, within 3 seconds after whistle signal"
    interpretation: "Regra 14.5: Exigência de arremesso direto ao gol em até 3 segundos após o apito do árbitro."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_010"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 8"
    evidence_type: "REGRA"
    excerpt: "14.8-GK and other players at least 1m away from the thrower"
    interpretation: "Regra 14.8: Distância mínima obrigatória de 1 metro do goleiro e demais jogadores em relação ao executante."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_011"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 8"
    evidence_type: "REGRA"
    excerpt: "14.9 – GK cannot be changed when thrower is ready to shoot"
    interpretation: "Regra 14.9: Proibição de substituição do goleiro quando o executante já estiver pronto para arremessar."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_012"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 9"
    evidence_type: "REGRA"
    excerpt: "14.6 - Thrower cannot touch or cross the 6m line"
    interpretation: "Regra 14.6: Proibição ao executante de tocar ou ultrapassar a linha de 6 metros na cobrança."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_013"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 9"
    evidence_type: "REGRA"
    excerpt: "14.7 Thrower cannot play the ball again until it has touched the goal or an opponent"
    interpretation: "Regra 14.7: Proibição de recontacto com a bola pelo executante antes que esta toque na baliza ou em um\
      \ adversário."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_014"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 10"
    evidence_type: "REGRA"
    excerpt: "14.10 - Fair Play – no movements during the execution by the opponents next to the thrower"
    interpretation: "Regra 14.10: Proibição de movimentos de distração ou provocação por adversários próximos ao cobrador\
      \ durante a execução."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_015"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 12"
    evidence_type: "REGRA"
    excerpt: "WHEN THE DEFENDER GOES TO THE BALL NO PUNISHMENT"
    interpretation: "Critério disciplinar: disputas focadas puramente na bola não acarretam sanção disciplinar pessoal."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_016"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 14"
    evidence_type: "DECISAO"
    excerpt: "PLAY ON - ALLOWED ACTIONS"
    interpretation: "Diretriz de arbitragem determinando a continuidade do jogo em ações consideradas legais."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_017"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 14"
    evidence_type: "DECISAO"
    excerpt: "PLAY ON - JUMPS FROM OUTSIDE OF THE GOAL AREA"
    interpretation: "Saltos iniciados fora da área de gol devem ser interpretados como ação legal sem interrupção."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_018"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 15"
    evidence_type: "REGRA"
    excerpt: "DEFENDER MOVES THE GOAL-AREA LINE"
    interpretation: "Infração referente ao ato do defensor de mover a fita delimitadora da área de gol."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_019"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 15"
    evidence_type: "REGRA"
    excerpt: "DEFENDER USES HIS LEG AGAINST THE OPPONENT - LONG STEP"
    interpretation: "Infração disciplinar pelo uso da perna com passada larga para bloquear o adversário."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_020"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 15"
    evidence_type: "REGRA"
    excerpt: "DEFENDER ARRIVES LATE AND ALSO ENTERS THE GOAL AREA"
    interpretation: "Infração cumulativa por abordagem defensiva atrasada acompanhada de invasão da área de gol."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_021"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 16"
    evidence_type: "REGRA"
    excerpt: "DEFENDER HITS THE OPPONENT WIHT HIS ELBOW"
    interpretation: "Infração física por atingir o adversário com o cotovelo (grafia literal 'WIHT' mantida do original)."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_022"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 16"
    evidence_type: "REGRA"
    excerpt: "DEFENDER IS NOT GOING TO PLAY THE BALL, HE GOES AGAINST THE OPPONENT"
    interpretation: "Infração caracterizada pela ausência de intenção de jogar a bola, direcionando a ação ao corpo do adversário."
  - id: "EVID_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_023"
    source_id: "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    locator: "Slide 16"
    evidence_type: "REGRA"
    excerpt: "DEFENDER HOLDS THE OPPONENT WITH HIS LEFT ARM"
    interpretation: "Infração por agarrar/retiver o adversário com o braço."
  - id: "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    source_id: "SRC_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2"
    locator: "Guia 00 — Controle Canônico / 4. Regras Canônicas Vigentes"
    evidence_type: "DECISAO"
    excerpt: "Referência vigente: DEC-001 — este Google Docs é o SSOT metodológico do projeto; decisões concluídas somente\
      \ se registradas aqui."
    interpretation: "Estabelece a DEC-001, definindo o documento Google Docs multi-guia como a única fonte canônica da metodologia\
      \ do projeto."
  - id: "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_002"
    source_id: "SRC_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2"
    locator: "Guia 00 — Controle Canônico / 4. Regras Canônicas Vigentes"
    evidence_type: "DECISAO"
    excerpt: "Referência vigente: DEC-019 — camada regulamentar deve seguir as Regras IHF de Beach Handball vigentes em 2026,\
      \ registrando versão da regra."
    interpretation: "Determina a primazia regulamentar das Regras Oficiais da IHF de 2026 sobre qualquer material interno\
      \ ou histórico."
  - id: "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
    source_id: "SRC_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2"
    locator: "Guia 05 — Protocolo Metodológico v0.9.2 / 2. Unidades / UNT-003"
    evidence_type: "REGRA"
    excerpt: "Definição: intervalo de direito/controle funcional ou legal da bola por uma equipe, iniciado pelo primeiro controle\
      \ funcional/legal inequívoco em bola viva ou pelo primeiro instante observável em que um reinício atribui inequivocamente\
      \ o direito à bola para uma nova posse, conforme COD-002/COD-027. Termina por gol validado, mudança de controle/direito\
      \ ou evento regulamentar que transfira/encerre a posse. Interrupção ou reinício sem mudança do direito à bola não encerra\
      \ nem reinicia automaticamente a posse."
    interpretation: "Mapeia a definição operacional rigorosa de posse de bola (UNT-003), vinculando o início ao controle funcional/legal\
      \ e excluindo interrupções sem troca de direito."
  - id: "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_004"
    source_id: "SRC_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2"
    locator: "Guia 05 — Protocolo Metodológico v0.9.2 / 2. Unidades / UNT-004"
    evidence_type: "REGRA"
    excerpt: "Definição operacional: intervalo do ataque posicional que começa quando a equipe atacante apresenta organização\
      \ estável/classificável em postos ofensivos diante de uma defesa organizada ou classificável e termina quando (a) a\
      \ posse termina; ou (b) uma interrupção/reorganização destrói a unidade e uma nova organização posicional subsequente\
      \ satisfaz novamente o critério de abertura."
    interpretation: "Operacionaliza a Basic Attack Unit (BOU) como unidade de observação do ataque posicional organizado."
  - id: "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_005"
    source_id: "SRC_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2"
    locator: "Guia 05 — Protocolo Metodológico v0.9.2 / 3. Fases / TAX-001"
    evidence_type: "REGRA"
    excerpt: "Valores: TO — Transição Ofensiva; AP — Ataque Posicional; TD — Transição Defensiva; DP — Defesa Posicional;\
      \ F_IND — fase/fronteira indeterminável."
    interpretation: "Fixa o domínio fechado das quatro fases ordinárias do jogo mais a categoria indeterminada para codificação."
  - id: "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_006"
    source_id: "SRC_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2"
    locator: "Guia 05 — Protocolo Metodológico v0.9.2 / 4. Categorias Táticas / TAX-006"
    evidence_type: "REGRA"
    excerpt: "Base geométrica: a largura regulamentar de 12 m da quadra, conforme SRC-018/Regra 1 IHF vigente, é dividida\
      \ em quatro faixas laterais analíticas iguais de 3 m. As linhas internas de 3 m, 6 m e 9 m são fronteiras do Scout e\
      \ não marcações oficiais da IHF."
    interpretation: "Mapeia o sistema de delimitação analítica da quadra em quatro faixas laterais de 3 metros (ZE, ZCE, ZCD,\
      \ ZD) para indicar a origem da finalização."
  - id: "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_007"
    source_id: "SRC_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2"
    locator: "Guia 06 — Dicionário de Variáveis / VAR-028"
    evidence_type: "DECISAO"
    excerpt: "Decisão: excluída da camada P1. Não usar em novos registros, ficha de codificação, filtros ou denominadores\
      \ observacionais. O vídeo, isoladamente, não sustenta julgamento de que uma troca era necessária, correta, incorreta\
      \ ou tardia."
    interpretation: "Registra a rejeição da variável inferencial 'troca_necessaria' (VAR-028) na codificação primária (P1)\
      \ por falta de observabilidade objetiva."
  - id: "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_008"
    source_id: "SRC_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2"
    locator: "Guia 08 — Indicadores e Denominadores / IND-016"
    evidence_type: "DERIVACAO"
    excerpt: "Fórmula: n_DEFESA_GK / (n_DEFESA_GK + n_GOL)."
    interpretation: "Formaliza a fórmula da taxa de defesa do goleiro em arremessos ao alvo, restringindo o denominador estritamente\
      \ a defesas e gols."
  - id: "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_009"
    source_id: "SRC_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2"
    locator: "Guia 11 — Confiabilidade / CON-006"
    evidence_type: "REGRA"
    excerpt: "Critério teórico: mínimo 18/20 respostas corretas (90%) e ZERO erro crítico definido em CON-004-D. Se houver\
      \ 18+ acertos mas erro crítico, status = NÃO_QUALIFICADO até revisão e reteste dos cenários críticos."
    interpretation: "Estipula o critério de qualificação teórico do observador (CON-006) exigido antes da liberação para a\
      \ codificação da partida piloto."
  - id: "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_001"
    source_id: "SRC_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC"
    locator: "p. 497, passage 7"
    evidence_type: "DERIVACAO"
    excerpt: "The Basic Attack Unit (BOU) is defined as the temporal span between the positioning of the attackers in specific\
      \ positions and the occurrence of a break in play or change of possession"
    interpretation: "Define a Unidade Básica de Ataque (BOU) como o intervalo de tempo compreendido entre o posicionamento\
      \ dos atacantes nos postos específicos e a interrupção do jogo ou mudança de posse da bola."
  - id: "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_002"
    source_id: "SRC_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC"
    locator: "p. 497, passage 8"
    evidence_type: "DERIVACAO"
    excerpt: "These group-tactical actions can be classified into three categories, namely, elementary (asymmetry situations),\
      \ simple (player and ball circulations), basic (crossing with ball, crossing without ball, cutting in, give and go,\
      \ blocking, block, screen and piston movement) and complex (tactical procedures)"
    interpretation: "Classifica as ações tático-grupais de ataque em elementares, simples, básicas e complexas."
  - id: "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_003"
    source_id: "SRC_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC"
    locator: "p. 497, passage 9"
    evidence_type: "DERIVACAO"
    excerpt: "Three types of collective play can be distinguished: free play, in which players take the initiative from the\
      \ outset of the BOU, depending on the responses of the opposing team; directed play, which begins with the planned play\
      \ BOU; and finally planned play, which involves the development of the pre-established BOU"
    interpretation: "Estabelece a taxonomia dos três tipos de jogo coletivo ofensivo: jogo livre, jogo dirigido e jogo planejado."
  - id: "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_004"
    source_id: "SRC_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC"
    locator: "p. 498, passage 19"
    evidence_type: "DERIVACAO"
    excerpt: "Thirteen criteria and the respective categories related to the attacking actions of collective play in beach\
      \ handball were created."
    interpretation: "Informa que o instrumento observacional criado ad hoc é estruturado em 13 critérios com suas respectivas\
      \ categorias sistemáticas."
  - id: "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_005"
    source_id: "SRC_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC"
    locator: "p. 503, passage 38"
    evidence_type: "SUPORTE"
    excerpt: "The LINCE PLUS software (Soto et al., 2022), developed at the University of Lleida for the management and application\
      \ of observational methodology, was used to record the observed actions."
    interpretation: "Identifica o software LINCE PLUS como a ferramenta utilizada para codificação, registro e análise dos\
      \ dados observacionais."
  - id: "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_006"
    source_id: "SRC_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC"
    locator: "p. 497, passage 17"
    evidence_type: "FATO"
    excerpt: "A total of 10 beach handball experts participated in the assessment of the observational and recording instrument\
      \ of this study"
    interpretation: "Registra a composição do painel de 10 especialistas para a validação de conteúdo pelo critério de autoridade."
  - id: "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_007"
    source_id: "SRC_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC"
    locator: "p. 496, passage 3"
    evidence_type: "FATO"
    excerpt: "To assess the quality of the data, Cohen's Kappa Index (intra-observer agreement) and Fleiss' Kappa Index (inter-observer\
      \ agreement) were employed. Both indexes demonstrated almost perfect concordance values."
    interpretation: "Comprova a confiabilidade dos dados observacionais através de índices Kappa de Cohen e Fleiss com valores\
      \ de concordância quase perfeita."
  - id: "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_008"
    source_id: "SRC_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC"
    locator: "p. 504, passage 42"
    evidence_type: "FATO"
    excerpt: "The matches observed for validation were the finals of the Beach Handball World Championship, held in Heraklion,\
      \ Greece, on 26 June 2022."
    interpretation: "Especifica as partidas analisadas para validação prática: finais masculina e feminina do Campeonato Mundial\
      \ de 2022."
  - id: "EVID_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC_009"
    source_id: "SRC_DEVELOPMENT_OF_AN_INSTRUMENT_FOR_OBSERVATION_OF_COLLECTI_7CF9CCAC"
    locator: "p. 507, passage 50"
    evidence_type: "FATO"
    excerpt: "The men only use 3 different procedures and the women 13 different procedures."
    interpretation: "Demonstra a diferença na diversidade tática observada, na qual equipes femininas utilizaram 13 procedimentos\
      \ táticos diferentes, comparadas a 3 utilizados pelas masculinas."
  - id: "EVID_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56_001"
    source_id: "SRC_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56"
    locator: "p. 1-2, Header & Title"
    evidence_type: "SUPORTE"
    excerpt: "Contextual Factors and Decision-Making in the Behavior of Finalization in the Positional Attack in Beach Handball:\
      \ Differences by Gender Through Polar Coordinates Analysis"
    interpretation: "Título formal da publicação acadêmica delimitando o objeto de estudo, modalidade e métodos empregados."
  - id: "EVID_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56_002"
    source_id: "SRC_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56"
    locator: "p. 3, Instruments"
    evidence_type: "FATO"
    excerpt: "It consists of 11 criteria and 90 categories that correspond chronologically with the development of an attack\
      \ on beach handball (Morillo-Baro and Hernández-Mendo, 2015)."
    interpretation: "Descrição da estrutura do instrumento observacional ad hoc utilizado, composto por 11 critérios e 90\
      \ categorias do ataque posicionado."
  - id: "EVID_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56_003"
    source_id: "SRC_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56"
    locator: "p. 4-5, Polar Coordinate Analysis"
    evidence_type: "FATO"
    excerpt: "The behaviors selected as criteria (focal) have been: GOAL2: this behavior is what refers to the final objective\
      \ of the attack and, therefore, its appearance can be associated with a pattern of success in the decision made by the\
      \ attacking team."
    interpretation: "Definição do gol de dois pontos (GOAL2) como comportamento focal indicador do padrão de sucesso na tomada\
      \ de decisão ofensiva."
  - id: "EVID_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56_004"
    source_id: "SRC_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56"
    locator: "p. 8, Discussion"
    evidence_type: "SUPORTE"
    excerpt: "In the male category, the achievement of the double value goal excites the appearance of pairing behaviors related\
      \ to the result of the favorable score, as shown in quadrants one, two and four."
    interpretation: "Evidência de que, na categoria masculina, a conversão de gols de valor duplo está associada a situações\
      \ de placar favorável."
  - id: "EVID_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56_005"
    source_id: "SRC_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56"
    locator: "p. 9, Discussion"
    evidence_type: "SUPORTE"
    excerpt: "With regard to the female category, the double value goal, as it happens in the male category, is directly related\
      \ to the score in favor, therefore, it can be considered that this fact favors the decisions made by the players."
    interpretation: "Evidência de que, na categoria feminina, o gol de valor duplo também se relaciona diretamente com o placar\
      \ favorável."
  - id: "EVID_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56_006"
    source_id: "SRC_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56"
    locator: "p. 10, Discussion"
    evidence_type: "SUPORTE"
    excerpt: "Finally, only Spanish players formed the sample, so this research has focused on the development of the game\
      \ in this country."
    interpretation: "Delimitação do alcance geográfico e populacional dos resultados obtidos."
  - id: "EVID_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2_001"
    source_id: "SRC_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2"
    locator: "p. 209"
    evidence_type: "FATO"
    excerpt: "O objetivo deste estudo foi identificar e analisar os aspectos estruturantes da fase ofensiva do handebol de\
      \ areia, em especial do ataque posicionado, a partir da perspectiva dos treinadores."
    interpretation: "Apresenta o objetivo geral da pesquisa científica [2]."
  - id: "EVID_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2_002"
    source_id: "SRC_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2"
    locator: "p. 209"
    evidence_type: "SUPORTE"
    excerpt: "Os resultados revelaram que a assimetria numérica é a base da estrutura do jogo ofensivo, pautada na presença\
      \ do especialista, o qual também influencia a composição dos sistemas ofensivos."
    interpretation: "Indica que a assimetria numérica induzida pelo especialista é o elemento estruturante central do ataque\
      \ posicionado [2]."
  - id: "EVID_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2_003"
    source_id: "SRC_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2"
    locator: "p. 210"
    evidence_type: "SUPORTE"
    excerpt: "a superioridade numérica ofensiva é verificada na maioria dos ataques posicionados das equipes, o que é proporcionado\
      \ pela atuação do especialista, que substitui o goleiro (o qual qualquer gol anotado equivale a dois pontos) e atua\
      \ como jogador de quadra, também com pontuação equivalente a dois pontos, em caso de gol."
    interpretation: "Explica a mecânica de substituição do goleiro pelo especialista gerando vantagem numérica de 4x3 [5]."
  - id: "EVID_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2_004"
    source_id: "SRC_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2"
    locator: "p. 211"
    evidence_type: "FATO"
    excerpt: "Participaram deste estudo cinco (todos) treinadores de handebol de areia de equipes masculinas e/ou femininas\
      \ adultas que disputaram ao menos uma das etapas do circuito paulista de handebol de areia de 2015, promovido pela Federação\
      \ Paulista de Handebol (FPH)."
    interpretation: "Registra a caracterização e delimitação da amostra de sujeitos da pesquisa [3]."
  - id: "EVID_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2_005"
    source_id: "SRC_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2"
    locator: "p. 215"
    evidence_type: "SUPORTE"
    excerpt: "Os sistemas ofensivos destacados pelos treinadores foram o 3:1 (dois laterais, central e pivô), 2:2 (dois laterais\
      \ e dois pivôs) e o 4:0 (dois laterais e dois armadores)."
    interpretation: "Detalha a estruturação posicional dos três sistemas ofensivos em superioridade numérica [7]."
  - id: "EVID_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2_006"
    source_id: "SRC_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2"
    locator: "p. 216"
    evidence_type: "SUPORTE"
    excerpt: "Os treinadores ainda elucidam elementos que dependem das ações coordenadas entre dois ou mais jogadores, como\
      \ o \"semi-giro com aérea\" (o jogador em posse da bola salta para realizar o giro, em seguida passa a bola para outro\
      \ jogador que arremessa em aérea) e a \"aérea com aérea\" (da qual participam três jogadores: o primeiro jogador faz\
      \ o passe para um segundo jogador que em aérea recebe a bola e, ainda no ar, passa para o terceiro jogador que recebe\
      \ em aérea e arremessa)."
    interpretation: "Descreve combinações táticas complexas entre finalizações espetaculares [8]."
  - id: "EVID_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2_007"
    source_id: "SRC_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2"
    locator: "p. 218"
    evidence_type: "SUPORTE"
    excerpt: "Como limitação do estudo aponta-se o fato de entrevistar treinadores de apenas um Estado brasileiro (São Paulo),\
      \ o que sugere como perspectivas futuras a investigação de treinadores de outros contextos no Brasil."
    interpretation: "Registra formalmente as limitações de abrangência geográfica apontadas pelos autores do estudo [4]."
  - id: "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_001"
    source_id: "SRC_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A"
    locator: "Slide 1"
    evidence_type: "SUPORTE"
    excerpt: "Latest Trends in Defence"
    interpretation: "Título principal do seminário técnico focado nas tendências recentes da fase defensiva no handebol de\
      \ praia."
  - id: "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_002"
    source_id: "SRC_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A"
    locator: "Slide 1"
    evidence_type: "SUPORTE"
    excerpt: "IHF Online Education Weeks 2023"
    interpretation: "Identificação do programa oficial de capacitação continuada da Federação Internacional de Handebol (IHF)."
  - id: "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_003"
    source_id: "SRC_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A"
    locator: "Slide 6"
    evidence_type: "SUPORTE"
    excerpt: "Pick 3 players only because they are good in defence"
    interpretation: "Diretriz tática de montagem de elenco recomendando a seleção de três atletas especialistas exclusivamente\
      \ defensivos."
  - id: "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_004"
    source_id: "SRC_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A"
    locator: "Slide 6"
    evidence_type: "SUPORTE"
    excerpt: "One of them must be able to be the goalkeeper in shootout"
    interpretation: "Requisito funcional de versatilidade para atuação como goleiro na disputa de Shootout."
  - id: "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_005"
    source_id: "SRC_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A"
    locator: "Slide 8"
    evidence_type: "SUPORTE"
    excerpt: "1. Reactive or proactive"
    interpretation: "Classificação da atitude tática defensiva em reativa ou proativa perante o sistema ofensivo adversário."
  - id: "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_006"
    source_id: "SRC_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A"
    locator: "Slide 8"
    evidence_type: "SUPORTE"
    excerpt: "2. 2-1 in the middle or on the side"
    interpretation: "Sistematização do modelo defensivo 2-1 com variação de foco central ou lateral."
  - id: "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_007"
    source_id: "SRC_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A"
    locator: "Slide 8"
    evidence_type: "SUPORTE"
    excerpt: "3. 1-2 on the side or with one in the middle"
    interpretation: "Sistematização do modelo defensivo 1-2 com distribuição do jogador de cobertura/pressão."
  - id: "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_008"
    source_id: "SRC_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A"
    locator: "Slide 8"
    evidence_type: "SUPORTE"
    excerpt: "6. 7 metres not 6 metres"
    interpretation: "Proposta tática de linha defensiva avançada a 7 metros em vez do posicionamento tradicional aos 6 metros."
  - id: "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_009"
    source_id: "SRC_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A"
    locator: "Slide 10"
    evidence_type: "SUPORTE"
    excerpt: "1. Take space and block from the middle"
    interpretation: "Diretriz operacional de ocupação de espaço e ação de bloqueio a partir da zona central."
  - id: "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_010"
    source_id: "SRC_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A"
    locator: "Slide 10"
    evidence_type: "SUPORTE"
    excerpt: "3. 1 or 2 arms in flying block"
    interpretation: "Técnica de execução do bloqueio em salto (flying block) com uso de um ou dois braços."
  - id: "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_011"
    source_id: "SRC_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A"
    locator: "Slide 11"
    evidence_type: "SUPORTE"
    excerpt: "1. Fair play and safety for all"
    interpretation: "Princípio defensivo orientador fundamentado no jogo limpo e na preservação da integridade física."
  - id: "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_012"
    source_id: "SRC_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A"
    locator: "Slide 11"
    evidence_type: "SUPORTE"
    excerpt: "3. Monster block and other traps"
    interpretation: "Aplicação do bloqueio de grande impacto (monster block) e indução do ataque a armadilhas defensivas."
  - id: "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_013"
    source_id: "SRC_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A"
    locator: "Slide 11"
    evidence_type: "SUPORTE"
    excerpt: "4. Not on the opponent but in between"
    interpretation: "Princípio de posicionamento focado em ocupar linhas de passe e intervalos, evitando o contato faltoso\
      \ direto."
  - id: "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_014"
    source_id: "SRC_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A"
    locator: "Slide 12"
    evidence_type: "SUPORTE"
    excerpt: "Keywords unpredictable, full presure, take control, we decide and teamwork"
    interpretation: "Síntese dos pilares conceituais da defesa proposta (imprevisibilidade, pressão constante, iniciativa\
      \ tática e cooperação)."
  - id: "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_015"
    source_id: "SRC_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A"
    locator: "Slide 13"
    evidence_type: "SUPORTE"
    excerpt: "1. Blocking from the pivot to prevent fast break"
    interpretation: "Ação de bloqueio/contenção exercida sobre o pivô para prevenção do contra-ataque adversário."
  - id: "EVID_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_016"
    source_id: "SRC_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A"
    locator: "Slide 15"
    evidence_type: "SUPORTE"
    excerpt: "We have a fairly new sport so we are responsible to explore all corners of our sport - we are the pioneers,\
      \ so my plea to you is to do so."
    interpretation: "Declaração final enfatizando o papel inovador dos treinadores na exploração de novas estratégias para\
      \ o desenvolvimento da modalidade."
  - id: "EVID_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94_001"
    source_id: "SRC_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94"
    locator: "p. 1, Abstract"
    evidence_type: "FATO"
    excerpt: "Five coaches of adult male and/or female teams that played the Beach Handball championship of Sao Paulo State\
      \ were interviewed."
    interpretation: "Delimitação do universo da amostra da pesquisa qualitativa com cinco treinadores do Campeonato Paulista\
      \ de Handebol de Praia."
  - id: "EVID_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94_002"
    source_id: "SRC_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94"
    locator: "p. 1, Abstract"
    evidence_type: "DERIVACAO"
    excerpt: "The numerical asymmetry and the defensive system are responsible for the choices of the technical-tactical actions."
    interpretation: "A assimetria numérica e o sistema defensivo são apontados como os condicionantes hierárquicos para a\
      \ escolha das ações técnico-táticas individuais e de grupo."
  - id: "EVID_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94_003"
    source_id: "SRC_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94"
    locator: "p. 4, Discussion"
    evidence_type: "SUPORTE"
    excerpt: "Defensive skills that stand out in the beach handball are the counter-spin and counter-fly which are attempts\
      \ to prevent the spin shot and inflight shot, respectively"
    interpretation: "Ações técnico-táticas defensivas específicas contra finalizações valorizadas de dois pontos: counter-spin\
      \ (contra o spin shot) e counter-fly (contra o in-flight)."
  - id: "EVID_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_001"
    source_id: "SRC_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E"
    locator: "p. 139, Resumo"
    evidence_type: "FATO"
    excerpt: "En ambos casos ha coincidido que la actuación del portero es determinante para acabar ganando un partido. Sin\
      \ embargo, en categoría masculina se ha observado una mayor participación en la construcción del contraataque posterior."
    interpretation: "O desempenho do goleiro no handebol de praia é determinante para o resultado final em ambas as categorias,\
      \ com maior participação tática dos goleiros masculinos na construção do contra-ataque posterior."
  - id: "EVID_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_002"
    source_id: "SRC_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E"
    locator: "p. 140, Introducción"
    evidence_type: "FATO"
    excerpt: "Algunas de las diferencias más significativas entre una modalidad y otra son la posibilidad de conseguir goles\
      \ de valor simple, mediante un lanzamiento clásico de cualquiera de los jugadores que no sea el portero - especialista,\
      \ o goles de valor doble, mediante lanzamiento en giro de 360 grados, lanzamientos en flight o por lanzamientos del\
      \ especialista."
    interpretation: "No handebol de praia, os gols de valor simples resultam de arremessos clássicos efetuados por jogadores\
      \ de linha comuns, enquanto os gols de valor duplo derivam de giros de 360 graus, in-flight (fly) ou arremessos do especialista/goleiro."
  - id: "EVID_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_003"
    source_id: "SRC_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E"
    locator: "p. 141, Material y Métodos - Participantes"
    evidence_type: "FATO"
    excerpt: "De los 24 equipos que participaron en la Copa de España sénior de 2016 se seleccionaron tres equipos, de forma\
      \ aleatoria en cada categoría, y se observaron los partidos en lo que interaccionaban entre ellos resultando, un total\
      \ de 12 sesiones de observación, seis para la categoría masculina y seis para la categoría femenina."
    interpretation: "A amostragem do estudo compreendeu 12 sessões de observação de jogos da Copa de España sénior de 2016,\
      \ divididas igualmente entre a categoria masculina (6) e feminina (6)."
  - id: "EVID_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_004"
    source_id: "SRC_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E"
    locator: "p. 141, Material y Métodos - Diseño"
    evidence_type: "FATO"
    excerpt: "La unidad de observación fue la secuencia de ataque posicional, que estará definida en esta investigación desde\
      \ que un jugador atacante realice un lanzamiento a portería hasta la acción posterior de la actuación del portero."
    interpretation: "A unidade de observação foi definida como a sequência de ataque posicional, delimitada entre o arremesso\
      \ do atacante e a ação subsequente do goleiro."
  - id: "EVID_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_005"
    source_id: "SRC_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E"
    locator: "p. 144, Procedimiento"
    evidence_type: "FATO"
    excerpt: "GOL2 y PAR: estas dos conductas engloban todas las posibilidades de conseguir un gol de dos puntos, objetivo\
      \ principal del ataque, y todos los tipos de paradas que puede realizar el portero."
    interpretation: "As condutas focais GOL2 e PAR englobam a totalidade das ocorrências de gol de valor duplo e as defesas\
      \ efetuadas pelo goleiro."
  - id: "EVID_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_006"
    source_id: "SRC_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E"
    locator: "p. 144, Procedimiento"
    evidence_type: "FATO"
    excerpt: "PETO y PIV: se ha decidido seleccionar la finalización de estos dos jugadores, ya que son sobre los que recae\
      \ una mayor atención por parte de la defensa rival. El especialista, por su relevancia a la hora de la construcción\
      \ del juego y la posibilidad de conseguir un golde valor doble con un lanzamiento normal, y el pivote, porque se encuentra\
      \ en la zona central del ataque, donde se considera que conseguir un gol implica menor dificultad."
    interpretation: "Especialista e pivô foram selecionados como condutas focais por concentrarem a atenção defensiva do adversário\
      \ no ataque posicional."
  - id: "EVID_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_007"
    source_id: "SRC_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E"
    locator: "p. 150, Discusión"
    evidence_type: "FATO"
    excerpt: "Analizando las conductas focales del gol de valor doble y de la parada, en ambas categorías ocurre lo mismo,\
      \ la aparición de las paradas del portero está relacionada con el marcador a favor y la aparición de los goles de valor\
      \ doble, lo cual implica la ausencia de paradas, se relaciona con el marcador en contra."
    interpretation: "As defesas do goleiro associam-se estatisticamente a momentos de placar favorável, enquanto a ocorrência\
      \ de gols de dois pontos relaciona-se a situações de placar desfavorável."
  - id: "EVID_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0_001"
    source_id: "SRC_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0"
    locator: "p. 2, Seção 1. Introdução"
    evidence_type: "SUPORTE"
    excerpt: "A falta de conhecimento e incentivo sobre a posição de goleiro de handebol ou handebol de praia pode afetar\
      \ negativamente quem optar pela função."
    interpretation: "Sinaliza a carência de fundamentação e incentivo específico para a posição de goleiro no handebol de\
      \ praia."
  - id: "EVID_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0_002"
    source_id: "SRC_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0"
    locator: "p. 2, Seção 1. Introdução"
    evidence_type: "SUPORTE"
    excerpt: "Assim, o objetivo deste estudo é desenvolver uma diretriz para o treinamento do goleiro de Handebol de Praia,\
      \ levando em consideração os estímulos necessários de acordo com a análise de cada estágio de defesa."
    interpretation: "Estabelece a finalidade do estudo na criação de uma diretriz pedagógica baseada nos estágios de defesa."
  - id: "EVID_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0_003"
    source_id: "SRC_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0"
    locator: "p. 4, Seção 4. Estágios da Defesa"
    evidence_type: "DERIVACAO"
    excerpt: "Nesta proposta de trabalho, subdividimos as ações do goleiro em quatro tempos, que chamamos de T1 a T4, e são\
      \ detalhados a seguir."
    interpretation: "Apresenta a taxonomia metodológica proposta, subdividindo as ações defensivas do goleiro em quatro tempos\
      \ (T1 a T4)."
  - id: "EVID_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0_004"
    source_id: "SRC_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0"
    locator: "p. 4, Seção 5. Tempo de Observação Antes do Arremesso (T1)"
    evidence_type: "DERIVACAO"
    excerpt: "Nessa proposta, chamamos o tempo de observação antes do arremesso no handebol de praia de Tempo 1 (T1)."
    interpretation: "Define o Tempo 1 (T1) como a fase perceptiva e de observação do posicionamento do atacante e leitura\
      \ prévia do jogo."
  - id: "EVID_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0_005"
    source_id: "SRC_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0"
    locator: "p. 5, Seção 6. Tempo da Bola no Lançamento/Posicionamento (T2)"
    evidence_type: "DERIVACAO"
    excerpt: "Chamamos o momento em que a bola sai da mão do atacante de Tempo 2 (T2)."
    interpretation: "Define o Tempo 2 (T2) como o instante do lançamento e do deslocamento motor do goleiro na areia em busca\
      \ do posicionamento ideal."
  - id: "EVID_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0_006"
    source_id: "SRC_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0"
    locator: "p. 5, Seção 7. Tempo de Reação Após Arremesso (T3)"
    evidence_type: "DERIVACAO"
    excerpt: "Chamamos de Tempo 3 (T3) o tempo de reação do goleiro no momento do arremesso e execução do movimento de defesa."
    interpretation: "Define o Tempo 3 (T3) como o tempo de reação e a execução da técnica defensiva ajustada à trajetória\
      \ da bola."
  - id: "EVID_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0_007"
    source_id: "SRC_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0"
    locator: "p. 5, Seção 8. Tempo de Organização após a Defesa/Gol (T4)"
    evidence_type: "DERIVACAO"
    excerpt: "Sendo assim, chamamos de Tempo 4 (T4) o tempo de organização ofensiva após a defesa ou gol."
    interpretation: "Define o Tempo 4 (T4) como o estágio de transição e organização ofensiva imediata promovida pelo goleiro\
      \ após intercepção ou sofrer gol."
  - id: "EVID_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0_008"
    source_id: "SRC_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0"
    locator: "p. 4, Seção 4. Estágios da Defesa"
    evidence_type: "FATO"
    excerpt: "No handebol de praia, o tempo do arremesso é diferenciado em quase todos os aspectos, por ter a opção de gols\
      \ espetaculares que valem 2 pontos, gol de aérea e gol de giro 360°."
    interpretation: "Destaca as características específicas de pontuação e técnica de arremesso que alteram o tempo defensivo\
      \ na praia."
  - id: "EVID_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0_009"
    source_id: "SRC_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0"
    locator: "p. 5, Seção 8. Tempo de Organização após a Defesa/Gol (T4)"
    evidence_type: "REGRA"
    excerpt: "No handebol de praia não há o tiro de saída tradicional como no handebol indoor, com isso todas as primeiras\
      \ ações ofensivas partem do goleiro."
    interpretation: "Menciona a regra de ausência de tiro de saída tradicional, determinando a obrigatoriedade da transição\
      \ ofensiva iniciar pelo goleiro."
  - id: "EVID_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533_001"
    source_id: "SRC_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533"
    locator: "p. 1 (passage 1)"
    evidence_type: "SUPORTE"
    excerpt: "This publication focuses on the psychological dynamics of the shootout in beach handball."
    interpretation: "A publicação tem como foco central a análise e aplicação das dinâmicas psicológicas durante as disputas\
      \ de shoot-out no handebol de praia."
  - id: "EVID_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533_002"
    source_id: "SRC_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533"
    locator: "p. 1 (passage 1)"
    evidence_type: "SUPORTE"
    excerpt: "These situations, occurring when the immediate winner must be determined typically after regular time or overtime\
      \ have failed to produce a decisive result - significantly increase the psychological demands placed on the athletes."
    interpretation: "Definição do contexto do shoot-out como fase desempate decisiva após o tempo regulamentar, a qual eleva\
      \ exponencialmente as exigências psicológicas sobre os atletas."
  - id: "EVID_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533_003"
    source_id: "SRC_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533"
    locator: "p. 2 (passage 3)"
    evidence_type: "FATO"
    excerpt: "Unlike the continuous flow of regular gameplay, the shootout format imposes a unique combination of cognitive,\
      \ emotional, and physiological stressors."
    interpretation: "O formato de shoot-out distingue-se do fluxo contínuo do jogo regular por impor uma combinação singular\
      \ de estressores cognitivos, emocionais e fisiológicos."
  - id: "EVID_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533_004"
    source_id: "SRC_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533"
    locator: "p. 3 (passage 9)"
    evidence_type: "SUPORTE"
    excerpt: "Deep breathing: controlled breathing helps regulate physiological arousal by activating the parasympathetic\
      \ nervous system, reducing tension, and promoting a state of calm focus"
    interpretation: "A respiração profunda e controlada é recomendada como técnica de regulação fisiológica para reduzir a\
      \ tensão muscular e promover foco calmo durante o shoot-out."
  - id: "EVID_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533_005"
    source_id: "SRC_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533"
    locator: "p. 17 (passage 67)"
    evidence_type: "FATO"
    excerpt: "Unlike shooters, who prepare to initiate an action, goalkeepers must respond to highly dynamic and unpredictable\
      \ stimuli under extreme time constraints."
    interpretation: "Diferenciação do papel tático-psicológico: o arremessador inicia a ação planejada, enquanto o goleiro\
      \ responde de forma reativa a estímulos dinâmicos e imprevisíveis em intervalo de tempo mínimo."
  - id: "EVID_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533_006"
    source_id: "SRC_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533"
    locator: "p. 28 (passage 115)"
    evidence_type: "SUPORTE"
    excerpt: "When athletes mentally rehearse high-stakes scenarios-such as walking to the 6-metre line, facing the goalkeeper,\
      \ or responding to crowd noise-they build a sense of psychological readiness."
    interpretation: "A prática de ensaio mental (visualização do deslocamento até a linha de 6 metros e do duelo com o goleiro)\
      \ desenvolve a prontidão psicológica do atleta."
  - id: "EVID_CEPRAEA_DATABASE_CCB2A718_001"
    source_id: "SRC_CEPRAEA_DATABASE_CCB2A718"
    locator: "Aba DB_CONFIG, linha architecture_role"
    evidence_type: "REGRA"
    excerpt: "Fonte primária de dados para alimentar o frontend."
    interpretation: "Define o papel arquitetural da base de dados como fonte única de verdade (SSOT Operacional) para integração\
      \ com as camadas de apresentação do frontend."
  - id: "EVID_CEPRAEA_DATABASE_CCB2A718_002"
    source_id: "SRC_CEPRAEA_DATABASE_CCB2A718"
    locator: "Aba DB_CONFIG, linha business_rule_competicoes_visiveis"
    evidence_type: "REGRA"
    excerpt: "Abas mensais e agendas operacionais devem mostrar apenas competições das quais o CEPRAEA participará ou participou.\
      \ Eventos sem participação permanecem no database para auditoria, mas não devem ser exibidos no frontend."
    interpretation: "Estabelece a regra de negócio que limita a visibilidade no frontend apenas a competições com participação\
      \ factual da equipe."
  - id: "EVID_CEPRAEA_DATABASE_CCB2A718_003"
    source_id: "SRC_CEPRAEA_DATABASE_CCB2A718"
    locator: "Aba DB_CONFIG, linha canonical_factual_presence_sheet"
    evidence_type: "DECISAO"
    excerpt: "SSOT canônica de presença factual. Nenhuma proposta ou autorrelato é promovido sem confirmação autorizada do\
      \ treinador."
    interpretation: "Determina a política de governança exigindo autorização explícita do treinador para que qualquer proposta\
      \ de presença seja convertida em fato em DB_PRESENCA."
  - id: "EVID_CEPRAEA_DATABASE_CCB2A718_004"
    source_id: "SRC_CEPRAEA_DATABASE_CCB2A718"
    locator: "Aba DB_CONFIG, linha goalkeeper_semantics"
    evidence_type: "DECISAO"
    excerpt: "Decisão humana 2026-08-10: GOLEIRA é posição, não função; pertence à função DEFESA."
    interpretation: "Sintetiza a decisão taxonômica de modelagem semântica das atletas que atuam no gol."
  - id: "EVID_CEPRAEA_DATABASE_CCB2A718_005"
    source_id: "SRC_CEPRAEA_DATABASE_CCB2A718"
    locator: "Aba DB_CONFIG, linha game_participation_entry_policy"
    evidence_type: "REGRA"
    excerpt: "Quando a convocação oficial contém 12 atletas e o limite por partida é 10, o treinador pode informar as 2 atletas\
      \ que ficaram de fora; as demais 10 são materializadas como JOGOU, salvo exceção explícita."
    interpretation: "Define o procedimento determinístico de registro de participação individual em partidas através do método\
      \ de exclusão."
  - id: "EVID_CEPRAEA_DATABASE_CCB2A718_006"
    source_id: "SRC_CEPRAEA_DATABASE_CCB2A718"
    locator: "Aba DB_CONFIG, linha RN-DISP-001"
    evidence_type: "REGRA"
    excerpt: "Disponibilidade ou compromisso declarado expressa intenção/compromisso prospectivo e não constitui presença\
      \ factual."
    interpretation: "Regra normativa que impede a reinterpretação automática ou fusão entre declaração prospectiva de disponibilidade\
      \ e presença factual."
  - id: "EVID_CEPRAEA_DATABASE_CCB2A718_007"
    source_id: "SRC_CEPRAEA_DATABASE_CCB2A718"
    locator: "Aba DB_COMPETICOES, linha COMP-2026-001"
    evidence_type: "FATO"
    excerpt: "CEPRAEA campeã adulta feminina. Calendário CBHb 2026 confirma Copa Brasil de 26/03 a 29/03/2026 em João Pessoa/PB."
    interpretation: "Registro factual do título conquistado na Copa Brasil Adulto de Handebol de Praia 2026."
  - id: "EVID_CEPRAEA_DATABASE_CCB2A718_008"
    source_id: "SRC_CEPRAEA_DATABASE_CCB2A718"
    locator: "Aba DB_COMPETICOES, linha COMP-2026-012"
    evidence_type: "FATO"
    excerpt: "Etapa Final Adulto Feminino concluída em São Miguel do Iguaçu/PR. CEPRAEA disputou seis jogos: J51 2x0 ADM Maricá;\
      \ J59 2x0 A. Bud's Handbeach; J71 2x1 APCEF/CT Rossana Marques (placar do shoot-out não documentado no boletim); J79\
      \ 2x0 Porto 360º/Talentos; J91 2x1 IDEC; J101 derrota por 0x2 para Campinas 360° Nas Areias."
    interpretation: "Registro factual consolidado da campanha e do vice-campeonato do CEPRAEA na Etapa Final do Circuito Brasileiro\
      \ 2026."
  - id: "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_001"
    source_id: "SRC_04A_MODELO_CONCEITUAL_MD_D7C900D7"
    locator: "Tab 1, METADADOS_SISTEMA"
    evidence_type: "FATO"
    excerpt: "TITULO_CANONICO: 04A — Modelo Conceitual — CEPRAEA Beach Pro\n\nSTATUS: ATIVO\n\nVERSAO: v1.0.0\n\nDOMINIO_PROPRIETARIO:\
      \ davisermenho@handballtrack.app\n\nCATEGORIA: Arquitetura Técnica / Dados\n\nAUTORIDADE: Davi Sermenho"
    interpretation: "Metadados de identificação, versão, proprietário e classificação de autoridade do documento técnico de\
      \ modelagem de dados."
  - id: "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_002"
    source_id: "SRC_04A_MODELO_CONCEITUAL_MD_D7C900D7"
    locator: "Seção 04A — MODELO CONCEITUAL — CEPRAEA BEACH PRO"
    evidence_type: "DECISAO"
    excerpt: "Estado: APPROVED — homologado pelo Steward em 2026-08-07T15:02:00-03:00 como Modelo Conceitual vigente da fase\
      \ de reconciliação."
    interpretation: "Declaração de aprovação formal do modelo pelo Steward em 07/08/2026."
  - id: "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_003"
    source_id: "SRC_04A_MODELO_CONCEITUAL_MD_D7C900D7"
    locator: "Seção 3. DOMÍNIOS CONCEITUAIS, item B"
    evidence_type: "REGRA"
    excerpt: "Não existe propriedade canônica única “atleta ativa”."
    interpretation: "Restrição de modelagem que impede a representação da condição de atleta ativa por um indicador booleano\
      \ simplificado."
  - id: "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_004"
    source_id: "SRC_04A_MODELO_CONCEITUAL_MD_D7C900D7"
    locator: "Seção 3. DOMÍNIOS CONCEITUAIS, item C"
    evidence_type: "REGRA"
    excerpt: "Atribuição Tática; FUNÇÃO {ATAQUE, DEFESA}; SISTEMA {ATAQUE→3X1|4X0; DEFESA→3X0|2X1}; POSIÇÃO conforme mapping\
      \ aprovado; PAPEL_TATICO ESPECIALISTA_CORINGA ortogonal e permitido apenas em atribuições ofensivas."
    interpretation: "Regras do domínio de estrutura tática e limitação do papel de especialista/coringa exclusivamente para\
      \ atribuições ofensivas."
  - id: "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_005"
    source_id: "SRC_04A_MODELO_CONCEITUAL_MD_D7C900D7"
    locator: "Seção 3. DOMÍNIOS CONCEITUAIS, item G"
    evidence_type: "REGRA"
    excerpt: "Competição → Edição → Divisão → Etapa → Partida → Segmento da Partida. Eixos paralelos: Equipe → Inscrição;\
      \ Etapa → Relação Nominal; Partida → Escalação; Escalação ≠ Participação Efetiva."
    interpretation: "Definição da hierarquia do domínio de competição e segregação conceitual entre os objetos de Inscrição,\
      \ Relação Nominal, Escalação e Participação Efetiva."
  - id: "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_006"
    source_id: "SRC_04A_MODELO_CONCEITUAL_MD_D7C900D7"
    locator: "Seção 4. RELAÇÕES CONCEITUAIS MÍNIMAS"
    evidence_type: "REGRA"
    excerpt: "A pontuação FHERJ 2026 está governada por SGATE-0023: posições 1..7 validadas em 16/13/11/10/9/8/7; o Art. 25º\
      \ armazenado está STALE_FOR_SCORING e valores não verificados não podem ser inferidos. SGATE-0024 governa a exceção\
      \ final de Campinas/SP."
    interpretation: "Mapeamento da regra de negócio para o cálculo de pontos do campeonato FHERJ 2026, com sinalização de\
      \ que o regulamento em arquivo encontra-se desatualizado (STALE) nessa matéria."
  - id: "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_007"
    source_id: "SRC_04A_MODELO_CONCEITUAL_MD_D7C900D7"
    locator: "Seção 6. RESTRIÇÕES CONCEITUAIS"
    evidence_type: "REGRA"
    excerpt: "GOLEIRA não pode ser reintroduzida como FUNÇÃO da taxonomia TACT V2 sem novo Semantic Change APPROVED."
    interpretation: "Invariante de governança semântica bloqueando a reutilização do termo GOLEIRA como função na versão 2\
      \ da taxonomia tática."
  - id: "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_008"
    source_id: "SRC_04A_MODELO_CONCEITUAL_MD_D7C900D7"
    locator: "Seção 9. ATUALIZAÇÃO CONCEITUAL — PONTUAÇÃO E RANKING FHERJ 2026"
    evidence_type: "DECISAO"
    excerpt: "Evidência: SGATE-0023 APPROVED, SGATE-0024 APPROVED, DEC-DATA-042 APPROVED e instrução direta do Steward em\
      \ 2026-08-08T05:50:00-03:00."
    interpretation: "Aprovação de atualização do modelo conceitual para suportar regras e exceções de cálculo do ranking FHERJ\
      \ 2026."
  - id: "EVID_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_009"
    source_id: "SRC_04A_MODELO_CONCEITUAL_MD_D7C900D7"
    locator: "Seção 10. ATUALIZAÇÃO CONCEITUAL — PLANO DE PARTICIPAÇÃO DA SESSÃO"
    evidence_type: "REGRA"
    excerpt: "Invariantes: disponibilidade != plano; compromisso da atleta != plano; Grupo Treinável != plano; Convocação\
      \ != plano; plano != presença factual; derivação != decisão humana."
    interpretation: "Conjunto de invariantes conceituais que garantem a separação rigorosa entre planejamento, intenção, convocação\
      \ e presença realizada."
  - id: "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_001"
    source_id: "SRC_04B_MODELO_LOGICO_MD_FFCFA1B3"
    locator: "METADADOS_SISTEMA"
    evidence_type: "FATO"
    excerpt: "TITULO_CANONICO: 04B — MODELO LÓGICO — CEPRAEA BEACH PRO"
    interpretation: "Proposta de título canônico registrada no cabeçalho de metadados do documento."
  - id: "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_002"
    source_id: "SRC_04B_MODELO_LOGICO_MD_FFCFA1B3"
    locator: "Seção 1. FINALIDADE"
    evidence_type: "REGRA"
    excerpt: "Tipar objetos, atributos, multiplicidades, identificadores lógicos, unicidades semânticas, temporalidade e constraints\
      \ declarativas."
    interpretation: "Definição do escopo e objetivo da modelagem lógica."
  - id: "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_003"
    source_id: "SRC_04B_MODELO_LOGICO_MD_FFCFA1B3"
    locator: "Seção 3.1 ATHLETE"
    evidence_type: "REGRA"
    excerpt: "Regra: não existe atributo canônico único active/status_ativo."
    interpretation: "Regra determinando que o estado ativo não é um booleano global, dependendo de vínculo, elegibilidade\
      \ e acesso independentes."
  - id: "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_004"
    source_id: "SRC_04B_MODELO_LOGICO_MD_FFCFA1B3"
    locator: "Seção 3.8 SESSION_REALIZATION"
    evidence_type: "REGRA"
    excerpt: "Regra: realização é FATO e exige evidência autorizada."
    interpretation: "Exigência de evidência autorizada para comprovação factual da realização de sessão."
  - id: "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_005"
    source_id: "SRC_04B_MODELO_LOGICO_MD_FFCFA1B3"
    locator: "Seção 3.25 CARIOCA_2026_SCORING_RULE"
    evidence_type: "DECISAO"
    excerpt: "Estado lógico: APPROVED_WITH_VERIFIED_RANGE por SGATE-0023. Mapeamento FHERJ 2026 validado para posições 1..7\
      \ = {1:16,2:13,3:11,4:10,5:9,6:8,7:7}."
    interpretation: "Tabela de pontuação por colocação homologada para o intervalo de 1ª a 7ª posições no Circuito FHERJ 2026."
  - id: "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_006"
    source_id: "SRC_04B_MODELO_LOGICO_MD_FFCFA1B3"
    locator: "Seção 7. STOP GATE FÍSICO"
    evidence_type: "REGRA"
    excerpt: "Nenhum elemento deste documento é DDL. Não converter tipos abstratos, identificadores ou referências em tipos/chaves\
      \ específicos de PostgreSQL nesta fase."
    interpretation: "Restrição proibindo a conversão do modelo lógico em DDL física para SGBD."
  - id: "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_007"
    source_id: "SRC_04B_MODELO_LOGICO_MD_FFCFA1B3"
    locator: "Seção 8. HOMOLOGAÇÃO DA RECONCILIAÇÃO LÓGICA"
    evidence_type: "DECISAO"
    excerpt: "Evidência: aprovação direta do Steward via sessão de governança estrutural em 2026-08-07T15:02:00-03:00."
    interpretation: "Registro da aprovação e homologação do modelo lógico pelo Steward."
  - id: "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_008"
    source_id: "SRC_04B_MODELO_LOGICO_MD_FFCFA1B3"
    locator: "Seção 10.6 EXCEÇÃO CAMPINAS/SP — PROJEÇÃO LÓGICA"
    evidence_type: "DECISAO"
    excerpt: "A exceção não é codificada no objeto TEAM e não cria enumeração geral “equipe de outro estado”. Ela é uma instância\
      \ contextual de FINAL_RANKING_ELIGIBILITY associada à participação de Campinas/SP no Circuito Carioca/FHERJ 2026, com\
      \ eligibility=INELIGIBLE_BY_EXCEPTION efetiva para a classificação final."
    interpretation: "Modelagem contextual do tratamento de inelegibilidade da equipe de Campinas/SP sem alteração da estrutura\
      \ global de equipe."
  - id: "EVID_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_009"
    source_id: "SRC_04B_MODELO_LOGICO_MD_FFCFA1B3"
    locator: "Seção 11.2 CARDINALIDADES NORMATIVAS PARA A PROJEÇÃO LÓGICA"
    evidence_type: "REGRA"
    excerpt: "ATHLETE 1 ↔ 0..N TACTICAL_ASSIGNMENT; cada TACTICAL_ASSIGNMENT refere exatamente 1 ATHLETE."
    interpretation: "Definição da cardinalidade entre atleta e atribuição tática no modelo."
  - id: "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_001"
    source_id: "SRC_04C_DICIONARIO_DE_DADOS_MD_6B0D9716"
    locator: "Cabeçalho do documento"
    evidence_type: "DECISAO"
    excerpt: "04C — DICIONÁRIO DE DADOS CANÔNICO — CEPRAEA BEACH HANDBALL PRO"
    interpretation: "Define o título e a denominação canônica do dicionário de dados do sistema CEPRAEA Beach Handball Pro."
  - id: "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_002"
    source_id: "SRC_04C_DICIONARIO_DE_DADOS_MD_6B0D9716"
    locator: "Cabeçalho do documento - Estado e Versão"
    evidence_type: "DECISAO"
    excerpt: "APPROVED — Reconciliado com 04A (Modelo Conceitual) e 04B (Modelo Lógico)."
    interpretation: "Registra a declaração interna de homologação e reconciliação com os modelos conceitual (04A) e lógico\
      \ (04B)."
  - id: "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_003"
    source_id: "SRC_04C_DICIONARIO_DE_DADOS_MD_6B0D9716"
    locator: "Seção 1 - Classes Epistemológicas"
    evidence_type: "REGRA"
    excerpt: "FATO: Registro observado e verificado de acontecimento real (ex.: presença confirmada pós-treino, súmula de\
      \ jogo)."
    interpretation: "Define a classe epistemológica FATO para acontecimentos reais observados e verificados no sistema."
  - id: "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_004"
    source_id: "SRC_04C_DICIONARIO_DE_DADOS_MD_6B0D9716"
    locator: "Seção 1 - Classes Epistemológicas"
    evidence_type: "REGRA"
    excerpt: "DERIVAÇÃO: Métrica ou indicador recomputado deterministicamente por fórmula/algoritmo sem intervenção manual."
    interpretation: "Define que métricas derivadas são recomputadas deterministicamente por fórmula/algoritmo sem intervenção\
      \ manual."
  - id: "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_005"
    source_id: "SRC_04C_DICIONARIO_DE_DADOS_MD_6B0D9716"
    locator: "Tabela 2.1 - public.athletes"
    evidence_type: "REGRA"
    excerpt: "Cadastro mestre imutável do elenco do CEPRAEA."
    interpretation: "Estabelece a tabela public.athletes como o cadastro mestre imutável do elenco de atletas."
  - id: "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_006"
    source_id: "SRC_04C_DICIONARIO_DE_DADOS_MD_6B0D9716"
    locator: "Tabela 2.6 - public.factual_presences"
    evidence_type: "REGRA"
    excerpt: "A ÚNICA Fonte Primária de Verdade para presenças factuais ocorridas. Nenhuma linha é criada sem homologação\
      \ humana do treinador."
    interpretation: "Define que a tabela public.factual_presences é a única fonte primária de verdade (SSOT) de presença factual,\
      \ exigindo homologação humana do treinador."
  - id: "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_007"
    source_id: "SRC_04C_DICIONARIO_DE_DADOS_MD_6B0D9716"
    locator: "Tabela 2.8 - public.convocations"
    evidence_type: "REGRA"
    excerpt: "Registro formal de convocação da relação nominal de 12 atletas para a etapa."
    interpretation: "Define a convocação por etapa com limite nominal de 12 atletas."
  - id: "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_008"
    source_id: "SRC_04C_DICIONARIO_DE_DADOS_MD_6B0D9716"
    locator: "Tabela 2.8 - public.convocations (coluna max_match_athletes)"
    evidence_type: "REGRA"
    excerpt: "Teto máximo em súmula por partida."
    interpretation: "Registra o teto máximo de atletas que podem compor a súmula por partida."
  - id: "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_009"
    source_id: "SRC_04C_DICIONARIO_DE_DADOS_MD_6B0D9716"
    locator: "Tabela 2.9 - public.matches"
    evidence_type: "REGRA"
    excerpt: "Registro canônico de partidas disputadas pelo CEPRAEA com placar por set e shoot-out."
    interpretation: "Define a estrutura de registro de partidas disputadas com detalhamento de placar por set e shoot-out."
  - id: "EVID_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_010"
    source_id: "SRC_04C_DICIONARIO_DE_DADOS_MD_6B0D9716"
    locator: "Tabela 2.10 - public.match_appearances"
    evidence_type: "REGRA"
    excerpt: "Materialização da atuação factual de cada atleta por partida individual."
    interpretation: "Registra a atuação factual individual de atletas por partida."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_001"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Cabeçalho"
    evidence_type: "DECISAO"
    excerpt: "**Estado:** APPROVED — Reconciliado com 04A (Modelo Conceitual), 04B (Modelo Lógico) e Regulamento IHF 2026."
    interpretation: "Declaração de aprovação e conciliação prévia do catálogo com o modelo conceitual, modelo lógico e Regulamento\
      \ IHF 2026."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_002"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Cabeçalho"
    evidence_type: "DECISAO"
    excerpt: "**Autoridade:** Davi Sermenho (`ROLE-CEPRAEA-DATA-GOVERNANCE-STEWARD`)"
    interpretation: "Identificação da autoridade de governança de dados responsável pelo documento."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_003"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 1, RN-DISP-001"
    evidence_type: "REGRA"
    excerpt: "* **`RN-DISP-001` (Declaração é Intenção, Não Presença):** Disponibilidade declarada ou compromisso expressa\
      \ intenção prospectiva e JAMAIS constitui, promove ou substitui presença factual."
    interpretation: "Regra normativa estabelecendo que disponibilidade declarada expressa intenção e jamais substitui presença\
      \ factual."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_004"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 1, RN-DISP-002"
    evidence_type: "REGRA"
    excerpt: "* **`RN-DISP-002` (Fonte Humana Exclusiva):** A declaração humana de disponibilidade nasce exclusivamente em\
      \ células válidas das abas mensais do frontend."
    interpretation: "Definição do ponto de entrada exclusivo da declaração humana de disponibilidade."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_005"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 1, RN-DISP-003"
    evidence_type: "REGRA"
    excerpt: "* **`RN-DISP-003` (Identidade Canônica):** `athlete_id` (formato `ATH-XXXX` ou `UUID`) é a identidade canônica\
      \ da atleta. Nomes e posições de linha são meros rótulos de exibição."
    interpretation: "Definição de athlete_id no formato ATH-XXXX ou UUID como a chave de identidade canônica da atleta."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_006"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 1, RN-DISP-004"
    evidence_type: "REGRA"
    excerpt: "* **`RN-DISP-004` (Unicidade de Estado Corrente):** A identidade do estado corrente de disponibilidade é a chave\
      \ composta `(event_id, athlete_id)`. Existe no máximo um registro corrente por essa chave."
    interpretation: "Definição da chave composta (event_id, athlete_id) para garantir a unicidade do estado corrente de disponibilidade."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_007"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 1, RN-DISP-005"
    evidence_type: "REGRA"
    excerpt: "* **`RN-DISP-005` (Domínio Estrito de Respostas):** Os estados canônicos permitidos são `'SIM'`, `'NAO'`, `'TALVEZ'`\
      \ e `'SEM_RESPOSTA'`."
    interpretation: "Enumeração do domínio estrito dos quatro estados canônicos de disponibilidade."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_008"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 1, RN-DISP-006"
    evidence_type: "REGRA"
    excerpt: "* **`RN-DISP-006` (Tratamento de Célula Vazia Mapeada):** Uma célula-fonte válida, mapeada e vazia representa\
      \ `'SEM_RESPOSTA'` (nunca `'NAO'`)."
    interpretation: "Definição de que célula vazia mapeada deve ser interpretada como SEM_RESPOSTA e não NAO."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_009"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 1, RN-DISP-007"
    evidence_type: "REGRA"
    excerpt: "* **`RN-DISP-007` (Evento sem Célula Mapeada):** Evento do calendário sem célula-fonte mapeada no frontend não\
      \ gera registro e não pode ser convertido artificialmente em `'SEM_RESPOSTA'`."
    interpretation: "Proibição de geração artificial de registros para eventos sem célula mapeada."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_010"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 1, RN-DISP-008"
    evidence_type: "REGRA"
    excerpt: "* **`RN-DISP-008` (Operação de Upsert):** Quando a atleta altera sua declaração, o novo valor atualiza o mesmo\
      \ estado corrente identificado por `(event_id, athlete_id)`, sem criar duplicatas concorrentes."
    interpretation: "Regra de operação de upsert sobre a chave (event_id, athlete_id) ao alterar declaração."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_011"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 1, RN-DISP-009"
    evidence_type: "REGRA"
    excerpt: "* **`RN-DISP-009` (Limpeza de Resposta):** Se uma resposta existente for apagada em célula-fonte válida, o estado\
      \ corrente passa a `'SEM_RESPOSTA'` (não deleta a linha do banco)."
    interpretation: "Regra determinando que a limpeza de célula altera o estado para SEM_RESPOSTA sem excluir a linha."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_012"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 1, RN-DISP-010"
    evidence_type: "REGRA"
    excerpt: "* **`RN-DISP-010` (Fail-Closed na Resolução de Identidade):** Se atleta ou evento não puderem ser resolvidos\
      \ de forma única, nenhuma escrita é permitida em `availability_declarations`. O caso deve falhar fechado (*Fail-Closed*)."
    interpretation: "Aplicação da diretriz Fail-Closed impedindo escritas em availability_declarations quando a resolução\
      \ da identidade for ambígua."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_013"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 1, RN-DISP-011"
    evidence_type: "REGRA"
    excerpt: "* **`RN-DISP-011` (Invalidação por Mudança de Data):** Mudança material da data de um evento invalida o uso\
      \ operacional da disponibilidade declarada para a data anterior; o histórico deve ser preservado e uma nova declaração\
      \ recolhida."
    interpretation: "Regra de invalidação operacional de declaração em caso de alteração de data do evento, mantendo histórico."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_014"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 1, RN-DISP-012"
    evidence_type: "REGRA"
    excerpt: "* **`RN-DISP-012` (Filtragem de Visibilidade Operacional):** As agendas operacionais devem solicitar/exibir\
      \ disponibilidade apenas de competições em que o CEPRAEA participará ou participou (`SOMENTE_PARTICIPACAO_CEPRAEA`)."
    interpretation: "Regra de visibilidade restringindo exibição de agendas apenas a competições com participação do CEPRAEA."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_015"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 1, RN-DISP-013"
    evidence_type: "REGRA"
    excerpt: "* **`RN-DISP-013` (Elegibilidade do Evento):** Somente evento canônico com `accepts_availability = true` pode\
      \ receber declaração pelo fluxo de disponibilidade."
    interpretation: "Condição obrigatória da flag accepts_availability para permitir recebimento de disponibilidade."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_016"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 1, RN-DISP-014"
    evidence_type: "REGRA"
    excerpt: "* **`RN-DISP-014` (Imutabilidade do Estado do Evento pelo Sincronizador):** O sincronizador de disponibilidade\
      \ não possui autoridade para alterar status/estado do evento no calendário."
    interpretation: "Restrição de escopo que veda ao sincronizador de disponibilidade alterar o status dos eventos."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_017"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 1, RN-DISP-015"
    evidence_type: "REGRA"
    excerpt: "* **`RN-DISP-015` (Isolamento entre Disponibilidade e Presença):** Nenhuma disponibilidade declarada ou autorrelato\
      \ é promovido automaticamente a fato em `factual_presences`."
    interpretation: "Isolamento garantindo que declarações e autorrelatos jamais sejam promovidos automaticamente a fatos\
      \ de presença."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_018"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 1, RN-DISP-016"
    evidence_type: "REGRA"
    excerpt: "* **`RN-DISP-016` (Normalização de Entrada):** Normalização obrigatória de caixa e acentos (`TRIM`, caixa alta).\
      \ Valores inválidos devem falhar sem escrita silenciosa."
    interpretation: "Obrigatoriedade de sanitização de entrada com TRIM e caixa alta, e falha explícita em valores inválidos."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_019"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 1, RN-DISP-017"
    evidence_type: "REGRA"
    excerpt: "* **`RN-DISP-017` (Expansão de Eventos Multidiários):** Quando uma única célula representa explicitamente uma\
      \ competição multidiária, a declaração vale para todos os eventos diários canônicos pertencentes ao intervalo."
    interpretation: "Regra de propagação de declaração única para todos os dias de evento multidiário."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_020"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 2, DEC-DATA-045.1"
    evidence_type: "REGRA"
    excerpt: "* **`DEC-DATA-045.1` (Single Source of Truth de Presença):** A tabela `public.factual_presences` é a ÚNICA fonte\
      \ de verdade para presenças factuais."
    interpretation: "Definição de public.factual_presences como a única fonte de verdade para registro factual de presenças."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_021"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 2, DEC-DATA-045.2"
    evidence_type: "REGRA"
    excerpt: "* **`DEC-DATA-045.2` (Fila Transitória):** As respostas do formulário *Wellness Pós-Treino* alimentam exclusivamente\
      \ a tabela `public.presence_proposals` com estado `'AGUARDANDO_CONFIRMACAO'`."
    interpretation: "Roteamento das respostas do formulário Wellness Pós-Treino para public.presence_proposals no estado AGUARDANDO_CONFIRMACAO."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_022"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 2, DEC-DATA-045.3"
    evidence_type: "DECISAO"
    excerpt: "* **`DEC-DATA-045.3` (Gate Humano do Treinador):** A conversão de proposta em presença factual exige a ação\
      \ explícita e autenticada do treinador (`'CONFIRMAR_PROPOSTA'`, `'AJUSTAR_FULL'`, `'AJUSTAR_PARTIAL'`, `'REJEITAR_PROPOSTA'`)."
    interpretation: "Exigência de intervenção e decisão explícita autenticada do treinador para converter proposta em presença\
      \ factual."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_023"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 2, DEC-DATA-045.4"
    evidence_type: "REGRA"
    excerpt: "* **`DEC-DATA-045.4` (Auditoria Mandatória):** Todo registro factual em `public.factual_presences` grava obrigatoriamente\
      \ `confirmed_by` (nome e papel do treinador) e `confirmed_at` (timestamp estático)."
    interpretation: "Obrigatoriedade de gravação dos campos de auditoria confirmed_by e confirmed_at em factual_presences."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_024"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 3, REG-IHF-001"
    evidence_type: "REGRA"
    excerpt: "* **`REG-IHF-001` (Súmula de Partida - Regra IHF 4):** Limite máximo de **10 jogadoras uniformizadas em súmula\
      \ por partida**, com no máximo 4 jogadoras em quadra (3 de linha e 1 goleira)."
    interpretation: "Especificação da regra da IHF fixando o limite de 10 jogadoras em súmula e 4 simultâneas em quadra."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_025"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 3, REG-IHF-002"
    evidence_type: "REGRA"
    excerpt: "* **`REG-IHF-002` (Regra `TWO_EXCLUDED_OF_TWELVE`):** Quando a convocação oficial da etapa contém 12 atletas,\
      \ a comissão informa as 2 ausentes da partida (`participation_status = 'NAO_JOGOU'`); as outras 10 são materializadas\
      \ como `'JOGOU'`."
    interpretation: "Regra operacional para seleção e exclusão das 2 atletas excedentes quando houver convocação de 12 para\
      \ partida."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_026"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 3, REG-IHF-003"
    evidence_type: "DERIVACAO"
    excerpt: "* **`REG-IHF-003` (Validação de Pontuação de Partida):** Partida de handebol de praia é disputada em 2 sets\
      \ independentes + Shoot-out em caso de empate (1 x 1). Vitória exige vencer 2 sets ou o Shoot-out. `sets_won_cepraea`\
      \ e `cepraea_victory` são derivados deterministicamente por fórmula armazenada."
    interpretation: "Regra de derivação determinística do resultado do jogo (sets e vitória) baseada na estrutura oficial\
      \ de sets e shoot-out do handebol de praia."
  - id: "EVID_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_027"
    source_id: "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    locator: "Seção 3, SGATE-0023 / DEC-DATA-042"
    evidence_type: "REGRA"
    excerpt: "* **`SGATE-0023` / `DEC-DATA-042` (Pontuação FHERJ 2026):** Mapeamento de pontuação por etapa do Circuito Carioca\
      \ 2026 validado para as posições 1ª a 7ª: `{1ª:16, 2ª:13, 3ª:11, 4ª:10, 5ª:9, 6ª:8, 7ª:7}`. O Artigo 25º da cópia armazenada\
      \ está classificado como `STALE_FOR_SCORING`. Posições 8+ sem tabela validada retornam `INDETERMINATE`."
    interpretation: "Mapeamento da tabela de pontuação FHERJ 2026 da 1ª à 7ª posição, com indicação de pendência/obsolescência\
      \ do Artigo 25º e retorno INDETERMINATE para posições 8+."
  - id: "EVID_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB_001"
    source_id: "SRC_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB"
    locator: "Cabeçalho / Metadados do Documento"
    evidence_type: "DECISAO"
    excerpt: "Estado: APPROVED — Reconciliado com 04A (Modelo Conceitual) e 04B (Modelo Lógico)."
    interpretation: "Registro de aprovação e alinhamento interno da matriz física de cardinalidades com o modelo conceitual\
      \ (04A) e o modelo lógico (04B)."
  - id: "EVID_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB_002"
    source_id: "SRC_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB"
    locator: "Seção 1. VISÃO GERAL DAS ASSOCIAÇÕES RELACIONAIS"
    evidence_type: "REGRA"
    excerpt: "O modelo físico do CEPRAEA Beach Handball Pro elimina ambiguidades através da especificação rigorosa de cardinalidades\
      \ mínimas e máximas em ambos os sentidos da relação, acompanhadas das regras de integridade referencial (ON DELETE RESTRICT\
      \ / CASCADE) e de isolamento de histórico."
    interpretation: "Diretriz de engenharia de dados exigindo definição bidirecional de cardinalidades e políticas explícitas\
      \ de ON DELETE para preservação do histórico esportivo."
  - id: "EVID_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB_003"
    source_id: "SRC_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB"
    locator: "Seção 2. MATRIZ DE CARDINALIDADES — Linha public.convocations / public.athletes"
    evidence_type: "REGRA"
    excerpt: "| public.convocations | 1 ↔ 0..12 | public.athletes (via convocation_athletes) | N ↔ 1..N | Tabela associativa\
      \ public.convocation_athletes | RESTRICT (ambos os lados) — Relação nominal de 12 convocadas. |"
    interpretation: "Especificação de cardinalidade (máximo de 12 atletas) e regra de integridade referencial RESTRICT para\
      \ convocações de etapa."
  - id: "EVID_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB_004"
    source_id: "SRC_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB"
    locator: "Seção 2. MATRIZ DE CARDINALIDADES — Linha public.matches / public.athletes"
    evidence_type: "REGRA"
    excerpt: "| public.matches | 1 ↔ 0..10 | public.athletes (via match_appearances) | N ↔ 1..N | Tabela associativa public.match_appearances\
      \ | RESTRICT (ambos os lados) — Roster ativo de 10 jogadoras por partida. |"
    interpretation: "Especificação de cardinalidade limitando o roster ativo em partida a no máximo 10 jogadoras, com restrição\
      \ RESTRICT em ambos os lados."
  - id: "EVID_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB_005"
    source_id: "SRC_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB"
    locator: "Seção 2. MATRIZ DE CARDINALIDADES — Linha public.matches / public.possessions"
    evidence_type: "REGRA"
    excerpt: "| public.matches | 1 ↔ 0..N | public.possessions | N ↔ 1 | possessions.match_id (FK) | CASCADE — Deletar posses\
      \ de scout se a partida for removida em ambiente de teste. |"
    interpretation: "Regra de integridade referencial definindo CASCADE para remoção de posses vinculadas a partidas em ambiente\
      \ de teste."
  - id: "EVID_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB_006"
    source_id: "SRC_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB"
    locator: "Seção 2. MATRIZ DE CARDINALIDADES — Linha public.bous / public.finalizations"
    evidence_type: "REGRA"
    excerpt: "| public.bous | 1 ↔ 0..N | public.finalizations | N ↔ 1 | finalizations.bou_id (FK) | SET NULL — Finalização\
      \ em transição pode existir sem BOU. |"
    interpretation: "Regra permitindo que arremessos/finalizações resultantes de transição rápida existam sem vinculação obrigatória\
      \ a uma Unidade Básica de Ataque (BOU)."
  - id: "EVID_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB_007"
    source_id: "SRC_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB"
    locator: "Seção 2. MATRIZ DE CARDINALIDADES — Linha public.finalizations / public.goalkeeper_actions"
    evidence_type: "REGRA"
    excerpt: "| public.finalizations | 1 ↔ 0..1 | public.goalkeeper_actions | 1 ↔ 1 | goalkeeper_actions.finalization_id (FK)\
      \ | CASCADE — Ação de goleira atrelada à tentativa de arremesso. |"
    interpretation: "Relacionamento 1:1 entre a tentativa de finalização e a ação defensiva da goleira com dependência física\
      \ do tipo CASCADE."
  - id: "EVID_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB_008"
    source_id: "SRC_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB"
    locator: "Seção 3.1 public.convocation_athletes (Atletas Convocadas na Etapa)"
    evidence_type: "REGRA"
    excerpt: "Constraint de Negócio: No máximo 12 atletas ativas por convocação de etapa."
    interpretation: "Invariante de negócio operacional limitando a 12 o número máximo de atletas em cada convocação oficial\
      \ de etapa."
  - id: "EVID_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB_009"
    source_id: "SRC_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB"
    locator: "Seção 3.2 public.match_appearances (Súmula de Partida e Participação Factual)"
    evidence_type: "REGRA"
    excerpt: "Constraint de Negócio (TWO_EXCLUDED_OF_TWELVE): No máximo 10 atletas com participation_status = 'JOGOU' por\
      \ partida; exatamente 2 com participation_status = 'NAO_JOGOU' quando vindas de convocação nominal de 12."
    interpretation: "Invariante de negócio formalizando a regra TWO_EXCLUDED_OF_TWELVE para divisão entre ativas (10 jogaram)\
      \ e não ativas (2 cortadas) a partir das 12 convocadas."
  - id: "EVID_SOURCE_05_SCHEMA_POSTGRESQL_SQL_B7F68C42_001"
    source_id: "SRC_05_SCHEMA_POSTGRESQL_SQL_B7F68C42"
    locator: "Linhas 1-7"
    evidence_type: "FATO"
    excerpt: "-- =============================================================================\n-- 05 — MODELO FÍSICO POSTGRESQL\
      \ / SUPABASE — CEPRAEA BEACH HANDBALL PRO\n-- =============================================================================\n\
      -- Estado: APPROVED — Reconciliado com 04A (Conceitual) e 04B (Lógico).\n-- Fuso Horário Padrão: 'America/Sao_Paulo'\n\
      -- Compatibilidade: PostgreSQL 15+ / Supabase\n-- ============================================================================="
    interpretation: "Declaração de cabeçalho do modelo físico PostgreSQL/Supabase, estabelecendo o fuso horário padrão como\
      \ 'America/Sao_Paulo', a compatibilidade com PostgreSQL 15+/Supabase e a alegação histórica de reconciliação com os\
      \ modelos 04A e 04B."
  - id: "EVID_SOURCE_05_SCHEMA_POSTGRESQL_SQL_B7F68C42_002"
    source_id: "SRC_05_SCHEMA_POSTGRESQL_SQL_B7F68C42"
    locator: "Seção 1 (Linhas 12-19)"
    evidence_type: "DECISAO"
    excerpt: "CREATE SCHEMA IF NOT EXISTS public;\nCREATE SCHEMA IF NOT EXISTS private;\n\nCREATE EXTENSION IF NOT EXISTS\
      \ \"uuid-ossp\";\nCREATE EXTENSION IF NOT EXISTS \"pgcrypto\";\n\n-- Set timezone for the current transaction\nSET LOCAL\
      \ timezone = 'America/Sao_Paulo';"
    interpretation: "Definição de infraestrutura do banco de dados com schemas 'public' e 'private', extensões 'uuid-ossp'\
      \ e 'pgcrypto' e fuso horário fixado em 'America/Sao_Paulo'."
  - id: "EVID_SOURCE_05_SCHEMA_POSTGRESQL_SQL_B7F68C42_003"
    source_id: "SRC_05_SCHEMA_POSTGRESQL_SQL_B7F68C42"
    locator: "Seção 2 (Enums táticos e de posições)"
    evidence_type: "REGRA"
    excerpt: "DO \\[ BEGIN\n    CREATE TYPE app_function_enum AS ENUM ('DEFESA', 'ATAQUE', 'INDEFINIDA');\nEXCEPTION WHEN\
      \ duplicate_object THEN NULL; END \\];\n\nDO \\[ BEGIN\n    CREATE TYPE app_position_enum AS ENUM (\n        'GOLEIRA',\
      \ 'CENTRAL', 'LATERAL_ESQUERDA', 'LATERAL_DIREITA', 'PIVO',\n        'DEFENSORA_SOLTA', 'DEFENSORA_BASE', 'DEFENSORA_COBERTURA',\n\
      \        'CENTRAL_DIREITA', 'CENTRAL_ESQUERDA', 'DEFENSORA_AVANCADA'\n    );\nEXCEPTION WHEN duplicate_object THEN NULL;\
      \ END \\];"
    interpretation: "Especificação dos tipos enumerados para representação em banco de dados das funções táticas e posições\
      \ específicas de atletas de handebol de praia."
  - id: "EVID_SOURCE_05_SCHEMA_POSTGRESQL_SQL_B7F68C42_004"
    source_id: "SRC_05_SCHEMA_POSTGRESQL_SQL_B7F68C42"
    locator: "Seção 3 (Tabela provenance_records)"
    evidence_type: "REGRA"
    excerpt: "CREATE TABLE IF NOT EXISTS public.provenance_records (\n    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),\n\
      \    source_document TEXT NOT NULL,\n    provenance_level VARCHAR(10) NOT NULL CHECK (provenance_level IN ('P0','P1','P2','P3','A1','A2','A3','A4','D1')),\n\
      \    epistemological_nature VARCHAR(20) NOT NULL CHECK (epistemological_nature IN ('FATO','DECLARACAO','PLANO','DECISAO','DERIVACAO','INFERENCIA')),\n\
      \    recorded_by TEXT NOT NULL,\n    recorded_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),\n    metadata JSONB\
      \ DEFAULT '{}'::jsonb\n);"
    interpretation: "Modelo de dados para governança da proveniência, definindo restrições CHECK para níveis de proveniência\
      \ (P0-D1) e natureza epistemológica dos fatos registrados."
  - id: "EVID_SOURCE_05_SCHEMA_POSTGRESQL_SQL_B7F68C42_005"
    source_id: "SRC_05_SCHEMA_POSTGRESQL_SQL_B7F68C42"
    locator: "Seção 4 (Tabela athletes)"
    evidence_type: "REGRA"
    excerpt: "CREATE TABLE IF NOT EXISTS public.athletes (\n    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),\n    athlete_code\
      \ VARCHAR(20) UNIQUE NOT NULL,\n    display_name TEXT NOT NULL,\n    primary_function app_function_enum NOT NULL DEFAULT\
      \ 'INDEFINIDA',\n    primary_position app_position_enum NOT NULL,\n    status_active BOOLEAN NOT NULL DEFAULT true,\n\
      \    jersey_number INTEGER CHECK (jersey_number BETWEEN 1 AND 99),\n    jersey_source TEXT,\n    provenance_id UUID\
      \ REFERENCES public.provenance_records(id) ON DELETE SET NULL,\n    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),\n\
      \    updated_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()\n);"
    interpretation: "Definição do cadastro de atletas, impondo restrição ao número da camisa (entre 1 e 99) e chave estrangeira\
      \ para o registro de proveniência."
  - id: "EVID_SOURCE_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E_001"
    source_id: "SRC_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E"
    locator: "linhas 1-6"
    evidence_type: "FATO"
    excerpt: "-- =============================================================================\n-- 06 — MIGRATIONS VERSIONADAS\
      \ E ROLLBACK — CEPRAEA BEACH HANDBALL PRO\n-- =============================================================================\n\
      -- Supabase / PostgreSQL Migration Pipeline\n-- Version: 20261013000001\n-- ============================================================================="
    interpretation: "Cabeçalho de identificação do script de migração para o pipeline Supabase / PostgreSQL do projeto CEPRAEA\
      \ Beach Handball Pro, especificando a versão 20261013000001."
  - id: "EVID_SOURCE_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E_002"
    source_id: "SRC_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E"
    locator: "linhas 8-21"
    evidence_type: "REGRA"
    excerpt: "-- [UP MIGRATION 001: Initial Core Setup]\nBEGIN;\n\nCREATE TABLE IF NOT EXISTS public.schema_migrations (\n\
      \    version VARCHAR(30) PRIMARY KEY,\n    description TEXT NOT NULL,\n    applied_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()\n\
      );\n\nINSERT INTO public.schema_migrations (version, description)\nVALUES ('20261013000001', 'Initial core tables for\
      \ CEPRAEA Beach Handball Pro')\nON CONFLICT (version) DO NOTHING;\n\nCOMMIT;"
    interpretation: "Instruções DDL/DML da migração UP 001 que definem a tabela public.schema_migrations para controle de\
      \ versão do esquema e registram a versão inicial 20261013000001."
  - id: "EVID_SOURCE_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E_003"
    source_id: "SRC_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E"
    locator: "linhas 23-24"
    evidence_type: "DECISAO"
    excerpt: "-- [DOWN / ROLLBACK MIGRATION 001]\n/*"
    interpretation: "Identificador da seção de rollback (DOWN MIGRATION 001) e abertura do bloco de comentário SQL que inativa\
      \ o código de reversão."
  - id: "EVID_SOURCE_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E_004"
    source_id: "SRC_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E"
    locator: "linhas 25-45"
    evidence_type: "DERIVACAO"
    excerpt: "BEGIN;\nDROP TABLE IF EXISTS public.goalkeeper_actions CASCADE;\nDROP TABLE IF EXISTS public.finalizations CASCADE;\n\
      DROP TABLE IF EXISTS public.tactical_events CASCADE;\nDROP TABLE IF EXISTS public.bous CASCADE;\nDROP TABLE IF EXISTS\
      \ public.possessions CASCADE;\nDROP TABLE IF EXISTS public.match_appearances CASCADE;\nDROP TABLE IF EXISTS public.matches\
      \ CASCADE;\nDROP TABLE IF EXISTS public.convocation_athletes CASCADE;\nDROP TABLE IF EXISTS public.convocations CASCADE;\n\
      DROP TABLE IF EXISTS public.competitions CASCADE;\nDROP TABLE IF EXISTS public.factual_presences CASCADE;\nDROP TABLE\
      \ IF EXISTS public.presence_proposals CASCADE;\nDROP TABLE IF EXISTS public.availability_declarations CASCADE;\nDROP\
      \ TABLE IF EXISTS public.calendar_events CASCADE;\nDROP TABLE IF EXISTS public.secondary_positions CASCADE;\nDROP TABLE\
      \ IF EXISTS public.athletes CASCADE;\nDROP TABLE IF EXISTS public.changelog CASCADE;\nDROP TABLE IF EXISTS public.system_config\
      \ CASCADE;\nDROP TABLE IF EXISTS public.provenance_records CASCADE;\nDROP TABLE IF EXISTS public.schema_migrations CASCADE;"
    interpretation: "Comandos DROP TABLE CASCADE listados no rollback, revelando o conjunto de 20 tabelas que compõem o modelo\
      \ de dados previsto para o sistema."
  - id: "EVID_SOURCE_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E_005"
    source_id: "SRC_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E"
    locator: "linhas 47-55"
    evidence_type: "DERIVACAO"
    excerpt: "DROP TYPE IF EXISTS convocation_state_enum;\nDROP TYPE IF EXISTS cepraea_participation_enum;\nDROP TYPE IF EXISTS\
      \ extent_type_enum;\nDROP TYPE IF EXISTS presence_status_enum;\nDROP TYPE IF EXISTS availability_response_enum;\nDROP\
      \ TYPE IF EXISTS app_event_status_enum;\nDROP TYPE IF EXISTS app_event_type_enum;\nDROP TYPE IF EXISTS app_position_enum;\n\
      DROP TYPE IF EXISTS app_function_enum;"
    interpretation: "Comandos DROP TYPE listados no rollback, indicando os 9 tipos enumerados (ENUMs) previstos no esquema\
      \ do banco de dados."
  - id: "EVID_SOURCE_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E_006"
    source_id: "SRC_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E"
    locator: "linhas 57-59"
    evidence_type: "REGRA"
    excerpt: "DELETE FROM public.schema_migrations WHERE version = '20261013000001';\nCOMMIT;\n*/"
    interpretation: "Instrução de remoção do registro de versão na tabela schema_migrations e encerramento do bloco de comentário\
      \ do rollback."
  - id: "EVID_SOURCE_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919_001"
    source_id: "SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919"
    locator: "linha 2 (cabeçalho)"
    evidence_type: "SUPORTE"
    excerpt: "-- 07 — MATRIZ RBAC E POLÍTICAS RLS (SUPABASE) — CEPRAEA BEACH HANDBALL PRO"
    interpretation: "Título do documento técnico e identificação do escopo do artefato para o sistema CEPRAEA Beach Handball\
      \ Pro."
  - id: "EVID_SOURCE_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919_002"
    source_id: "SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919"
    locator: "seção 1 (Habilitar RLS em todas as tabelas expostas)"
    evidence_type: "REGRA"
    excerpt: "ALTER TABLE public.athletes ENABLE ROW LEVEL SECURITY;\nALTER TABLE public.secondary_positions ENABLE ROW LEVEL\
      \ SECURITY;\nALTER TABLE public.calendar_events ENABLE ROW LEVEL SECURITY;\nALTER TABLE public.availability_declarations\
      \ ENABLE ROW LEVEL SECURITY;\nALTER TABLE public.presence_proposals ENABLE ROW LEVEL SECURITY;\nALTER TABLE public.factual_presences\
      \ ENABLE ROW LEVEL SECURITY;\nALTER TABLE public.competitions ENABLE ROW LEVEL SECURITY;\nALTER TABLE public.convocations\
      \ ENABLE ROW LEVEL SECURITY;\nALTER TABLE public.convocation_athletes ENABLE ROW LEVEL SECURITY;\nALTER TABLE public.matches\
      \ ENABLE ROW LEVEL SECURITY;\nALTER TABLE public.match_appearances ENABLE ROW LEVEL SECURITY;\nALTER TABLE public.possessions\
      \ ENABLE ROW LEVEL SECURITY;\nALTER TABLE public.bous ENABLE ROW LEVEL SECURITY;\nALTER TABLE public.tactical_events\
      \ ENABLE ROW LEVEL SECURITY;\nALTER TABLE public.finalizations ENABLE ROW LEVEL SECURITY;\nALTER TABLE public.goalkeeper_actions\
      \ ENABLE ROW LEVEL SECURITY;"
    interpretation: "Obrigação de ativação de Row Level Security (RLS) para 16 tabelas do esquema público."
  - id: "EVID_SOURCE_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919_003"
    source_id: "SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919"
    locator: "seção 2 (Revogar concessões padrão públicas)"
    evidence_type: "DECISAO"
    excerpt: "REVOKE ALL ON ALL TABLES IN SCHEMA public FROM anon, authenticated;"
    interpretation: "Adoção da política de segurança default-deny revogando todas as concessões padrões dos papéis anon e\
      \ authenticated."
  - id: "EVID_SOURCE_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919_004"
    source_id: "SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919"
    locator: "seção 3.1 (Papel anon)"
    evidence_type: "REGRA"
    excerpt: "GRANT SELECT ON public.calendar_events TO anon;\nGRANT SELECT ON public.competitions TO anon;"
    interpretation: "Concessão restrita de leitura pública aos usuários não autenticados (anon) apenas para calendários de\
      \ eventos e competições."
  - id: "EVID_SOURCE_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919_005"
    source_id: "SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919"
    locator: "seção 3.2 (Papel authenticated)"
    evidence_type: "REGRA"
    excerpt: "GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO authenticated;"
    interpretation: "Concessão ampla de manipulação de dados (CRUD) no esquema público aos usuários autenticados, subordinada\
      \ ao controle do RLS."
  - id: "EVID_SOURCE_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919_006"
    source_id: "SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919"
    locator: "seção 4 (Função private.get_current_athlete_id)"
    evidence_type: "REGRA"
    excerpt: "CREATE OR REPLACE FUNCTION private.get_current_athlete_id()\nRETURNS UUID\nLANGUAGE sql\nSECURITY DEFINER\n\
      SET search_path = ''\nSTABLE\nAS \\\\[\n    SELECT id FROM public.athletes \n    WHERE athlete_code = current_setting('request.jwt.claim.athlete_code',\
      \ true)\n    LIMIT 1;\n\\\\];"
    interpretation: "Função de segurança responsável por associar o código de atleta presente na claim JWT ao UUID correspondente\
      \ na tabela public.athletes."
precedence_rules:
  - id: "PRECEDENCE_001"
    higher_authority_source_id: "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    lower_authority_source_id: "SRC_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2"
    scope: "REGRAS_DE_JOGO_E_CAMADA_REGULAMENTAR_DO_SCOUT"
    rationale: "O protocolo de scout determina expressamente que sua camada regulamentar siga as Regras IHF vigentes em 2026."
    evidence_ref_ids:
      - "EVID_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_002"
  - id: "PRECEDENCE_002"
    higher_authority_source_id: "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    lower_authority_source_id: "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    scope: "LEIS_DO_JOGO_E_INTERPRETACAO_ESTADUAL"
    rationale: "O documento estadual declara que seus esclarecimentos se baseiam nas atuais Leis do Jogo de Handebol de Praia\
      \ da IHF."
    evidence_ref_ids:
      - "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_001"
conflicts:
  - id: "CONFLICT_001"
    status: "COMPATIVEL"
    subject_id: "ESTRUTURA_TEMPORAL_DA_PARTIDA_E_PERIODOS"
    source_ids:
      - "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
      - "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    description: "Os dois textos definem dois períodos pontuados separadamente, com duração de 10 minutos cada."
    impact: "Confirma a convergência documental do formato temporal básico da partida."
    resolution: null
    decision_id: null
    evidence_ref_ids:
      - "EVID_IHF_RULES_2026_EN_002"
      - "EVID_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_003"
  - id: "CONFLICT_002"
    status: "SUBSTITUICAO_DEMONSTRADA"
    subject_id: "VIGENCIA_DAS_ATUALIZACOES_IHF_2026"
    source_ids:
      - "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
      - "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    description: "A nota do livro de regras indicava 1º de julho de 2026 para disposições destacadas; a comunicação posterior\
      \ da IHF antecipou para 1º de abril de 2026 as alterações de Beach Handball nela descritas."
    impact: "A vigência deve ser registrada por disposição, distinguindo as alterações cobertas pela comunicação posterior."
    resolution: "Usar 1º de abril de 2026 somente para as alterações de Beach Handball explicitamente abrangidas pela comunicação\
      \ posterior da IHF."
    decision_id: null
    evidence_ref_ids:
      - "EVID_IHF_RULES_2026_EN_001"
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_002"
  - id: "CONFLICT_003"
    status: "COMPLEMENTAR"
    subject_id: "JOGO_PASSIVO"
    source_ids:
      - "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
      - "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    description: "A atualização IHF limita a quatro os passes após o sinal de pré-aviso; o esclarecimento estadual trata da\
      \ recusa intencional de oportunidade clara seguida da obrigação de arremesso pelo recebedor."
    impact: "Os dois critérios devem permanecer distinguíveis no registro de jogo passivo."
    resolution: null
    decision_id: null
    evidence_ref_ids:
      - "EVID_ATUALIZACOES_IHF_2026_MD_02D99F75_004"
      - "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_011"
  - id: "CONFLICT_004"
    status: "COMPLEMENTAR"
    subject_id: "INCORPORACAO_DE_ESCLARECIMENTOS_DE_ARBITRAGEM_NO_CIRCUITO_ESTADUAL"
    source_ids:
      - "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
      - "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    description: "Os esclarecimentos adotam orientações de arbitragem baseadas no Mundial IHF para o Circuito Estadual; o\
      \ regulamento geral exige observância conjunta de suas normas e das normas nacionais e internacionais aplicáveis."
    impact: "Vincula a interpretação operacional de arbitragem ao contexto específico do circuito estadual."
    resolution: null
    decision_id: null
    evidence_ref_ids:
      - "EVID_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_001"
      - "EVID_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_002"
open_issues:
  - id: "ISSUE_IHF_RULES_2026_EN_001"
    status: "ABERTA"
    question: "Quais são as regras/linhas específicas no PDF que contêm o destaque em amarelo mencionado na página 1 (previstas\
      \ para vigorar a partir de 1º de julho de 2026), já que a extração do texto não preserva o estilo visual de cor?"
    affected_ids:
      - "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_IHF_RULES_2026_EN_002"
    status: "ABERTA"
    question: "Existe alguma divergência terminológica ou conceitual relevante entre o texto original oficial em inglês e\
      \ a tradução em português de 29 de maio de 2026 presente nas fontes?"
    affected_ids:
      - "SRC_REGRAS_IHF_BEACH_HANDBALL_2026_EN_PDF_PDF_C96E8C2E"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_001"
    status: "ABERTA"
    question: "Existe alguma divergência pontual de redação ou terminologia entre este documento traduzido e o texto oficial\
      \ em inglês da IHF (regras_ihf_beach_handball_2026_en.pdf.pdf)?"
    affected_ids:
      - "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487_002"
    status: "ABERTA"
    question: "Há regulamentos específicos de entidades nacionais ou regionais (ex.: CBHb ou FEHERJ) que façam ressalvas aos\
      \ regulamentos de uniforme ou infraestrutura previstos nos apêndices?"
    affected_ids:
      - "SRC_REGRAS_DE_HANDEBOL_DE_PRAIA_2026_TRADUCAO_29_DE_MAIO_DE__92E1E487"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_ATUALIZACOES_IHF_2026_MD_02D99F75_001"
    status: "ABERTA"
    question: "Quais são as nuances regulatórias e adaptações específicas para a modalidade de Handebol em Cadeira de Rodas\
      \ 6x6, mencionada apenas de forma correlata no texto?"
    affected_ids:
      - "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_ATUALIZACOES_IHF_2026_MD_02D99F75_002"
    status: "ABERTA"
    question: "Como as normativas das federações nacionais (ex: CBHb) internalizaram a nova contagem limite de 4 passes no\
      \ jogo passivo para as competições do circuito nacional de 2026?"
    affected_ids:
      - "SRC_ATUALIZACOES_IHF_2026_MD_02D99F75"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA_001"
    status: "ABERTA"
    question: "Se a penalidade automática de suspensão mínima de uma partida por desqualificação direta aplica-se apenas no\
      \ âmbito do Circuito Estadual FHERJ ou se segue diretriz padronizada da CBHb e IHF."
    affected_ids:
      - "SRC_ESCLARECIMENTOS_REGRAS_DE_JOGO_PDF_067CB8EA"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_001"
    status: "ABERTA"
    question: "Quais são os adendos específicos e boletins de programação aprovados no Congresso Técnico de 2026 que definem\
      \ as sedes e tabelas detalhadas?"
    affected_ids:
      - "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327_002"
    status: "ABERTA"
    question: "Qual o procedimento de prevalência no caso de atualizações de regras formais de uniforme promulgadas pela IHF\
      \ ao longo do ano de 2026 que colidam com o Art. 19 deste regulamento?"
    affected_ids:
      - "SRC_REGULAMENTO_GERAL_CAMPEONATO_CARIOCA_DE_HANDEBOL_DE_PRAI_85DF0327"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_REGULAMENTO_CBHB_2026_PDF_818BCC8B_001"
    status: "ABERTA"
    question: "O documento contém anotações de trabalho pendentes de edição, sendo necessário verificar se esta minuta reflete\
      \ o texto definitivo aprovado pela diretoria da CBHb."
    affected_ids:
      - "SRC_REGULAMENTO_CBHB_2026_PDF_818BCC8B"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_REGULAMENTO_CBHB_2026_PDF_818BCC8B_002"
    status: "ABERTA"
    question: "Quais os links e diretrizes específicas do Caderno de Encargos e Regras Oficiais que devem preencher as lacunas\
      \ sinalizadas no texto?"
    affected_ids:
      - "SRC_REGULAMENTO_CBHB_2026_PDF_818BCC8B"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_SOURCE_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5_001"
    status: "ABERTA"
    question: "Como o protocolo de scout deve registrar os casos de giros incompletos (<360°) detalhados nos slides 13 a 31\
      \ quando a arbitragem desclassifica a jogada para 1 ponto?"
    affected_ids:
      - "SRC_2_POINT_GOALS_SPIN_AND_IN_FLIGHT_SHOTS_MIN_PDF_923EFFD5"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_SOURCE_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD_001"
    status: "ABERTA"
    question: "Por consistir em um roteiro de apresentação em tópicos acompanhado por trechos em vídeo na palestra original,\
      \ a tipificação formal exata das punições (ex.: exclusão temporária ou desqualificação) deve ser confirmada em conjunto\
      \ com o texto oficial integral das Regras de Jogo da IHF."
    affected_ids:
      - "SRC_6_METRE_THROW_PUNISHMENTS_PDF_D2567ACD"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_001"
    status: "ABERTA"
    question:
      question: "Qual será a concordância interobservador (Kappa de Cohen / Fleiss) obtida na prática durante a execução da\
        \ partida piloto para variáveis sensíveis como estrutura defensiva (DEF_VP) e procedimentos táticos?"
      context: "A guia 11 e o Controle Canônico registram que os parâmetros de confiabilidade e concordância entre observadores\
        \ permanecem pendentes de execução prática no piloto."
    affected_ids:
      - "SRC_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_002"
    status: "ABERTA"
    question:
      question: "A malha espacial de origem em quatro faixas de 3 metros (TAX-006) sem dimensão longitudinal será suficiente\
        \ para responder às perguntas táticas sem necessidade de refinamento futuro?"
      context: "DEC-015 registrou que a ausência da dimensão longitudinal na malha espacial de origem deve ser avaliada durante\
        \ o piloto."
    affected_ids:
      - "SRC_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2_003"
    status: "ABERTA"
    question:
      question: "Qual será a taxa de incidência das categorias residuais 'OTHER_RESTART' (origem de posse) e 'PT_OUTRO' (procedimentos\
        \ táticos) durante o teste com vídeos de broadcast?"
      context: "O protocolo determina que uma ocorrência superior a 20% em categorias residuais exige revisão obrigatória\
        \ do dicionário e do codebook."
    affected_ids:
      - "SRC_PROTOCOLO_DE_SCOUT_BEACH_HANDBALL_05F9B6E2"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56_001"
    status: "ABERTA"
    question: "De que maneira os 11 critérios e 90 categorias do instrumento de observação HOISAN se relacionam com o protocolo\
      \ de scout e a modelagem de eventos de partida do CEPRAEA?"
    affected_ids:
      - "SRC_CONTEXTUAL_FACTORS_AND_DECISION_MAKING_IN_POSITIONAL_ATT_1A033B56"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2_001"
    status: "ABERTA"
    question: "A fonte baseia-se em entrevistas de 2015 com treinadores paulistas, necessitando validação quanto a eventuais\
      \ atualizações de regras IHF posteriores [1, 3, 11]."
    affected_ids:
      - "SRC_O_JOGO_OFENSIVO_DO_HANDEBOL_DE_AREIA_2BD736C2"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A_001"
    status: "ABERTA"
    question: "Não há detalhamento escrito das análises em vídeo mencionadas nos slides (partidas Dinamarca vs Brasil e Dinamarca\
      \ vs Espanha), demandando consulta aos vídeos originais caso se deseje analisar os exemplos práticos."
    affected_ids:
      - "SRC_LATEST_TRENDS_IN_DEFENCE_PDF_9CE6234A"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94_001"
    status: "ABERTA"
    question: "Como as atualizações recentes de arbitragem e interpretação de faltas de 6 metros na área de gol impactam a\
      \ eficácia das ações de bloqueio com salto na área descritas no artigo?"
    affected_ids:
      - "SRC_THE_STRUCTURING_OF_THE_DEFENSIVE_PHASE_OF_BEACH_HANDBALL_16FFDB94"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_001"
    status: "ABERTA"
    question: "As matrizes de dados brutos completas de todas as 85 categorias observadas não constam na íntegra no corpo\
      \ do texto publicado, estando resumidas nos vetores e gráficos de coordenadas polares."
    affected_ids:
      - "SRC_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E_002"
    status: "ABERTA"
    question: "A amostragem abrange a Copa de España de 2016, podendo refletir padrões táticos específicos de clubes espanhóis\
      \ daquele ciclo competitivo."
    affected_ids:
      - "SRC_ESTUDO_DAS_ACOES_DO_GUARDA_REDES_DE_ANDEBOL_DE_PRAIA_ATR_A9DF465E"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0_001"
    status: "ABERTA"
    question: "Como o protocolo de scout CEPRAEA operationaliza a codificação dos tempos T1 a T4 durante o registro de eventos\
      \ observacionais de partidas?"
    affected_ids:
      - "SRC_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0_002"
    status: "ABERTA"
    question: "Existe validação experimental quantitativa demonstrando o impacto direto do treinamento focado em T4 no tempo\
      \ de transição ofensiva da equipe?"
    affected_ids:
      - "SRC_TEMPOS_DE_DEFESA_DO_GOLEIRO_DE_HANDEBOL_DE_PRAIA_PDF_EB0902C0"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533_001"
    status: "ABERTA"
    question: "Data exata de publicação não consta no texto, devendo ser estimada como circa 2025 com base na lista de referências\
      \ bibliográficas."
    affected_ids:
      - "SRC_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533_002"
    status: "ABERTA"
    question: "Inexistência de diretrizes específicas de coleta de dados de scout no documento, exigindo integração com os\
      \ manuais de scout operacionais do CEPRAEA."
    affected_ids:
      - "SRC_UNDERSTANDING_PSYCHOLOGICAL_PRESSURE_IN_BEACH_HANDBALL_S_28248533"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_CEPRAEA_DATABASE_CCB2A718_001"
    status: "ABERTA"
    question: "Ausência do placar individual do shoot-out no jogo J71 (CEPRAEA 2 x 1 APCEF/CT Rossana Marques) no Boletim\
      \ 05 oficial da CBHb."
    affected_ids:
      - "SRC_CEPRAEA_DATABASE_CCB2A718"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_CEPRAEA_DATABASE_CCB2A718_002"
    status: "ABERTA"
    question: "Falta de parciais individuais de sets para os jogos JOGO-2026-025 a JOGO-2026-029 da 4ª Etapa Estadual."
    affected_ids:
      - "SRC_CEPRAEA_DATABASE_CCB2A718"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_001"
    status: "ABERTA"
    question: "Existe um boletim normativo ou aditivo oficial emitido e publicado pela FHERJ que formalize a tabela de pontuação\
      \ 16/13/11/10/9/8/7 (SGATE-0023) utilizada no sistema para substituir o Art. 25º?"
    affected_ids:
      - "SRC_04A_MODELO_CONCEITUAL_MD_D7C900D7"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_SOURCE_04A_MODELO_CONCEITUAL_MD_D7C900D7_002"
    status: "ABERTA"
    question: "As extensões e alterações físicas em PostgreSQL descritas nas seções de atualização do modelo (Seções 9 e 10)\
      \ encontram-se totalmente refletidas e validadas nos arquivos de script de banco de dados do repositório?"
    affected_ids:
      - "SRC_04A_MODELO_CONCEITUAL_MD_D7C900D7"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_001"
    status: "ABERTA"
    question: "Pontuação do Circuito FHERJ 2026 para a 8ª posição em diante permanece não verificada pela publicação operacional\
      \ corrente, retornando INDETERMINATE."
    affected_ids:
      - "SRC_04B_MODELO_LOGICO_MD_FFCFA1B3"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_SOURCE_04B_MODELO_LOGICO_MD_FFCFA1B3_002"
    status: "ABERTA"
    question: "Objetos SESSION_SEGMENT e PLANNED_TRAINING_LOAD possuem bloqueio de implementação/persistência até aprovação\
      \ de métricas e autoridades competentes."
    affected_ids:
      - "SRC_04B_MODELO_LOGICO_MD_FFCFA1B3"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_001"
    status: "ABERTA"
    question: "Qual a data exata de publicação ou atualização do documento 04C, dada a ausência de carimbo de data no cabeçalho?"
    affected_ids:
      - "SRC_04C_DICIONARIO_DE_DADOS_MD_6B0D9716"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_SOURCE_04C_DICIONARIO_DE_DADOS_MD_6B0D9716_002"
    status: "ABERTA"
    question: "Como é gerida a sincronização em tempo de execução caso os modelos 04A ou 04B sofram alterações posteriores\
      \ à v1.0.0?"
    affected_ids:
      - "SRC_04C_DICIONARIO_DE_DADOS_MD_6B0D9716"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_001"
    status: "ABERTA"
    question: "Qual é a tabela de pontuação validada para posições da 8ª em diante no Circuito Carioca FHERJ 2026, visto que\
      \ atualmente retornam INDETERMINATE?"
    affected_ids:
      - "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_002"
    status: "ABERTA"
    question: "Qual o texto atualizado do Artigo 25º do regulamento FHERJ para substituir a versão classificada como STALE_FOR_SCORING?"
    affected_ids:
      - "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7_003"
    status: "ABERTA"
    question: "Qual é a data exata de homologação/emissão da versão v1.0.0, já que não há indicação temporal precisa no documento?"
    affected_ids:
      - "SRC_CATALOGO_REGRAS_INVARIANTES_MD_3A0566A7"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB_001"
    status: "ABERTA"
    question: "A política ON DELETE CASCADE entre partida e posses de scout menciona aplicação em 'ambiente de teste'. Como\
      \ deve ser tratada a integridade referencial dessa relação no ambiente de produção?"
    affected_ids:
      - "SRC_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB_002"
    status: "ABERTA"
    question: "Há total alinhamento entre as cláusulas ON DELETE especificados nesta matriz e as constraints físicas criadas\
      \ nos arquivos de DDL/migrations em PostgreSQL?"
    affected_ids:
      - "SRC_MATRIZ_RELACOES_CARDINALIDADES_MD_43B1FECB"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_SOURCE_05_SCHEMA_POSTGRESQL_SQL_B7F68C42_001"
    status: "ABERTA"
    question: "Como será corrigida a comparação da coluna gerada `sets_won_opponent` na tabela `public.matches`?"
    affected_ids:
      - "SRC_05_SCHEMA_POSTGRESQL_SQL_B7F68C42"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_SOURCE_05_SCHEMA_POSTGRESQL_SQL_B7F68C42_002"
    status: "ABERTA"
    question: "Qual é a data/hora original de criação ou última atualização deste arquivo DDL, dada a ausência de timestamp\
      \ no cabeçalho?"
    affected_ids:
      - "SRC_05_SCHEMA_POSTGRESQL_SQL_B7F68C42"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_SOURCE_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E_001"
    status: "ABERTA"
    question: "Qual arquivo fonte detém o DDL de UP correspondente para a criação das tabelas e enums referenciados na seção\
      \ de rollback?"
    affected_ids:
      - "SRC_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_SOURCE_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E_002"
    status: "ABERTA"
    question: "A versão de migração 20261013000001 foi efetivamente aplicada no banco de dados de produção/staging ou permanece\
      \ apenas como especificação de arquivo?"
    affected_ids:
      - "SRC_06_MIGRATIONS_ROLLBACK_SQL_MD_B809827E"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
  - id: "ISSUE_SOURCE_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919_001"
    status: "ABERTA"
    question: "As tabelas secondary_positions, calendar_events, competitions, convocations, convocation_athletes, matches,\
      \ match_appearances, possessions, bous, tactical_events, finalizations e goalkeeper_actions têm RLS habilitado na Seção\
      \ 1, mas não possuem diretivas CREATE POLICY declaradas no documento."
    affected_ids:
      - "SRC_07_MATRIZ_RBAC_E_POLITICAS_RLS_0BB80919"
    impact: "A reconciliação semântica da fonte permanece parcial."
    required_evidence: "Resposta documentada com localização na fonte pertinente."
    owner: "OPERADOR"
```
