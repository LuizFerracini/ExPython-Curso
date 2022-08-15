def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO! Tente digitar um número inteiro!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário interrompeu a entrada de dados!\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO! Tente digitar um número REAL!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário interrompeu a entrada de dados!\033[m')
            return 0
        else:
            return n


num = leiaInt("Digite um número inteiro: ")
numr = leiaFloat('Digite um número real: ')
print(f"O valor inteiro digitado foi {num} e o real foi {numr:.1f}.")
