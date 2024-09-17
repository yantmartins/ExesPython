total_pedido = 0
quest = input("Bem Vindo ao DEV Restaurant \nDeseja fazer um pedido? \n Digite s - para SIM \n Digite n - para NÃO\n")

while quest == "s":
    prato = int(input("MENU: \n [1]Bife acebolado R$15,00; \n [2]Lasanha R$25,00; \n [3]Macarronada R$:30,00; \n [4]Frango Grelhado R$35,00; \n [5]Strogonoff R$40,00; \n [6]Sushi R$100,00; \n [7]Churrasco R$100,00; \n [8]Pizza R$80,00; \n [9]Cachorro Quente R$20,00; \n [10]Café R$50,00; \n FAÇA SUA ESCOLHA: "))
    qtd = int(input("Informe a quantidade: "))
    match prato:
        case 1:
            valor = 15
            total = valor * qtd
            print(f"RESUMO DO PEDIDO --> {qtd} Bife acebolado por R$ {total}")
        case 2:
            valor = 25
            total = valor * qtd
            print(f"RESUMO DO PEDIDO --> {qtd} Lasanha por R$ {total}")
        case 3:
            valor = 30
            total = valor * qtd
            print(f"RESUMO DO PEDIDO --> {qtd} Macarronada por R$ {total}")         
        case 4:
            valor = 35
            total = valor * qtd
            print(f"RESUMO DO PEDIDO --> {qtd} Frango Grelhado por R$ {total}")
        case 5:
            valor = 40
            total = valor * qtd 
            print(f"RESUMO DO PEDIDO --> {qtd} Strogonoff por R$ {total}")
        case 6:
            valor = 100
            total = valor * qtd
            print(f"RESUMO DO PEDIDO --> {qtd} Sushi por R$ {total}")
        case 7:
            valor = 100
            total = valor * qtd
            print(f"RESUMO DO PEDIDO --> {qtd} Churrasco por R$ {total}")
        case 8:
            valor = 80
            total = valor * qtd
            print(f"RESUMO DO PEDIDO --> {qtd} Pizza por R$ {total}")     
        case 9:
            valor = 20
            total = valor * qtd
            print(f"RESUMO DO PEDIDO --> {qtd} Cachorro Quente por R$ {total}")
        case 10:
            valor = 50
            total = valor * qtd 
            print(f"RESUMO DO PEDIDO --> {qtd} Café por R$ {total}")   

    total_pedido += total
    print(f"Valor a pagar parcial: {total_pedido}")
    add = int(input("Deseja fazer outro pedido? \n[1]sim \n[2]nao: "))
    if add == 2:
        break

gorjeta = int(input("Aceita pagar a gorjeta do garçom (10% sobre o valor do pedido)? \n[1]sim \n[2]nao : "))
if gorjeta == 1:
    total_final = total_pedido + (total_pedido * 0.1)
    print(f"O valor da gorjeta foi de {total_pedido * 0.1}, totalizando {total_final} a ser pago.")
else:
    total_final = total_pedido


