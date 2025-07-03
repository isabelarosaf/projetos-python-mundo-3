from datetime import datetime

def voto(idade):
    if idade >= 18 and idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
        
    if idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
        
    else:
        print(f'Com {idade} anos: NÃO VOTA.')
        
    return 

nascimento = int(input('Em que ano você nasceu? '))
idade = datetime.now().year - nascimento

voto(idade)


# formato guanabara

#def voto(ano):
    #from datetime import date
    #atual = date.today().year
    #idade = atual - ano
    
    #if idade < 16:
        #return f' com {idade} anos: n vota'
    #elif 16 <= idade < 18 or idade > 65:
        #return f'com {idade} anos: opcional'
    #else:
        #return f'com {idade} anos: vota

#nasc = int(input('Em que ano voce nasceu? ))
#print(voto(nasc))