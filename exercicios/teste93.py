#   BIBLIOTECA PARA INSERIR NA LISTA JA DE FORMA ORDENADA 
import bisect
numbers = []

for i in range(5):
    n = int(input('Type a number: '))
    bisect.insort(numbers, n)
    print(f'Number {n} included in position {numbers.index(n)}')
print(f'Numbers typed: {numbers}')
