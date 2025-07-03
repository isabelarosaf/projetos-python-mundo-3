# ler ano de nasc mas salvar apns a idade no dicionario
# a pessoa deve se aposentar depois de 35 anos trabalhado
from datetime import datetime

while True: 
    nome = str(input('Nome: '))
    nascimento = int(input('Ano de nascimento: '))
    idade = datetime.now().year - nascimento

    carteira = int(input('Carteira de trabalho (0 não tem): '))

    if carteira == 0:
        print(f'nome tem valor: {nome}')
        print(f'idade tem valor: {idade}')
        break
    
    ano_contracao = int(input('Ano de contração: '))
    salario = float(input('Salário: '))

    aposentadoria = datetime.now().year - ano_contracao
    conta_aposentadoria = 35 - aposentadoria
    idade_aposentadoria = conta_aposentadoria + idade

    sistema = {'nome': nome,
            'idade': idade,
            'ctps': carteira,
            'contratação': ano_contracao,
            'salário': salario,
            'aposentadoria': idade_aposentadoria}

    print(sistema)

    for v, k in sistema.items():
        print(f'{v} tem valor {k}.')
    break

# esse exercicio nao tinha necessidade de usar while 