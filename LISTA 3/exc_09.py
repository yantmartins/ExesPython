numeros = []
contador = 0

while contador < 10:
    numero = int(input(f"Digite o {contador +1 }º número: "))
    numeros.append(numero)
    contador += 1

    menor = min(numeros)
    maior = max(numeros)

    print(f"O menor valor digitado é {menor} ")
    print(f"O maior valor digitado é {maior} ")
