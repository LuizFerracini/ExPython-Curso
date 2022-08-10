numeros = []
maior = menor = 0

for x in range(0,5):
    numeros.append(int(input("Digite um número: ")))
    if x == 0:
        maior = menor = numeros[x]
    else:
        if numeros[x] > maior:
            maior = numeros[x]
        elif numeros[x] < menor:
            menor = numeros[x]

print(f"O maior número é o {maior} e está na posição:", end=" ")
for pos, num in enumerate(numeros):
    if num == maior:
        print(f"{pos}...", end=" ")
print()

print(f"O menor número é o {menor} e está na posição:", end=" ")
for pos, num in enumerate(numeros):
    if num == menor:
        print(f"{pos}...", end=" ")
print()
