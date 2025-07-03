#     interactive help

#>  help() é uma função interna
#é usado no console do python
#ele serve para explicar qualquer comando. O help é um manual de tudo.
#outra maneira de fazer é sem precisar usar o console e sim escreever aq msm.
#ex :  help(print) < será retornado o manual do print 
#outa maneira(n tao usada)
#ex:  print(print__doc__) < será retornado a informação sobre a função 



#    docstring 

#string de documentação 
#explicação de uma função criada por alguem, ex abaixo \/

def contador(i, f, p):
    c = i 
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('fim')

contador(2, 10, 2)

# esse codigo foi feito por alguem, e a pessoa pode deixar salvo observações
# para ajudar quem vai usar 
# para receber o manual é só usar: help(contador)
# para criar é necessario usar 3vezes aspas duplas, ex\/
def contador(i, f, p):
    """
     faz uma contagem e mostra na tela
    :param i:inicio da contagem
    :param f:fim da contagem
    :parar p:passo da contagem
    :return:sem retorno
    """
    c = i 
    
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('fim')

contador(2, 10, 2)


#     parametros opcionais

def somar (a, b, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 4)#  < o codigo quebraria aqui pq só é enviado 2 parametros enquanto a função
#    recebe especificamente 3 
#  para evitar a quebra, é usado parametro opcional; por isso o c = 0
# te permiti enviar parametro ou nao, assim o codigo nao quebra ao ser enviado apns 2
# TDS OS 3 PODEM SER COLOCADOS COMO OPCIONAIS 
somar(c=3, a=2)# < deu numeros especificos para cada parametro e nenhum para o B
# mesmo assim da certo
somar() #  < da certo tb( se todas estiverem como opcional )


#      escopo de variaveis 


#  escopo global: tudo que está dentro e fora da função
#  escopo local: o que está apenas dentro da função 

def teste():
    x = 8 
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

n = 2
print(f'No programa principal, n vale {n}')
#print(f'No programa principal, x vale {x}')

# esse ultimo print quebra o codigo pq o valor de X só é existente no escopo local
# ja a varivel N funciona em ambos escopos,

#>>>>>>>> PRINT IMPORTANTE NO NOTION <<<<<<<
# situação dos 2 primeiros prints:
def teste(b):
    b += 4

a = 5
teste(a)
#  /\ nessa situação o b vale 9 pq ele pega o valor do B que esta no escopo global
#  e adiciona mais o valor que ele recebe no escopo local
#  a = 5 e dps teste toma como parametro o A
# dentro da def ja existe um valor para B, que seria 4, logo, eles sao somados
#   A continua valendo 5

def funçao():
    n1 = 4
    print(f'n1 dentro vale{n1}')

n1 = 2
funçao()
print(f'n1 fora vale {n1}')
# resultado:
#  n1 dentro vale 4
#  n1 fora vale 2

# n1 local nao afeta o de fora


def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A dentro vale {a}')

#  usando o GLOBAL, ele passa a considerar o valor de A apenas o que está declarado
#  no escopo global, ou seja, mesmo que no valor local A vale 8, ele passa a ter
#  um unico valor que é o cinco por causa da FUNÇAO GLOBAL 
# ( b vale 9 e c vale 2)



#       retorno de valores 

def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(2, 2)
somar(6)
# resultado:
# a soma vale 10
# a soma vale 4
# a soma vale 6

#   e se eu quiser mostrar ' a soma vale 10, 4 e 6' ?
# para funcionar:
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

resp1 = somar(3, 2, 5)
resp2 = somar(2, 2)
resp3 = somar(6)
print(f'A soma vale {resp1}, {resp2} e {resp3}')

#       OU 
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

print(somar(3, 2, 5))
