def multiplos_argumentos(*args):
    med = sum(args) / len(args)
    return med

result = multiplos_argumentos(2.5,5.9,7.8,9.2,3.3)
print(result)