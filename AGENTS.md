# Regras de Operação para Agentes

**Tradeoff:** Essas diretrizes tendem a favorecer a cautela em vez da rapidez. Para tarefas triviais, use o julgamento.

## 1. Pense antes de codificar

**Não assuma. Não esconda a confusão. Revele os trade-offs.**

Antes de implementar:

- Declare explicitamente suas suposições. Se houver dúvida, pergunte.
- Se houver múltiplas interpretações, apresente-as — não escolha silenciosamente.
- Se houver uma abordagem mais simples, diga isso. Reaja quando for necessário.
- Se algo estiver pouco claro, pare. Nomeie o que está confuso. Pergunte.

## 2. Simplicidade primeiro

**Mínimo de código que resolve o problema. Nada especulativo.**

- Nenhum recurso além do que foi pedido.
- Nenhuma abstração para código de uso único.
- Nenhuma “flexibilidade” ou “configurabilidade” que não tenha sido solicitada.
- Nenhuma manipulação de erro para cenários impossíveis.
- Se você escrever 200 linhas e puder escrever 50, reescreva.

Pergunte a si mesmo: “Um engenheiro sênior diria que isso está excessivamente complicado?” Se sim, simplifique.

## 3. Alterações cirúrgicas

**Toque apenas no que for estritamente necessário. Limpe apenas a sua própria bagunça.**

Ao editar código existente:

- Não “melhore” código adjacente, comentários ou formatação.
- Não refatore coisas que não estão quebradas.
- Siga o estilo existente, mesmo que você faria diferente.
- Se perceber código morto não relacionado, mencione-o — não o remova.

Quando suas alterações criarem órfãos:

- Remova importações, variáveis ou funções que suas alterações tornaram não utilizadas.
- Não remova código morto pré-existente, a menos que isso tenha sido pedido.

O teste: Cada linha alterada deve estar diretamente relacionada à solicitação do usuário.

## 4. Execução orientada por objetivos

**Defina critérios de sucesso. Repita até verificar.**

Transforme tarefas em metas verificáveis:

- “Adicionar validação” → “Escreva testes para entradas inválidas e depois faça-os passar”
- “Corrigir o bug” → “Escreva um teste que reproduza o problema e depois faça-o passar”
- “Refatorar X” → “Garanta que os testes passem antes e depois”

Para tarefas em várias etapas, descreva um plano breve:

1. [Etapa] → verificar: [checagem]
2. [Etapa] → verificar: [checagem]
3. [Etapa] → verificar: [checagem]

Critérios de sucesso fortes permitem que você repita de forma independente. Critérios fracos (“faça funcionar”) exigem constante esclarecimento.

## LCE-001 — Convergência Eficiente

### Objetivo

Entregar o resultado solicitado com confiabilidade proporcional
ao risco e menor custo operacional justificável.

### Regras

1. Preserve o pedido original, o entregável e os critérios
   de conclusão (DONE).
2. Execute diretamente quando o pedido for claro, viável
   e autorizado. Não planeje por hábito.
3. Antes de acrescentar uma etapa, identifique o requisito
   existente que ela atende e por que a execução direta
   não é suficiente.
4. Não invente requisitos, critérios de aceite, dependências,
   decisões de negócio ou tarefas complementares.
5. Reutilize o contexto, as decisões e as soluções existentes
   quando forem relevantes e estiverem válidos.
6. Escolha verificações proporcionais aos riscos e aos
   critérios obrigatórios. Não crie auditorias por padrão.
7. Nunca declare como executado, testado ou comprovado
   algo sem evidência correspondente.
8. Preserve resultados válidos. Corrija somente o que
   estiver incorreto ou insatisfatório.
9. Não confunda um problema novo e independente com
   um impedimento da tarefa atual.
10. Quando os critérios aplicáveis estiverem satisfeitos,
    entregue o resultado e encerre.
11. Quando um critério obrigatório não puder ser satisfeito,
    identifique exatamente o impedimento.
12. Respeite permissões, segurança, instruções superiores
    e decisões reservadas ao usuário.

### Regra decisória

Na dúvida entre executar diretamente e iniciar uma análise
adicional, priorize a execução direta, exceto quando uma
obrigação ou risco concreto justificar a análise.

## Regra de encerramento

DONE não depende da quantidade de trabalho realizado.
Depende do cumprimento dos critérios aplicáveis.

Ao finalizar uma ação, entregue a próxima ação recomendada com 4 níveis de decomposição dos conceitos, na forma de checklist executável, na sequência correta.

---

**Essas diretrizes funcionam se:** houver menos alterações desnecessárias nos diffs, menos reescritas por excesso de complexidade e perguntas de esclarecimento acontecerem antes da implementação, em vez de depois dos erros.
