valores = []

for c in range (0,5):
    valores.append(int(input('Digite um número: ')))

for p, v in enumerate(valores):
    print(f'Na posição {p} você digitou o valor {v}')

menor = min(valores)
maior = max(valores)

print(f'Você digitou os valores: {valores}')

print(f'O maior valor digitado foi {maior} na(s) posição(s) {valores.index(maior)}')
print(f'O menor valor digitado foi {menor} na(s) posição(s) {valores.index(menor)}')
