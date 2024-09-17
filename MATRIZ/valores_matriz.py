### LISTA DE LISTA
### LINHAS X COLUNAS -> cada elemento de uma lista é um valor da coluna
matriz = [
    [24,34,44], #linha 0
    [33,29,60], #linha 1
    [21,18,19]
]

i = 0
while i < len(matriz):
    print(matriz[i])
    i +=1

matriz[0][0] = 13
matriz[0][1] = 2
matriz[0][2]= 99
matriz[1][0]= 29
matriz[1][1]= 5
matriz[1][2]= 20
matriz[2][0]= 18
matriz[2][1]= 12
matriz[2][2]= 67

print()

i = 0
while i < len(matriz):   ## SEMPRE USAR ESSE CÓDIGO PARA PRINTAR
    print(matriz[i])
    i +=1

i = 0
while i < len(matriz): # i contador que percorre as linhas
    j = 0
    while j < len(matriz[i]): # j contador que percorre as colunas
        print(matriz[i][j])   # matriz e posição [i][j]
        j += 1
    i += 1        