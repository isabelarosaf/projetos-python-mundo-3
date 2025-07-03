lista_participantes = []

while True:
    nome = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    
    lista_gols = []
    soma_lista = 0

    for p in range(partidas):
        gols = int(input(f'Quantos gols na partida {p+1}? '))
        lista_gols.append(gols)

    soma_lista = sum(lista_gols)

    sistema = {'nome': nome,
            'gols':lista_gols,
            'total': soma_lista}
    lista_participantes.append(sistema.copy())
        
    pergunta = str(input('Gostaria de continuar? [S/N] ')).upper().strip()
    if pergunta == 'N':
        break

print('nome jogador  /   gols    /  total')
for indice, jogadores in enumerate(lista_participantes):
    print(f'{indice:<4}{jogadores["nome"]:<10}{str(jogadores["gols"]):<10}{jogadores["total"]:>5.1f}')

while True:
    opcao = int(input('Mostrar ddados de qual jogador? (999 para interromper) : '))
    if opcao == 999:
        break
    if opcao <= len(lista_participantes) -1:
        jogador = lista_participantes[opcao]
        print(f'Levantamento do jogador {jogador["nome"]}')
        print(f'Gols por partida: {jogador["gols"]}')
        print(f'Total de gols: {jogador["total"]}')
    else:
        print('Opção inválida, tente novamente!')