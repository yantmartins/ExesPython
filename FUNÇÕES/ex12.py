def media(lista):
    med = sum(lista) / len(lista) ##somar a lista toda e dividi-la pelo seu tamanho para obter a média
    return med


resultado = media([2,9,22,5,78,19,24])

numeros = [99,98,97,96,95,94]

x = media(numeros)
print(x)

print(f'{resultado:.2f}')
