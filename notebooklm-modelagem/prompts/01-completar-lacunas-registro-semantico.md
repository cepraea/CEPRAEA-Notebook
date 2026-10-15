# Prompt 01C — Completar somente as lacunas do registro semântico

Produza um suplemento pequeno para o registro semântico do domínio `PARTIDAS_SCOUT_ANALISE_TATICA`, usando somente evidências existentes no manifesto promovido.

Não repita estes conceitos já recuperados:

`PARTIDA`, `EQUIPE`, `ATLETA`, `GOLEIRA_POSICAO`, `PERIODO_SET`, `GOL_DE_OURO`, `SHOOT_OUT`, `GOL_SIMPLES`, `GOL_DUPLO`, `SPIN_SHOT`, `IN_FLIGHT_SHOT`, `TIRO_SEIS_METROS`, `EXCLUSAO_DISCIPLINAR`, `DESQUALIFICACAO_SEGUNDA_EXCLUSAO`, `CARTAO_AZUL_SUSPENSAO`, `POSSE_DE_BOLA`, `UNIDADE_BASICA_ATAQUE_BOU`, `FASE_TATICA`, `SISTEMA_TATICO`, `ZONA_ANALITICA_QUADRA`, `PROTOCOLO_SCOUT`, `CONFIABILIDADE_OBSERVADOR`, `EVENTO_SCOUT`, `ANALISTA_OBSERVADOR`, `TIMECODE`, `TRECHO_OBSERVADO`.

## Lacunas a verificar

Crie conceitos separados, somente quando houver evidência literal, para:

- competição;
- papel esportivo ou operacional;
- segmento observado;
- placar, estado do placar, evolução do placar e evento de pontuação;
- punição e consequência disciplinar genéricas, sem duplicar as sanções específicas existentes;
- fase ofensiva, fase defensiva e sistema defensivo, sem duplicar os conceitos genéricos existentes;
- ação da goleira;
- ação observada e resultado da ação;
- observação de scout;
- versão do protocolo de scout;
- revisão da observação e estado de revisão;
- mídia ou vídeo;
- proveniência da observação ou do evento.

Se uma lacuna não tiver evidência suficiente, não invente o conceito: registre uma questão em `open_issues` indicando exatamente a ausência documental.

## Contrato estrutural obrigatório

Retorne somente YAML válido, sem título e sem cerca Markdown, com a raiz `semantic_registry`.

Cada item de `concepts` deve conter exatamente:

- `id`, em `UPPER_SNAKE_CASE`;
- `preferred_term`;
- `canonical_name`;
- `classification`: `ENTITY|ATTRIBUTE|EVENT|ROLE|ASSOCIATION|VALUE_OBJECT|STATE|CATALOG|RULE|INDICATOR|SNAPSHOT`;
- `definition`;
- `valid_context`, `invalid_context`, `inclusions`, `exclusions`, `synonyms`, `related_concept_ids` e `allowed_values`, sempre como listas, inclusive quando houver somente um valor ou nenhum;
- `temporality`;
- `privacy_classification`: `PUBLICO|INTERNO|PESSOAL|SENSIVEL|RESTRITO`;
- `status: "PROPOSTO"`;
- `evidence_ref_ids`, sempre como lista contendo somente IDs iniciados por `EVID_` e existentes no manifesto.

Cada item de `rules`, se houver, deve conter exatamente:

- `id`, em `UPPER_SNAKE_CASE`;
- `name`;
- `rule_type`: `DEFINITION|OBLIGATION|PROHIBITION|PERMISSION|CONDITION|EXCEPTION|CLASSIFICATION|CALCULATION|TEMPORAL`;
- `subject_ids`, referenciando conceitos deste suplemento ou os conceitos existentes listados acima;
- `statement`;
- `conditions`, `exceptions`, `valid_context`, `invalid_context`, `implementation_targets`, `verification_test_ids` e `evidence_ref_ids`, sempre como listas;
- `valid_from` e `valid_to`;
- `status: "PROPOSTO"`.

Não proponha decisões para preencher lacunas factuais. Use `decisions: []`.

Cada questão aberta deve usar:

- `id` em `UPPER_SNAKE_CASE`;
- `description`;
- `affected_ids`, como lista;
- `status: "ABERTA"`;
- `evidence_ref_ids`, como lista de IDs `EVID_` existentes ou lista vazia quando a questão documenta ausência de evidência.

Não crie tabelas, colunas, SQL, políticas de acesso, migrações ou questões de infraestrutura. Não converta material científico ou histórico em regra oficial.

Retorne exatamente:

semantic_registry:
  concepts: []
  rules: []
  decisions: []
  open_issues: []
