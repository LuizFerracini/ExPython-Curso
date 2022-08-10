def area(comp, larg):
    a = comp * larg
    print(f"A área de um terreno {comp}x{larg} é {a}m²")


print("Cálculadora de ÁREA DE TERRENOS")
print('-='*20)
c = float(input("Digite o comprimento do terreno (m) : "))
l = float(input("Digite a largura do terreno (m) : "))
area(c, l)
print('-='*20)
print("FINALIZANDO... VOLTE SEMPRE!")
