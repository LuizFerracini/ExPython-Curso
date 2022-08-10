listaN = []
listaP = []
listaImp = []

while True:
    n = (int(input("Digite um número: ")))
    listaN.append(n)
    cont = str(input("Deseja continuar? [S/N] "))
    if n % 2 == 0:
        listaP.append(n)
    elif n % 2 != 0:
        listaImp.append(n)
    if cont in "Nn":
        break

print(f"A lista de números digitados é: {listaN}")
print(f"A lista de números pares é: {listaP}")
print(f"A lista de números ímpares é: {listaImp}")
