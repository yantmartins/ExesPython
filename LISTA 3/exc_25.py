idades = []
soma = 0
contador = 0
while True:
    idade = int(input("Digite a idade, ou 0 para finalizar: "))
    if idade == 0:
        break
    idades.append(idade)
    soma +=idade
    contador +=1
if contador > 0:
    media = soma / contador
    print(f"A idade média do grupo é: {media}")
else:
    print("Nenhuma idade foi digitada!") 