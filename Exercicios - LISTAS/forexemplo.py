compra = ["Carne","Refirgerante","Nescau","Mussarela","Miojo"]

print(len(compra))
i = 0
while i < 4:
    compra.append(input("Digite um produto: "))
    i = i + 1
else:
    print(compra)
    print(len(compra))    