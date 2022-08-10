p1 = float(input("Digite sua nota da prova 1: "))
p2 = float(input("Digite sua nota da prova 2: "))
med = (p1+p2)/2
print("Calculando a sua média final...")
if med < 5:
    print("Sua média final foi {:.2f} e você foi REPROVADO.".format(med))
elif 5 <= med < 7:
    print("Sua média final foi {:.2f} e você está de RECUPERAÇÃO.".format(med))
else:
    print("Sua média final foi {:.2f} e você foi APROVADO!".format(med))
