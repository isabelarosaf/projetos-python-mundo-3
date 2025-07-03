teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
# resultado >    ['Gustavo', 40]
#############################################

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
print(galera)
# resultado >   [['Gustavo', 40]]   < uma lista dentro de outra lista 
###############################################################################

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) # < não esquecer os colchetes para evitar de criar uma ligação nas listas
teste[0] = 'Maria'      # sem os colchetes o resultado seria: [['Maria', 22], ['Maria', 22]] 
teste[1] = 22
galera.append(teste[:])
print(galera)
# resultado  >  [['Gustavo', 40], ['Maria', 22]]
###############################################################################################

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0])  # resultado   ['João', 19]
print(galera[0][0]) # resultado   João
print(galera[2][1]) # resultado   13
#########################################################################
 
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p)
# resultado 
#['João', 19]
#['Ana', 33]
#['Joaquim', 13]
#['Maria', 45]

for p in galera:
    print(p[0])
# resultado 
#João
#Ana
#Joaquim
#Maria
################################################################################

