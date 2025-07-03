def notas(*num, sit=True):
    soma_media = 0
    sistema = dict()
    sistema['maior'] = max(num)
    sistema['menor'] = min(num)
    sistema['tamanho'] = len(num)

    for v in num:
        soma_media = soma_media + v
    sistema['media'] = soma_media / sistema['tamanho']
    # para media dava pra fazer tb:
    # sistema['media'] = sum(num)/len(num)

    if sit == True:
        if sistema['media'] >= 7:
            sistema['situação'] = 'boa'
        elif sistema['media'] >= 5:
            sistema['Situação'] = 'razoável'
        else:
            sistema['Situação'] = 'ruim'
    print(sistema)


resp = notas(2.5, 9.5, 7, 4.5, sit=True)
 