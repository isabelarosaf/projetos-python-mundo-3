grupo = soma_idade = 0
lista_idade = []
lista_pessoas = []

while True:
    pessoas = dict()
    pessoas['nome'] = str(input('Nome: '))
    grupo += 1
    
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite M ou F')
        lista_pessoas.append(pessoas.copy())
    
    idade = int(input('Idade: '))
    pessoas['idade'] = idade
    lista_idade.append(idade)

    lista_pessoas.append(pessoas.copy())

    while True:
        pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()
        if pergunta in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if pergunta == 'N':
        break

print(f'O grupo tem {grupo} pessoas')

for i in lista_idade:
    soma_idade = soma_idade + i
media_idade = soma_idade / grupo 
print(f'A média de idade é de {media_idade:.2f} anos.')

print('Pessoas do sexo feminino:')
for pessoa in lista_pessoas:
    if pessoa["sexo"] == 'F':
        print(f'{pessoa["nome"]}', end=' ')
print()

print("Pessoas acima da média de idade:")
for pessoa in lista_pessoas:
    if pessoa["idade"] > media_idade: 
        print(f'{pessoa["nome"]}, {pessoa["sexo"]}, {pessoa["idade"]} anos')
