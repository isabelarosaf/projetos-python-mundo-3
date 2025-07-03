lista = []
soma_lista = 0

nome = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {nome} jogou? '))

for p in range(partidas):
    gols = int(input(f'Quantos gols na partida {p+1}? '))
    lista.append(gols)

for numeros in lista:
    soma_lista = soma_lista + numeros

sistema = {'nome': nome,
           'gols':lista,
           'total': soma_lista}

print(sistema)

for v, k in sistema.items():
    print(f'O campo {v} tem o valor {k}')

print(f'O jogador {nome} jogou {partidas} partidas')

for i, g in enumerate(sistema['gols']):
    print(f' Na partida {i+1}, fez {g} gols')