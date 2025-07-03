from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador1':randint(0,6),
'jogador2':randint(0,6),
'jogador3':randint(0,6),
'jogador4':randint(0,6)}

ranking = list()

for k, v in jogadores.items():
    sleep(1)
    print(f'{k} tirou {v} no dado.')
print()

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
# a função itemgetter é muito útil quando você precisa acessar e manipular elementos
#  dentro de coleções, especialmente em operações de ordenação ou filtragem.

print('Ranking dos jogadores:')
print()

for i, v in enumerate(ranking):
    print(f'{i+1}o lugar: {v[0]} com {v[1]}')
    sleep(1)