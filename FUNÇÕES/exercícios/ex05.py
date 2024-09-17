def somaImposto(taxaImposto, custo):
    return custo + (custo * (taxaImposto / 100))

taxa = float(input("Digite a taxa percentual do imposto: "))
custo_inicial = float(input("Digite o custo inicial: R$"))

novo_valor = somaImposto(taxa,custo_inicial)

print(f"O novo valor, considerando o imposto, é de R${novo_valor} ")

    
    
