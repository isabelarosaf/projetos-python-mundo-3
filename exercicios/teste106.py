# exercicio para demonstração da aula dicionarios 

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())

for estad in brasil:
    #print(estad)
# resultado: 
#{'uf': 'rio', 'sigla': 'rj'}
#{'uf': 'sampa', 'sigla': 'sp'}
#{'uf': 'acre', 'sigla': 'ac'}
                                   # esse for debaixo esta dentro do for de cima\/    
    for key, val in estad.items(): # < aqui eu coloquei key e val pra ajuda a lembra
        print(f'O campo {key} tem valor {val}')#   que eu estou me referindo a KEYS 
# resultado:                                # e values, mas no original ele usa apns
#O campo uf tem valor sampa          for k, v in e.items
#O campo sigla tem valor sp
#O campo uf tem valor rio
#O campo sigla tem valor rj
#O campo uf tem valor acre
#O campo sigla tem valor ac

# EM VEZ DE USAR O         FOR KEY, VAL IN ESTAD.ITEMS():      DA PRA FAZER ASSIM \/
    for val in estad.values():
        print(val)
# resultado:
# RIO
# RJ
# SAMPA 
# SP 
# BAHIA
# BH 
#############################################################

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
#  resultado:
# AcreAC
#AmazonasAC
#ParáPA