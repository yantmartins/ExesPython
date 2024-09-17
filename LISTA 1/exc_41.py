valor_total = float(input("Informe o valor total: "))

desc = valor_total - (valor_total * 0.1)
parcela = valor_total / 3
comi_desc = desc * 0.05
comi_parc = valor_total * 0.05





print("O valor, com desconto de 10%, fica em: R$",desc)
print("O valor de cada parcela, no parcelamento de 3× sem juros fica: R$",parcela)
print("A comissão do vendedor, na venda a vista é de: R$", comi_desc)
print("A comissão do vendedor, no caso da venda ser parcelada é de: R$", comi_parc)