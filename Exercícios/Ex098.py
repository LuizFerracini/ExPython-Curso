def contador(s, e, c):
    if c < 0:
        c *= -1

    if c == 0:
        c = 1

    print(f"Contagem de {s} até {e} de {c} em {c}:")

    if s > e:
        total = s
        while total >= e:
            print(f"{total}", end=' ')
            total -= c
        print("FIM!")

    else:
        total = s
        while total <= e:
            print(f"{total}", end=' ')
            total += c
        print("FIM!")


contador(1, 10, 1)
print("-=" * 20)
contador(10, 0, 2)
print("-=" * 20)
print("SUA VEZ, PERSONALIZE A SUA CONTAGEM:")
print("-=" * 20)
i = int(input("Digite o primeiro termo: "))
f = int(input("Digite o último termo: "))
p = int(input("Dgite o passo: "))
contador(i, f, p)
