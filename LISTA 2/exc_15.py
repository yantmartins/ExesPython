horas_trab = float(input("Informe o número de horas trabalhadas: "))
valor_hora = 40.5
pag = horas_trab * valor_hora

if pag > 2500:
    tax = pag - (pag * 0.11)
    print("O valor de seu salário líquido é de: ", tax)
    print("O valor de seu salário bruto é de: ", pag)
else:
    print("O valor de seu salário líquido é de: ",pag)    