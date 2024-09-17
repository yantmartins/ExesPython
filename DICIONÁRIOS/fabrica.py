###PREENCHER e PRINTAR um DICIONÁRIO VAZIO
fabrica = {}

n = int(input("Digite a quantidade de alunos que deseja cadastrar: "))
for i in range(n):
    fabrica[f'aluno{i}'] = input("Digite o nome do aluno: ")

for k,v in fabrica.items():
    print(f'{k} : {v}')    

print(fabrica)