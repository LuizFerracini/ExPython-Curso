ano = int(input("Qual ano você deseja analisar? "))
print("Analisando o ano....")
if ano % 100 == 0 and ano % 400 != 0:
    print("O ano {} NÃO é BISSEXTO".format(ano))
else:
    print("O ano {} é BISSEXTO".format(ano))
