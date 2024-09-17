area = int(input("AREA: "))
cob_por_lata = 18 * 6
print(cob_por_lata)
cob_por_galao = 3.6 * 6

print(f"COBERTURA POR LATA: {cob_por_lata}")
print(f"COBERTURA POR GALAO: {cob_por_galao}")

total_latas = area / cob_por_lata
total_galoes = area / cob_por_galao

preco_lata = 80
preco_galao = 25

print(f"Total de latas: {total_latas}")
print(f"Total de galões: {total_galoes}")

print("CUSTO TOTAL LATAS: ", total_latas * preco_lata)
print("CUSTO TOTAL GALOES: ", total_galoes * preco_galao)