soma_dos_quadrados = 0
soma = 0
i = 1

while i <= 100:
    soma_dos_quadrados += i ** 2
    soma += i
    i += 1

diferenca = (soma ** 2) - soma_dos_quadrados 
print(diferenca)    
