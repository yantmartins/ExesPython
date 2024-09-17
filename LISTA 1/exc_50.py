import math

num1 = float(input("Digite o número na posição x1: "))
num2 = float(input("Digite o número na posição y1: "))
num3 = float(input("Digite o número na posição x2: "))
num4 = float(input("Digite o número na posição y2: "))

d = (((num1 - num2)**2) + ((num3 - num4)**2))
d_raiz = math.sqrt(d)

if d_raiz >= 10:
    print("Longe")
else:
    print("Perto")

   



