inicio = int(input("Início:"))
fim = int(input("Fim:"))

soma = 0
if inicio > fim:
    print("Intervalo inválido")
else:
    while inicio <= fim:
        if inicio % 2 == 1:
            soma += inicio
            print(inicio)
        inicio +=1
    print(soma)        