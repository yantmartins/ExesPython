pao = float(input("Informe a quantidade de pães vendidos: "))
broa = float(input("Informe a quantidade de broas vendidas: "))

paes = pao * 0.12
broas  = broa * 1.5

total = paes + broas
poupanca = total * 0.1

print("O total arrecadado da venda de pães e broas foi de: ", total)
print("O valor a ser guardado na poupança será de: ",poupanca)