countHomem = maior = mulherMenos = 0

while True:
    print("CADESTRE UMA PESSOA")
    print("-="*25)
    idade = int(input("Digite a sua idade: "))
    sex = str(input("Digite o seu sexo [M/F] "))
    print("-=" * 25)
    cont = str(input("Deseja continuar? [S/N]"))
    print("-=" * 25)
    if idade > 18:
        maior += 1
    if sex in "mM":
        countHomem += 1
    if sex in "Ff" and idade < 20:
        mulherMenos += 1
    if cont in "Nn":
        break

print(f"O total de pessoas com mais de 18 anos é {maior}.\nO total de homens cadastrados é {countHomem}."
      f"\nO total de mulheres com menos de 20 anos é {mulherMenos}!\nPrograma ENCERRADO, volte sempre!")
