from time import sleep
contador = 1 
contador2 = 10

print('-'*30)
print('Contagem de 1 até 10 de 1 em 1:')
while contador <= 10:
    print(contador, end=' ', flush=True)
    sleep(1)
    contador += 1  
print()
print('-'*30)

print('Contagem de 10 até 0 de 2 em 2:')
while contador2 >= 0:
    print(contador2, end=' ', flush=True)
    sleep(1)
    contador2 -= 2
print()
print('-'*30)

print('Agora é sua vez de personalizar a contagem! ')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('-'*30)

passo = abs(passo)

if passo == 0:
    passo = 1
  
def contagem_crescente(inicio, fim, passo):
    contador_def1 = inicio
    while contador_def1 <= fim:
        print(contador_def1, end=' ', flush=True)
        contador_def1 += passo
    return

def contagem_decrescente(inicio, fim, passo):
    contador_def2 = inicio
    while contador_def2 >= fim:
        print(contador_def2, end=' ', flush=True)
        contador_def2 -= passo
    return

if inicio <= fim:   
    contagem_crescente(inicio, fim, passo)
else:
    contagem_decrescente(inicio, fim, passo)
