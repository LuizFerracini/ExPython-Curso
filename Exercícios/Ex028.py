import random
print("="*30)
print("Vou pensar em um número entre 0 e 5, tente adivinhar....")
print("="*30)
num = int(input("Em que número eu pensei? "))
n = random.randint(0, 5)
if num == n:
    print("PARABÉNS, você me venceu")
else:
    print("GANHEI, pensei no número {} e não no {}".format(n, num))
print("="*30)
