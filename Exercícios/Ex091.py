from random import randint
from time import sleep
from operator import itemgetter

print("dado sendo jogados...")
print("-="*20)

dados = {"Jogador1": randint(1, 6),
         "Jogador2": randint(1, 6),
         "Jogador3": randint(1, 6),
         "Jogador4": randint(1, 6)}

for k, v in dados.items():
    print(f"O {k} tirou {v} no dado.")
    sleep(0.5)

ordem = sorted(dados.items(), key= itemgetter(1), reverse=True)

print("-="*20)
print("              -==- RANKING -==-")

for pos, num in enumerate(ordem):
    print(f"{pos + 1}º Lugar : {num[0]} com {num[1]} prontos")
    sleep(0.5)
