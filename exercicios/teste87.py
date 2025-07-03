num = [2, 5, 9, 1]
num.sort() #             < sort coloca na ordem do menor para o maior
print(num)

num.sort(reverse=True) # <  coloca na ordem do maior para o menor 

len(num)#   < retorna quantos elementos tem 

num.insert(2, 0) #      < insert insere valor. Na prosição 2 eu quero inserir o 0 (2,0)

num.pop()#   < elimina valor, nesse caso vai elimir o ultimo valor pq as () estao vazias
num.pop(2)#    < aqui ele vai eliminar o elemento que está na segunda posição

num.remove(2)#    < vamo supor que na lista tem dois numeros 2, um no começo e outro no fim da lista
#          o remove vai remover apenas o primeiro que ele encontrar, NÃO TODOS 

if 4 in num:
    num.remove(4)
else:
    print('Numero n encontrado')
##########################################################################################
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final')

#  RESULTADO:
#Na posição 0 encontrei o valor 5
#Na posição 1 encontrei o valor 9
#Na posição 2 encontrei o valor 4
#Cheguei ao final

############################################################
valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final')

#      RESULTADO
#Digite um valor:1
#Digite um valor:2
#Digite um valor:3
#Digite um valor:4
#Digite um valor:5
#Na posição 0 encontrei o valor 1
#Na posição 1 encontrei o valor 2
#Na posição 2 encontrei o valor 3
#Na posição 3 encontrei o valor 4
#Na posição 4 encontrei o valor 5
#Cheguei ao final

############################################################
#              ligação e Cópia  entre listas:
a = [2, 3, 4, 7]
b = a
b[2] = 8  # < aqui estou pedindo para ele alterar apenas na lista B mas ele altera as duas
#        pois o python criou uma ligação e não cópia

#    PARA FAZER UMA CÓPIA:
a = [2, 3, 4, 7]
b = a[:]  #     Esse [:] faz ele criar uma cópia, ao invez de uma ligação possibilitando a
b[2] = 8  #        alteração apenas de uma 
