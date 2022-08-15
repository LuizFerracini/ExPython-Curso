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


def resumo(num, tax, desc):
    print("-="*20)
    print("\t\t\tRESUMO DO VALOR   ")
    print("-="*20)
    print(f"Preço analisado: \t\t{moeda(num)}")
    print(f"Dobro do preço: \t\t{dobro(num, True)}")
    print(f"Metade do preço: \t{metade(num, True)}")
    print(f"{tax}% de aumento: \t{aumentar(num, tax, True)}")
    print(f"{desc}% de desconto: \t{diminuir(num, desc, True)}")
    print("-=" * 20)