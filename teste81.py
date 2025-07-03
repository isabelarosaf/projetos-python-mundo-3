from num2words import num2words

while True:
    numero = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    usuario = int(input('Digite um numero entre 0 e 20: '))
    
    if usuario not in numero:
        print('Número invalido.')
        continue
    elif usuario in numero:
        num_ptbr = num2words(usuario, lang='pt-br')
        print(f'Você digitou o número {num_ptbr}')
        break