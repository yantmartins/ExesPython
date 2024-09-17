import math

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))

delta = (b ** 2) - (4 * a * c)
print(delta)


if delta < 0:
    print("Não existe raiz")
elif delta == 0:
    raiz = math.sqrt(delta)
    print(f"Existe raiz real: {raiz}")
elif delta >= 0:
    x1 = (-b + math.sqrt(delta) / (2 * a))        
    x2 = (-b - math.sqrt(delta) /( 2 * a))
    print(f"A primeira raiz é igual a: {x1}")        
    print(f"A segunda raiz é igual a: {x2}")        