matriz = []
i = 0
valor = 1 #INICIA EM 1 PARA PREENCHER 
while i < 3:
    linha = []
    j = 0
    while j < 3:
        linha.append(valor)
        valor += 1
        j +=1
    matriz.append(linha)
    i += 1

i = 0
while i < len(matriz):   ## SEMPRE USAR ESSE CÓDIGO PARA PRINTAR
    print(matriz[i])
    i +=1
