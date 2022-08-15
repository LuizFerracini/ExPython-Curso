from Exercícios.Ex115.Library.interface import *

def fileExist(name):
    try:
        o = open(name, 'rt')
        o.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createFile(name):
    try:
        o = open(name, 'wt+')
        o.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print(f'Arquivo {name} criado com sucesso!')


def readFile(name):
    try:
        o = open(name, 'rt')
    except:
        print("Erro na leitura do arquivo!")
    else:
        titulo('PESSOAS CADASTRADAS')
        for lines in o:
            registro = lines.split(';')
            registro[1] = registro[1].replace('\n', '')
            print(f'{registro[0]:<30}{registro[1]:>3} anos')
    finally:
        o.close()


def signUp(file, nome='unknown', idade=0):
    try:
        o = open(file, 'at')
    except:
        print("Erro na abertura do arquivo")
    else:
        try:
            o.write(f'{nome};{idade}\n')
        except:
            print('Erro no cadastro dos dados')
        else:
            print(f'Registro de {nome} adicionado com sucesso!')
            o.close()
