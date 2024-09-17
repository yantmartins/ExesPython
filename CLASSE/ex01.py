class Pessoa:
    def __init__(self, nome,idade,endereco="Não possui"):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostarNome(self):
        return self.nome

    def alterarIdade(self,nova_idade):
        self.idade = nova_idade

    def imprimirEndereco(self):
        print(f"Endereço: {self.endereco} ")  

pessoa1 = Pessoa("YAN",25,"AV. AFONSO PENA, 5000")
pessoa2 = Pessoa("LIA",24,"R. RIO CLARO, 55")
pessoa3 = Pessoa("ISA",27,"R. LAGUNA, 75")

print( pessoa1.mostarNome() )
print(pessoa1.idade)

pessoa1.alterarIdade(24)

print(pessoa1.idade)

pessoa1.imprimirEndereco()

nome = pessoa1.mostarNome()
print(nome)