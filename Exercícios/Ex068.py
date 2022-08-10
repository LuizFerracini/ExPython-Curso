import random
count = 0
while True:
    n = int(input("Digite um número: "))
    print("-="*30)
    esc = str(input("Escolha par ou ímpar [P/I]: "))
    comp = random.randint(0, 10)
    soma = n + comp
    if soma % 2 == 0 and esc in "Pp":
        print(f"Você jogou {n} e o computador {comp}. Total de {soma} que é PAR!")
        print("-=" * 30)
        print("Você GANHOU, vamos jogar novamente...")
        count += 1
    elif soma % 2 != 0 and esc in "Ii":
        print(f"Você jogou {n} e o computador {comp}. Total de {soma} que é ÍMPAR!")
        print("-=" * 30)
        print("Você GANHOU, vamos jogar novamente...")
        count += 1
    elif soma % 2 == 0 and esc in "Ii":
        print(f"Você jogou {n} e o computador {comp}. Total de {soma} que é PAR!")
        print("-=" * 30)
        print("Você PERDEU")
        break
    elif soma % 2 != 0 and esc in "Pp":
        print(f"Você jogou {n} e o computador {comp}. Total de {soma} que é ÍMPAR!")
        print("-=" * 30)
        print("Você PERDEU")
        break
print("-="*30)
print(f"Encerrando o jogo, você ganhou {count} vezes!")
