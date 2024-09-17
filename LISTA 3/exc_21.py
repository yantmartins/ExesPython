num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

menor = 0
maior = 0

if num1 > num2:
    menor = num2
    maior = num1
else:
    menor = num1
    maior = num2

soma = 0
mult = 1

while menor <= maior:
    if menor % 2 == 0:
        soma += menor
    elif menor % 2 == 1:
        mult = mult * menor 
    menor +=1 

print(f"A soma dos pares é igual a: {soma}")
print(f"A multiplicação dos ímpares é igual a: {mult}")             