valor_pagar = 0
pedido = int(input("Deseja fazer um pedido? \n Digite 1 - Para Sim \n Digite 2 - Para Não\n"))

while pedido == 1:
    print("  Lanche             Codigo           Preço")
    print("Cachorro Quente      100            R$11,20")
    print("Ovo Simples          101            R$10,20")
    print("Misto Quente         102            R$15,20")
    print("Bauru com Ovo        103            R$18,20")
    print("Hamburguer           104            R$20,20")

    lanche = int(input("Digite o código do lanche desejado: "))
    qtd_lanche = int(input("Digite a quantidade de lanches"))

    match lanche:
        case 100:
            valor_lanche = 11.20
            total_lanche = valor_lanche * qtd_lanche
        case 101:
            valor_lanche = 10.20
            total_lanche = valor_lanche * qtd_lanche
        case 102:
            valor_lanche = 15.20
            total_lanche = valor_lanche * qtd_lanche 
        case 103:
            valor_lanche = 18.20
            total_lanche = valor_lanche * qtd_lanche
        case 104:
            valor_lanche = 20.20
            total_lanche = valor_lanche * qtd_lanche

    valor_pagar = total_lanche + valor_pagar
    print("Valor a pagar parcial: ", valor_pagar)                    
    
    pedido = int(input("Deseja fazer outro pedido? \n Digite 1 - Para Sim \n Digite 2 - Para Não\n"))

    gorjeta = input("Deseja contribuir com uma gorjeta?\nDigite S - Para Sim \n Digite N- Para Não")
    if gorjeta == "s":
        valor_total = (valor_pagar * 0.1) + valor_pagar
        print(f"O valor da gorjeta foi de {valor_pagar * 0.1}, totalizando {valor_total} a ser pago.")
    else:
        print(f"O valor a ser pago sem gorjeta é de R$: {valor_pagar}")

       

    