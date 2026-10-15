# Plano de Extração e Estruturação do Artefato YAML: Enriquecimento da Fonte "IHF Beach Handball Rules 2026"

---

## 1. Instruções Gerais de Formatação e Contrato do Artefato

### 1.1. Regra de Emissão e Diretivas do Envelope CEPRAEA (YAML Puro)
A geração automatizada do artefato de enriquecimento normativo por LLMs ou pipelines de extração deve obedecer rigorosamente às especificações de governança documental e arquitetura de dados do sistema CEPRAEA / Gemini Notebook (`GOV-901` e `CTRL — Contrato_Artefatos`).

* **Emissão Estrita do Artefato Final:** Quando este documento for utilizado como prompt operacional para emissão do manifesto final, o gerador deve emitir exclusivamente o payload YAML válido. Não devem ser incluídos textos preambulares, saudações, explicações conversacionais ou marcas de formatação externa.
* **Envelope Obrigatório de Sistema:** Em estrita conformidade com o padrão `CTRL — Contrato_Artefatos (schema_version: "1.1")`, a raiz do artefato deve conter o bloco identificador `document` e as seções canônicas de modelagem:
  * `schema_version`
  * `document`
  * `source_assessment`
  * `evidence_refs`
  * `reconciliation_signals`
  * `open_issues`
* **Tratamento de Dados Ausentes e Não Demonstrados:** Metadados operacionais não demonstráveis no texto da norma de origem (tais como `run_id`, `generated_at`, `supersedes` ou hashes de execução) devem ser obrigatoriamente declarados como o valor escalar `null` (em minúsculas, sem aspas). É vedada a criação de identificadores fictícios ou preenchimento de campos com textos genéricos (ex.: "TBD", "A definir").

### 1.2. Convenções Sintáticas e Regras Validadoras YAML 1.2
Para garantir *parsing* determinístico no pipeline de validação e ingestão relacional (PostgreSQL / Supabase), o artefato deve respeitar as seguintes restrições estruturais:

* **Indentação e Espaçamento:** Indentação uniforme de exatamente dois (2) espaços por nível hierárquico. O uso do caractere *tab* (tabulação) é expressamente proibido.
* **Proibição de Recursos Avançados:** É vedado o uso de *anchors* (`&`), *aliases* (`*`) ou *merge keys* (`<<`).
* **Tipagem e Enquadramento de Valores:**
  * Datas em formato ISO-8601 (`YYYY-MM-DD`), números de versão, códigos de idioma (ISO 639-1), identificadores semânticos e valores enumerados (*enums*) devem ser grafados entre aspas duplas (ex.: `"2026-03-01"`, `"en"`, `"VIGENTE"`, `"AUTORITATIVA"`).
  * Valores booleanos devem ser declarados estritamente como `true` ou `false` (em minúsculas, sem aspas).
* **Ausência de Valor e Listas Vazias:** A ausência de valor escalar deve ser representada como `null`. Coleções ou listas sem elementos devem ser representadas explicitamente como `[]`.
* **Identificadores Semânticos:** Todos os identificadores de elementos, evidências e pendências devem seguir a convenção `UPPER_SNAKE_CASE` sem acentuação (ex.: `EVID_IHF2026_001`, `ISSUE_BEACH_HANDBALL_001`).

---

## 2. Mapeamento da Avaliação da Fonte (`source_assessment`)

### 2.1. Identificação Canônica e Metadados Formais
A extração dos metadados formais da norma primária "IHF Beach Handball Rules 2026" reflete os dados extraídos da capa, folha de rosto e cabeçalhos oficiais da publicação.

| Campo do Esquema | Valor Extraído / Proposto | Fundamentação na Fonte |
| :--- | :--- | :--- |
| `canonical_title_proposal` | `"IX. Rules of the Game - b) Beach Handball"` | Capa e folha de rosto oficial do documento da IHF. |
| `publisher` | `"International Handball Federation"` | Entidade reguladora e emissora internacional. |
| `source_revision` | `"Edition: 1 March 2026"` | Edição declarada na página de título e rodapés. |
| `publication_date` | `"2026-03-01"` | Data oficial de publicação em formato ISO-8601. |
| `language` | `"en"` | Idioma oficial primário do texto normativo. |
| `source_type` | `"NORMA_OFICIAL"` | Categoria documental de regra esportiva internacional. |

