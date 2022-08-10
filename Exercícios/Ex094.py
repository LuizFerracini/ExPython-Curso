pessoas = {}
listaPessoas = []
perg = "S"
count = soma = 0

while perg in "Ss":
    pessoas["Nome"] = str(input("Nome: "))
    pessoas["Sexo"] = str(input("Sexo [M/F]: "))
    if pessoas["Sexo"] not in "MmFf":
        pessoas["Sexo"] = str(input("ERRO! Por favor, digite apenas M ou F: "))
    pessoas["Idade"] = int(input("Idade: "))
    soma += pessoas["Idade"]
    perg = str(input("Deseja continuar? [S/N] "))
    listaPessoas.append(pessoas.copy())
    pessoas.clear()
    count += 1
med = soma / count

print("-="*30)
print(f"Foram cadastradas {count} pessoas.")
print(f"A média de idade foi de {med:.2f} anos")

print(f"As mulheres cadastradas foram: ", end="")
for p in listaPessoas:
    if p["Sexo"] in "fF":
        print(f"{p['Nome']}", end=" ")
print()

print(f"As pessoas com idade ácima da média foram: ", end=" ")
for p in listaPessoas:
    if p["Idade"] >= med:
        print(f"\n       nome =  {p['Nome']};"
              f" sexo = {p['Sexo'].upper()};"
              f" idade = {p['Idade']} anos", end=" ")
print("\n>>PROGRAMA FINALIZADO<<")
