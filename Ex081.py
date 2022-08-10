count = 0
listaN = []
cont = "S"

while cont in "Ss":
    n = int(input("Digite um número: "))
    cont = str(input("Deseja continuar? [S/N] "))
    listaN.append(n)
    count += 1

listaN.sort(reverse=True)

print(f"Foram digitados {count} números."
      f"\nA lista de números digitados "
      f"na ordem decrescente é: {listaN}")

if 5 in listaN:
    print(f"O número 5 está na lista.")
else:
    print(f"O número 5 não está na lista.")
