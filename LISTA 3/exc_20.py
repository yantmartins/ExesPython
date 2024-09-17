p = 0
fim = False
while fim == False:
    num = int(input("Digite um número para começar ou 0 para finalizar: "))
    if num == 0:
        fim = True
    else:
        if num % 2 == 0:
            p += 1
print(f"O total de números pares é de: {p}")            