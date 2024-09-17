def valorpadrao(quant,valor):
    lista = []
    for i in range(quant):
        lista.append(valor)
    return lista

a = int(input("Digite o tamanho da lista: "))
b = input("Digite o valor padrão da lista: ")

result = valorpadrao(a,b)
print(result)
