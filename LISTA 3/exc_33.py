numeros = [25,12,3,48,55,6,8,11,13,44]
numero_digitado = int(input("Digite um número: "))

i = 0
while i < len(numeros):
    if numeros[i] == numero_digitado:
        print("Está na lista")
    i +=1

        