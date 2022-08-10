nome = str(input("Digite seu nome completo: ")).strip()
nomeSplit = nome.split()
print("Seu primeiro nome é {}.".format(nomeSplit[0]))
print("Seu último nome é {}".format(nomeSplit[len(nomeSplit)-1]))
