matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]
nova_matriz = []

i = 0

while i < len(matriz):
    linha_nova = []
    j = 0
    while j < len(matriz[i]):
        mult = matriz[i][j] * 5
        linha_nova.append(mult)
        j += 1
    nova_matriz.append(linha_nova)
    i += 1    

x = 0
while x < len(matriz):
    print(matriz[x])
    x +=1

print()

x = 0
while x < len(nova_matriz):
    print(nova_matriz[x])
    x +=1