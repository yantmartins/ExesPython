valor_aq = float(input("Informe o valor de aquisição do produto: "))

if valor_aq < 50:
    venda = valor_aq + (valor_aq * 0.45)
    print("O valor de venda desse produto é de: ",venda)
else:
    venda = valor_aq + (valor_aq * 0.3)
    print("O valor de venda desse produto é de: ",venda)     