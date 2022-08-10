listaN = []
cont = "S"

while cont in "S":
    n = int(input("Digite um número: "))
    print("Valor adicionado com sucesso!")
    cont = str(input("Deseja continuar? [S/N] ")).upper()
    if n not in listaN:
        listaN.append(n)
    else:
        break

print(f"Os número digitados foram: {sorted(listaN)}")
