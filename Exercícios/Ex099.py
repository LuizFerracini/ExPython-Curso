def maior(* num):
    maior = total = 0
    print("Analisando os valores...")

    for n in num:
        print(f"{n}", end=" ")
        if total == 1:
            maior = n
        else:
            if n > maior:
                maior = n
        total += 1

    print(f"Foram informados {total} números.")
    print(f"O maior valor informado é {maior}.")


maior(2, 9, 4, 5, 7, 1)
print("-="*20)

maior(4, 7, 0)
print("-="*20)

maior(1, 2)
print("-="*20)

maior(6)
print("-="*20)

maior()
