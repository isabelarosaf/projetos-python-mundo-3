lista_completa = []

while True:
    notas_lista = []
    aluno = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2

    notas_lista.append(nota1)
    notas_lista.append(nota2)

    lista_aluno = [aluno, notas_lista, media]
    lista_completa.append(lista_aluno)

    continuar = str(input('Gostaria de continuar? [S/N] ')).upper().strip()

    if continuar != 'S':
        break

for indice, estudante in enumerate(lista_completa):
    print(f'{indice:<4}{estudante[0]:<10}{estudante[2]:>8.1f}')

while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 para interromper) : '))
    if opcao == 999:
        break
    if opcao <= len(lista_completa) -1:
        print(f'Notas de {lista_completa[opcao][0]} são {lista_completa[opcao][1]}')
        