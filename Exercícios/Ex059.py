n1 = float(input("Digite um valor: "))
n2 = float(input("Digite outro valor: "))
opt = 0
maior = 0
while opt != 5:
    print("-="*30)
    print("[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa")
    opt = int(input("Digite uma opção: "))
    if opt == 1:
        soma = n1 + n2
        print("A soma entre {} e {} vale {}".format(n1, n2, soma))
    elif opt == 2:
        mul = n1 * n2
        print("A multiplicação entre {} e {} vale {}".format(n1, n2, mul))
    elif opt == 3:
        if n2 > n1:
            maior = n2
        print("O maior é o {}".format(maior))
    elif opt == 4:
        n1 = float(input("Digite um novo valor: "))
        n2 = float(input("Digite mais um valor: "))
    elif opt == 5:
        print("-=" * 30)
        print("Finalizando o programa...")
    else:
        print("Opção inválida, tente novamente: ")
print("-="*30)
print("FIM do programa, até a próxima!")
print("-="*30)
