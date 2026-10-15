# Correção 02 do estágio 06 — Segurança e referências válidas

Gere novamente somente YAML válido, sem H1, prosa introdutória ou cerca Markdown.

A proposta anterior acertou estes pontos e deve preservá-los:

- exatamente 32 recursos, cobrindo as 32 relações promovidas uma vez cada;
- classificações exatas: 9 `PUBLICO`, 19 `INTERNO` e 4 `RESTRITO`;
- somente recursos `TABLE` e `view_security_mode: "NOT_APPLICABLE"`;
- referências internas de papéis e recursos válidas;
- ao menos uma permissão `ALLOW` por recurso;
- um teste positivo e um negativo únicos por permissão.

Corrija obrigatoriamente os pontos abaixo.

## Papéis e fonte de autorização

Use o seguinte conjunto mínimo de papéis propostos:

- `ROLE_PUBLICO_LEITOR`: `authentication_required: false`, `assignment_scope: "GLOBAL"`, `authorization_claim_source: "NONE"`;
- `ROLE_ADMIN_DADOS`: autenticação obrigatória, escopo `GLOBAL`, fonte `DATABASE_MEMBERSHIP`;
- `ROLE_TREINADOR`: autenticação obrigatória, escopo `TEAM`, fonte `DATABASE_MEMBERSHIP`;
- `ROLE_ANALISTA_SCOUT`: autenticação obrigatória, escopo `MATCH`, fonte `DATABASE_MEMBERSHIP`;
- `ROLE_REVISOR_SCOUT`: autenticação obrigatória, escopo `MATCH`, fonte `DATABASE_MEMBERSHIP`;
- `ROLE_ATLETA`: autenticação obrigatória, escopo `SELF`, fonte `DATABASE_MEMBERSHIP`.

Não mencione disponibilidade, presença, treino, bem-estar ou outras entidades fora das 32 relações promovidas. Como ainda não existe relação promovida entre identidade autenticada e atleta, registre uma pendência bloqueante para qualquer permissão de `ROLE_ATLETA` que dependa de escopo `SELF`; não invente essa associação.

## Escopos de linha

`row_scope` é uma descrição semântica independente de plataforma. Não use SQL nem expressões como:

- `auth.jwt()`;
- `auth.uid()`;
- `auth.role()`;
- `current_user`;
- `user_metadata`;
- comparação textual de claim ou papel.

Descreva o escopo por associação confiável, por exemplo: `"Somente partidas vinculadas à equipe atribuída ao papel por associação vigente no banco."`.

Escopos `TEAM`, `MATCH` e `SELF` nunca podem virar simples `authenticated`. O acesso global de `ROLE_ADMIN_DADOS` deve continuar explícito e sujeito a atribuição administrativa no banco.

## Regras válidas

Os únicos `rule_ids` permitidos são:

- `RN_IHF_VIGENCIA_2026`
- `RN_SGATE_0023_PONTUACAO_FHERJ_2026`
- `RN_SEMANTICA_GOLEIRA`
- `RN_TETO_PARTICIPANTES_SUMULA`
- `RN_REJEICAO_VARIAVEIS_INFERENCIAIS`
- `RN_PASSIVO_QUATRO_PASSES`
- `RN_SANCAO_FINAL_15_SEGUNDOS`
- `RN_PROTECAO_CABECA_GOLEIRA`
- `RN_PROIBICAO_RETARDO_REPETIDO`
- `RN_PRAZO_INSCRICAO_ATLETA_72H`
- `RN_REGRAS_EXECUCAO_TIRO_SEIS_METROS`

Remova `REG-IHF-001`, `REG-IHF-002`, `REG-IHF-003`, `RN-DISP-003` e qualquer outro ID ausente dessa lista. Se nenhuma regra sustentar diretamente uma permissão, use `rule_ids: []`.

## Política padrão exata

Use exatamente:

```yaml
default_policy:
  anonymous: "DENY"
  authenticated_without_role: "DENY"
  cross_tenant: "DENY"
  privileged_service_role: "SERVER_ONLY"
  client_authorization_from_user_metadata: "DENY"
```

Leitura pública é uma exceção `ALLOW` explícita para `ROLE_PUBLICO_LEITOR`; ela não altera a negação padrão de operações não autorizadas.

## Recursos restritos e exposição

- Para `ATLETA`, `ANALISTA_OBSERVADOR`, `DESQUALIFICACAO_SEGUNDA_EXCLUSAO` e `CARTAO_AZUL_SUSPENSAO`, não conceda leitura pública.
- Permissões sobre recursos `RESTRITO` devem usar `column_scope` explícito quando o papel não necessita de todas as colunas.
- `exposed_via_data_api` é apenas proposta de exposição técnica; use `false` quando o recurso não precisar de acesso direto pelo cliente.

## Pendências

Use somente pendências relacionadas ao modelo promovido e a decisões de acesso atuais. Não reproduza a pendência histórica sobre tabelas inglesas antigas. Preserve a pendência factual de placar somente se ela afetar concretamente uma permissão; caso contrário, ela permanece no artefato anterior.

Cada pendência usa exatamente `id`, `status`, `question`, `affected_ids`, `impact`, `required_evidence` e `owner`.

## Estrutura exata

Use somente os campos do template para papéis, recursos, permissões, política padrão e pendências. Em particular:

- `operation` é um único valor do enum;
- `grant_required` é booleano;
- `column_scope` e `conditions` são listas;
- `negative_test_ids` e `positive_test_ids` são listas de IDs, não objetos;
- strings com dois-pontos devem estar entre aspas;
- nenhum SQL, DDL, `GRANT`, `REVOKE`, policy RLS, migration ou resultado de teste.

Retorne exatamente esta raiz:

```yaml
roles: []
resources: []
permissions: []
default_policy: {}
open_issues: []
```
