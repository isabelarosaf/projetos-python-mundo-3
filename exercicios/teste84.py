lista_pares = []
lista = []

for _ in range (1, 5):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        lista_pares.append(numero)
    lista.append(numero)  
tupla = tuple(lista)

if 3 not in tupla:
    print(f'O valor 3 não foi digitado')
else:
     print(f'O valor 3 foi digitado na posição: {(tupla.index(3)+1)}')# +1 para começar a contar a 
                                                                      # partir do 1 e nao 0     
print(f'Os valores pares digitados foram: {lista_pares}')
print(f'Você digitou os números: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
