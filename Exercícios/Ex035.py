seg1 = float(input("Qual a medida do primeiro segmento? "))
seg2 = float(input("Qual a medida do segundo segmento? "))
seg3 = float(input("Qual a medida do terceiro segmento? "))
if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    print("Os segmentos PODEM formar um triângulo")
else:
    print("Os segmentos NÃO PODEM formar um triângulo")
