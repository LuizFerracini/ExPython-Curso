def leiaInt(num):
    validar = False
    numero = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            numero = int(n)
            validar = True
        else:
            print("Erro, digite um número inteiro válido: ")
        if validar:
            break
    return numero


n = leiaInt("Digite um número: ")
print(f"O número digitado foi o {n}.")
