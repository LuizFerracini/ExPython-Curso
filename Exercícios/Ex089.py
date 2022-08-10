listaT = []
listaP = []
med = 0

while True:
    listaT.append(str(input("Nome: ")))
    listaT.append(float(input("Nota P1: ")))
    listaT.append(float(input("Nota P2: ")))
    med = (listaT[1] + listaT[2]) / 2
    listaT.append(med)
    listaP.append(listaT[:])
    listaT.clear()
    cont = str(input("Deseja continuar? [S/N] "))
    if cont in "Nn":
        break

print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print("-="*26)

for pos, al in enumerate(listaP):
        print(f"{pos:<4}  {al[0]:<10} {al[3]:>8.1f}")

while True:
    print("-="*15)
    notasInd = int(input("Mostrar notas de qual aluno? (999 para interromper): "))
    for pos, al in enumerate(listaP):
        if notasInd == pos:
            print(f"Notas de {al[0]} são [{al[1]}, {al[2]}]")
    if notasInd == 999:
        break

print("-="*15)
print("Até mais, volte sempre!")
