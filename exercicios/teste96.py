# EXEMPLO DE EXERCICIO SOBRE A AULA

galera = list()
dado = list() # < estrutura auxiliar que serve para pegar os dados para depois ir para estrutura galera
total_maior = total_menor = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))

    dado.append(int(input('Idade: ')))

    galera.append(dado[:])
    dado.clear()# aqu apaga os dados apenas nessa lista pq so a usamos como auxiliar nesse caso

for p in galera:
    
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        total_maior += 1 
    else:
        print(f'{p[0]} é menor de idade.')
        total_menor += 1

print(f'Temos {total_maior} maiores e {total_menor} menores de idade.')