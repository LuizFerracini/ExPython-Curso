listaN = []

for x in range(0, 5):
    n = int(input("Digite um número: "))
    if x == 0 or n > listaN[-1]:
        listaN.append(n)
    else:
        pos = 0
        while pos < len(listaN):
            if n <= listaN[pos]:
                listaN.insert(pos, n)
                break
            pos += 1

print(listaN)
