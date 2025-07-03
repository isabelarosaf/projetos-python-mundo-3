def fatorial(numero, show=True):
    for c in range(numero, 0, -1):
        if show == True:
            if c == 1:
                print(f'{c} = ', end='')
            else:
               print(f'{c} x ', end='') 
        c -= 1
        if c == 0:
            break
        numero *= c
    return numero 

print(fatorial(5, show=True))   
   
