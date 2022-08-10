n = count = soma =  0
while True:
    n = int(input("Digite um número [999 para parar]: "))
    if n == 999:
        break
    soma += n
    count += 1
print("Foram digitados {} números e a soma deles foi {}.".format(count, soma))
