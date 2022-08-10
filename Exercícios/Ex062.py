ptermo = int(input("Digite o primeiro termo da progressão: "))
razao = int(input("Digite a razão da progressão: "))
cont = 1
termo = ptermo
num = 10
soma = 0
while num != 0:
    soma = soma + num
    while cont <= soma:
        print("{} --> ".format(termo), end="")
        termo = termo + razao
        cont += 1
    print("PAUSA")
    num = int(input("Deseja ver mais quantos números? "))
print("FIM, ao todo foram mostrados {} números.".format(soma))
