matriz = [[11,12,13,21],
          [19,18,17,22],
          [45,20,27,15],
          [16,14,14,29]
]
cont = 0
lista = []

i = 0
while i < len(matriz):
    j = 0
    while j < len(matriz[i]):
        x = matriz[i][j]
        if x > 20:
            cont += 1
            lista.append(x)
        j += 1
    i += 1

print(f"Elementos maiores que 20: {cont}")
print(f"Total maior que 20: {lista}")