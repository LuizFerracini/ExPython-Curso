n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))
n4 = int(input("Digite o último número: "))
tup = (n1, n2, n3, n4)
count = 0
print(f"Você digitou os valores {tup}")

print(f"O número 9 apareceu {tup.count(9)} vezes")

if 3 in tup:
    print(f"O número 3 apareceu na posição {tup.index(3) + 1}.")
else:
    print(f"O número 3 não foi digitado")

print(f"Os números pares digitados foram ", end="")

for x in tup:
    if x % 2 == 0:
        print(f"{x}", end=" ")
        count += 1
    if count == 0:
        print("Nenhum.")
        break
