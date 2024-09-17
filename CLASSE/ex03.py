class Aluno:
    def __init__(self,nome,RA,nota1,nota2,nota3,nota4):
        self.nome = nome
        self.RA = RA
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def mostrar_situacao(self):
        media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
        if media >= 7:
            return "APROVADO"
        elif 5 <= media < 7:
            return " DE EXAME"
        else:
            return "REPROVADO"
        
aluno1 = Aluno("Yan",1302,3,5,3,0)
situacao = aluno1.mostrar_situacao()
print(f"O aluno {aluno1.nome} está {situacao}")        
        