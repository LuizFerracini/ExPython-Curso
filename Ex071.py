print("=-"*5, "Banco CEV", "-="*5)
valor = float(input("Digite o valor que deseja sacar: R$"))
ced = 50
total = valor
totalNotas = 0

while True:
    if total >= ced:
        total -= ced
        totalNotas += 1
    else:
        if totalNotas > 0:
            print(f"Total de {totalNotas} cédulas de R${ced}.")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalNotas = 0
        if total == 0:
            break

print("-="*20)
print("Encerrando, volte sempre!")



