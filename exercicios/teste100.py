linhas = colunas = 3
pares = []
matriz = []
soma_valores = soma_terceira_coluna = 0


for l in range(linhas):
    linhas = []
    for c in range(colunas):
        valor = int(input(f'Digite um valor para a posição ({l+1}, {c+1}): '))
        if valor % 2 ==  0:
            pares.append(valor)
        linhas.append(valor)

    matriz.append(linhas)

for linhas in matriz:
    soma_terceira_coluna = soma_terceira_coluna + linhas[2]
    print(linhas)

for v in pares:
    soma_valores = soma_valores + v

maior = max(matriz[1])

print(f'A soma dos valores pares é {soma_valores}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior}')