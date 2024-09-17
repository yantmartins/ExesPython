matriz = []
linha = 0

while linha < 4:
    matriz.append([])

    coluna = 0
    while coluna < 4:
        valor = input(f"ENTRADA DE DADOS: \nLin-{linha} Col-{coluna}: ")
        matriz[linha].append(valor)
        coluna += 1

    linha += 1
print("SAÍDA DE DADOS:")
for linha in matriz:
    print(linha)            