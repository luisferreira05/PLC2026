# TPC 1: Expressão regular para ler strings binárias que não contêm a string `011`

## Autor

**Nome:** Luís Pereira Oliveira Ferreira  
**ID:** A108648

<img src="./IMG_3891.jpg" width="200">

## Resumo

Este trabalho consiste na definição de uma expressão regular que permite reconhecer strings binárias que não contêm a substring `011`.

A linguagem considerada é constituída por strings sobre o alfabeto `{0,1}`, sendo excluídas todas as strings que contenham `011`.

A expressão regular utilizada é:

[Resolução](./resolucao.txt)

A ideia central da expressão regular consiste em permitir uma sequência inicial arbitrária de 1s e, a partir do momento em que ocorre o primeiro 0, restringir as ocorrências seguintes de 1 ao bloco 01. Desta forma, após um 0, nunca podem surgir dois 1s consecutivos, o que garante que a substring proibida 011 não pode ocorrer.
