# Dados dos alunos
matriculas = [1, 2, 3, 4, 5]  # Exemplo com 5 alunos, adicione mais para chegar a 50
sexos = ['F', 'M', 'F', 'M', 'F']
alturas = [172, 165, 160, 180, 171]
status_fisico = [1, 2, 3, 1, 2]

# Variáveis para contagem e cálculo
quantidade_feminino_altura_superior_170 = 0
total_masculino = 0
masculino_status_bom = 0

# Processar dados dos alunos
for i in range(len(matriculas)):
    if sexos[i] == 'F' and alturas[i] > 170:
        quantidade_feminino_altura_superior_170 += 1
    if sexos[i] == 'M':
        total_masculino += 1
        if status_fisico[i] == 1:
            masculino_status_bom += 1

# Calcular porcentagem de alunos do sexo masculino com status físico bom
percentual_masculino_status_bom = (masculino_status_bom / total_masculino) * 100 if total_masculino > 0 else 0

# Imprimir resultados
print(f"Quantidade de alunas com altura superior a 170 cm: {quantidade_feminino_altura_superior_170}")
print(f"Porcentagem de alunos do sexo masculino com status físico bom: {percentual_masculino_status_bom:.2f}%")
