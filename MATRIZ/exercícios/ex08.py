matriz = [[12,11,16],
          [17,13,14],
          [15,24,26]
]
cont = 0
lista = []

i = 0
while i < len(matriz):
    j = 0
    while j < len(matriz[i]):
        x = matriz[i][j]
        if x % 2 == 0:
            cont += 1
            lista.append(x)
        j += 1
    i += 1

print(f"Números Pares: {lista}")