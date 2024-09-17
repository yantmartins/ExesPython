jose = 0
yuri = 0
enzo = 0
luiz = 0
brancos = 0
nulos = 0
total = 0

while True:
    print("Eleições 2024")
    print(" 1 - José \n 2 - Yuri \n 3 - Enzo \n 4 - Luiz \n 5 - Brancos \n 6 - Nulos")
    voto = int(input("Digite seu voto: "))
    if voto == 0:
        print("Programa Finalizado")
        break
    total += 1
    if voto == 1:
        jose += 1
    elif voto == 2:
        yuri += 1
    elif voto == 3:
        enzo += 1
    elif voto == 4:
        luiz += 1
    elif voto == 5:
        brancos += 1
    elif voto == 6:
        nulos += 1                   

print(f"Total de votos: {total}")
print(f"José recebeu: {jose}")
print(f"Yuri recebeu: {yuri}")
print(f"Enzo recebeu: {enzo}")
print(f"Luiz recebeu: {luiz}")
print(f"Brancos recebeu: {brancos / total * 100:.2f} % dos votos")
print(f"Nulos recebeu: {nulos / total * 100:.2f} % dos votos")
