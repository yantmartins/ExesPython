try:
    num = int(input("Digite um número inteiro: "))
    i = num

    while i >=0:
        print(i)
        i -= 1
except ValueError:
    print("Digite apenas números inteiros")        