ano = 2022
maior = 0
menor = 0
for pessoas in range (1, 8):
    nasc = int(input('Qual o de nascimento da {}ª pessoa? '.format(pessoas)))
    idade = ano - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print("-="*50)
print("Entre as sete pessoas, {} são maiores de idade e {} são menores de idade em {}.".format(maior, menor, ano))
print("-="*50)
