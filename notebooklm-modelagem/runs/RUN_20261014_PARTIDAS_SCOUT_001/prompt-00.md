# Execução 00 — Reconciliar fontes

Produza somente o conteúdo de `00-manifesto-fontes.yaml`.

## Identificação da execução

- `run_id`: `RUN_20261014_PARTIDAS_SCOUT_001`
- `domain_id`: `PARTIDAS_SCOUT_ANALISE_TATICA`
- `reference_date`: `2026-10-14`

## Escopo incluído

- partida, sets, segmentos e shoot-out;
- placar e eventos de pontuação;
- gols de um e dois pontos, spin shot, in-flight e tiro de seis metros;
- punições e exclusões;
- posses, fases ofensivas e sistemas defensivos;
- ações da goleira e zonas da quadra;
- resultado das ações;
- scout, protocolo, observador, revisão e confiabilidade;
- mídia observacional, trecho e timecode somente como proveniência do fato esportivo;
- modelos e SQL existentes somente como propostas históricas a reconciliar.

## Escopo excluído

- carga e planejamento de treinamento;
- saúde, prontuário ou avaliação médica;
- gestão financeira ou administrativa;
- mídia institucional e acervo fotográfico;
- autenticação, armazenamento e infraestrutura fora do necessário para classificar os artefatos históricos.

## Regras

Use apenas as fontes explicitamente selecionadas nesta solicitação. Siga as fontes de controle `Fluxo_Modelagem`, `Instrucoes_Notebook`, `Contrato_Artefatos` e `Template_00_Manifesto_MD`.

1. Registre o `notebook_source_id` real de cada fonte selecionada.
2. Classifique autoridade, vigência, escopo, revisão e limitações.
3. Detecte duplicidades, traduções, substituições e material histórico.
4. Crie `evidence_refs` com IDs únicos e localizadores precisos.
5. Registre precedências demonstráveis e conflitos não resolvidos.
6. Trate modelos, dicionários e SQL já existentes como propostas históricas, salvo decisão humana em contrário.
7. Não promova uma fonte por nome, pasta ou rótulo editorial.
8. Não faça modelagem conceitual, lógica ou física.
9. Não alegue leitura de fonte que não esteja entre os IDs selecionados.

Use `null` quando revisão, hash, data ou localizador não estiverem disponíveis. Crie pendência rastreável quando a ausência impedir uma conclusão.

Retorne somente YAML válido conforme o template selecionado, sem cerca Markdown, introdução ou conclusão. O documento deve começar como `PROPOSTO`.
