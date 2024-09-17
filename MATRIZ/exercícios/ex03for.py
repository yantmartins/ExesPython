matriz = [[13,2,99],[18,12,67],[30,11,60]]
nova_matriz = []

for linha in matriz:
    nova_linha = []

    for item in linha:
        nova_linha.append(item * 5) ## multiplico os itens
    nova_matriz.append(nova_linha) ## adiciono eles a nova matriz

print("Entrada:")
for linha in matriz:
    print(linha)
    
print()

print("Saída:")
for linha in nova_matriz:
    print(linha)        