from random import randint


def sorteia(num):
    print(f"Sorteando os 5 valores da lista...", end=" ")
    for x in range(0, 5):
        x = randint(1, 10)
        num.append(x)
        print(f"{x} ", end=" ")
    print("... PRONTO!")


def somaPar(num):
    soma = 0
    for n in num:
        if n % 2 == 0:
            soma += n
    print(f"A soma dos números pares de {num} é {soma}")


numeros = list()
sorteia(numeros)
somaPar(numeros)
