def fatorial(num, show=False):
    """
    --> Calcula o Fatorial de um número.
    param num: número que deseja saber o fatorial.
    param show: True ou False para exibir ou não a conta.
    return: Valor fatorial do numero num.
    """
    fat = 1
    for x in range(num, 0, -1):
        if show:
            print(f'{x}', end=" ")
            if x > 1:
                print(' x ', end=" ")
            else:
                print(' = ', end=' ')
        fat *= x
    return fat


print(fatorial(5, show=True))
help(fatorial)