### 2.2. Classificação de Autoridade e Ciclo de Vida
* **`authority_class_proposal`:** `"AUTORITATIVA"`
* **`lifecycle_status_proposal`:** `"VIGENTE"`
* **`classification_rationale`:** O documento constitui o regulamento internacional oficial emitido pela International Handball Federation (IHF) regendo a modalidade de Handebol de Praia. Conforme estabelecido nas regras de precedência da diretiva de governança `GOV-901` (Prioridade 1 — Regras IHF vigentes, versão oficial em inglês), este documento possui o nível máximo de autoridade normativa sobre regulamentos locais, estaduais ou traduções.

### 2.3. Demonstração de Limitações Normativas (`limitations`)
O campo `limitations` dentro de `source_assessment` registra as ressalvas e escopos temporais específicos contidos na nota oficial da página 2 do regulamento:

1. As provisões normativas destacadas em grifo amarelo ao longo do texto entram em vigor especificamente em 1 de julho de 2026 (*"The provisions highlighted in yellow will come into force on 1 July 2026"*).
2. As provisões relativas aos uniformes das atletas femininas entraram em vigor em 1 de janeiro de 2022 (*"The provisions related to the uniform for female athletes will come into force on 1 January 2022"*).
3. Por razões de simplicidade, o texto utiliza genericamente a forma masculina para se referir a jogadores, oficiais e árbitros, aplicando-se equitativamente a ambos os gêneros, com exceção expressa da Regra 3 (Tamanho da Bola).

---

## 3. Mapeamento de Referências de Evidência Normativa (`evidence_refs`)

O mapeamento de evidências extrai as regras do texto normativo, fornecendo localizadores precisos, categorização e interpretação relacional para fundamentar as restrições e esquemas do banco de dados PostgreSQL.

### 3.1. Especificações Geométricas, Estruturais e de Iluminação (Regra 1 e Anexo)

* **Evidência EVID_IHF2026_001:**
  * `source_id`: `"SRC_IHF_RULES_2026"`
  * `locator`: `"Rule 1:1, Page 4"`
  * `evidence_type`: `"REGRA"`
  * `interpretation`: Dimensões oficiais da quadra de jogo: retângulo de $27\text{ m}$ de comprimento por $12\text{ m}$ de largura, composto por uma área de jogo ($15\text{ m} \times 12\text{ m}$) e duas áreas de gol ($6\text{ m} \times 12\text{ m}$). A profundidade da camada de areia nivelada, fina e livre de pedras deve ser de no mínimo $40\text{ cm}$.
* **Evidência EVID_IHF2026_002:**
  * `source_id`: `"SRC_IHF_RULES_2026"`
  * `locator`: `"Rule 1:1, Page 4; Sand Quality and Lighting Regulations, Page 64"`
  * `evidence_type`: `"REGRA"`
  * `interpretation`: Níveis de iluminação artificial para partidas noturnas: mínimo absoluto de $400\text{ lux}$ para competições locais e faixa de $1000\text{ a }1500\text{ lux}$ (medidos a $1\text{ m}$ da superfície) para competições internacionais noturnas ou transmissões televisivas.

### 3.2. Composição da Equipe, Limites e Delimitações Posicionais de Substituição (Regras 1, 4 e 5)

* **Evidência EVID_IHF2026_003:**
  * `source_id`: `"SRC_IHF_RULES_2026"`
  * `locator`: `"Rule 4:2-3, Pages 11-12"`
  * `evidence_type`: `"REGRA"`
  * `interpretation`: Uma equipe é composta por até 10 jogadores. É exigido o mínimo de 6 jogadores presentes no início da partida. Se o número de jogadores aptos cair abaixo de 4 durante o jogo, a partida é encerrada e a equipe adversária é declarada vencedora. O máximo de jogadores em quadra simultaneamente é 4 (3 jogadores de linha e 1 goleiro).
* **Evidência EVID_IHF2026_004:**
  * `source_id`: `"SRC_IHF_RULES_2026"`
  * `locator`: `"Rule 1:7, Pages 5-6; Rule 4:13, Page 14; Rule 5:12, Page 15"`
  * `evidence_type`: `"REGRA"`
  * `interpretation`: A área de substituição dos jogadores de linha possui $15\text{ m}$ de comprimento por $3\text{ m}$ de largura. Jogadores de linha e goleiro podem sair da quadra pelo caminho mais curto na lateral de sua própria área de substituição. Contudo, a entrada do goleiro substituto deve ocorrer obrigatoriamente pela linha lateral da sua própria área de gol no lado da sua área de substituição. O goleiro reserva pode aguardar sua entrada sentado ou ajoelhado no trecho entre a linha de gol e a linha da área de gol (exceto no Shoot-out).

