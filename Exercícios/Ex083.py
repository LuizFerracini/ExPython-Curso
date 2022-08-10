listaE = []
exp = str(input("Digite uma expressão: "))

for x in exp:
    if x in "(":
        listaE.append(x)
    elif x in ")":
        if len(listaE) > 0:
            listaE.pop()
        else:
            listaE.append(x)
            break

if len(listaE) == 0:
    print("A expressão está correta!")
else:
    print("A expressão está errada!")
