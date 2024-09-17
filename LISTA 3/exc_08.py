soma = 0
contador = 0

while contador < 2:
    inteiro = int(input("Digite um número: "))
    if inteiro > 0:
     soma += inteiro
     contador += 1

media = soma / contador
print(f"A média dos números digitados é de: {media}")  

