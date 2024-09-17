matriz = [[3,4,5,6],
          [7,6,5,4],
          [9,3,2,1],
          [1,2,3,4]
]
produto = 1

i = 0
while i < len(matriz):
    produto *= matriz[i][i]
    i += 1

print(f"Resultado: {produto}")