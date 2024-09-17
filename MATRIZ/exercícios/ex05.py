matriz = [
    [1,2,3,4],
    [5,4,6,7],
    [7,9,8,8],
    [9,8,7,6]
]
maior = 0
i = 0
while i < len(matriz):
    soma = sum(matriz[i])
    if soma > maior:
        linha = i
        maior = soma
    i += 1

print(f"LINHA: {linha} \n SOMA: {maior}")     

