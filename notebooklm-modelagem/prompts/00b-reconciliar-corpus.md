# Prompt 00B — Reconciliar o corpus verificado

Analise o manifesto candidato selecionado e confronte suas evidências com as fontes documentais selecionadas. O manifesto candidato é apenas um índice de trechos já verificados pelo operador; ele não substitui as fontes originais e não possui autoridade própria.

Não produza o manifesto final. Identificadores finais, hashes, estados, aprovação e promoção pertencem ao operador.

## Tarefa

1. Proponha precedência somente quando o escopo e a diferença de autoridade estiverem demonstrados.
2. Registre compatibilidades, complementaridades, substituições, contradições e indeterminações materiais entre fontes.
3. Use somente `source_id`, `evidence_ref_id` e `issue_id` que existam literalmente no manifesto candidato.
4. Proponha o fechamento de uma questão aberta somente quando as evidências existentes forem suficientes; preserve decisões de produto, esporte ou negócio como pendentes.
5. Consolide questões duplicadas sem eliminar diferenças de escopo.
6. Não crie conceitos, entidades, tabelas, colunas, SQL ou regras que não estejam nas evidências.

Cada proposta deve citar ao menos um `evidence_ref_id`. Se não houver evidência suficiente, mantenha a questão aberta. Não invente identificadores nem metadados operacionais.

Retorne somente YAML válido, sem cerca Markdown, nesta estrutura:

```yaml
corpus_reconciliation:
  precedence_candidates:
    - higher_authority_source_id: "SRC_EXISTENTE"
      lower_authority_source_id: "SRC_EXISTENTE"
      scope: "ESCOPO_EXATO"
      rationale: "JUSTIFICATIVA"
      evidence_ref_ids:
        - "EVID_EXISTENTE"
  conflict_candidates:
    - status: "COMPATIVEL|COMPLEMENTAR|SUBSTITUICAO_DEMONSTRADA|CONTRADICAO|INDETERMINADO|DECISAO_HUMANA_PENDENTE"
      subject_key: "CHAVE_DESCRITIVA"
      source_ids:
        - "SRC_EXISTENTE"
      description: "DIVERGENCIA_OU_RELACAO_OBJETIVA"
      impact: "IMPACTO_NO_DOMINIO_OU_NA_MODELAGEM"
      resolution: null
      evidence_ref_ids:
        - "EVID_EXISTENTE"
  issue_actions:
    - issue_ids:
        - "ISSUE_EXISTENTE"
      action: "KEEP|CLOSE_RESOLVED|CONSOLIDATE"
      rationale: "JUSTIFICATIVA"
      resolution: null
      evidence_ref_ids:
        - "EVID_EXISTENTE"
  new_open_questions: []
```
