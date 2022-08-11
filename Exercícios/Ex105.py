def notas(*num, sit=False):
    boletim = dict()
    boletim['Total'] = len(num)
    boletim['Maior'] = max(num)
    boletim['Menor'] = min(num)
    boletim['Média'] = sum(num)/len(num)
    if sit:
        if boletim['Média'] >= 7:
            boletim['Situação'] = "BOA"
        elif boletim['Média'] >= 5:
            boletim['Situação'] = 'NA MÉDIA'
        elif boletim['Média'] < 5:
            boletim['Situação'] = 'RUIM'
    return boletim
