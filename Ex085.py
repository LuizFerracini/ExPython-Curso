listaN = [[], []]

for x in range(1, 8):
    n = (int(input(f"Digite o {x}º número: ")))
    if n % 2 == 0:
        listaN[0].append(n)
    else:
        listaN[1].append(n)

listaN[0].sort()
print(f"Os números pares digitados foram {listaN[0]}.")

listaN[1].sort()
print(f"Os números ímpares digitados foram {listaN[1]}.")
