sal = float(input("Qual o seu salário atual: "))
if sal > 1250:
    print("O salário de quem ganhava R${:.2f} passará a ser R${:.2f}!".format(sal, sal*1.1))
else:
    print("O salário de quem ganhava R${:.2f} passará a ser R${:.2f}!".format(sal, sal*1.15))
