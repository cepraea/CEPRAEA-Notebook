# Execução do `STAGE_09` — segurança e RLS candidatas

Produza somente `09-politicas-rls.candidate.sql`, contendo exclusivamente SQL e comentários SQL.

## Entradas autoritativas selecionadas

- `ACCESS_REQUIREMENTS@0.1.0`, fonte promovida `c7f18856-d7c7-4b77-8feb-3266d60337c0`.
- Schema PostgreSQL candidato promovido, fonte `1f69f4e5-f4f3-43fd-b8b0-87f19b8b2c8b`.
- Decisão externa do operador do `STAGE_09`, fornecida como fonte selecionada desta execução.

## Tarefa

1. Trate grants e policies como controles separados e necessários.
2. Para cada tabela exposta, habilite RLS, revogue grants de cliente e devolva somente os privilégios exigidos.
3. Crie policies por operação e declare `TO anon` ou `TO authenticated` explicitamente.
4. Em `UPDATE`, cubra policy de `SELECT`, `USING` e `WITH CHECK` conforme o requisito.
5. Use `(select auth.uid())` ou `(select auth.jwt())` quando o valor for estável por instrução.
6. Indexe colunas usadas pelos filtros RLS quando justificado e ainda não coberto.
7. Não use `user_metadata` como fonte de autorização; use `app_metadata` somente quando a regra demonstrar confiança e atualização adequadas.
8. Views expostas devem usar `security_invoker = true`; caso contrário, mantenha-as fora do schema exposto e revogue acesso de clientes.
9. Funções `SECURITY DEFINER` devem ficar em schema não exposto, ter `search_path` fixo, referências qualificadas e `EXECUTE` revogado por padrão.
10. Nunca exponha `service_role` ou secrets ao cliente.
11. Não invente relações, colunas, vínculos de identidade ou atribuições de papel ausentes das entradas promovidas.
12. Se uma policy fiel depender de estrutura ausente, retorne somente comentários `GENERATION_BLOCKED`, identificando a policy, o requisito e a dependência faltante.

Este arquivo é candidato de composição, não migration autônoma. Não alegue execução, teste ou implantação.
