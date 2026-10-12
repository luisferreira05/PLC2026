# TPC 3: Analisador léxico

## Autor

**Nome:** Luís Pereira Oliveira Ferreira  
**ID:** A108648

<img src="./IMG_3891.jpg" width="200">

## Resumo

Este trabalho consiste no desenvolvimento de um analisador léxico em Python, utilizando expressões regulares para reconhecer os elementos de uma linguagem e classificá-los em tokens.

As categorias consideradas são:

- Comentários iniciados por `#`, que se prolongam até ao fim da linha;
- Identificadores de variáveis iniciados por `?`, seguidos de carateres alfanuméricos;
- Identificadores de língua iniciados por `@`;
- Strings delimitadas por aspas duplas;
- Identificadores de conceitos constituídos por sequências alfanuméricas;
- Delimitadores `{`, `}` e `.`;
- Palavra reservada `LIMIT`;
- Valores numéricos.

[Resolução](./resolucao.py)

A análise é realizada pela função `tokenize`, que utiliza `re.finditer` e grupos nomeados para identificar os padrões presentes no texto. Os tokens são representados por tuplos com a categoria, o valor, a linha e o intervalo de posições devolvido por `m.span()`.

A função utiliza `yield` para devolver os tokens ao longo da análise. O programa lê o texto através da entrada padrão e apresenta os tokens correspondentes.
