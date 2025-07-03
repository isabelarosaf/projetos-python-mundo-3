def ficha(nome, gol):
    print('-'*30)

    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0

    if nome.strip() == '':
        nome = '<desconhecido>'
    if nome.isnumeric():
        nome = '<desconhecido>'
        
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato')

nome = str(input('Nome do jogador: '))
gol = input('Número de gols: ')


ficha(nome, gol)