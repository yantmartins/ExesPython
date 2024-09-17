print("##" * 16)
print("SYS CALC")
print("--" * 16)
print("Escolha a Opção")
print("1 - Soma de 2 números")
print("2 - Diferença entre 2 números")
print("3 - Produto de 2 números")
print("4 - Divisão entre 2 números")
print("##" * 16)

opcao = int(input("Digite a sua opção: "))

if opcao == 1:
    n1 = float(input("DIGITE N1: "))
    n2 = float(input("DIGITE N2: "))
    soma = n1 + n2
    print(soma)
elif opcao == 2:
    n1 = float(input("DIGITE N1: "))
    n2 = float(input("DIGITE N2: "))
    if n1 > n2:
     sub = n1 - n2
     print(sub)
    if n2 > n1:
     sub = n2 - n1 
     print(sub)
elif opcao == 3:
    n1 = float(input("DIGITE N1: "))
    n2 = float(input("DIGITE N2: "))
    mult = n1 * n2
    print(mult)
elif opcao == 4:
    n1 = float(input("DIGITE N1: "))
    n2 = float(input("DIGITE N2: "))
    if n1 <= 0:
       print("O DENOMINADOR NÃO PODE SER ZERO")
    else:   
     div = n1 / n2
     print(div)
else:
   print("OPÇÃO INVÁLIDA")              
          