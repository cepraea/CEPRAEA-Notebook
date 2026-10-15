# Reexecução 08 — Schema PostgreSQL candidato após reconciliação de enforcement

Produza somente o conteúdo de `08-schema-postgresql.candidate.sql`.

Retorne exclusivamente SQL PostgreSQL e comentários SQL iniciados por `--` ou delimitados por `/* ... */`. A primeira linha deve começar com `--`. Não use título Markdown, cercas de código, explicação, YAML ou JSON.

## Fontes selecionadas e autoridade

Use somente estas sete fontes selecionadas:

- `LOGICAL_MODEL@0.1.2`
  - `sha256`: `7a82bd2235897e67338036ba5be67f222ac3fdcf19a05bb919ecb1787824b1cb`
  - `source_id`: `1689f311-fd8c-420e-bf53-593d7d90cd1d`
- `DATA_DICTIONARY@0.1.1`
  - `sha256`: `82ed6eb37a7872bb1eb66c6d853dd3e9d96b53f5a93b4670b67bd489a44c348e`
  - `source_id`: `0f1d2800-6195-4758-be73-a61da4546429`
- `TRACEABILITY_MATRIX@0.1.1`
  - `sha256`: `e2d497b0f96bcc74e9287561a2432d821a0dbd5349b01699acb2d2b50042959e`
  - `source_id`: `8b83dda5-dc87-4562-a1d0-ea2e89558b10`
- `ACCESS_REQUIREMENTS@0.1.0`
  - `sha256`: `bafce57a9d71ef3ea0ba54c79fac585f075d8d0efe5fe22967e62bde6c424c92`
  - `source_id`: `c7f18856-d7c7-4b77-8feb-3266d60337c0`
- `STOP_GATE_PARTIDAS_SCOUT_ANALISE_TATICA@0.2.0`
  - `sha256`: `8034fc8290a814a2cb63d7d43138c8552ea087d787f44566b94393449a2d09f0`
  - `source_id`: `8347d2e6-f0fd-4872-a5f6-b23adae009f3`
- decisão externa do operador do `STAGE_07`
  - `sha256`: `95861272d84e896a0ba82793b63788d8ec070efa284d4100da47b773e1657c66`
  - `source_id`: `167b105a-d750-4d7e-bc53-3da5d56e10f4`
- `STAGE_08_ENFORCEMENT_REVIEW@1.0.0`
  - `sha256`: `8931793affb327caf64a69d6508d97a6e9cee0c178b756c59e82837e704d1d75`
  - `source_id`: `4761f1cf-bf81-463f-bd36-a78ab24786de`

Não use fontes históricas, conversas anteriores nem versões substituídas. Para estrutura, cardinalidade, FKs, unicidades e checks, o modelo lógico v0.1.2 prevalece. Para colunas e tipos, use o dicionário v0.1.1. Para responsabilidade de enforcement, a decisão `STAGE_08_ENFORCEMENT_REVIEW` prevalece.

## Limites autorizados

- Gere somente o schema candidato das mesmas 32 relações autorizadas.
- Não acrescente relações, colunas, views, funções, triggers ou tipos.
- Não execute nem alegue executar SQL.
- Não gere migration, rollback, dados, seeds, grants, revogações, roles, RLS ou início de outro estágio.
- Não implemente como constraint as três invariantes estruturais nem as cinco regras adiadas registradas na decisão de enforcement.
- Não mencione IDs legados proibidos, nem mesmo em comentários.

## Cabeçalho SQL obrigatório

Declare em comentários SQL:

- arquivo `08-schema-postgresql.candidate.sql`;
- `RUN_ID: RUN_20261014_PARTIDAS_SCOUT_001`;
- domínio `PARTIDAS_SCOUT_ANALISE_TATICA`;
- estado `CANDIDATO`;
- alvo `PostgreSQL 15+`, com versão do ambiente `NAO_VERIFICADA`;
- IDs, versões, hashes e source IDs das sete entradas;
- gate `READY_WITH_RESTRICTIONS` e decisão `APPROVED_WITH_RESTRICTIONS`;
- implementação `NAO_INICIADO` e verificação `NAO_EXECUTADO`;
- escopo autorizado de 32 relações.

