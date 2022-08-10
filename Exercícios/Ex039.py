nasc = int(input("Qual o ano do seu nascimento? "))
ano = 2022
print("-="*30)
print("Analisando dados de alistamento...")
print("-="*30)
print("Quem nasceu em {} tem {} anos em {}.".format(nasc, ano - nasc, ano))
if ano - nasc == 18:
    print("Está no ano exato de você se alistar!")
elif ano - nasc <18:
    print("Ainda faltam {} anos para seu alistamento, que deverá occorer em {}.".format(18 - (ano-nasc), nasc + 18))
else:
    print("Você já deveria ter se alistado há {} anos, em {}.".format((ano - nasc) - 18, nasc + 18))
print("-="*30)
