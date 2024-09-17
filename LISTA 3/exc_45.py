salCarlos = float(input("Digite o salário de Carlos: "))
salJoao = salCarlos / 3
meses = 0

while salJoao <= salCarlos:
    meses += 1
    salCarlos += salCarlos * 0.02
    salJoao += salJoao * 0.05
    print(f"MES {meses} AUMENTO CARLOS: {salCarlos}")
    print(f"MES {meses} AUMENTO JOÃO: {salJoao}")
    

print(f"Quantidade de meses: {meses}")    