## DDL obrigatório

1. Não crie o schema `public`; ele já existe no PostgreSQL alvo.
2. Crie somente o schema `private` sem `IF NOT EXISTS`.
3. Declare `CREATE EXTENSION IF NOT EXISTS btree_gist;` como a única exceção autorizada ao veto de `IF NOT EXISTS`, comentando que a dependência ainda não foi verificada no ambiente.
4. Crie exatamente 32 tabelas: os 9 recursos `PUBLICO` em `public` e os 23 recursos `INTERNO` ou `RESTRITO` em `private`, conforme `ACCESS_REQUIREMENTS@0.1.0`.
5. Preserve exatamente as 204 colunas, os tipos PostgreSQL, a nulabilidade e os nomes físicos do dicionário v0.1.1.
6. Emita todas as PKs e as 17 unicidades do modelo lógico v0.1.2, incluindo `UQ_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA` sobre `COMPETICAO_ID`, `EQUIPE_ID`, `VALIDO_DESDE`.
7. Emita exatamente as 59 FKs. Cada FK deve declarar explicitamente `ON DELETE` e `ON UPDATE` conforme `on_delete_semantics` e `on_update_semantics` do modelo lógico.
8. Crie índice de suporte para cada FK ou registre, junto à FK, cobertura por prefixo esquerdo de PK ou `UNIQUE` compatível. Preserve o resultado esperado de 50 índices explícitos e 9 coberturas compatíveis.
9. Use identificadores SQL `lower_snake_case`, sem aspas. Registre o ID lógico em comentário adjacente ao objeto.
10. Não use `serial`, `DROP`, `TRUNCATE`, dados reais ou blocos que silenciem conflitos.

## Cinco CHECKs declarativos

Emita os cinco IDs abaixo como constraints nomeadas, com predicados equivalentes:

- `CHK_PARTIDA_VIGENCIA_2026`: `data_hora_inicio` nula ou em/apos `DATE '2026-04-01'`.
- `CHK_NUMERO_SET_VALIDO`: `numero_set IN (1, 2)`.
- `CHK_SHOOT_OUT_COMPLETUDE`: `COMPLETO` exige as duas pontuações; `PARCIAL` ou `NAO_DOCUMENTADO` exige motivo não vazio e permite pontuações nulas.
- `CHK_ELEGIBILIDADE_RANKING_CONTEXTUAL`: `INELEGIVEL_POR_DECISAO_COLETIVA` exige `motivo_decisao` e `decisao_ref` não vazios. Não tente inferir elegibilidade por UF ou país.
- `CHK_INTERVALO_VIGENCIA_PARTICIPACAO`: `valido_ate IS NULL OR valido_ate > valido_desde`.

Checks adicionais podem existir somente para materializar `allowed_values` do dicionário e devem ter nomes distintos desses cinco IDs.

## Exclusão temporal

Na tabela `PARTICIPACAO_EQUIPE_COMPETICAO`, emita uma constraint executável identificada em comentário como `EXCL_PARTICIPACAO_EQUIPE_COMPETICAO_VIGENCIA`:

- `EXCLUDE USING gist`;
- igualdade para `competicao_id` e `equipe_id`;
- sobreposição `&&` para `tstzrange(valido_desde, valido_ate, '[)')`;
- sem trigger substituto.

## Critérios de saída

- Primeira linha iniciada por `--` e nenhuma sintaxe Markdown.
- 32 tabelas e 204 colunas exatas.
- 59 FKs, todas com ações `ON DELETE` e `ON UPDATE` explícitas.
- 17 unicidades lógicas, cinco CHECKs declarativos e uma exclusão temporal executável.
- 50 índices explícitos de FK e nove coberturas por PK ou `UNIQUE` compatível.
- 9 tabelas em `public` e 23 em `private`.
- Zero objetos fora do escopo e zero regras adiadas falsamente materializadas.

Se uma entrada selecionada contrariar estes critérios após a reconciliação, retorne somente comentários SQL `GENERATION_BLOCKED`, identificando campo, objeto e fontes conflitantes. Não preencha lacunas por inferência.
