def calculo(potencia_eletrica, tempo_ligado):
     calc = (potencia_eletrica / 1000) * tempo_ligado
     return calc

def calcular_conta_energia(calculo, valor_kwh):
     custo = calculo * valor_kwh
     return custo

potencia_eletrica = 6000
tempo_ligado = 500
valor_kwh = 0.67

calculos = calculo(potencia_eletrica, tempo_ligado)
print(f"O calculo de consumo é de {calculos} KWh")

custos = calcular_conta_energia(calculos,valor_kwh)
print(f"O custo da conta de energia é de R$ {custos:.2f}")








#def calcula_kwh(pot,tempo):
    # consumo = (pot * (tempo/60) / 1000)
    # return consumo

#banho = calcula_kwh(4600,30)
#print(f'Consumo: {banho:.2f} KWh')

#preco = 0.67 * banho

#print("Valor do banho: ",preco)