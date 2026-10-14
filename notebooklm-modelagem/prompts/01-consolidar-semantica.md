# Prompt 01 — Consolidar semântica e regras

Produza somente `01-registro-semantico.yaml` para o domínio e o `run_id` informados.

O manifesto promovido deve estar entre as fontes selecionadas. Copie sua versão, hash e `promoted_source_id` para `document.input_artifacts`. Use apenas `evidence_ref_ids` existentes no manifesto.

## Tarefa

1. Extraia somente conceitos e regras necessários ao domínio.
2. Separe definição, obrigação, proibição, permissão, condição, exceção, cálculo e temporalidade.
3. Preserve fato, regra, decisão, derivação, interpretação e hipótese.
4. Registre contexto, inclusões, exclusões, sinônimos e vigência.
5. Não decida questões de produto, esporte ou negócio sem decisão humana registrada.
6. Não crie tabelas, colunas ou SQL.

Se o domínio incluir partidas ou scout, cubra segmentos, shoot-out, pontuação, gols de um e dois pontos, técnicas de finalização, tiros de seis metros, punições, posses, sistemas defensivos, goleira, zonas, resultados, mídia, timecodes, protocolo, analista, revisão e confiabilidade.

Retorne somente YAML válido conforme `01-registro-semantico.template.yaml`, sem cerca Markdown.
