listaT = []
listaP = []
maior = menor = 0

while True:
    listaT.append(str(input("Nome: ")))
    listaT.append(float(input("Peso: ")))
    if len(listaP) == 0:
        maior = menor = listaT[1]
    else:
        if listaT[1] > maior:
            maior = listaT[1]
        if listaT[1] < menor:
            menor = listaT[1]
    listaP.append(listaT[:])
    listaT.clear()
    cont = str(input("Deseja continuar? [S/N] "))
    if cont in "Nn":
        break

print(f"Ao todo foram cadastradas {len(listaP)} pessoas.")

print(f"O maior peso foi de {maior}kg, de...", end=" ")
for pessoas in listaP:
    if pessoas[1] == maior:
        print(f"[{pessoas[0]}]", end=" ")
print()

print(f"O menor peso foi de {menor}kg, de...", end=" ")
for pessoas in listaP:
    if pessoas[1] == menor:
        print(f"[{pessoas[0]}]", end=" ")
print()
