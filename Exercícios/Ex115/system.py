from Exercícios.Ex115.Library.interface import *
from Exercícios.Ex115.Library.file import *

file = 'cadastros.txt'

if not fileExist(file):
    createFile(file)

while True:
    answer = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if answer == 1:
        readFile(file)
    elif answer == 2:
        titulo('NOVO CADASTRO')
        nome = str(input("Digite o nome: "))
        id = leiaInt('Digite a idade: ')
        signUp(file, nome, id)
    elif answer == 3:
        titulo('Encerrando o sistema... Volte sempre!')
        break
    else:
        titulo('\033[0;31mErro! Escolha uma opção válida!\033[m')
