dados = dict()
listaGols = []

dados["Nome"] = str(input("Nome do jogador: "))
jogos = int(input(f"Quantas partidas {dados['Nome']} jogou? "))

for x in range(1, jogos + 1):
    gols = int(input(f"     Quantos gols na partida {x}? "))
    listaGols.append(gols)
dados["Gols"] = listaGols
dados["Total"] = sum(listaGols)

print("-="*25)
print(f"{dados}")
print("-="*25)

for k, v in dados.items():
    print(f"O campo {k} tem o valor {v}")
print("-="*25)

print(f"O jogador {dados['Nome']} jogou uma total de {jogos} partidas.")
for jogo, gol in enumerate(dados["Gols"]):
    print(f"       ==>   Na partida {jogo}, ele fez {gol} gols")
print(f"Totalizando {sum(listaGols)} gols.")
