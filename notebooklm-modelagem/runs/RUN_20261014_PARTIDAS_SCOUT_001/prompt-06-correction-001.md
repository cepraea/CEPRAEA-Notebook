# Correção 01 do estágio 06 — Aderir ao modelo promovido

A proposta anterior foi rejeitada. Gere novamente somente o corpo de `06-requisitos-acesso.yaml`, sem H1, prosa introdutória, comentários ou cerca Markdown.

## Erros que devem ser eliminados

- Não use as tabelas históricas `public.competitions`, `public.matches`, `public.athletes`, `public.calendar_events`, `public.schema_migrations`, `public.audit_logs` ou quaisquer outras relações ausentes do `LOGICAL_MODEL` promovido.
- Não use os campos `role_id`, `display_name`, `requires_authentication`, `authorization_source`, `resource_id`, `logical_relation_id`, `resource_type`, `data_classification`, `semantic_ownership_rule`, `security_invoker`, `permission_id`, `required_grant`, `columns` ou `planned_tests`.
- Não escreva SQL nem texto de `GRANT`, `REVOKE`, RLS, `CREATE POLICY` ou migration.
- Não use `conditions` como string, `row_scope` como booleano ou objetos de teste dentro das permissões.
- Não invente IDs de regras como `SGATE-*`, `DEC-DATA-*`, `CON-*` ou `TAX-*`.
- Não alegue que `ISSUE_REQUISITOS_ACESSO_STAGE_06` foi resolvida; a proposta ainda exige revisão do operador.

## Relações canônicas obrigatórias

Crie exatamente 32 recursos `TABLE`, um para cada relação abaixo. Use o ID da relação literalmente em `logical_relation_ids`, sem prefixo `public.` e sem tradução:

### `PUBLICO` — 9

- `COMPETICAO`
- `PARTIDA`
- `EQUIPE`
- `PARTIDA_EQUIPE`
- `PERIODO_SET`
- `SHOOT_OUT`
- `PLACAR_JOGO`
- `ESTADO_DO_PLACAR`
- `EVOLUCAO_DO_PLACAR`

### `INTERNO` — 19

- `EQUIPE_ATLETA_INSCRICAO`
- `POSSE_DE_BOLA`
- `UNIDADE_BASICA_ATAQUE_BOU`
- `EVENTO_SCOUT`
- `OBSERVACAO_DE_SCOUT`
- `PROTOCOLO_SCOUT`
- `MIDIA_VIDEO`
- `SEGMENTO_OBSERVADO`
- `SISTEMA_DEFENSIVO`
- `CONFIABILIDADE_OBSERVADOR`
- `REVISAO_DA_OBSERVACAO`
- `ESTADO_DE_REVISAO`
- `PROVENIENCIA_OBSERVACAO`
- `TRECHO_OBSERVADO`
- `SPIN_SHOT`
- `IN_FLIGHT_SHOT`
- `SISTEMA_TATICO`
- `PAPEL_ESPORTIVO_OPERACIONAL`
- `PARTICIPACAO_EQUIPE_COMPETICAO`

### `RESTRITO` — 4

- `ATLETA`
- `ANALISTA_OBSERVADOR`
- `DESQUALIFICACAO_SEGUNDA_EXCLUSAO`
- `CARTAO_AZUL_SUSPENSAO`

## Campos exatos do template

Cada papel usa exatamente:

```yaml
- id: "ROLE_ID"
  name: "NOME"
  description: "DESCRICAO"
  authentication_required: true
  assignment_scope: "GLOBAL"
  authorization_claim_source: "DATABASE_MEMBERSHIP"
  evidence_ref_ids: []
```

Cada recurso usa exatamente:

```yaml
- id: "RESOURCE_ID"
  resource_kind: "TABLE"
  logical_relation_ids:
    - "RELATION_ID"
  classification: "PUBLICO"
  exposed_via_data_api: true
  owner_rule: "REGRA SEMANTICA"
  view_security_mode: "NOT_APPLICABLE"
```

Cada permissão usa exatamente:

```yaml
- id: "PERMISSION_ID"
  role_id: "ROLE_ID"
  resource_id: "RESOURCE_ID"
  operation: "SELECT"
  effect: "ALLOW"
  grant_required: true
  row_scope: "EXPRESSAO SEMANTICA"
  column_scope: []
  conditions: []
  rule_ids: []
  evidence_ref_ids: []
  negative_test_ids:
    - "TEST_ACCESS_NEG_001"
  positive_test_ids:
    - "TEST_ACCESS_POS_001"
```

Cada pendência usa exatamente `id`, `status`, `question`, `affected_ids`, `impact`, `required_evidence` e `owner`.

## Regras de referência e segurança

- Use somente `rule_ids` existentes no registro semântico selecionado.
- Use somente `evidence_ref_ids` existentes no manifesto selecionado.
- Todos os `role_id` e `resource_id` usados em permissões devem existir neste mesmo artefato.
- Cada permissão `ALLOW` deve possuir pelo menos um teste positivo e um negativo, todos com IDs únicos.
- `operation` contém uma única operação do enum, nunca uma lista disfarçada nem SQL.
- `grant_required` é booleano.
- `row_scope` é string semântica, nunca booleano.
- `column_scope` e `conditions` são listas.
- A autorização deve depender de associação confiável no banco, não de `user_metadata` nem de IDs livres enviados pelo cliente.
- Use menor privilégio. Não conceda CRUD genérico a todo autenticado.
- Use em `default_policy` exatamente os cinco campos do template e os valores exigidos pela fonte de controle.
- Coloque entre aspas toda string que contenha dois-pontos ou caracteres que possam tornar o YAML inválido.
- Não gere envelope `document`.

Retorne exatamente esta raiz:

```yaml
roles: []
resources: []
permissions: []
default_policy: {}
open_issues: []
```
