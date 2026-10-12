import re 
import sys




def tokenize(input_string):
   
    linha = 1
    mo = re.finditer(r'(?P<Comentário>#(.*))|(?P<Idvariavel>\?[a-zA-Z0-9]+)|(?P<Lingua>@[a-zA-Zá-úÁ-ÚçÇ]{2})|(?P<String>\"[^\"]*\")|(?P<Conceito>[a-zA-Z0-9]+)|(?P<Delimitador>[{}.])|(?P<Reservada>LIMIT)|(?P<ValorNumerico>\'[0-9]*\')|(?P<Erro>.)', input_string) #sem espoaços entre a |
    for m in mo:
        dic = m.groupdict()
# O caráter '#' marca o início de um comentário que se prolonga até ao fim da linha e deve ser ignorado;
        if dic['Comentário']:
            
            t = ("Comentário", dic ['Comentário'][1:],linha,m.span())

# O caráter '?' marca o início de um identificador de uma variável que se prolonga até ao primeiro
#caráter não alfanumérico;
        elif dic ['Idvariavel']:

            t = ("Idvariavel", dic ['Idvariavel'][1:],linha, m.span())

        elif dic ['Lingua'] :

            t = ("Lingua", dic ['Lingua'][1:], linha, m.span())


        elif dic ['String']:

            t= ("String", dic ['String'][1:-1], linha, m.span())


        elif dic ['Conceito']:
                if dic ['Conceito'] == 'LIMIT':

                    t=("Reservada", dic ['Conceito'], linha, m.span())
        
                else:

                    t= ("Conceito", dic ['Conceito'], linha, m.span())

        
        elif dic ['Delimitador']:

            t=("Delimitador", dic ['Delimitador'], linha, m.span())


        
        elif dic ['ValorNumerico']:

             t=("ValorNumerico", dic ['ValorNumerico'], linha, m.span())



        else:
            t = ("UNKNOWN", m.group(), linha, m.span())

        yield t #usamos yield pois return termina a funçao imediatamente. PARA USAR RETURN teria de acumular os tokens numa lista e dar return tokens
    #Yield é mais otimizado em termos de memória mas não necessariamente mais rápido
        




for linha in sys.stdin:
    for tok in tokenize(linha):
        print(tok, end= " ", flush=True)
    print()
