m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = terCol = maior = 0

for l in range(0, 3):
    for c in range(0,3):
        m[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
        if m[l][c] % 2 == 0:
            soma += m[l][c]
        if c == 2:
            terCol += m[l][c]
        if l == 1 and c == 0:
            maior = m[1][0]
        else:
            for x in range(1, 3):
                if m[1][x] > maior:
                    maior = m[1][x]

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{m[l][c]:^5}]", end=" ")
    print()

print(f"A soma dos valores pares da matriz é {soma}.")
print(f"A soma dos números na terceira coluna é {terCol}.")
print(f"O maior número da segunda linha é {maior}.")
