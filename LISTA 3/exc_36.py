alunos = []

for i in range(1, 11):
    print()
    print(f"-=-=-=-=- {i}º aluno-=-=-=-=-=-")

    nota1 = float(input("1ª nota: "))
    while nota1 < 0 or nota1 > 10:
        nota1 = int(input("Nota inválida! Digite novamente a 1ª nota: "))

    nota2 = float(input("2ª nota: "))
    while nota2 < 0 or nota2 > 10:
        nota2 = int(input("Nota inválida! Digite novamente a 2ª nota: "))

    nota3 = float(input("3ª nota: "))
    while nota3 < 0 or nota3 > 10:
        nota3 = int(input("Nota inválida! Digite novamente a 3ª nota: "))

    nota4 = float(input("4ª nota: "))
    while nota4 < 0 or nota4 > 10:
        nota4 = float(input("Nota inválida! Digite novamente a 4ª nota: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    aluno = {
        i: media
    }
    alunos.append(aluno)

print()

c = 1
for aluno in alunos:
    if aluno[c] >= 7:
        print(f"Média do {c}º aluno: {aluno[c]}")
    c += 1
