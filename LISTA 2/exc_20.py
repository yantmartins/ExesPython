n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

if (n1 < 0.0 or n1 > 10.0 ) or (n2 < 0.0 or n2 > 10.0) or (n3 < 0.0 or n3 > 10.0):
    print("Nota inválida!")
else:
    media = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10
    if media > 0.0 and media <= 2.9:
        print(f"REPROVADO! MÉDIA: {media}")
    elif media >= 3.0 and media <= 5.9:
        print(f"EXAME! MÉDIA: {media}")
    elif media >= 6.0 and media <= 9.0:
        print(f"APROVADO! MÉDIA: {media}")
    else:
        print(f"APROVADO COM LOUVOR!!! Média de: {media}")    
