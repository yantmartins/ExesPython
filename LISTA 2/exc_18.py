numero = int(input("Digite um numero: "))

if numero <=0:
    print("Numero invalido!")
else:
    aux = str(numero)
    soma = int(aux[0]) + int(aux[1]) + int(aux[2])
    print(soma)
