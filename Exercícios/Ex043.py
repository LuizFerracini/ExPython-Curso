peso = float(input("Qual o seu peso em kg? "))
alt = float(input("Qual a sua altura em m? "))
imc = peso/(alt*alt)
if imc < 18.5:
    print("Seu imc é {:.2f} e vc está abaixo do peso.".format(imc))
elif 18.5 <= imc < 25:
    print("Seu imc é {:.2f} e você está com o peso ideal.".format(imc))
elif 25 <= imc < 30:
    print("Seu imc é {:.2f} e você está com sobrepeso.".format(imc))
elif 30 <= imc < 40:
    print("Seu imc é {:.2f} e você está com obesidade.".format(imc))
else:
    print("Seu imc é {:.2f} e você está com obesidade mórbida.".format(imc))
