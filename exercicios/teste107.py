sistema = dict()

sistema['aluno'] = str(input('Nome: '))
sistema['media'] = float(input(f'Média de {sistema["aluno"]}: '))

print(f'O nome é {sistema["aluno"]}')

print(f'A média é {sistema["media"]}')

if sistema["media"] >= 7:
    print('Situação é igual APROVADO')
elif 5 <= sistema["media"] < 7:
    print('Situção é igual a Recuperação')
else:
    print('Situação é igual REPROVADO')
