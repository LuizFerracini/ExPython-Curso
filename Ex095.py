jogador = {}
listaGols = []
listaJogadores = []
perg = "s"

while perg in "sS":
    listaGols.clear()
    jogador.clear()
    jogador["Nome"] = str(input("Nome do jogador: "))
    partidas = int(input("Quantidade de partidas: "))
    for jogos in range(1, partidas + 1):
        gol = int(input(f"Quantos gols na partida {jogos}?"))
        listaGols.append(gol)
    jogador["Gols"] = listaGols[:]
    jogador["Total"] = sum(listaGols)
    listaJogadores.append(jogador.copy())
    perg = str(input("Quer continuar? [S/N] "))

print("-="*30)
print('cod ', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
print("-=" * 30)

for pos, p in enumerate(listaJogadores):
    print(f"{pos:>3}", end=" ")
    for x in p.values():
        print(f"{str(x):<15}", end=" ")
    print()

while True:
    dados = int(input("Deseja mostrar os números individuais de qual jogador?"
                      " (999 para parar) "))
    if dados == 999:
        break
    if dados >= len(listaJogadores):
        print(f"ERRO, Não existe jogador com o código {dados}")
    else:
        print(f"LEVANTAMENTO DO JOGADOR {listaJogadores[dados]['Nome']}: ")
        for match, g in enumerate(listaJogadores[dados]['Gols']):
            print(f'        Na {match + 1}ª partida fez {g} gols')
    print("-="*30)
print("Volte sempre!!")
