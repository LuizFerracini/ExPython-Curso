def leiaDinheiro(msg):
    while True:
        preco = str(input(f"{msg}"))
        if preco.isnumeric():
            return float(preco)
        else:
            print(f"\033[0;31mERRO: '{preco}' é um preço inválido!\033[m")
