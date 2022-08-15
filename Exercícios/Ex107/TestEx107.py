import Moeda

preco = float(input("Digite o preço: "))
taxa = float(input("Digite a taxa: "))

print(f"A metade de R${preco} é R${Moeda.metade(preco)}")
print(f"O dobro de R${preco} é R${Moeda.dobro(preco)}")

while True:
    opt = str(input("Aumento ou desconto?: [A/D] "))
    if opt in "Aa":
        print(f"Aumentando R${preco} em {taxa}% temos R${Moeda.aumentar(preco, taxa)}")
        break
    elif opt in "Dd":
        print(f"Diminuindo R${preco} em {taxa} temos R${Moeda.diminuir(preco, taxa)}")
        break
    else:
        print(f"OPÇÃO INVÁLIDA, TENTE NOVAMENTE!", end=' ')
print("-="*20)
print("Volte sempre!")
print("-="*20)
