# versao do guanabara do exercicio 97 

lista_temporaria = []
lista_principal = []
maiorpeso = menorpeso = 0

while True:
    lista_temporaria.append(str(input('nome: ')))
    lista_temporaria.append(float(input('peso: ')))

    if len(lista_principal) == 0:
        maiorpeso = menorpeso = lista_temporaria[1]
    else:
        if lista_temporaria[1] > maiorpeso:
            maiorpeso = lista_temporaria[1]
        if lista_temporaria[1] < menorpeso:
            menorpeso = lista_temporaria[1]

    lista_principal.append(lista_temporaria[:])
    lista_temporaria.clear() 

    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print(f'Os dados foram {lista_principal}')
print(f'Ao todo você cadastrou {len(lista_principal)} pessoas')

print(f'O maior peso foi de {maiorpeso}kg. Peso de ', end='')
for pessoa in lista_principal:
    if pessoa[1] == maiorpeso:
        print(f'[{pessoa[0]}] ', end='')
print() #    < esse print está assim apenas pra ele pular p linha debaixo

print(f'O menor peso foi de {menorpeso}kg. Peso de ', end='')
for pessoa in lista_principal:
    if pessoa[1] == menorpeso:
        print(f'[{pessoa[0]}] ', end='')
print()