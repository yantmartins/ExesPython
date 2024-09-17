class Pessoa:
    def __init__(self,nome,idade,email): #Método Construtor
        self.nome = nome #Atributo  
        self.idade = idade #Atributo
        self.email = email #Atributo

    def hello(self): #Método da Classe
        print(f"Olá {self.nome}")

    def getIdade(self):
        return self.idade    

p1 = Pessoa("YAN",25,"yantmartins@live.com")
p2 = Pessoa("LIA",24,"liatorrespet@outlook.com")

x = p1.getIdade()
print("Valor de X: ",x)
print(p1.nome)
print(p1.idade)
p1.hello()

print(p2.nome)
p2.hello()