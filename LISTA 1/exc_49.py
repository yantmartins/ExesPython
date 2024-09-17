latas = float(input("Informe o número de latas compradas: "))
garrafinha = float(input("Informe o número de garrafinhas compradas: "))
garrafa = float(input("Informe o número de garrafas compradas: "))

total = (latas * 350) + (garrafinha * 600) + (garrafa * 2000)
total_litros = total / 1000

print("A quantidade de refrigerantes comprada, em litros, é de: ",total_litros, "litros")