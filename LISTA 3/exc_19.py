num = int(input("Digite um número entre 100 e 9999: "))

if num < 100 or num > 9999:
    print("Número fora do alcance")
else:
    contador = 1

    while num > 0:

        resto = num % 10

        print(f"Algarismo {contador}:{resto}")

        num //=10
        contador +=1


 