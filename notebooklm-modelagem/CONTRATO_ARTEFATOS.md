# Contrato dos artefatos

## Separação de estados

O NotebookLM produz propostas. Aprovação, promoção, execução e homologação pertencem ao registro do operador e às evidências externas.

Vocabulários distintos não devem ser misturados:

| Campo | Valores |
| --- | --- |
| `document.status` | `PROPOSTO`, `SUBSTITUIDO`, `HISTORICO` |
| `source.lifecycle_status` | `VIGENTE`, `COMPLEMENTAR`, `SUBSTITUIDA`, `HISTORICA`, `EM_VERIFICACAO`, `QUARENTENA` |
| `conflict.status` | `COMPATIVEL`, `COMPLEMENTAR`, `SUBSTITUICAO_DEMONSTRADA`, `CONTRADICAO`, `INDETERMINADO`, `DECISAO_HUMANA_PENDENTE` |
| `gate.recommendation` | `READY`, `READY_WITH_RESTRICTIONS`, `BLOCKED` |
| implementação | `NAO_INICIADO`, `CANDIDATO`, `IMPLEMENTADO`, `BLOQUEADO`, `NAO_APLICAVEL` |
| verificação | `NAO_EXECUTADO`, `PASS`, `FAIL`, `BLOQUEADO`, `NAO_APLICAVEL` |

## Envelope YAML obrigatório

Todo artefato YAML começa com:

```yaml
schema_version: "1.1"
document:
  id: "IDENTIFICADOR_ESTAVEL"
  artifact_kind: "TIPO_DO_ARTEFATO"
  title: "Título"
  version: "0.1.0"
  status: "PROPOSTO"
  run_id: "RUN_AAAAMMDD_DOMINIO_NNN"
  domain_id: "DOMINIO"
  notebook_id: "93446a17-55bf-4cd8-b9f9-18c52c8f4c1d"
  generated_at: null
  supersedes: null
  input_artifacts: []
```

`generated_at` permanece `null` na proposta do NotebookLM. O operador registra o instante observado, o hash do arquivo baixado e a eventual aprovação em `operator/estado-execucao.yaml`.

Quando houver entrada promovida:

```yaml
input_artifacts:
  - document_id: "SEMANTIC_REGISTRY"
    version: "0.1.0"
    sha256: "HASH_REGISTRADO_PELO_OPERADOR"
    promoted_source_id: "NOTEBOOK_SOURCE_ID"
```

## YAML permitido

- YAML 1.2 sem chaves duplicadas;
- indentação de dois espaços e sem tabulações;
- sem anchors, aliases ou merge keys;
- datas, versões, IDs, cardinalidades e enums entre aspas;
- booleanos somente como `true` ou `false`;
- ausência como `null`, nunca string vazia;
- listas explícitas;
- IDs em `UPPER_SNAKE_CASE`, sem acentos;
- referências por ID, sem duplicação do objeto.

## Proveniência

O manifesto define evidências uma única vez:

```yaml
evidence_refs:
  - id: "EVID_SOURCE_001"
    source_id: "SOURCE_ID"
    locator: "Página, regra, seção, aba, célula ou timecode"
    evidence_type: "FATO|REGRA|DECISAO|DERIVACAO|SUPORTE"
    interpretation: "Como a evidência sustenta o elemento"
```

Os demais artefatos usam somente `evidence_ref_ids`. O manifesto conserva título canônico, revisão, hash quando disponível, vigência, autoridade e limitações da fonte.

## Pendências

```yaml
open_issues:
  - id: "ISSUE_DOMAIN_001"
    status: "ABERTA|BLOQUEANTE|RESOLVIDA|NAO_APLICAVEL"
    question: "Questão objetiva"
    affected_ids:
      - "ELEMENT_ID"
    impact: "Consequência concreta"
    required_evidence: "Fonte ou decisão necessária"
    owner: "RESPONSAVEL"
```

## Cardinalidades

```yaml
cardinality:
  from_to:
    min: 1
    max: "N"
  to_from:
    min: 1
    max: 1
```

`max` aceita somente `1` ou `"N"`.

## Convenções

| Elemento | Convenção |
| --- | --- |
| ID semântico | `UPPER_SNAKE_CASE` |
| Schema, tabela e coluna PostgreSQL | `lower_snake_case` |
| PK | `id` |
| FK | `<entidade>_id` |
| Migration real | `supabase/migrations/<timestamp>_<descricao>.sql` |
| Regra | `RULE_<DOMINIO>_<NNN>` |
| Decisão | `DEC_<DOMINIO>_<NNN>` |
| Teste | `TEST_<DOMINIO>_<NNN>` |
| Evidência | `EVID_<FONTE>_<NNN>` |
| Pendência | `ISSUE_<DOMINIO>_<NNN>` |

## Artefatos SQL candidatos

Todo candidato SQL declara em comentários:

- `RUN_ID`, domínio e estado `CANDIDATO`;
- IDs, versões e hashes das entradas;
- versão alvo do PostgreSQL e dependências;
- recomendação do gate e escopo autorizado pelo operador;
- objetos lógicos e regras implementados.

O candidato não é fonte de verdade da execução. A migration real é criada pelo operador com `supabase migration new <descricao>`. Migration de avanço e estratégia de rollback permanecem em arquivos distintos.

DDL, revogações, grants, ativação de RLS e policies de uma tabela exposta devem entrar na mesma migration segura, evitando uma janela de exposição.

## Validação antes da promoção

- YAML carrega sem erro, respeita o schema e não contém placeholders.
- IDs são únicos e referências resolvem.
- Entradas possuem versão, hash e `promoted_source_id` registrados pelo operador.
- Toda regra implementada possui evidência ou decisão.
- Toda entidade e atributo lógico aparece no dicionário.
- Toda FK física possui índice quando o padrão de acesso ou manutenção o exige.
- Toda restrição material possui teste positivo ou negativo.
- Grants e policies cobrem papéis e operações delimitados.
- Rastreabilidade planejada é reconciliada após a implementação.
- Relatório distingue proposta, aprovação, implementação, execução, teste e homologação.
