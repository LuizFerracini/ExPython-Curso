price = float(input("Qual o preço original do produto? "))
print("Selecione uma das opções de pagamento abaixo:")
print("[1]  Pagamento à vista dinheiro/cheque com 10% de desconto;")
print("[2]  Pagamento à vista no cartão com 5% de desconto;")
print("[3]  Pagamento em até 2x no cartão sem juros; ")
print("[4]  Pagamento 3x ou mais no cartão com 20% de juros.")
forma = int(input("Selecione a sua opção de 1 a 4: "))
if forma == 1:
    print("O produto que custa R${:.2f} sairá por R${:.2f} à vista no dinheiro ou cheque.".format(price, price*0.9))
elif forma == 2:
    print("O produto que custa R${:.2f} sairá por R${:.2f} à vista no cartão".format(price, price*0.95))
elif forma == 3:
    print("O produto que custa R${:.2f} sairá por 2x de R${}.".format(price, price/2))
elif forma == 4:
    print("O produto que custa R${:.2f} sairá por 3x de R${}.".format(price, (price*1.2)/3))
else:
    print("Opção inválida, tente novamente um número de 1 a 4!!")
