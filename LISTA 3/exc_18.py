qtd = int(input("Digite a quantidade de números: "))
maior_numero = float(input("Digite um número: "))
contador = 1

while contador < qtd:
    numero = float(input("Digite outro número: "))

    if numero > maior_numero:
        maior_numero = numero
        contador +=1
    else:
        contador +=1

print(f"O maior número é: {maior_numero}")           