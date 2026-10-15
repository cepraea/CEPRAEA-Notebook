# Prompt 09 — Gerar segurança e RLS candidatas

Produza somente `09-politicas-rls.candidate.sql`.

Exija requisitos de acesso promovidos e decisão externa do operador para o escopo. Se estiverem ausentes ou incompletos, retorne apenas comentários `GENERATION_BLOCKED`.

## Tarefa

1. Trate grants e policies como controles separados e necessários.
2. Para cada tabela exposta, habilite RLS, revogue grants de cliente e devolva somente os privilégios exigidos.
3. Crie policies por operação e declare `TO anon` ou `TO authenticated` explicitamente.
4. Em `UPDATE`, cubra policy de `SELECT`, `USING` e `WITH CHECK` conforme o requisito.
5. Use `(select auth.uid())` ou `(select auth.jwt())` quando o valor for estável por instrução.
6. Indexe colunas usadas pelos filtros RLS quando justificado.
7. Não use `user_metadata` como fonte de autorização; use `app_metadata` somente quando a regra demonstrar confiança e atualização adequadas.
8. Views expostas devem usar `security_invoker = true`; caso contrário, mantenha-as fora do schema exposto e revogue acesso de clientes.
9. Funções `SECURITY DEFINER` devem ficar em schema não exposto, ter `search_path` fixo, referências qualificadas e `EXECUTE` revogado por padrão.
10. Nunca exponha `service_role` ou secrets ao cliente.

Este arquivo é candidato de composição, não migration autônoma. Retorne somente SQL e comentários SQL.
