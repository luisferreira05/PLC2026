# TPC 2: Conversor de Markdown para HTML

## Autor

**Nome:** Luís Pereira Oliveira Ferreira  
**ID:** A108648

<img src="./IMG_3891.jpg" width="200">

## Resumo

Este trabalho consiste no desenvolvimento de um conversor de Markdown para HTML em Python, utilizando expressões regulares para reconhecer e transformar os elementos de formatação.

O programa suporta as seguintes conversões:

- Cabeçalhos iniciados por `#`, convertidos em etiquetas `<h1>`, `<h2>`, etc.;
- Texto em negrito, delimitado por `**`, convertido em `<b>`;
- Texto em itálico, delimitado por `*`, convertido em `<i>`;
- Listas numeradas, convertidas em `<ol>` com elementos `<li>`;
- Links no formato `[texto](URL)`, convertidos em `<a>`;
- Imagens no formato `![texto alternativo](URL)`, convertidas em `<img>`.

[Resolução](./resolucao.py)

A conversão é realizada através de funções específicas para cada elemento. As expressões regulares permitem identificar os padrões de Markdown e substituir a formatação pelas etiquetas HTML correspondentes.

Nas listas numeradas, o programa identifica os itens consecutivos e agrupa-os numa lista, preservando o texto que aparece antes e depois. As imagens são convertidas antes dos links, devido à semelhança entre os dois padrões.

O programa recebe o texto através da entrada padrão e apresenta o resultado em HTML. Para introduzir várias linhas numa única entrada, é possível utilizar a sequência literal `\n`, que é transformada numa quebra de linha.
