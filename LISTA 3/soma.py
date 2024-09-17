soma = 0
aux = 0
while aux < 10:
    num = int(input("DIGITE UM NUMERO: "))
    if num > 0:
        print("caiu no IF")
        soma = soma + num
        aux = aux + 15
    else:
     print("VALOR do cont:", aux)
     print("VALOR da soma: ",soma)
     continue

media = soma / aux
print("MEDIA: ",media)