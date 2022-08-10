num = int(input("Digite um número qualquer: "))
print("Escolha uma das opções abaixo: ")
print("[1] Para converter em binário.")
print("[2] Para converter em octal.")
print("[3] Para converter em hexadecimal.")
opt = int(input("Digite sua opção: "))
if opt == 1:
    print("O número escolhido em binário é igual a {} ".format(bin(num)[2:]))
elif opt == 2:
    print("O número escolhido em octal é igual a {} ".format(oct(num)[2:]))
elif opt ==3:
    print("O número escolhido em hexadecimal é igual a {} ".format(hex(num)[2:]))
else:
    print("Essa opção não existe, tente novamente")
