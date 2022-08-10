# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.


def ficha(name="*desconhecido*", goals=0):
    print(f"O jogador {name} fez {goals} gol(s) no campeonato.")


nomeJogador = str(input("Nome do jogador: "))
gols = str(input("Número de gols: "))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nomeJogador.strip() == '':
    ficha(goals=gols)
else:
    ficha(nomeJogador, gols)
