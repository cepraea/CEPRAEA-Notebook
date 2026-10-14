# Prompt 01 — Corrigir e completar o registro semântico

Corrija o rascunho semântico rejeitado usando o manifesto promovido e o template selecionados. Preserve somente conteúdo sustentado por `evidence_ref_ids` existentes no manifesto.

O rascunho foi rejeitado porque usou campos diferentes do template, IDs com hífen, estados de aprovação não pertencentes ao NotebookLM e cobertura esportiva insuficiente.

## Contrato estrutural obrigatório

Retorne somente YAML válido, sem título e sem cerca Markdown, com a raiz `semantic_registry`.

Cada item de `concepts` deve conter exatamente:

- `id`, em `UPPER_SNAKE_CASE`;
- `preferred_term`;
- `canonical_name`;
- `classification`: `ENTITY|ATTRIBUTE|EVENT|ROLE|ASSOCIATION|VALUE_OBJECT|STATE|CATALOG|RULE|INDICATOR|SNAPSHOT`;
- `definition`;
- `valid_context`, `invalid_context`, `inclusions`, `exclusions`, `synonyms`, `related_concept_ids` e `allowed_values`, sempre como listas;
- `temporality`;
- `privacy_classification`: `PUBLICO|INTERNO|PESSOAL|SENSIVEL|RESTRITO`;
- `status: "PROPOSTO"`;
- `evidence_ref_ids`.

Cada item de `rules` deve conter exatamente:

- `id`, em `UPPER_SNAKE_CASE`;
- `name`;
- `rule_type`: `DEFINITION|OBLIGATION|PROHIBITION|PERMISSION|CONDITION|EXCEPTION|CLASSIFICATION|CALCULATION|TEMPORAL`;
- `subject_ids`, referenciando conceitos existentes;
- `statement`, `conditions`, `exceptions`, `valid_from`, `valid_to`, `valid_context`, `invalid_context`, `implementation_targets`, `verification_test_ids`;
- `status: "PROPOSTO"`;
- `evidence_ref_ids`.

Cada item de `decisions` deve conter exatamente:

- `id`, em `UPPER_SNAKE_CASE`;
- `question`, `alternatives`, `selected_alternative`, `rationale`, `affected_ids`, `risk` e `evidence_ref_ids`;
- `status: "EM_REVISAO"`.

O NotebookLM não aprova decisões. Use `selected_alternative: null` quando não houver decisão humana explícita e vigente no corpus.

## Cobertura mínima verificável

Além de corrigir os itens aproveitáveis do rascunho, cubra separadamente quando houver evidência:

- partida, competição, equipe, atleta e papel;
- período/set, segmento observado, Gol de Ouro e Shoot-out/cobrança;
- placar, estado do placar, evolução do placar e evento de pontuação;
- gol de um e dois pontos, Spin Shot, In-flight e tiro de seis metros;
- punição, exclusão e consequência disciplinar;
- posse, unidade/fase ofensiva e sistema/fase defensiva;
- ação da goleira, zona da quadra, ação observada e resultado da ação;
- evento de scout, observação, protocolo de scout e versão do protocolo;
- analista, revisão, estado de revisão e confiabilidade da observação;
- vídeo/mídia, timecode e trecho observado;
- proveniência e temporalidade dos eventos.

Não force cobertura sem evidência: transforme a ausência material em `open_issues`. Não crie tabelas, colunas ou SQL. Não trate material científico, didático ou histórico como regra oficial.

Retorne:

```yaml
semantic_registry:
  concepts: []
  rules: []
  decisions: []
  open_issues: []
```
