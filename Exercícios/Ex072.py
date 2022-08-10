numExt = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze",
          "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
num = int(input("Digite um número de 0 a 20: "))

print("-="*20)

while num not in range(0, 21):
    num = int(input("Número inválido, digite novamente um número de 0 a 20: "))

print("-="*20)

if num in range(0, 21):
    for x in numExt:
        print(f"Você digitou o número {numExt[num].upper()}")
        break

print("-="*20)
print("Obrigado, volte sempre!")
print("-="*20)
