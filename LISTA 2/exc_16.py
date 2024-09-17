salario = float(input("Insira o valor de seu salário: "))
prest = float(input("Insira o valor da prestação do empréstimo: "))

cond = salario * 0.2

if prest > cond:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")     