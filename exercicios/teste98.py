numeros = []
valores_pares = []
valores_impar = []

for c in range(1,7+1):
    numeros.append(int(input(f'Digite o {c}o número: ')))
for num in numeros:
    if num % 2 == 0:
         valores_pares.append(num)
    else:
        valores_impar.append(num)
    
valores_pares.sort()
valores_impar.sort()

print(f'Os valores pares digitados foram: {valores_pares}')
print(f'Os valores ímpares digitados foram: {valores_impar}')