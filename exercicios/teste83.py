import random

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_aleatorios = [random.choice(numeros) for _ in range(5)]


tupla_aleatoria = tuple(numeros_aleatorios)

print(tupla_aleatoria)
print(min(tupla_aleatoria))
print(max(tupla_aleatoria))


#                                    OU


from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram:', end='')
for n in numeros:
    print (f'{n}', end='')
print(f'O maior valor sorteado foi: {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)}')