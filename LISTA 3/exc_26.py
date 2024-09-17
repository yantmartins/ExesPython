base = int(input("Digite o valor da base: "))
expo = int(input("Digite o valor do expoente: "))

total = 1

if expo < 0:
    base = 1 / base
    expo = - expo


for _ in range(expo):
    total *= base
print(f"O resultado de {base} elevado a {expo} é: {total}")        