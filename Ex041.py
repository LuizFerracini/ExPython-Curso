nasc = int(input("Qual o ano do seu nascimento? "))
ano = 2022
idade = ano - nasc
if idade <= 9:
    print("Você tem {} anos e se enquadra na categoria MIRIM.".format(idade))
elif 14 >= idade:
    print("Você tem {} anos e se enquadra na categoria INFANTIL.".format(idade))
elif 19 >= idade:
    print("Você tem {} anos e se enquadra na categoria JÚNIOR.".format(idade))
elif 25 >= idade:
    print("Você tem {} anos e se enquadra na categoria SÊNIOR.".format(idade))
else:
    print("Você tem {} anos e se enquadra na categoria MASTER.".format(idade))
