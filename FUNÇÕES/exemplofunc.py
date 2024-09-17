## *ARGS é uma lista de PARAMETROS
def somar(num, *args):
    s = num
    s = s + args[0]
    return s

res = somar(11,12,13,14,15) #O primeiro parametro é obrigatório, o restante é a lista ARGS podendo ter vários parametros
print(res)

def soma(nume,*args):
    so = nume
    i = 0
    while i < len(args):
        so += args[i]
        i += 1
    return so

resul = soma(12,12,13,15,15)
print(resul) 


