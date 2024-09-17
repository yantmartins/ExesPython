matriz = []
valor = 1
for lin in range(3):
    linha = []
    for col in range(3):
        linha.append(valor)
        valor +=1
    matriz.append(linha)
for linha in matriz:
    print(linha)    