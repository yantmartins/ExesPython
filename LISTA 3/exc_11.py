soma = 0
contador = 0
numero = 0

while contador < 50:
    if numero % 2 == 0:
     soma += numero
    numero +=2
    contador +=1

print(f"o total da soma dos 50 primeiros números pares é de: {soma}")    





soma = 0
for num in range(100):
    if num % 2 == 0:
        soma += num
print(f"o total da soma dos 50 primeiros números pares é de: {soma}")