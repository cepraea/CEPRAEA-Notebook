# Estágio 06 — Propor requisitos de acesso e políticas semânticas

Produza somente o corpo proposto para `06-requisitos-acesso.yaml`.

O manifesto, o registro semântico, o modelo conceitual, o modelo lógico, o dicionário de dados, a matriz de rastreabilidade promovida e o template do estágio 06 estão entre as fontes explicitamente selecionadas. O artefato histórico de RBAC/RLS serve apenas como evidência de proposta anterior, nunca como implementação vigente. As demais fontes selecionadas são controles de formato e operação.

Não produza o envelope `document`. `run_id`, `notebook_id`, versões, hashes, `promoted_source_id`, timestamps, estado, aprovação e promoção pertencem ao operador.

## Entradas promovidas

- `SOURCE_MANIFEST` v0.1.0;
- `SEMANTIC_REGISTRY` v0.1.0;
- `CONCEPTUAL_MODEL` v0.1.1;
- `LOGICAL_MODEL` v0.1.0;
- `DATA_DICTIONARY` v0.1.0;
- `TRACEABILITY_MATRIX` v0.1.0.

## Cobertura obrigatória

O dicionário promovido contém exatamente 32 relações candidatas:

- 9 classificadas como `PUBLICO`;
- 19 classificadas como `INTERNO`;
- 4 classificadas como `RESTRITO`;
- nenhuma classificada como `PESSOAL` ou `SENSIVEL` nesta versão.

Crie exatamente um recurso `TABLE` para cada uma das 32 relações lógicas. Preserve a classificação do dicionário sem reclassificá-la silenciosamente. Qualquer discordância deve ser registrada em `open_issues`.

A matriz promovida possui 113 traços e a pendência `ISSUE_REQUISITOS_ACESSO_STAGE_06`; seus `permission_requirement_ids` estão vazios porque este estágio é responsável por defini-los. Não alegue que a pendência foi resolvida, nem altere a matriz nesta proposta.

## Tarefa

1. Defina o conjunto mínimo de papéis de negócio necessário ao domínio de partidas, scout e análise tática. Diferencie papel de negócio de papel técnico do PostgreSQL ou da plataforma.
2. Para cada papel, declare se exige autenticação, o escopo de atribuição e uma fonte confiável de autorização. Prefira `DATABASE_MEMBERSHIP`; use `APP_METADATA` somente quando a fonte selecionada sustentar metadados administrativos imutáveis. Nunca use metadados editáveis pelo próprio usuário.
3. Para cada uma das 32 relações, crie um recurso `TABLE` com o `logical_relation_id` existente, a classificação exata do dicionário e uma regra semântica objetiva de titularidade ou escopo.
4. Marque `exposed_via_data_api` apenas como proposta. Exposição não implica acesso: todo recurso exposto continua sujeito a grant mínimo e escopo de linha.
5. Para cada permissão permitida, declare operação, grant necessário, escopo de linha, colunas e condições. Use o menor privilégio necessário; não conceda CRUD genérico a todo usuário autenticado.
6. Modele negação padrão para anônimo, autenticado sem papel e acesso cruzado. Não é necessário repetir uma permissão `DENY` para cada combinação já coberta por `default_policy`, mas toda exceção `ALLOW` deve ser explícita.
7. Para recursos `RESTRITO`, restrinja também as colunas quando a exposição integral não for necessária. Não trate ausência de classificação `PESSOAL` ou `SENSIVEL` como prova de que nenhum atributo pessoal ou sensível exista.
8. Vincule cada permissão aos `rule_ids` e `evidence_ref_ids` existentes que realmente a sustentam. Quando a autorização for apenas uma decisão de segurança derivada, deixe `rule_ids` vazio, use a evidência disponível e registre a necessidade de decisão humana se material.
9. Planeje ao menos um teste positivo e um negativo por permissão `ALLOW`, com IDs únicos em `UPPER_SNAKE_CASE`. Os testes são planejados, nunca executados.
10. Trate o documento histórico `07-matriz-rbac-e-politicas-rls` como proposta: aproveite somente decisões compatíveis com o modelo promovido e registre divergências ou autoridade insuficiente.
11. Considere `SECURITY_INVOKER` somente para recursos `VIEW`; como esta versão exige recursos `TABLE`, use `NOT_APPLICABLE` em todos eles.
12. Não gere SQL, DDL, `GRANT`, `REVOKE`, ativação de RLS, policies PostgreSQL, funções `SECURITY DEFINER`, migrations ou resultados de teste.

## Políticas de segurança a preservar

- menor privilégio e separação de responsabilidades;
- `anonymous: "DENY"` como padrão, salvo leitura pública explicitamente sustentada por permissão `ALLOW`;
- `authenticated_without_role: "DENY"`;
- `cross_tenant: "DENY"`;
- `privileged_service_role: "SERVER_ONLY"`;
- `client_authorization_from_user_metadata: "DENY"`;
- escopos de equipe, competição e partida devem depender de associação confiável, não de identificador fornecido livremente pelo cliente;
- eventual implementação RLS deverá possuir índices nas colunas usadas por escopo, mas este artefato não cria índices nem SQL.

## Estrutura obrigatória

Siga exatamente os campos de `roles`, `resources`, `permissions`, `default_policy` e `open_issues` do template selecionado.

Retorne somente YAML válido, sem título, comentário ou cerca Markdown, nesta raiz:

```yaml
roles: []
resources: []
permissions: []
default_policy: {}
open_issues: []
```
