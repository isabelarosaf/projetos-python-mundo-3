# VARIAVEIS COMPOSTAS  -- DICIONARIOS 

# dicionario pode ser identificado como:

dados = dict()
#  ou
dados = {'nome': 'Pedro', 'idade': 25} 
print(dados['nome']) 
# resultado: Pedro 

# no dicionario n precisa usar APPEND, apenas coloque o q vc quer add desta forma:
dados['sexo'] = 'M'

#para remover: 
del dados['idade']
####################################################################################

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
         }

print(filme.values()) # <  retorna os valores " star wars, 1977, george lucas"
print(filme.keys()) #  < retorna os valores " titulo, ano, diretor "
print(filme.items()) #  < retorna tudo 


for k, v in filme.items():     # K  -E-  V    É KEY  E VALUES 
    print(f'O {k} é {v}')       
# resultado:                     
# O titulo é Star Wars 
# O ano é 1977
# O diretor é George Lucas 
#################################################################################

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') 
# resultado: O gustavo tem 22 anos.

pessoas['nome'] = 'Leandro' # < alterei informação 
############################################################################

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'rj'}
estado2 = {'uf': 'São Paulo', 'sigla': 'sp'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
# resultado:
# [{'uf': 'Rio de Janeiro', 'sigla': 'rj'}, {'uf': 'São Paulo', 'sigla': 'sp'}]

print(brasil[0])
#resultado:
# {'uf': 'Rio de Janeiro', 'sigla': 'rj'}

print(brasil[1])
#resultado:
# {'uf': 'São Paulo', 'sigla': 'sp'}

print(brasil[0]['uf'])
#resultado:
# Rio de Janeiro

################################################################################

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) # .copy para add as info em uma lista
print(brasil)

###########################################################################
