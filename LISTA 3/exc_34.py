numeros = []
pares = []
impares = []

i = 0
while i < 20:
    num = int(input("Digite um número: "))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    i += 1

print("LISTA DE NUMEROS DIGITADOS:",numeros)
print(f"A soma dos números digitados é de: {sum(numeros)}")
print(f"Os números pares digitados são: {pares}")
print(f"Os números impares digitados são: {impares}")
