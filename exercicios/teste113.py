# aula funçao

def soma(a, b):
    s = a + b
    print(s)

soma(4, 5)
soma(8, 9)
soma(2, 1)
#resultado: 
#9
#17
#3

######################################
# empacotar parametros:

def contador(*num): # a estrela significa ' desempacotar ',> posso receber varios num
    print(num)

contador(2, 1, 7)
contador(8, 0)
contador(4, 7, 6)
# resultado:
# (2, 1, 7)
# (8, 0)
# (4, 7, 6)

#############################################

def contador (*num):
    for valor in num:
        print(f'{valor}', end='')
    print('fim')

contador(2, 1, 7)
contador(8, 0)
contador(4, 7, 6)
# resultado:
# 2, 1, 7 fim
# 8, 0 fim
# 4, 7, 6 fim

#################################################

def contador (*num):
   tamanho = len(num)
   print(f'Recebi os valores {num} e sao ao todo {tamanho} numeros')

contador(2, 1, 7)
contador(8, 0)
contador(4, 7, 6)
# resultado:
# Recebi os valores (2, 1, 7) e sao ao todo 3 numeros
# Recebi os valores (8, 0) e sao ao todo 2 numeros
# Recebi os valores (4, 7, 6) e sao ao todo 3 numeros

##################################################################

