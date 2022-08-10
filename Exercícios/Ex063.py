print("-="*30)
print("Sequência de Fibonacci")
print("-="*30)
termos = int(input("Quantos termos deseja mostrar? "))
t1 = 0
t2 = 1
t3 = 1
print("-="*30)
print("{} --> {} --> ".format(t1, t2), end="")
num = 3
while num <= termos:
    t3 = t2 + t1
    print("{} --> ".format(t3), end="")
    t1 = t2
    t2 = t3
    num += 1
print("FIM")
print("-="*30)
