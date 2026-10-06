import re 




# conversor md para HTML


#primeiro titulos. Cada # representa um titulo. # -> <h1> ## -> <h2> etc

stringinicial = input("\n")
stringinicial = stringinicial.replace("\\n", "\n") #serve para passar o \n para realmente
#quebrar a linha para me permitir fazer as listas numeradas
def converte_cabecalho(stringinicial):
    count =0
    match = re.match("#", stringinicial)
    while (match):
        count+=1
        stringinicial[1:]
        stringinicial = stringinicial[1:]
        match = re.match("#", stringinicial)
    if count >= 1:
         return f"<h{count}>{stringinicial.lstrip()}</h{count}>"
        # O .lstrip() remove os espaços em branco do início de uma string.
    return stringinicial
#converter italico com um * antes até aparecer outro depois. 
# atenção ao italico que é * dfsd * e o negrito é ** jfsdf **
    
def converte_negrito(stringinicial):
    return re.sub(
        r"\*\*([^*]+)\*\*",
        r"<b>\1</b>", #o /1 é o primeiro gruppo capturad ex grupo 0 *luis* g1 luis
        stringinicial
    )


def converte_italico(stringinicial):
    return re.sub(
        r"(?<!\*)\*(?!\*)([^*]+)\*(?!\*)",
        r"<i>\1</i>",
        stringinicial
    )


def listas_numeradas(stringinicial):
    linhas = stringinicial.splitlines()
    resultado = []
    dentro_lista = False

    for linha in linhas:
        match = re.match(r"\s*\d+\.\s+(.+)", linha)
        if match:
            if not dentro_lista:
                resultado.append("<ol>")
                dentro_lista = True
            resultado.append(f"<li>{match.group(1)}</li>")
        else:
            if dentro_lista:
                resultado.append("</ol>")
                dentro_lista = False
            # Preserva o texto que não pertence a uma lista numerada.
            resultado.append(linha)

    if dentro_lista:
        resultado.append("</ol>")
    return "\n".join(resultado)

def converte_url (stringinicial):

    link_pattern = r"\[([^]]+)\]\(([^)]+)\)"
    return re.sub(link_pattern, r'<a href="\2">\1</a>', stringinicial)
    #re.sub substitui apenas a parte correspondente ao padrao o resto mantem se


def converte_imagem (stringinicial):
    image_pattern = r"!\[([^]]+)\]\(([^)]+)\)"
    return re.sub (image_pattern, r'<img src="\2" alt="\1"/>',stringinicial)



    




stringinicial = converte_negrito(stringinicial)
stringinicial = converte_italico(stringinicial)
stringinicial = converte_cabecalho(stringinicial)
stringinicial=listas_numeradas(stringinicial)
stringinicial= converte_imagem(stringinicial) #precisa de estar antes de url
stringinicial= converte_url(stringinicial)

print(stringinicial)


