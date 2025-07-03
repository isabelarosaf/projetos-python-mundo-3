
def leiaint(pergunta):
    global n 
    n = input(pergunta)
    valido = n.isdigit()
    if valido == False:
        print('Erro! Digite um número inteiro.')
        leiaint(pergunta)
    return n 

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
