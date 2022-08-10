nome = str(input("Qual o nome do aluno? "))
med = float(input("Qual a média do aluno? "))

sit = "APROVADO"
if med < 7:
    sit = "REPROVADO"

dic = {"Nome": nome, "Média": med, "Situação": sit}

for k, v in dic.items():
    print(f"{k} do(a) aluno(a) é {v}.")
