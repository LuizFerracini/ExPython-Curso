listaEsc = ("Borracha", 2.00,
            "Lápis", 1.50,
            "Caderno", 15.00,
            "Estojo", 25.00,
            "Transferidor", 4.20,
            "Compasso", 9.99,
            "Mochila", 150.99,
            "Canetas", 40.37,
            "Livro", 55.60)

for x in range(0, len(listaEsc)):
    if x % 2 == 0:
        print(f"{listaEsc[x]:.<30}", end=" ")
    else:
        print(f"R${listaEsc[x]:>.2f}")
