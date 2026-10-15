# Prompt 00B — Corrigir a reconciliação do corpus

Revise criticamente a resposta anterior usando somente o manifesto candidato selecionado, que contém os excertos já verificados pelo operador.

A resposta anterior foi rejeitada parcialmente porque existência do ID não comprova adequação da evidência. Foram observados estes erros:

- cabeçalhos de documentos foram usados para afirmar substituição ou correção técnica;
- objetivos institucionais e datas de revisão foram usados para inferir hierarquia normativa;
- títulos de materiais didáticos foram usados para sustentar detalhes técnicos não presentes no excerto;
- regras possivelmente complementares foram classificadas como contradição;
- a existência de uma migração e de um rollback foi tratada como prova de substituição do DDL;
- questões amplas foram propostas como resolvidas sem comparação suficiente.

## Critério obrigatório

Cada afirmação deve ser demonstrada pelo conteúdo literal dos `excerpt` dos `evidence_ref_ids` citados, e não apenas pelo título, interpretação ou classe da fonte. Não infira hierarquia somente porque uma entidade é internacional, nacional ou estadual. Não proponha fechamento da questão geral de reconciliação.

Retorne uma versão completa substitutiva da reconciliação, ainda que contenha poucas propostas. Omita qualquer precedência, conflito ou ação cuja fundamentação literal seja insuficiente. Preserve decisões de produto, esporte e negócio como abertas.

Use exatamente a mesma estrutura YAML solicitada no Prompt 00B, sem cerca Markdown e sem inventar IDs.
