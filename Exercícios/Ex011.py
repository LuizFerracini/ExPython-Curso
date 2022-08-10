alt = float(input("A altura da parede em metros vale: "))
larg = float(input("A largura da parede em metros vale: "))
print("Sua parede tem uma dimensão de {}x{} e sua área é de {}m²".format(alt, larg, alt*larg ))
print("Para pintar essa parede você precisará de {}l de tinta".format((alt*larg)/2))
