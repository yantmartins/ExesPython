cons_mensal = int(input("Informe o consumo mensal de energia de sua residencia: "))

cap_diaria_painel = 4

cons_diario = cons_mensal / 30
print(f"O consumo médio diário é de: {cons_diario} kWh")

prod_mensal_painel = cap_diaria_painel * 30
print(f"A produção mensal do painel é de: {prod_mensal_painel} kWh")

quantidade_paineis = cons_mensal / prod_mensal_painel
print(f"Quantidade de painéis solares necessários: {quantidade_paineis}")
