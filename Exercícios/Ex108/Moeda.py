def dobro(num):
    res = num * 2
    return res


def metade(num):
    res = num / 2
    return res


def aumentar(num, tax):
    res = num * ((100 + tax) / 100)
    return res


def diminuir(num, tax):
    res = num * ((100 - tax) / 100)
    return res


def moeda(num, currency='R$'):
    return f'{currency}{num:.2f}'.replace('.', ',')
