num = int(input("Digite um número para saber o seu fatorial: "))
x = num
fat = 1
while x > 0:
    fat*= x
    x -= 1
print("O fatorial de {} é {}".format(num, fat))
