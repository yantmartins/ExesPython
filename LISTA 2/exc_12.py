num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro: "))

dif = num1 - num2
dif2 = num2 - num1

if num1 > num2:
    print("O maior número digitado é: ",num1, " e a diferença entre eles é de: ", dif)
else:
    print("O maior número digitado é: ", num2, "e a diferença entre eles é de: ", dif2)    