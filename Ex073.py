brasil = ("Palmeiras", "Corinthians", "Fluminense", 	"Athletico-PR", "Flamengo", "Internacional",
          "Atlético-MG", "Bragantino", "Santos", "São Paulo", "Goiás", "Botafogo", "América-MG", "Ceará",
          "Coritiba", "Avaí", "Cuiabá", "Fortaleza", "Atlético-GO", "Juventude")

print(f"A lista de times é: {brasil}")
print("-="*25)

print(f"Os 5 primeiros colocados são: {brasil[0:5]}")
print("-="*25)

print(f"Os 4 últimos colocados são: {brasil[16:20]}")
print("-="*25)

print(f"Em ordem alfabética: {sorted(brasil)}")
print("-="*25)

print(f"O Botafogo está na {brasil.index('Botafogo') + 1}ª posição")
print("-="*25)
