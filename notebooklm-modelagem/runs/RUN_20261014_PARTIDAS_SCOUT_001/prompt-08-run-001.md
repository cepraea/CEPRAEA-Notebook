# Execução 08 — Schema PostgreSQL candidato

Produza somente o conteúdo de `08-schema-postgresql.candidate.sql`.

Retorne exclusivamente SQL PostgreSQL e comentários SQL. Não use título Markdown, cercas de código, explicação antes ou depois do SQL, YAML ou JSON.

## Entradas promovidas selecionadas

- `LOGICAL_MODEL@0.1.1`
  - `sha256`: `aebdbd4c7b725a25ce1b89d632ae56e94ee25d5529e8ce7c82ab87387ef2e492`
  - `promoted_source_id`: `e2ba2453-a22f-4784-b90d-34173898d6ed`
- `DATA_DICTIONARY@0.1.0`
  - `sha256`: `969b7479813c97f5b2da95631b185211495b509cf86147a0337a53dcbb909c2f`
  - `promoted_source_id`: `1c227cde-1ffd-472f-b0ab-92594c05ec2b`
- `TRACEABILITY_MATRIX@0.1.0`
  - `sha256`: `3e36cfb319571923d213c8527eda511bd6cba0f193e75dfbb795b94e839e66d1`
  - `promoted_source_id`: `5b4b8ee3-c08d-40b5-bc0d-705f68f2e0dd`
- `ACCESS_REQUIREMENTS@0.1.0`
  - `sha256`: `bafce57a9d71ef3ea0ba54c79fac585f075d8d0efe5fe22967e62bde6c424c92`
  - `promoted_source_id`: `c7f18856-d7c7-4b77-8feb-3266d60337c0`
- `STOP_GATE_PARTIDAS_SCOUT_ANALISE_TATICA@0.2.0`
  - `sha256`: `8034fc8290a814a2cb63d7d43138c8552ea087d787f44566b94393449a2d09f0`
  - `promoted_source_id`: `8347d2e6-f0fd-4872-a5f6-b23adae009f3`
- decisão externa do operador do `STAGE_07`
  - `sha256`: `95861272d84e896a0ba82793b63788d8ec070efa284d4100da47b773e1657c66`
  - `source_id`: `167b105a-d750-4d7e-bc53-3da5d56e10f4`

Use somente essas seis fontes selecionadas. Não use conhecimento de outras fontes visíveis no notebook, modelos físicos históricos, tabelas legadas ou conversas anteriores.

## Autoridade e escopo

1. A decisão externa autoriza somente o `STAGE_08` para gerar um schema candidato das 32 relações listadas em `authorized_scope`.
2. A geração não autoriza execução, implantação, migration, rollback, carga de dados, grants, RLS ou início de outro estágio.
3. Para estrutura, cardinalidade, FKs, unicidades e checks, `LOGICAL_MODEL@0.1.1` prevalece.
4. Para tipos e metadados de coluna, use `DATA_DICTIONARY@0.1.0`, exceto nas duas divergências explicitamente reconciliadas.
5. Para as duas divergências, `LOGICAL_MODEL@0.1.1` e `TRACEABILITY_MATRIX@0.1.0` prevalecem:
   - não crie `UQ_TRECHO_EVENTO`;
   - não crie `CHK_VIGENCIA_PARTICIPACAO`;
   - crie somente `CHK_INTERVALO_VIGENCIA_PARTICIPACAO` para validar uma linha;
   - represente a não sobreposição temporal como constraint separada e dependente de `btree_gist`.
6. Use `ACCESS_REQUIREMENTS@0.1.0` apenas para classificação e colocação em schema. Não gere policies, grants, roles ou funções de autorização.

## Cabeçalho SQL obrigatório

Declare em comentários SQL:

- arquivo `08-schema-postgresql.candidate.sql`;
- `RUN_ID: RUN_20261014_PARTIDAS_SCOUT_001`;
- domínio `PARTIDAS_SCOUT_ANALISE_TATICA`;
- estado `CANDIDATO`;
- alvo de compatibilidade `PostgreSQL 15+`, explicitando que a versão do ambiente ainda não foi verificada;
- IDs, versões, hashes e source IDs das seis entradas;
- gate `READY_WITH_RESTRICTIONS`;
- decisão `APPROVED_WITH_RESTRICTIONS`;
- escopo autorizado de 32 relações;
- implementação `NAO_INICIADO` e verificação `NAO_EXECUTADO`.

## Tarefa

1. Derive DDL somente do modelo lógico e do dicionário autorizados.
2. Declare os schemas necessários, tipos, tabelas, PKs, FKs, `NOT NULL`, `UNIQUE` e `CHECK`.
3. Use identificadores `lower_snake_case`, sem identificadores entre aspas e sem nomes históricos em inglês.
4. Preserve temporalidade, histórico, proveniência e correções previstas nas entradas.
5. Crie índices de suporte para todas as 59 FKs. Não duplique índice já coberto pelo prefixo esquerdo de PK ou `UNIQUE` compatível.
6. Mantenha os 9 recursos `PUBLICO` e explicitamente expostos no schema `public`; coloque os 23 recursos `INTERNO` ou `RESTRITO` no schema `private` para que permaneçam fora da Data API.
7. Para FKs entre schemas, qualifique integralmente tabela de origem e de destino.
8. Use `text`, `boolean`, `bigint`, `numeric`, `date`, `timestamptz`, `interval` ou outros tipos PostgreSQL somente conforme os tipos candidatos do dicionário. Não transforme catálogos controlados em enums sem decisão explícita.
9. Não crie defaults sem suporte. Para PKs substitutas, preserve o tipo candidato registrado; não troque silenciosamente UUID por identidade ou vice-versa.
10. Crie `EXCLUDE USING gist` para a não sobreposição de vigência somente como candidato claramente comentado e declare `btree_gist` como dependência ainda não verificada. Não use trigger para essa regra.
11. Use funções ou triggers apenas quando uma regra autorizada não puder ser expressa declarativamente. Se não forem necessárias, não as crie.
12. Registre em comentários próximos aos objetos os IDs lógicos, constraints e regras implementadas.
13. Não inclua policies RLS, `ENABLE ROW LEVEL SECURITY`, grants, revogações, roles, dados, seeds, secrets, views de exposição ou alegações de execução.
14. Não use `IF NOT EXISTS`, blocos que silenciem `duplicate_object`, `DROP`, `TRUNCATE` ou comandos destrutivos.
15. Não use `serial`; se o modelo exigir identidade numérica, use `bigint generated always as identity`.
16. Este arquivo é candidato de composição e não deve ser aplicado isoladamente.

## Critérios de saída

- Exatamente 32 tabelas, uma por relação autorizada.
- Exatamente 59 FKs, com correspondência aos IDs do modelo lógico.
- Todas as FKs possuem índice de suporte ou comentário verificável de cobertura por índice compatível.
- Nenhuma ocorrência de `UQ_TRECHO_EVENTO` ou `CHK_VIGENCIA_PARTICIPACAO`.
- Ocorrência de `CHK_INTERVALO_VIGENCIA_PARTICIPACAO` e da exclusão temporal separada.
- Nenhum objeto fora das 32 relações autorizadas.
- Nenhuma policy, grant, dado real ou alegação de execução.

Se qualquer dado obrigatório estiver ausente ou contraditório fora das duas divergências já reconciliadas, retorne apenas comentários SQL `GENERATION_BLOCKED`, listando o campo, o objeto afetado e as fontes conflitantes. Não complete lacunas por inferência.
