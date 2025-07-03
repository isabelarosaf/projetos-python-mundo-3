valores = []

while True:
    usuario = int(input('Digite um valor: '))
    if usuario not in valores:
        valores.append(usuario)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado não será adicionado.')
    pergunta = str(input('Gostaria de continuar? [S/N] ')).upper().strip()
    if pergunta != 'S':
        break
valores.sort()
print(f'Você digitou os valores {valores}')