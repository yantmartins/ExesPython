numeros = [2,11,4,11,5,9,99,11]
i = -1
contador = 0
print(len(numeros))
# Contar a quantidade de números 11 na lista
# Estamos usando len(numeros) -1 para percorrer a lista dentro do índice
while i < len(numeros) - 1:
    i = i + 1
    if numeros[i] != 11:
        continue
    else:
        print("11 está aqui!")
        contador += 1

print(f"Quantidade de números 11 encontrados: {contador} ")        