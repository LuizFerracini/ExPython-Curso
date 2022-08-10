vel = float(input("Qual é a velocidade atual do carro? "))
if vel > 80:
    print("Você excedeu o limite permitido de 80Km/h\nVocê deve pagar uma multa de R${:.2f}".format((vel - 80)*7))
print("Tenha um bom dia, dirija com segurança!")
