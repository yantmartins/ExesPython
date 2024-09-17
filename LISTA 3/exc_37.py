num = int(input("Digite um número: "))

i = num
cont = 0

while i >= 1:
    if num % i == 0:
        cont += 1
        i -= 1
    i -= 1

if cont == 2:
    print(f"{num} é um número primo")
else:
    print(f"{num} não é um número primo")         