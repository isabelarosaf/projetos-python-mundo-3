from time import sleep

def contador(*num):
    if num == ():
        print('-'*50)
        print('Foram informados 0 valores.')
        print('O maior valor informado foi 0')
        print('-'*50)  
    else:
        tamanho = len(num)
        maior = max(num) 
        print('-'*50)
        for valor in num:
            sleep(1)
            print(valor, end=' ', flush=True)
        print(f'Foram informador {tamanho} valores ao todo.')
        print(f'O maior valor informado foi {maior}')

contador(2, 9, 4, 5, 7, 1)
contador(4, 7, 0)
contador(1, 2)
contador(6)
contador()
