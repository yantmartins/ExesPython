n = int(input("DIGITE UM NUMERO NÃO NEGATIVO: "))

if n < 0:
    print("Por favor, digite um número não negativo.")
else:
    soma = 0
    contador = 0
    numero = 2
    
    while contador < n:
        primo = True
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                primo = False
                break
        
        if primo:
            soma += numero
            contador += 1
        
        numero += 1
    
    print(f"A soma dos {n} primeiros números primos é: {soma}")
