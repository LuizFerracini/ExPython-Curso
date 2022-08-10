from random import randint
print("Vou pensar em um número de 1 a 10, tente acertar...")
n = int(input("Tente acertar o número: "))
comp = randint(1, 11)
count = 1
while n != comp:
    count += 1
    if n < comp:
        n = int(input("Ops, você errou! Tente um número maior: "))
    if n > comp:
        n = int(input("Ops, você errou! Tente um número menor: "))
print("Parabéns, você acertou com {} tentativas.".format(count))
