# Exercício Python 104: Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)


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