### 3.3. Sistema de Pontuação, Exceção Negativa de In-Flight e Desempates (Regra 9 e Clarificações 1 e 2)

* **Evidência EVID_IHF2026_005:**
  * `source_id`: `"SRC_IHF_RULES_2026"`
  * `locator`: `"Rule 9:2, 9:3, 9:6, Page 22; Clarification 1, Page 47"`
  * `evidence_type`: `"REGRA"`
  * `interpretation`: Valoração de gols de 2 pontos: gols criativos ou espetaculares (*spin shot*, *in-flight*), gols em tiro de 6 metros e gols marcados pelo goleiro. Regra de Exceção Negativa para *In-Flight*: 2 pontos são concedidos **apenas** se o atleta controlar a bola e arremessar enquanto estiver no ar; dar um tapa (*slap*) ou empurrar (*push*) a bola para o gol sem o controle aéreo completo vale apenas **1 ponto**.
* **Evidência EVID_IHF2026_006:**
  * `source_id`: `"SRC_IHF_RULES_2026"`
  * `locator`: `"Rule 9:7-8, Pages 22-23; Clarification 2, Page 47; Clarification 9, Page 56"`
  * `evidence_type`: `"REGRA"`
  * `interpretation`: Desempates: empate ao fim de um período é decidido por *Golden Goal* (vence quem marcar o primeiro gol). Se cada equipe vencer um período (1-1), a partida é decidida via *Shoot-out* (5 arremessos alternados por equipe, com o atleta partindo da interseção da linha da área de gol com a linha lateral e passando para o seu goleiro antes de finalizar).

### 3.4. Controle de Jogo Passivo e Algoritmo de Contagem de Passes (Regra 7 e Clarificação 4)

* **Evidência EVID_IHF2026_007:**
  * `source_id`: `"SRC_IHF_RULES_2026"`
  * `locator`: `"Rule 7:10-11, Page 18; Clarification 4-D, Pages 50-54"`
  * `evidence_type`: `"REGRA"`
  * `interpretation`: Jogo Passivo e sinal de advertência (Gesto nº 16). Limite de 4 passes após a advertência para finalização. Exceções de contagem:
    1. Antes do 4º passe: passe desviado pela defesa para fora da linha lateral/fundo, falta cometida pela defesa durante o passe, ou arremesso bloqueado recuperado pelo ataque **não** contam como passe na contagem limite.
    2. Após o 4º passe: se a equipe atacante sofrer falta, obtiver tiro livre/tiro lateral/tiro de goleiro ou tiver um arremesso bloqueado e mantiver a posse, é permitido **1 passe adicional** para finalizar o ataque.
    3. Rebound do gol/goleiro ou punição pessoal (Regra 16) aplicada à defesa **anulam** o sinal de advertência, iniciando nova fase de armação.

### 3.5. Protocolo de Exceção dos Últimos 15 Segundos e Golden Goal (Regra 8:11 e Clarificação 10)

* **Evidência EVID_IHF2026_008:**
  * `source_id`: `"SRC_IHF_RULES_2026"`
  * `locator`: `"Rule 8:11, Page 21; Clarification 10, Pages 56-57"`
  * `evidence_type`: `"REGRA"`
  * `interpretation`: A regra dos últimos 15 segundos aplica-se quando o cronômetro do placar indica **`9:45`** (em contagem progressiva de 10 minutos) ou **`0:15`** (em contagem regressiva), e durante todo o *Golden Goal*. Se a bola estiver fora de jogo e um defensor impedir/atrasar a execução do tiro, ou se a bola estiver em jogo e houver infração enquadrada nas Regras 8:5, 8:7 ou 8:10, o infrator deve ser desqualificado (*cartão vermelho*) e um tiro de 6 metros deve ser concedido à equipe adversária.

---

## 4. Sinais de Reconciliação e Precedência (`reconciliation_signals`)

### 4.1. Precedência Idiomática e Hierarquia Normativa (GOV-901 / Prioridade 1)
* **Sinal de Precedência de Idioma:** O documento analisado corresponde à versão oficial em inglês da IHF ("Edition: 1 March 2026").
* **Diretriz de Governança:** Conforme a diretiva de modelagem `GOV-901` (Seção 2), em caso de conflitos interpretativos com regulamentos locais, estaduais ou traduções em português (ex.: regulamentos estaduais ou nacionais), a presente norma oficial em inglês possui precedência absoluta no modelo relacional.

