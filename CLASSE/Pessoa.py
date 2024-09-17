class Pessoa:
    def __init__(self,nome,idade,sexo,altura,peso):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura
        self.peso = peso

    def mostrarDados(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade} anos de idade\nSexo: {self.sexo}\nAltura: {self.altura}cm\nPeso: {self.peso}kg')

pes1 = Pessoa("YAN",25,"M",1.81,84)                   
pes2 = Pessoa("LIA",24,"F",1.79,75)                   
pes3 = Pessoa("PAULO",33,"M",1.75,68)                   
pes4 = Pessoa("ISA",27,"F",1.81,55)        

pes1.mostrarDados()