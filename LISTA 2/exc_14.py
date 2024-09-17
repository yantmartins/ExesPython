n1 = float(input("Informe a primeita nota: "))
n2 = float(input("Informe a segunda nota: "))

media = (n1 + n2) / 2

if n1 > 0 and n1 <= 10:
   if n2 > 0 and n2 <= 10:
      print("A média é igual a: ",media)
else:
   print("As notas digitadas são inválidas")        