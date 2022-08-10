frase = str(input("Digite uma frase para saber se é um palíndromo: ")).strip().upper()
palavras = frase.split()
juntar = "".join(palavras)
invertido = ""
for letra in range (len(juntar) - 1, -1, -1):
    invertido += juntar[letra]
if invertido == juntar:
    print("A frase {} invertida é {} e ela É um palíndromo".format(frase, invertido))
else:
    print("A frase {} invertida é {} e NÃO É um palíndromo".format(frase, invertido))
