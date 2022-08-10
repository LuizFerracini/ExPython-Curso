total = custoM = count = custoB = 0
maisB = ""

while True:
    prod = str(input("Digite o nome do Produto: "))
    preco = float(input("Digite o preço do Produto: "))
    cont = str(input("Deseja continuar? [S/N]: "))
    total += preco
    count += 1
    if preco > 1000:
        custoM += 1
    if count == 1 or preco < custoB:
        custoB = preco
        maisB = prod
    if cont in "Nn":
        break

print(f"Foram gastos R${total:.2f} na compra.\nO produto mais barato foi {maisB}, custando R${custoB:.2f}.\nFinalizando o programa, volte sempre!")
