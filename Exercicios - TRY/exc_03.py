saldo = float(input("Digite o saldo inicial da conta: "))
valor_saque = float(input("Digite o valor a ser sacado: "))

try: 
    if valor_saque > saldo:
        saldo -= 1 / 0

    saldo -= valor_saque
    print(f"Saque realizado com sucesso. Saldo restante {saldo}")
except ZeroDivisionError:
    print("Saldo insuficiente para saque")           