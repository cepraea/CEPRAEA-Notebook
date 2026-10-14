# Fontes NotebookLM

Nenhuma ação foi executada.

## Correções necessárias na proposta

1. **As normas pagas não estão atualmente no notebook**

   A lista atual de 28 fontes não contém os textos integrais da ISO/IEC 42001, ISO/IEC 42005 ou ISO/IEC 23894. Elas apareceram apenas como recomendações na auditoria anterior.

   Portanto, a ação correta é **evitar introduzir dependência de fontes pagas**, e não substituir fontes já existentes.

2. **Não existe equivalência gratuita para conformidade ISO**

   NIST e OWASP podem oferecer cobertura técnica equivalente ou superior em determinados assuntos, mas não permitem declarar conformidade com uma norma ISO.

   A substituição é válida se o objetivo for:

   - conhecimento técnico;
   - definição de controles;
   - segurança e governança operacional;
   - avaliação de riscos.

   Ela não é válida para certificação, auditoria contratual ou declaração de conformidade ISO.

3. **“Completar o conhecimento” é um critério impossível de verificar**

   O resultado verificável deve ser: cobrir as lacunas identificadas em uma matriz finita de capacidades, não garantir conhecimento completo do domínio.

4. **A transformação não pode apagar a proveniência**

   Cada Markdown deve continuar identificado como síntese ou transformação de uma fonte externa. Ele não deve parecer uma nova norma interna nem herdar autoridade apenas por receber um prefixo `DRTZ`.

5. **Não convém consolidar tudo em um documento único**

   Isso repetiria o problema de `DRTZ-0001`: mistura de escopos, perda de granularidade e recuperação RAG ambígua.

## Conjunto mínimo recomendado

Um conjunto enxuto de fontes gratuitas e primárias seria:

