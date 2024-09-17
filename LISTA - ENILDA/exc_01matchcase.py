num1 = float(input("Digite o primeiro número: "))
operacao = input("Informe a operação que deseja realizar: \n + - PARA SOMAR \n - - PARA SUBTRAIR \n * - PARA MULTIPLICAR  \n / - PARA DIVIDIR:  ")
num2 = float(input("Digite o segundo número: "))

match operacao:
    case "+":
     tot = num1 + num2
     print(tot)

    case "-":
     to = num1 - num2
     print(to)

    case "*":
     tott = num1 * num2
     print(tott)

    case "/":
     tota = num1 / num2
     print(tota)