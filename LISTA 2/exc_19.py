n1 = float(input("DIGITE A PRIMEIRA NOTA: "))
n2 = float(input("DIGITE A SEGUNDA NOTA: "))
n3 = float(input("DIGITE A TERCEIRA NOTA: "))

media = ((n1 + n2 + (n3 *2)) / 4) * 10

if media >= 60:
    print("A média é: ", media,". APROVADO")
else:
    print("REPROVADO")    