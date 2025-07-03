def ajuda(comando):
    help(comando)

while True:
    pergunta = str(input('Função ou biblioteca > '))

    if pergunta.lower() == 'fim':
        print('Até logo.')
        break

    ajuda(pergunta)