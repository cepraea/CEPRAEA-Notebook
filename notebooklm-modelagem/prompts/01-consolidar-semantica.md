# Prompt 01 — Propor semântica e regras

Produza somente o corpo semântico proposto para `01-registro-semantico.yaml`.

O manifesto promovido e o template da etapa devem estar entre as fontes selecionadas. Use apenas `evidence_ref_ids` existentes no manifesto.

Não produza o envelope `document`. `run_id`, `notebook_id`, versão, hashes, `promoted_source_id`, timestamps, estado, aprovação e promoção pertencem ao operador.

## Tarefa

1. Extraia somente conceitos e regras necessários ao domínio.
2. Separe definição, obrigação, proibição, permissão, condição, exceção, cálculo e temporalidade.
3. Preserve fato, regra, decisão, derivação, interpretação e hipótese.
4. Registre contexto, inclusões, exclusões, sinônimos e vigência.
5. Não decida questões de produto, esporte ou negócio sem decisão humana registrada.
6. Não crie tabelas, colunas ou SQL.
7. Não transforme fonte científica, material didático ou artefato histórico em regra oficial.
8. Não replique pendências documentais sem impacto semântico; mantenha somente questões que afetem conceito, regra ou decisão do domínio.

Se o domínio incluir partidas ou scout, cubra segmentos, shoot-out, pontuação, gols de um e dois pontos, técnicas de finalização, tiros de seis metros, punições, posses, sistemas defensivos, goleira, zonas, resultados, mídia, timecodes, protocolo, analista, revisão e confiabilidade.

Siga exatamente os campos de `concepts`, `rules`, `decisions` e `open_issues` do template selecionado. Retorne somente YAML válido, sem cerca Markdown, nesta raiz:

```yaml
semantic_registry:
  concepts: []
  rules: []
  decisions: []
  open_issues: []
```
