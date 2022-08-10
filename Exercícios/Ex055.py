maior = 0
menor = 0

for pessoas in range(1,6):
    peso = float(input("Qual é o peso em kg da {}ª pessoa? ".format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print("O maior peso entre as {} pessoas é {}kg e o menor é {}kg.".format(pessoas, maior, menor))
