dados = list()
galera = list()
resposta = 'S'
peso_maior = peso_menor = total_pessoas =  0
pesos_menores = []
pesos_maiores = []

while True:
    dados.append(str(input('Nome: ')))
    total_pessoas +=1
    dados.append(int(input('Peso: ')))

    galera.append(dados[:])
    dados.clear()

    pergunta = str(input('Gostaria de continuar? [S/N] ')).upper().strip()
    if pergunta != 'S':
        break

peso_maior = galera[0]
peso_menor = galera[0]
pesos_maiores.append(peso_maior)
pesos_menores.append(peso_menor)


for c in galera:
    if c[1] > peso_maior[1]:
        peso_maior = c
        pesos_maiores = [c]

    elif c[1] == peso_maior[1]:
        pesos_maiores.append(c)

    if c[1] < peso_menor[1]:
        peso_menor = c
        pesos_menores = [c]
    
    elif c[1] == peso_menor[1]:
        pesos_menores.append(c)

print(f'Ao todo, você cadastrou {total_pessoas} pessoas.')
print(f'O maior peso foi de {peso_maior[1]}kg, pertencente(a) a(s) {", ".join([p[0] for p in pesos_maiores])}.')
print(f'O menor peso foi de {peso_menor[1]}kg, pertencente(a) a(s) {", ".join([p[0] for p in pesos_menores])}.')
