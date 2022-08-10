ptermo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão dessa PA: "))
print("-="*40)
for x in range(ptermo, ptermo+(razao*10), razao):
    print(x, end=" --> ")
print("FIM!")
print("-="*40)