### 4.2. Temporalidade e Coexistência de Vigências Diferenciadas
* **Sinal de Coexistência Temporal Interna:** O documento normativo possui duas camadas de vigência distintas que devem ser refletidas nos testes de validação temporal do sistema:
  1. *Regra Geral e Trechos Grifados:* Disposições grifadas em amarelo entram em vigor em **1 de julho de 2026**.
  2. *Regulamento do Vestuário Feminino:* As especificações do uniforme feminino possuem marco de vigência mantido desde **1 de janeiro de 2022**.

---

## 5. Mapeamento de Pendências e Inconsistências Operacionais (`open_issues`)

### 5.1. Formulário de Registro de Pendências
Para assegurar o correto preenchimento do envelope relacional, quaisquer lacunas do sistema devem ser mapeadas utilizando identificadores semânticos em `UPPER_SNAKE_CASE` no campo `affected_ids`.

* **Pendência ISSUE_BEACH_HANDBALL_001:**
  * `status`: `"ABERTA"`
  * `question`: "Como os metadados de execução de runtime do CEPRAEA (run_id, generated_at e hashes sha256 dos artefatos de entrada) serão injetados no envelope do manifesto?"
  * `affected_ids`: `["DOC_RUN_ID", "DOC_GENERATED_AT", "DOC_INPUT_ARTIFACTS"]`
  * `impact`: "A ausência desses metadados operacionais impede a promoção automatizada do artefato do estado PROPOSTO para VIGENTE no catálogo do PostgreSQL."
  * `required_evidence`: "Registro do operador no arquivo de controle 'operator/estado-execucao.yaml'."
  * `owner`: `"OPERADOR_SISTEMA"`

---

## 6. Especificação Completa do Artefato YAML Proposto (Modelo Executável Reconciliado)

Abaixo é apresentada a especificação exata do artefato YAML, pronta para ingestão, totalmente compatível com a especificação YAML 1.2 e em conformidade com o contrato de dados do CEPRAEA.

schema_version: "1.1"
document:
  id: "EVID_IHF_BEACH_HANDBALL_2026"
  artifact_kind: "SOURCE_ENRICHMENT_MANIFEST"
  title: "Manifesto de Enriquecimento e Extração Normativa - IHF Beach Handball Rules 2026"
  version: "0.1.0"
  status: "PROPOSTO"
  run_id: null
  domain_id: "BEACH_HANDBALL"
  notebook_id: "93446a17-55bf-4cd8-b9f9-18c52c8f4c1d"
  generated_at: null
  supersedes: null
  input_artifacts: []

source_assessment:
  canonical_title_proposal: "IX. Rules of the Game - b) Beach Handball"
  publisher: "International Handball Federation"
  source_revision: "Edition: 1 March 2026"
  publication_date: "2026-03-01"
  language: "en"
  source_type: "NORMA_OFICIAL"
  authority_class_proposal: "AUTORITATIVA"
  lifecycle_status_proposal: "VIGENTE"
  classification_rationale: "Documento oficial emanado pela federação internacional (IHF) regendo as regras do Handebol de Praia. De acordo com as diretrizes de governança GOV-901 / Prioridade 1, normas oficiais da IHF na língua inglesa possuem nível máximo de precedência sobre regulamentos regionais ou traduções."
  limitations:
    - "As provisões normativas destacadas em grifo amarelo ao longo do texto entram em vigor em 1 de julho de 2026."
    - "As provisões relativas aos uniformes das atletas femininas entraram em vigor em 1 de janeiro de 2022."
    - "O texto utiliza genericamente a forma masculina para se referir a participantes, aplicando-se equitativamente a ambos os gêneros, com exceção da Regra 3 (Tamanho da Bola)."

