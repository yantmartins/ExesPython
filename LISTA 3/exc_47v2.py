somadosquadrados = soma = 0
for i in range(1,101):
    somadosquadrados += i ** 2
    soma += i
print((soma ** 2) - somadosquadrados)