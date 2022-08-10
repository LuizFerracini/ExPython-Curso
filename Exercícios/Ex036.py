casa = float(input("Qual o valor da casa? "))
sal = float(input("Qual o seu salário? "))
fin = int(input("Quantos anos de financeamento? "))
men = casa/(fin*12)
print("A prestação mensal para pagar uma casa de R${:.2f} em {} anos será de R${:.2f}".format(casa, fin, men))
if men > 0.3 * sal:
    print("Empréstimo negado.")
else:
    print("Empréstimo pode ser concedido.")
