n = 0
while True:
    n = int(input("Digite um número para ver a sua tabuada: "))
    print("-=" * 25)
    if n < 0:
        break
    for x in range (1, 11):
        print(f"{n} x {x} = {n*x}")
    print("-="*25)
print("Programa encerrado!")
print("-="*25)
