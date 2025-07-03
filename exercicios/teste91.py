lista_numeros = []
lista_numeros_pares = []
lista_numeros_impar = []

while True:
    numeros = int(input('Digite um número: '))
    lista_numeros.append(numeros)
    
    if numeros % 2 == 0:
        lista_numeros_pares.append(numeros)
    else:
        lista_numeros_impar.append(numeros)

    usuario = str(input('Gostaria de continuar?[S/N] ')).upper().strip()

    if usuario != 'S':
        break

print(f'A lista completa é {lista_numeros}')
print(f'A lista de pares é {lista_numeros_pares}')
print(f'A lista de impares é {lista_numeros_impar}')