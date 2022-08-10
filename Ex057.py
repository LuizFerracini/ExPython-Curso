sexo = str(input("Informe seu sexo [M/F]: ")).upper()
while sexo not in "mMfF":
    sexo = str(input("Opção inválida, tente novamente [M/F]: ")).upper()

print("O sexo {} foi registrado com sucesso".format(sexo))
