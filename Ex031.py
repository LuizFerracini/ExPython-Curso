dist = float(input("Qual a distância da sua viagem em km? "))
if dist <= 200:
    print("O custo da passagem será de R${}".format(dist*0.5))
else:
    print("O custo da passagem será de R${}".format(dist*0.45))
