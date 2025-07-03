pergunta = 'S'
lista_numeros = []

while True:
    numero = int(input('Digite um número: '))
    usuario = str(input('Gostaria de continuar? [S/N] ')).upper().strip()

    lista_numeros.append(numero)

    if usuario != 'S':
        break

print(f'Foram digitados ao todo {len(lista_numeros)} números.')

lista_numeros.sort(reverse=True)
print(f'A lista de valores em ordem decrescente fica: {lista_numeros} ')
    
if 5 in lista_numeros:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista')