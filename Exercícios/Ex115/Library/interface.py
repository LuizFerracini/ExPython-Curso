def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO! Tente digitar um número inteiro!\033[m')
            continue
        else:
            return n


def line(comp=55):
    return '-' * comp


def titulo(msg):
    print(line())
    print(f'{msg:^50}')
    print(line())


def menu(list):
    titulo('MENU INICIAL')
    for pos, i in enumerate(list):
        print(f'\033[0;32m{pos + 1}\033[m - \033[m{i}\033[m')
    print(line())
    opt = leiaInt('Digite sua opção: ')
    return opt
