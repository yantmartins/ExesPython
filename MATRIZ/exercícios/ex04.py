matriz = [
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1]
]
while True:
    op = input("Deseja marcar X? S - Sim / N - Não: ")
    if op == "N" or op == "n":
        break
    linha = int(input("Digite a linha desejada: "))
    coluna = int(input("Digite a coluna desejada: "))

matriz[linha][coluna] = "X"
print()

i = 0
while i < len(matriz):
    print(matriz[i])
    i += 1