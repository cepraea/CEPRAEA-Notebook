# Manual do operador

## Objetivo

Executar o fluxo sem atribuir ao NotebookLM capacidades de orquestração, aprovação ou execução. Este manual controla um domínio por `run_id`.

## Antes de começar

1. Confirme que `Fluxo_Modelagem.md`, `INSTRUCOES_NOTEBOOK.md`, `CONTRATO_ARTEFATOS.md` e o template da etapa existem no notebook como fontes de controle atualizadas.
2. Copie `operator/estado-execucao.template.yaml` para um arquivo da execução.
3. Preencha `run.id`, `run.domain_id` e o ID completo do notebook.
4. Liste e registre somente as fontes pertinentes.
5. Confirme que cada `source_id` selecionada está pronta.
6. Defina o prompt e o artefato esperado para uma única etapa.

Na etapa 00, monte primeiro o manifesto-base sem geração:

```bash
python3 notebooklm-modelagem/scripts/build_source_manifest.py \
  caminho/estado-execucao.yaml \
  caminho/00-manifesto-fontes.yaml
```

O NotebookLM não preenche IDs da API, hashes, estados ou timestamps. Para enriquecer o manifesto, analise uma fonte documental por execução, mantenha o vínculo com o `source_id` selecionado no estado do operador e revise a resposta antes da mesclagem.

Nunca envie `.yaml` ou `.yml` diretamente. Antes do upload, derive uma fonte aceita:

```bash
python3 notebooklm-modelagem/scripts/yaml_to_markdown.py \
  --output caminho/templates-yaml.md \
  notebooklm-modelagem/templates/00-manifesto-fontes.template.yaml
```

Para vários YAML do mesmo módulo, passe todos na mesma execução. O arquivo Markdown conserva um cabeçalho por caminho e cada conteúdo dentro de um bloco `yaml`. Registre o hash do YAML canônico e o hash da fonte derivada.

Liste IDs e estados sem depender do título:

```bash
notebooklm source list \
  --notebook 93446a17-55bf-4cd8-b9f9-18c52c8f4c1d \
  --json
```

As fontes de uma etapa incluem os documentos de controle necessários, os artefatos promovidos anteriores e as fontes originais usadas como evidência. Caminhos mencionados no prompt não tornam arquivos locais visíveis ao NotebookLM.

Não execute geração, upload ou promoção sem autorização para modificar o notebook.

## Executar uma etapa

Use somente a fonte documental analisada e os controles indispensáveis. Repita `--source` para esses IDs:

```bash
notebooklm generate report \
  --notebook 93446a17-55bf-4cd8-b9f9-18c52c8f4c1d \
  --source SOURCE_ID_1 \
  --source SOURCE_ID_2 \
  --format custom \
  --language pt_BR \
  --prompt-file notebooklm-modelagem/prompts/00-reconciliar-fontes.md \
  --json
```

Registre o `task_id` retornado. Aguarde exatamente esse ID:

```bash
notebooklm artifact wait TASK_ID \
  --notebook 93446a17-55bf-4cd8-b9f9-18c52c8f4c1d \
  --timeout 600 \
  --json
```

Baixe pelo mesmo identificador, sem selecionar por “mais recente”:

```bash
notebooklm download report caminho/artefato.yaml \
  --notebook 93446a17-55bf-4cd8-b9f9-18c52c8f4c1d \
  --artifact ARTIFACT_ID \
  --no-clobber \
  --json
```

## Validar e aprovar

```bash
python3 notebooklm-modelagem/scripts/validate_yaml.py \
  --schema notebooklm-modelagem/schemas/artifact-envelope.schema.json \
  --state caminho/estado-execucao.yaml \
  caminho/artefato.yaml

sha256sum caminho/artefato.yaml
```

Para `SOURCE_MANIFEST`, `--state` exige correspondência integral entre `sources[].notebook_source_id` e `selected_sources[].source_id`. Validação de schema isolada não comprova a identidade das fontes. Além da validação mecânica, confirme escopo, evidências, conflitos e ausência de alegações de execução. Registre resultado, hash, revisor e decisão no estado do operador.

O prompt `07` gera apenas `recommendation`. A autorização física existe somente quando `physical_gate.operator_decision` foi preenchida por responsável humano com escopo, data e evidência.

## Promover o artefato aprovado

Converta o YAML validado em Markdown de ingestão e registre os hashes dos dois arquivos:

```bash
python3 notebooklm-modelagem/scripts/yaml_to_markdown.py \
  --output caminho/artefato.yaml.md \
  caminho/artefato.yaml

sha256sum caminho/artefato.yaml caminho/artefato.yaml.md
```

Adicione apenas o Markdown derivado como nova fonte:

```bash
notebooklm source add caminho/artefato.yaml.md \
  --notebook 93446a17-55bf-4cd8-b9f9-18c52c8f4c1d \
  --type file \
  --title "RUN_ID — DOCUMENT_ID vVERSAO" \
  --json
```

Registre a nova `source_id` e aguarde seu processamento:

```bash
notebooklm source wait SOURCE_ID \
  --notebook 93446a17-55bf-4cd8-b9f9-18c52c8f4c1d \
  --timeout 600 \
  --json
```

Somente depois do estado pronto essa fonte pode aparecer no `--source` da etapa seguinte.

## Construir e verificar a migration real

O NotebookLM entrega candidatos separados. O operador:

1. cria a migration com `supabase migration new <descricao>`;
2. compõe nela DDL, revogações, grants, RLS e policies do mesmo escopo;
3. mantém rollback em arquivo operacional separado;
4. executa `supabase db reset` em ambiente local descartável;
5. executa `supabase test db`;
6. registra comandos, códigos de saída e logs como evidência;
7. não usa `db reset --linked` sem autorização explícita, pois é destrutivo.

Não altere objetos internos dos schemas `auth`, `storage` ou `realtime`. Não fixe versão de extensão em `CREATE EXTENSION` ou `ALTER EXTENSION`.

## Encerrar a execução

A execução só pode ser concluída quando:

- a matriz `AS_BUILT` reflete os objetos realmente implementados;
- os testes possuem resultados observáveis;
- divergências e riscos residuais estão registrados;
- a conclusão é emitida por domínio;
- aprovações necessárias possuem responsável, instante e evidência.
