dist = float(input("Quantos kilometros foram percorridos? km"))
t = int(input("Durante quantos dias o carro foi utilizado?"))
custo = (dist * 0.15) + (t * 60)
print("O valor total do aluguel será de R${:.2f}".format(custo))
