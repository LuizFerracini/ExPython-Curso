seg1 = float(input("Digite o valor do primeiro segmento: "))
seg2 = float(input("Digite o valor do segundo segmento: "))
seg3 = float(input("Digite o valor do terceiro segmento: "))
if seg1 + seg2 > seg3 and seg2 + seg3 > seg1 and seg1 + seg3 > seg2:
    print("Os segmentos podem formar um triângulo ", end="")
    if seg1 != seg2 !=seg3:
        print("ESCALENO.")
    elif seg1 == seg2 == seg3:
         print("EQUILÁTERO.")
    elif seg2 == seg3 != seg1 or seg3 == seg1 != seg2 or seg1 == seg2 !=seg3:
         print("ISÓSCELES.")
else:
    print("Os segmentos não formam um triângulo.")
