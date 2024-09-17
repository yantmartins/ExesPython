soma = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        soma +=1
print(f"A soma de todos os números naturais abaixo de 1000 que são multiplos de 3 ou 5 é: {soma}")        