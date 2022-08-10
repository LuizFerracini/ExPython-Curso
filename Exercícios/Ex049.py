num = int(input("Digite um número para ver a sua tabuada: "))
print("-="*20)
print("A tabuada de {} é:".format(num))
print("-="*20)
for x in range(1, 11):
    print("{} x {} = {}".format(num, x, num*x))
print("-="*20)
