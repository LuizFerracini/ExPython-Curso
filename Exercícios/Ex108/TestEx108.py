import Moeda

preco = float(input("Digite o preço: "))
taxa = float(input("Digite a taxa: "))

print(f"A metade de {Moeda.moeda(preco)} é {Moeda.moeda(Moeda.metade(preco))}")
print(f"O dobro de {Moeda.moeda(preco)} é {Moeda.moeda(Moeda.dobro(preco))}")

while True:
    opt = str(input("Aumento ou desconto?: [A/D] "))
    if opt in "Aa":
        print(f"Aumentando {Moeda.moeda(preco)} em {taxa}% temos {Moeda.moeda(Moeda.aumentar(preco, taxa))}")
        break
    elif opt in "Dd":
        print(f"Diminuindo {Moeda.moeda(preco)} em {taxa} temos {Moeda.moeda(Moeda.diminuir(preco, taxa))}")
        break
    else:
        print(f"OPÇÃO INVÁLIDA, TENTE NOVAMENTE!", end=' ')
print("-="*20)
print("Volte sempre!")
print("-="*20)
