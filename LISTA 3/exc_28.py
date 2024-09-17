cont = 1
numerador = 1
denominador = 1
soma = 0
while cont <= 50:
    soma += numerador / denominador
    numerador +=2
    denominador +=1
    cont +=1
    print(soma)

print(f"Resultado final: {soma:.2f}")