evidence_refs:
  - id: "EVID_IHF2026_001"
    source_id: "SRC_IHF_RULES_2026"
    locator: "Rule 1:1, Page 4"
    evidence_type: "REGRA"
    interpretation: "Dimensões da quadra (27m x 12m), constituída por área de jogo (15m x 12m) e duas áreas de gol (6m x 12m). Profundidade mínima da areia de 40 cm composta de grãos finos e nivelados."

  - id: "EVID_IHF2026_002"
    source_id: "SRC_IHF_RULES_2026"
    locator: "Rule 1:1, Page 4; Sand Quality and Lighting Regulations, Page 64"
    evidence_type: "REGRA"
    interpretation: "Requisitos de iluminação artificial: mínimo de 400 lux para jogos locais e faixa de 1000 a 1500 lux para competições internacionais noturnas ou transmissões de TV."

  - id: "EVID_IHF2026_003"
    source_id: "SRC_IHF_RULES_2026"
    locator: "Rule 4:2-3, Pages 11-12"
    evidence_type: "REGRA"
    interpretation: "Equipe com até 10 jogadores. Exigido mínimo de 6 para iniciar a partida. Se o número de aptos cair abaixo de 4, a partida é encerrada. Máximo de 4 jogadores em quadra simultaneamente (3 de linha e 1 goleiro)."

  - id: "EVID_IHF2026_004"
    source_id: "SRC_IHF_RULES_2026"
    locator: "Rule 1:7, Pages 5-6; Rule 4:13, Page 14; Rule 5:12, Page 15"
    evidence_type: "REGRA"
    interpretation: "Área de substituição de 15m x 3m. Substituições são ilimitadas. Saída permitida pelo caminho mais curto na lateral de substituição. Entrada do goleiro obrigatoriamente pela linha lateral da sua área de gol. Goleiro reserva pode aguardar sentado/ajoelhado entre a linha de gol e a linha da área de gol."

  - id: "EVID_IHF2026_005"
    source_id: "SRC_IHF_RULES_2026"
    locator: "Rule 9:2, 9:3, 9:6, Page 22; Clarification 1, Page 47"
    evidence_type: "REGRA"
    interpretation: "Valoração de 2 pontos para gols criativos/espetaculares (spin shot, in-flight), tiro de 6m e gol do goleiro. Regra Negativa de In-Flight: 2 pontos exigem controle aéreo e arremesso no ar; tapa ('slap') ou empurrão ('push') na bola sem controle aéreo vale apenas 1 ponto."

  - id: "EVID_IHF2026_006"
    source_id: "SRC_IHF_RULES_2026"
    locator: "Rule 9:7-8, Pages 22-23; Clarification 2, Page 47; Clarification 9, Page 56"
    evidence_type: "REGRA"
    interpretation: "Desempates: empate em período é decidido por Golden Goal. Empate em períodos (1-1) é decidido por Shoot-out (5 arremessos alternados com passe inicial ao próprio goleiro)."

  - id: "EVID_IHF2026_007"
    source_id: "SRC_IHF_RULES_2026"
    locator: "Rule 7:10-11, Page 18; Clarification 4-D, Pages 50-54"
    evidence_type: "REGRA"
    interpretation: "Jogo passivo: limite de 4 passes após o sinal de advertência (Gesto 16). Passes desviados pela defesa, faltas sofridas na passagem ou chutes bloqueados não incrementam a contagem prévia. Após o 4º passe, infrações defensivas ou chutes bloqueados concedem 1 passe adicional para finalizar. Rebound de gol/goleiro ou sanção pessoal anulam a advertência."

  - id: "EVID_IHF2026_008"
    source_id: "SRC_IHF_RULES_2026"
    locator: "Rule 8:11, Page 21; Clarification 10, Pages 56-57"
    evidence_type: "REGRA"
    interpretation: "Regra dos últimos 15 segundos: iniciada quando o relógio indica 9:45 (contagem progressiva de 10 min) ou 0:15 (contagem regressiva) e durante o Golden Goal. Impedir/atrasar tiros com bola fora de jogo ou cometer infrações das Regras 8:5, 8:7 ou 8:10 com bola em jogo resulta em desqualificação direta e tiro de 6 metros."

reconciliation_signals:
  - signal_type: "LANGUAGE_PRECEDENCE"
    description: "O documento é a versão oficial em inglês da IHF (Edição 1 de Março de 2026). Conforme GOV-901, possui precedência sobre qualquer tradução ou regulamento local."
  - signal_type: "TEMPORAL_COEXISTENCE"
    description: "Coexistência de vigências: alterações em amarelo vigoram a partir de 01/07/2026; regulamento de uniforme feminino vigora desde 01/01/2022."

open_issues:
  - id: "ISSUE_BEACH_HANDBALL_001"
    status: "ABERTA"
    question: "Como os metadados de execução de runtime do CEPRAEA (run_id, generated_at e hashes sha256 dos artefatos de entrada) serão injetados no envelope do manifesto?"
    affected_ids:
      - "DOC_RUN_ID"
      - "DOC_GENERATED_AT"
      - "DOC_INPUT_ARTIFACTS"
    impact: "A ausência desses metadados operacionais impede a promoção automatizada do artefato do estado PROPOSTO para VIGENTE no catálogo do PostgreSQL."
    required_evidence: "Registro do operador no arquivo de controle 'operator/estado-execucao.yaml'."
    owner: "OPERADOR_SISTEMA"
