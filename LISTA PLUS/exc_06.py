maior_numero = None  

while True:
    numero = float(input("Digite um número (ou um número negativo para sair): "))
    
    if numero < 0:  
        break
    
    if maior_numero is None or numero > maior_numero:  
        maior_numero = numero

if maior_numero is None:
    print("Nenhum número foi digitado.")
else:
    print(f"O maior número é: {maior_numero}")