| Fonte | Lacuna preenchida |
| --- | --- |
| NIST AI RMF 1.0 | Governança e gestão de riscos de IA |
| [NIST AI 600-1 — Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | Proveniência, testes prévios, governança e incidentes |
| [NIST SP 800-218A](https://csrc.nist.gov/pubs/sp/800/218/a/final) | Secure SDLC específico para IA |
| [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | Principais riscos de sistemas agentic |
| [OWASP Agentic AI — Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) | Controles e mitigações detalhados |
| SLSA Provenance | Proveniência e integridade de builds |
| [SPDX](https://spdx.dev/) | SBOM, componentes e cadeia de suprimentos |
| CISA/NCSC Guidelines for Secure AI System Development | Desenvolvimento e operação segura de sistemas de IA |

Esse conjunto é suficiente para a primeira execução. MITRE ATLAS, Google SAIF e outras referências podem ser avaliadas depois, somente se permanecer alguma lacuna.

## Avaliação dos fluxos possíveis

| Fluxo | Vantagem | Problema | Veredito |
| --- | --- | --- | --- |
| Adicionar URLs e PDFs diretamente | Mais rápido e quase sem transformação | Ruído, páginas mutáveis e estrutura inconsistente | Aceitável apenas para fontes limpas |
| Converter cada fonte em Markdown próprio | Melhor recuperação, rastreabilidade e controle | Exige transformação e validação | **Recomendado** |
| Criar um único “manual completo” | Poucos arquivos | Mistura autoridades, repete conteúdo e prejudica o RAG | Não recomendado |
| Usar Deep Research e importar tudo | Descoberta rápida | Seleção opaca, excesso de fontes e desperdício | Não recomendado |
| Originais mais sínteses duplicadas | Facilita comparação | Duplica conhecimento e competição entre trechos | Evitar como padrão |
| Markdown por fonte mais matriz transversal | Preserva autoridade e oferece visão integrada | Um artefato adicional para manter | **Melhor equilíbrio** |

## Fluxo recomendado

### 1. Congelar a matriz de lacunas

Usar somente estas dimensões:

1. governança e risco de IA;
2. segurança de agentes;
3. identidade, autorização e menor privilégio;
4. uso seguro de ferramentas;
5. prompt injection e goal hijacking;
6. memória e comunicação interagentes;
7. proveniência e cadeia de suprimentos;
8. testes prévios, monitoramento e incidentes;
9. supervisão humana e interrupção segura.

Verificação: cada dimensão deve apontar para pelo menos uma fonte primária.

### 2. Selecionar as fontes

Aceitar uma fonte somente quando ela for:

- primária e publicada pela organização responsável;
- gratuita e acessível integralmente;
- diretamente relevante para uma lacuna;
- identificada por versão ou data;
- legalmente transformável conforme sua licença;
- não redundante com outra fonte mais autoritativa.

Verificação: produzir uma tabela `lacuna → fonte → seções relevantes`.

### 3. Extrair apenas o conteúdo relevante

A transformação deve preservar:

- definições;
- ameaças;
- controles;
- responsabilidades;
- condições e exceções;
- evidências e critérios de validação.

Devem ser removidos:

- navegação, rodapés e menus;
- marketing;
- repetição;
- referências sem relação com o escopo;
- exemplos puramente promocionais.

Não reproduzir integralmente conteúdo protegido quando a licença não permitir. Nesses casos, produzir síntese fiel com referências por seção.

### 4. Criar um Markdown por fonte

Estrutura mínima:

```markdown
---
id: AGNT-0001
title: ...
publisher: ...
canonical_url: ...
source_version: ...
publication_date: ...
retrieved_at: ...
license: ...
document_type: primary-source-derived
authority_scope: ...
---

# Título

## Escopo

## Conceitos e definições

## Riscos ou requisitos

## Controles recomendados

## Evidências e critérios de verificação

## Limitações

## Rastreabilidade para a fonte primária
```

A sigla definitiva não deve ser decidida silenciosamente. `AGNT`, `SECU`, `RISK` ou outra taxonomia precisa ser aprovada ou incorporada formalmente à norma de nomenclatura existente.

### 5. Criar uma matriz transversal separada

Um único documento derivado deve mapear:

```text
Lacuna → ameaça/requisito → controle → fonte primária → seção
```

Ele não deve criar novas obrigações. Sua função é somente indexar e reconciliar os controles existentes.

### 6. Validar mecanicamente

Sem gastar tokens de modelo:

- exatamente um H1;
- hierarquia sem saltos;
- ausência de HTML e navegação;
- links válidos;
- metadados completos;
- nenhuma URL mutável quando houver versão fixa;
- nenhum marcador editorial pendente;
- nenhuma duplicação literal extensa;
- nenhum documento com múltiplos domínios desconexos.

### 7. Fazer validação semântica focalizada

Usar uma única passagem por documento para confirmar:

- fidelidade à fonte;
- ausência de controle inventado;
- preservação das condições;
- distinção entre requisito, recomendação e exemplo;
- escopo de autoridade correto.

### 8. Preparar pacote local antes da importação

Entregar para aprovação:

- arquivos Markdown;
- manifesto das fontes;
- matriz de cobertura;
- relatório de validação;
- lista do que continuará não coberto.

Somente depois dessa aprovação os arquivos seriam adicionados ao NotebookLM.

### 9. Validar após a futura importação

Após autorização específica:

1. adicionar cada fonte;
2. aguardar `status == ready`;
3. executar um conjunto fixo de perguntas de regressão;
4. confirmar que as respostas citam a fonte correta;
5. verificar que fontes candidatas não são apresentadas como normas internas.

## Economia de tokens

O fluxo evita desperdício porque:

- não executa Deep Research;
- limita a primeira rodada a aproximadamente oito fontes;
- não envia repetidamente todo o corpus ao modelo;
- usa validação mecânica para formatação;
- transforma somente as seções necessárias;
- evita originais e sínteses duplicados;
- usa uma única matriz de cobertura;
- adia fontes complementares até existir uma lacuna residual demonstrada.

## Tarefa revisada

> Identifique um conjunto mínimo de fontes primárias, gratuitas, atuais e legalmente reutilizáveis que cubra as lacunas confirmadas de governança e segurança de sistemas agentic no notebook `# Documentação Escrita`.
>
> Não trate referências gratuitas como equivalentes para fins de conformidade ISO. Use-as somente para cobertura técnica e operacional.
>
> Para cada fonte aprovada, extraia apenas o conteúdo relevante às lacunas, preserve sua proveniência e autoridade, e produza um arquivo Markdown independente, limpo, modular e compatível com o NotebookLM.
>
> Produza também um manifesto e uma matriz de rastreabilidade entre lacunas, controles, fontes e seções. Não crie novas regras de governança nem atribua caráter normativo a sínteses.
>
> Valide mecanicamente a estrutura dos arquivos e semanticamente sua fidelidade. Antes de qualquer importação, apresente o pacote, a cobertura obtida e as lacunas remanescentes para aprovação.
>
> Critério de sucesso: todas as dimensões priorizadas possuem ao menos uma fonte primária e controles verificáveis; todos os arquivos preservam versão, licença e proveniência; nenhuma obrigação foi inventada; e nenhuma fonte foi adicionada ao notebook sem aprovação posterior.

Essa versão é executável, econômica e possui critérios objetivos de conclusão.