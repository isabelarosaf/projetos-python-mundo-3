from time import sleep
import random

jogos = int(input('Quantos jogos você quer que eu sorteie? '))

for j in range(jogos):
    numeros = random.sample(range(60), 6)
    numeros.sort()
    sleep(1)
    print(f'Jogo {j+1}: {numeros}')