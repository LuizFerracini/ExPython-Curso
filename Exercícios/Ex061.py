ptermo = int(input("Digite o primeiro termo da progressão: "))
razao = int(input("Digite a razão da progressão: "))
cont = 1
termo = ptermo
while cont <= 10:
    print(" {} --> ".format(termo), end="")
    termo = termo + razao
    cont += 1
print("FIM")
