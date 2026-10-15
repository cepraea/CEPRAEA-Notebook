# Correção da etapa 00 — YAML estrito

Sua resposta deve começar exatamente com `schema_version: "1.1"`. Não escreva título Markdown, introdução, plano de execução, cerca de código ou conclusão.

Produza o conteúdo completo de `00-manifesto-fontes.yaml` conforme a fonte `00-manifesto-fontes.template`.

## Identificação fixa

- `run_id`: `RUN_20261014_PARTIDAS_SCOUT_001`
- `domain_id`: `PARTIDAS_SCOUT_ANALISE_TATICA`
- `reference_date`: `2026-10-14`
- `document.status`: `PROPOSTO`

Nenhuma fonte ou artefato está aprovado. Valores como `APPROVED`, `ACTIVE` ou `CANÔNICO` encontrados nos documentos são alegações históricas, não estados válidos desta execução.

## Mapa obrigatório de fontes

Use o UUID da esquerda literalmente em `notebook_source_id`. Não substitua UUID por título, índice ou ID inventado.

```text
965f27f8-7475-43d0-a5b3-0fc985debf80 | CTRL — Fluxo_Modelagem — acf6afa2aab0
991b26f0-0d26-4cfe-935d-81b92dee7c76 | CTRL — Instrucoes_Notebook — a6ede74b1baa
cf663fd6-cb2a-4c03-82a0-a31023023f1c | CTRL — Contrato_Artefatos — db2d64da9680
718459c6-32df-46cc-bfb8-15b981a2b01e | 00-manifesto-fontes.template
d7ebb4e2-04f1-43f8-b2a0-152b98e5a226 | regras_ihf_beach_handball_2026_en.pdf.pdf
236e788c-9c85-4133-93c8-4650a26e867a | Regras de Handebol de Praia 2026 — tradução
0d48291e-32ab-449e-8f86-ea43244c921c | atualizacoes_ihf_2026.md
9c553f24-6f99-4a21-b63c-9cbfda6552c1 | Esclarecimentos regras de jogo.pdf
e593c4e6-903a-4169-a1c5-7f551bbe5b9d | Regulamento Geral Campeonato Carioca 2026
bb8b9ba4-cd24-452a-aa2b-2a3a3854e0a0 | regulamento_cbhb_2026.pdf
f68c1687-7153-4283-a6a0-5e33b814fe00 | 2-point goals — spin and in-flight
049d2bf2-ac90-44f8-951a-ae9a32c0cc64 | 6-metre throw + punishments
a44eece7-56e3-407c-9348-23b35ab0efa4 | Protocolo de Scout — Beach Handball
162256e7-41bf-40ac-b77f-7b892250771f | Instrument for observation of collective tactical procedures
605ea05f-b931-405d-984f-4773065aa6c8 | Contextual factors and decision-making in positional attack
74cb7983-decc-42de-86eb-f691d8e00d53 | O jogo ofensivo do handebol de areia
d8076ca2-b651-48af-be4e-b14dd524c377 | Latest trends in defence
de6241bc-cad8-42a5-80db-015ef2c1a780 | Structuring of the defensive phase
a3068def-bef6-49bd-b063-c8593116298f | Estudo das ações do guarda-redes
9b742f2e-0d21-4fb1-bca9-33411d6c6ec2 | Tempos de defesa do goleiro
36d92b57-69c1-4563-a2a4-71a7bd357dc7 | Psychological pressure in shootouts
569f2d66-ba38-41fc-aa84-d854bb6d0df9 | CEPRAEA DATABASE
3bb0c332-947d-494f-a6fa-85493b579464 | 04A-MODELO-CONCEITUAL.md
aef04d7f-4e75-4597-8f96-acc3b87f945d | 04B-MODELO-LOGICO.md
fef688f6-d141-475d-87c0-abbeaffe46fb | 04C-DICIONARIO-DE-DADOS.md
475ce51f-f4bd-44ca-8194-31d42ea308e8 | catalogo-regras-invariantes.md
2cea376b-08be-4969-b2e4-d66189ca0935 | matriz-relacoes-cardinalidades.md
c30b6966-654c-4682-84d5-41b0d15febb0 | 05-schema-postgresql.sql
e9e4272e-d302-4ce3-bf80-b1c9bdc84060 | 06-migrations-rollback.sql.md
49ceb0ca-9160-4d36-a8ac-b58470c73f80 | 07-matriz-rbac-e-politicas-rls
```

## Escopo

Inclua regras da partida, sets, segmentos, shoot-out, placar, pontuação, finalizações de um e dois pontos, tiro de seis metros, punições, posses, fases ofensivas, sistemas defensivos, ações da goleira, zonas, resultado, scout, protocolo, observador, revisão, confiabilidade, trecho e timecode.

Exclua treinamento, saúde, finanças, gestão administrativa, mídia institucional e infraestrutura não necessária a este domínio.

## Classificação

- As quatro fontes `CTRL` são controles da execução, não evidência esportiva.
- Regras IHF e regulamentos vigentes têm precedência dentro de seus escopos demonstrados.
- Protocolo e planilha CEPRAEA são fontes operacionais, não regras oficiais do esporte.
- Artigos e materiais técnicos são suporte.
- Os oito modelos ou SQL ao final do mapa são propostas históricas; não comprovam implementação, teste ou aprovação.
- Tradução não supera o texto oficial quando houver divergência.

Crie IDs semânticos estáveis em `UPPER_SNAKE_CASE`. Use somente `evidence_ref_ids` existentes. Localizador desconhecido deve ser `null` ou gerar pendência; nunca use `...`, `TBD`, `TODO` ou “a definir”.

Retorne somente YAML válido.
