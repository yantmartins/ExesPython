class Pessoa:
    def __init__(self,matricula,nome,idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, notas, media):
        super().__init__(matricula, nome, idade)
        self.notas = notas
        self.media = media

    def estudar(self):
        print(f"O aluno {self.nome}, da matricula {self.matricula} de {self.idade} anos de idade, estuda no SENAC, só tira nota {self.notas} e tem uma boa média curricular de {self.media}")    

class Professor(Pessoa):
    def __init__(self, matricula, nome, idade, formacao, disciplina, cargaHoraria, salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.cargaHoraria = cargaHoraria
        self.salario = salario

    def lecionar(self):
        print(f"O professor {self.nome}, da matricula {self.matricula}, de {self.idade} anos de idade, com formação em {self.formacao} leciona {self.disciplina} com a carga horária de {self.cargaHoraria}horas por semana e recebe R${self.salario} de salário mensal")

    def calcularMedia(self):
        print(f"O professor {self.nome} faz o calculo da media baseado nas notas obtidas pelo aluno")                        


aluno1 = Aluno(202455,"Yan",25, 10, 10)
aluno1.estudar()

prof1 = Professor(20242024,"Thiago","38","Análise e Desenvolvimento de Sistemas","Programação Orientada a Objetos",80,30000)
prof1.lecionar()
prof1.calcularMedia()