nomeHvelho =0
idadeHvelho = 0
countMmenor = 0
sTidade = 0
midade = 0

for pessoas in range (1, 5):
    print("-="*20,"{}ª PESSOA".format(pessoas),"-="*20)
    nome = str(input("Qual o nome da {}ª pessoa? ".format(pessoas)))
    idade = int(input("Qual a idade da {}ª pessoa? ".format(pessoas)))
    sexo = str(input("Qual a sexualidade da {}ª pessoa [M/F]? ".format(pessoas)))
    print("-="*46)
    sTidade += idade
    midade = sTidade/4
    if pessoas == 1 and sexo in "Mm":
        idadeHvelho = idade
        nomeHvelho = nome
    if sexo in "Mm" and idade > idadeHvelho:
        idadeHvelho = idade
        nomeHvelho = nome
    if sexo in "Ff" and idade < 20:
        countMmenor += 1

print("A idade média do grupo foi de {:.2f} anos;\nO homem mais velho se chama {} e tem {} anos;\nTemos um total de {} mulheres com menos de 20 anos".
      format(midade, nomeHvelho, idadeHvelho, countMmenor))
