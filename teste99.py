linhas = 3
colunas = 3

matriz = []
 
for l in range(linhas):
    linhas = []
    
    for c in range(colunas):
        valor = int(input(f'Digite um valor para a posição ({l+1}, {c+1}): '))
        
        linhas.append(valor)

    matriz.append(linhas)

for linhas in matriz:
    print(linhas)