count = 0
soma = 0
for x in range(1, 7):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        count += 1
        soma += n
print("-="*25)
print("A soma dos {} números pares que você digitou é {}.".format(count, soma))
print("-="*25)
