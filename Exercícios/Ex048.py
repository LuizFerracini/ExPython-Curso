count = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        count += x
print("A soma de todos os números múltiplos de 3 entre 1 e 500 é {}".format(count))
