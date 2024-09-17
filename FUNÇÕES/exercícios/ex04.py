def pos_neg(x):
    if x > 0:
        return "P"
    else:
        return "N" 

i = int(input("Digite um número: "))

res = pos_neg(i)
print(res)    