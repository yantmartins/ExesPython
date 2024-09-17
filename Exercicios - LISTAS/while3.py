terminou = False
p = i = 0

while not terminou:
    num = int(input("Digite um número, ou zero para terminar: "))
    if num == 0:
        terminou = True
    else:
        if num % 2 == 0:
            p = p + 1
        else:
            i = i + 1


print("Quantidade de Pares: ",p)
print("Quantidade de Impares: ",i)