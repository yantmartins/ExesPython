num1 = float(input("Digite o primeiro número: "))
operacao = input("Informe a operação que deseja realizar: \n + - PARA SOMAR \n - - PARA SUBTRAIR \n * - PARA MULTIPLICAR  \n / - PARA DIVIDIR:  ")
num2 = float(input("Digite o segundo número: "))

if operacao == "+":
    tot = num1 + num2
    print(tot)

elif operacao == "-":
    to = num1 - num2
    print(to)

elif operacao == "*":
    tott = num1 * num2
    print(tott)

elif operacao == "/":
    tota = num1 / num2
    print(tota)


