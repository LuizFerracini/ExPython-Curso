def ajuda(command):
    help(command)


def titulo(frase, cor=0):
    comp = len(frase)
    print(cores[cor], end=' ')
    print("-=" * (comp + 4))
    print(f'    {frase}')
    print("-=" * (comp + 4))
    print(cores[0], end=' ')


cores = ('\033[m',                # 0 sem cores
         '\033[0;30;41m',        # 1 vermelho
         '\033[0;30;42m',        # 2 verde
         '\033[0;30;43m',        # 3 amarelo
         '\033[0;30;44m',        # 4 azul
         '\033[0;30;45m',        # 5 roxo
         )

function = ' '
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 5)
    function = str(input("Digite o nome da função ou "
                         "biblioteca que deseja ajuda: "))
    if function.lower() == "fim":
        break
    else:
        ajuda(function)
titulo('VOLTE SEMPRE!', 1)
