hora_normal = float(input("Informe a quantidade de horas normais trabalhadas: "))
hora_extra = float(input("Informe a quantidade de horas extras trabalhadas: "))

bruto = (hora_normal * 32.50) + (hora_extra * 44.50)
liquido = bruto - (bruto * 0.11)

print("O salário bruto corresponde a: R$",bruto, " e o salário líquido corresponde a: ",liquido)