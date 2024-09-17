class Cachorro:
    def __init__(self,nome,peso,idade,cor):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.cor = cor

    def latir(self):
        print(f'{self.nome} AU AU AU')

    def comer(self):
        print(f'{self.nome} comeu')

dog1 = Cachorro("BILU",7,5,"CARAMELO")

print(dog1.nome)
print(dog1.cor)

dog1.latir()
dog1.comer()