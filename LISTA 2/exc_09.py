num1 = float(input("DIGITE UM NÚMERO: "))
num2 = float(input("DIGITE OUTRO NÚMERO: "))

inv1 = num1 - num1 - num1
inv2 = num1 - num1 - num1
inv3 = num2 - num2 - num2
inv4 = num2 - num2 - num2

if num1 > 0:
    print("O valor invertido do primeiro número é igual a: ", inv1)
else:
    print("O valor invertido do primeiro número é igual a: ", inv2)    

if num2 > 0:
    print("O valor invertido do segundo número é igual a: ",inv3)
else:
    print("O valor invertido do segundo número é igual a: ",inv4)    