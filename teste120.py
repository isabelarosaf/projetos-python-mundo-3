from random import randint
from time import sleep

def sorteio():
    valores_sorteados = [randint(1, 10), randint(1, 10), randint(1, 10),
                        randint(1, 10), randint(1, 10)]
    print(f'Sorteando 5 valores da lista: ')
    for valor in valores_sorteados:
        sleep(1)
        print(valor, end=' ', flush=True)
    print()
    divisao(valores_sorteados)
        


def divisao(numeros):
    soma_pares = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma_pares = soma_pares + numero 
    print(f'Somando os valores pares de {numeros} temos', end=' ')   
    print(soma_pares)

sorteio()
