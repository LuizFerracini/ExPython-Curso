import random
print("Sua opções:")
print("-="*45)
print("[0] PEDRA")
print("[1] PAPEL")
print("[2] TESOURA")
esc = int(input("Qual a sua escolha? "))
joken = [0, 1, 2]
comp = random.choice(joken)
print("-="*45)
print("JO!!\nKEN!!\nPO!!")
print("-="*45)
if comp == 0 and esc == 1:
    print("O computador jogou PEDRA\nVocê jogou PAPEL\nVOCÊ VENCEU!")
elif comp == 0 and esc == 2:
    print("O computador jogou PEDRA\nVocê jogou TESOURA\nVOCÊ PERDEU!")
elif comp == 1 and esc == 2:
    print("O computador jogou PAPEL\nVocê jogou TESOURA\nVOCÊ VENCEU!")
elif comp == 1 and esc == 0:
    print("O computador jogou PAPEL\nVocê jogou PEDRA\nVOCÊ PERDEU!")
elif comp == 2 and esc == 0:
    print("O computador jogou TESOURA\nVocê jogou PEDRA\nVOCÊ VENCEU!")
elif comp == 2 and esc == 1:
    print("O computador jogou TESOURA\nVocê jogou PAPEL\nVOCÊ PERDEU!")
elif comp == 0 == esc:
    print("O computador jogou PEDRA\nVocê jogou PAPEL\nEMPATOU!")
elif comp == 1 == esc:
    print("O computador jogou PAPEL\nVocê jogou PAPEL\nEMPATOU!")
elif comp == 2 == esc:
    print("O computador jogou TESOURA\nVocê jogou PAPEL\nEMPATOU!")
else:
    print("Opção inválida, escolha entre 0 e 2!!!!")
print("-="*45)
