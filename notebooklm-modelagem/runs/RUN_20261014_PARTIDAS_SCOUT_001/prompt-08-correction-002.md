# Correção cirúrgica do schema candidato — `STAGE_08`

Use `REJECTED — STAGE 08 schema candidate report 002` como texto-base. Reproduza integralmente o SQL e os comentários SQL dessa fonte, alterando somente os pontos enumerados abaixo.

Retorne exclusivamente SQL PostgreSQL e comentários SQL. A primeira linha deve começar com `--`. Não use título Markdown, cercas de código, explicação, YAML ou JSON.

## Alterações obrigatórias e exaustivas

1. Remova a primeira linha H1 Markdown.
2. No comentário de distribuição, registre 9 tabelas em `public` e 23 em `private`; remova `atleta` da lista pública.
3. Troque `CREATE TABLE public.atleta` por `CREATE TABLE private.atleta`.
4. Troque todas as cinco ocorrências de `REFERENCES public.atleta` por `REFERENCES private.atleta`.
5. Corrija somente as ações `ON DELETE` destas 12 FKs; preserve `ON UPDATE CASCADE`:
   - `fk_partida_competicao`: `RESTRICT`;
   - `fk_inscricao_equipe`: `CASCADE`;
   - `fk_periodo_set_equipe_vencedora`: `RESTRICT`;
   - `fk_shoot_out_equipe_vencedora`: `RESTRICT`;
   - `fk_evento_scout_atleta_exec`: `RESTRICT`;
   - `fk_evento_scout_atleta_alvo`: `RESTRICT`;
   - `fk_segmento_observado_midia`: `RESTRICT`;
   - `fk_placar_jogo_equipe_vencedora`: `RESTRICT`;
   - `fk_trecho_observado_midia`: `RESTRICT`;
   - `fk_cartao_azul_atleta`: `RESTRICT`;
   - `fk_cartao_azul_papel_operacional`: `RESTRICT`;
   - `fk_participacao_equipe_competicao_competicao`: `RESTRICT`.

## Preservação obrigatória

- Não altere nenhuma outra linha, ação referencial, tabela, coluna, tipo, nulabilidade, default, PK, `UNIQUE`, `CHECK`, exclusão temporal ou índice.
- Preserve exatamente 32 tabelas, 204 colunas, 59 FKs, 17 unicidades, cinco CHECKs lógicos, a exclusão temporal e a estratégia de 50 índices explícitos mais nove coberturas.
- Não acrescente nem remova objetos.
- Não mencione IDs legados proibidos.
- Não execute nem alegue executar SQL.

Se não puder reproduzir a fonte com somente essas alterações, retorne apenas comentários SQL `GENERATION_BLOCKED`.
