def cobranca(preco, qtd_itens):
    tabela = "Lojas Quase Dois - Tabela de preços\n"
    for i in range(1, qtd_itens + 1):
        total = i * preco
        tabela += f"{i} - RS$ {total:.2f}\n"
    return tabela



preco = 1.99
qtd_itens = 50

tabela_precos = cobranca(preco, qtd_itens)
print(tabela_precos)


