salario = 4000
ano = 2020
aumento = 0.015

while ano <= 2024:
    print(f"Ano: {ano} | Percentual: {aumento}")
    salario += salario * aumento
    aumento *= 2
    print(f"R${salario:.2F}")
    ano +=1