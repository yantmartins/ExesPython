n = int(input("Digite um número inteiro: "))

if n <= 0:
    print("Por favor digite um número inteiro positivo")
else:
      soma = 0
      contador = 1

      while contador <= n:
       soma += contador
       contador +=1

print(f"A soma dos {n} primeiros numeros naturais é: {soma}")          