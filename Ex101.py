def voto(ano):
    idade = 2022 - ano
    if idade < 16:
        return f"Com {idade} anos: Voto NEGADO!"
    elif 16 < idade <=18 or idade > 65:
        return f"Com {idade} anos: Voto OPCIONAL!"
    else:
        if idade >= 18:
            return f"Com {idade} anos: Voto OBRIGATÓRIO!"


nasc = int(input("Ano de nascimento: "))
print(voto(nasc))
