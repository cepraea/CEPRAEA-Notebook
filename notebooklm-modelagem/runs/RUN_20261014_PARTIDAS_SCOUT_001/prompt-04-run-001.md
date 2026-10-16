# Estágio 04 — Propor corpo do dicionário de dados

Produza somente o corpo proposto para `04-dicionario-dados.yaml`.

O registro semântico promovido, o modelo lógico promovido e o template do estágio 04 estão entre as fontes explicitamente selecionadas. As demais fontes selecionadas são controles de formato e operação.

Não produza o envelope `document`. `run_id`, `notebook_id`, versão, hashes, `promoted_source_id`, timestamps, estado, aprovação e promoção pertencem ao operador.

## Cobertura obrigatória

O modelo lógico promovido contém exatamente:

- 32 relações;
- 204 atributos, contados no escopo de suas relações;
- 59 FKs;
- 18 restrições de unicidade;
- 13 checks;
- 1 pendência aberta.

O resultado deve cobrir exatamente as 32 relações e seus 204 atributos, sem adicionar, remover, renomear, fundir ou dividir relações e atributos. `attribute_id` é único apenas dentro de sua relação; não trate IDs como `ID`, `PARTIDA_ID` ou `EQUIPE_ID` como duplicações globais.

## Tarefa

1. Para cada relação lógica, produza exatamente uma entrada em `tables`, preservando `relation_id`, `physical_name_candidate`, descrição, grão, domínio proprietário, classificação de acesso e retenção.
2. Para cada atributo lógico, produza exatamente uma entrada em `columns`, preservando `attribute_id`, `physical_name_candidate`, nulabilidade, derivação, regras e evidências.
3. Proponha tipos PostgreSQL conservadores e reversíveis. Não gere SQL, DDL, migrations, grants, RLS ou policies.
4. Diferencie explicitamente ausência factual, desconhecido, não observado, não informado, não aplicável e informação protegida. Preserve o `null_meaning` lógico; não converta ausência de evidência em zero, `false`, string vazia ou valor padrão.
5. Só proponha `default_candidate` quando o modelo lógico ou uma regra selecionada sustentar o valor. Caso contrário use `null`.
6. Copie os valores de domínio já definidos no modelo lógico para `allowed_values`. Não invente valores nem feche vocabulários que o modelo lógico mantém abertos.
7. Registre as PKs, as 59 FKs, as 18 restrições de unicidade e os 13 checks por seus IDs existentes. Não invente IDs de constraints.
8. Proponha um índice de suporte para cada FK marcada com `supporting_index_required: true`. Índices adicionais são permitidos somente quando houver padrão de consulta, unicidade ou RLS demonstrado nas fontes; cada índice precisa de justificativa específica.
9. Em `catalogs`, registre somente domínios controlados explicitamente sustentados pelos `domain_values` do modelo lógico. Use catálogos versionados e preserve evidências quando existirem.
10. Preserve em `open_issues` a pendência `ISSUE_LACUNA_PLACAR_SHOOTOUT_E_ETAPAS`, adaptando apenas `affected_ids` se necessário para referenciar relações ou atributos documentados. Não a declare resolvida.
11. Garanta rastreabilidade apenas com `rule_ids` e `evidence_ref_ids` existentes nas fontes promovidas selecionadas.

## Regras de tipos e ausência

- IDs opacos: `uuid`, salvo demonstração explícita em contrário.
- Instantes com fuso: `timestamptz`; datas civis sem horário: `date`; duração ou deslocamento temporal: tipo que preserve unidade e precisão declaradas.
- Contagens e ordens inteiras: tipo inteiro com limites coerentes.
- Pontuação ou medida decimal: tipo numérico com precisão conservadora e unidade explícita.
- Texto aberto: `text`; códigos controlados podem usar `text` com catálogo/check candidato, sem criar enum PostgreSQL nesta etapa.
- Dados estruturados estáveis não devem ser escondidos em `jsonb`.
- `nullable`, `generated` e `derivation_rule_id` devem permanecer coerentes com o modelo lógico.

## Estrutura obrigatória

Siga exatamente os campos de `tables`, `catalogs` e `open_issues` do template selecionado.

Retorne somente YAML válido, sem título, comentário ou cerca Markdown, nesta raiz:

```yaml
data_dictionary:
  tables: []
  catalogs: []
  open_issues: []
```
