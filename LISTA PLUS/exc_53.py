i = 0
imc = 0
fem = 0
masc = 0
alturas = 0

idade = int(input("IDADE: "))
sexo = input("SEXO: ")
peso = float(input("PESO: "))
altura = float(input("ALTURA: "))

mais_velho = idade
mais_novo = idade
mais_alto = altura
mais_baixo = altura
maior_peso = peso

while i <= 3:
    if idade > mais_velho:
        mais_velho = idade
    if idade < mais_novo:
        mais_novo = idade
    if altura > mais_alto:
        mais_alto = idade
    if altura < mais_baixo:
        mais_baixo = altura
    if peso > maior_peso:
        maior_peso = peso
    
    alturas += altura
    imc += peso / (altura * altura)

    if sexo == "F" or sexo == "f":
        fem += 1
    if sexo == "M" or sexo == "m":
        masc +=1
    
    i += 1
    idade = int(input("IDADE: "))
    sexo = input("SEXO: ")
    peso = float(input("PESO: "))
    altura = float(input("ALTURA: "))


print(f"Mais velho {mais_velho}")
print(f"Mais novo {mais_novo}")
print(f"Mais alto: {mais_alto}")
print(f"Mais baixo: {mais_baixo}")
print(f"Mais pesado: {maior_peso}")