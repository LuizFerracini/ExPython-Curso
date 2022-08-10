n = int(input("Digite um número: "))
cont = str(input("Deseja continuar [S/N]? "))
soma = n
med = 0
count = 1
maior = n
menor = n
while cont in 'Ss':
    n = int(input("Digite um número: "))
    cont = str(input("Deseja continuar [S/N]? "))
    soma += n
    count += 1
    med = soma/count
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
print("Você digitou {} valores\nA média entre os eles é {}\nO maior entre eles é o {} e o menor {}.".format(count, med, maior, menor))
