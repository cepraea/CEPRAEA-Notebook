# Pacote operador + NotebookLM

Este diretório organiza a transformação das fontes dispersas do CEPRAEA em documentação verificável para o banco de dados. O NotebookLM analisa e propõe; o operador controla contexto, versões, validações, aprovações e promoção; Supabase/PostgreSQL executa e comprova o modelo físico.

## Notebook canônico

- **Título:** `# BANCO - CEPRAEA Beach Handball`
- **ID:** `93446a17-55bf-4cd8-b9f9-18c52c8f4c1d`
- **Fluxo normativo:** `Fluxo_Modelagem.md`

Use sempre o ID completo. Títulos semelhantes não identificam o notebook com segurança.

## Responsabilidades

| Componente | Responsabilidade | Não pode declarar |
| --- | --- | --- |
| NotebookLM | Extrair, comparar, modelar e propor artefatos fundamentados nas fontes selecionadas | Aprovação, execução, teste ou homologação |
| Operador | Selecionar fontes, executar uma etapa por vez, baixar, validar, versionar, aprovar e promover artefatos | Evidência esportiva ou técnica não presente nas fontes |
| Responsável humano | Resolver decisões semânticas, esportivas, de segurança e de risco | Execução que não tenha evidência observável |
| Supabase/PostgreSQL | Aplicar migrations e produzir resultados verificáveis de constraints, RLS e testes | Validade semântica do domínio |

## Estrutura

```text
notebooklm-modelagem/
├── README.md
├── OPERADOR.md
├── INSTRUCOES_NOTEBOOK.md
├── CONTRATO_ARTEFATOS.md
├── operator/
│   └── estado-execucao.template.yaml
├── schemas/
│   └── artifact-envelope.schema.json
├── scripts/
│   ├── validate_yaml.py
│   └── yaml_to_json.py
├── templates/
│   └── 00-...07-*.template.yaml
└── prompts/
    └── 00-...15-*.md
```

## Ciclo obrigatório de uma etapa

```text
selecionar fontes prontas
        ↓
gerar um artefato proposto no NotebookLM
        ↓
aguardar e baixar pelo artifact_id
        ↓
validar estrutura, referências e conteúdo
        ↓
obter aprovação quando exigida
        ↓
calcular SHA-256 e promover como nova fonte
        ↓
aguardar a nova source_id ficar pronta
```

O artefato gerado não entra automaticamente no contexto do NotebookLM. A promoção explícita para fonte é o mecanismo que permite à etapa seguinte consumi-lo.

## Ordem das etapas

1. `00` reconcilia as fontes selecionadas.
2. `01` consolida semântica e regras.
3. `02` produz o modelo conceitual.
4. `03` produz o modelo lógico.
5. `04`, `05` e `06` produzem dicionário, rastreabilidade planejada e requisitos de acesso.
6. `07` emite uma recomendação para o `STOP GATE` físico.
7. O responsável humano registra a decisão no estado do operador.
8. `08` a `13` produzem candidatos físicos, apenas para o escopo autorizado.
9. O operador cria a migration real com a CLI do Supabase, aplica e testa localmente.
10. `14` reconcilia a rastreabilidade com o estado implementado.
11. `15` audita a entrega usando evidências reais.

Cada execução usa `--source` para todas as fontes selecionadas. Não use o notebook inteiro como contexto implícito.

## Saídas esperadas

### Modelagem e gate

```text
00-manifesto-fontes.yaml
01-registro-semantico.yaml
02-modelo-conceitual.yaml
03-modelo-logico.yaml
04-dicionario-dados.yaml
05-matriz-rastreabilidade-planejada.yaml
06-requisitos-acesso.yaml
07-stop-gate-<dominio>.yaml
```

### Candidatos físicos e verificação

```text
08-schema-postgresql.candidate.sql
09-politicas-rls.candidate.sql
10-seeds-simulados.candidate.sql
11-testes-pgtap.candidate.sql
12-migration-up.candidate.sql
13-rollback.candidate.sql
14-matriz-rastreabilidade-as-built.yaml
15-relatorio-validacao.md
```

Os candidatos SQL não são migrations executáveis por si só. O operador compõe a migration real em `supabase/migrations/<timestamp>_<descricao>.sql`, incluindo DDL, grants, RLS e policies na mesma mudança segura.

## Validação local

```bash
python3 notebooklm-modelagem/scripts/validate_yaml.py \
  --schema notebooklm-modelagem/schemas/artifact-envelope.schema.json \
  caminho/do/artefato.yaml

python3 notebooklm-modelagem/scripts/yaml_to_json.py \
  caminho/do/artefato.yaml \
  caminho/do/artefato.json
```

Use `--allow-placeholders` somente para validar templates. O JSON é derivado mecanicamente do YAML e não é editado.

## Critério de conclusão

Um domínio está concluído somente quando:

> Para o domínio delimitado, todos os conceitos, regras, relações, atributos, restrições, permissões e testes necessários foram rastreados, implementados e verificados.

“Fontes lidas”, “documento gerado”, “SQL proposto”, “migration aplicada”, “testes aprovados” e “homologação” são estados distintos.
