n = int(input("Digite um número [999 para parar]: "))
soma = 0
count = 0
while n != 999:
    count += 1
    soma += n
    n = int(input("Digite um número [999 para parar]: "))
print("Foram digitados {} números e a soma deles deu {}".format(count, soma))
