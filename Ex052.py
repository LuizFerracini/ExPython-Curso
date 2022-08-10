num = int(input("Digite um número para saber se ele é um número PRIMO: "))
count = 0
for x in range(1, num+1):
    if num % x == 0:
        count += 1
print("-="*30)
if count == 2:
    print("O número {} é um número PRIMO!".format(num))
else:
    print("O número {} NÃO é um número PRIMO".format(num))
print("-="*30)
