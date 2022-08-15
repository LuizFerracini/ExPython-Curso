def dobro(num, cur=False):
    res = num * 2
    if cur:
        return moeda(res)
    else:
        return res


def metade(num, cur=False):
    res = num / 2
    if cur:
        return moeda(res)
    else:
        return res


def aumentar(num, tax, cur=False):
    res = num * ((100 + tax) / 100)
    if cur:
        return moeda(res)
    else:
        return res


def diminuir(num, tax, cur=False):
    res = num * ((100 - tax) / 100)
    if cur:
        return moeda(res)
    else:
        return res


def moeda(num, currency='R$'):
    return f'{currency}{num:.2f}'.replace('.', ',')
