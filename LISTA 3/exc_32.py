i = 0
soma = 0
numeros = []

while i < 5:
    num = int(input("Digite um número: "))
    numeros.append(num)
    i = i + 1

print(sum(numeros))
for num in numeros:
    print(num)    
