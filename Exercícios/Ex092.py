cadastro = dict()
cadastro['Nome']= str(input("Nome: "))
nasc = int(input("Ano de Nascimento: "))
idade = 2022 - nasc
cadastro["Idade"] = idade
ctps = int(input("Carteira de trabalho (0 não tem): "))

if ctps == 0:
    cadastro["Ctps"] = 0
    for k, v in cadastro.items():
        print(f"{k} tem o valor {v}")
else:
    cadastro["Ctps"] = ctps
    cadastro["Contratação"] = int(input("Ano de contratação: "))
    cadastro["Salário"] = float(input("Salário: R$"))
    cadastro["Aposentadoria"] = 2022 - cadastro["Contratação"] + 35
    for k, v in cadastro.items():
        print(f"{k} tem o valor {v}")
