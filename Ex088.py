from random import randint
from time import sleep

jogosT = []
jogosP = []
total = 0

qtd = int(input("Quantos jogos quer sortear? "))
while total < qtd:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogosT:
            jogosT.append(num)
            cont += 1
        if cont >= 6:
            break
    jogosT.sort()
    jogosP.append(jogosT[:])
    jogosT.clear()
    total += 1

print("-="*15)
for n, j in enumerate(jogosP):
    print(f"Jogo {n+1}: {j}")
    sleep(1)
print("-="*15)
