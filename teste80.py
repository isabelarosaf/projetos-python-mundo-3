lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

print(lanche[-2]) # < conta de trás para frente e nesse contexto nao existe posição zero

print(lanche[1:3]) # <  aqui vai mostrar suco e pizza mas não o elemento da ultima posição (3)

print(lanche[2:]) #  < aqui vai mostrar do elemento dois até o final 

print(lanche[:2])#    < do inicio ate o elemento dois, ignorando o elemento dois 

print(lanche[-2:])# < começa contando do final mas vai ate o fim no contexto normal 
# vai ficar: pizza, pudim 



for comida in lanche:
    print('Eu vou comer {comida}')  # < vai ser printado todos os elemntos mas um por linha 
print('Eu comi pra caramba')#                  até ter printado todos os itens 


for contador in range (0, len(lanche)):
    print(lanche(contador))  #  < se printar apenas o contador, ele vai tornar os elementos 
#    em numeros, mas colocando o lanche ele mostra os elementos
#   o len serviu para ler o comprimento e enumerar  - por isso tb colocou contador ao inves de comida
#  nao que seja uma regra usar o contadoe para enumerar
# USANDO O LEN DA PRA MOSTRAR AS POSIÇÕES DOS ELEMENTOS (EX: SUCO NA POSIÇÃO 1)
    print(f'Eu vou comer{lanche[contador]} na posição {contador}')

# para mostrar a posição no IN:
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')#  < aqui ele enumera as posições dos elementos



print (sorted(lanche)) # < printa em ordem ( se eu entendi, é ordem alfabetica) e o print aparece em 
# [], que é um modelo listta 

#TUPLA EM NUMEROS:

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
#   aqui o print cola as duas tuplas, result: (2, 5, 4, 5, 8, 1, 2) 
#  a ordem da soma tem total influencia, se for b + a se torna:  (5, 8, 1, 2, 2, 5, 4)

print(len(c))# < aqui vai ler o tamanho do c, result: 7
print(c.count(5))#  < quantas vezes o elemento 5 apareceu na tupla C, result: 2

c = b + a
print(c.index(8))#  < o index mostra a posição do 8, result: 1 
print(c.index(5))# < aqui ele mostra a primeira posição em que o cinco aparece, que seria 0
# mas eu quero ver alem dessa posição:
print(c.index(5, 1))#   o 1 foi colocado para ele procurar mais algum 5 depois da posição 1 
# dos elementos. O resultado será 5, que a outra posição em que novamente aparece um 5

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa) #  < aqui vai printar todas as info da tupla, mesmo tendo int,float e str em um só lugar
del(pessoa)# < é uma ordem de apagar a varialve pessoa da memoria 

# UMA TUPLA É IMUTAVEL OU APAGADA POR INTEIRO.