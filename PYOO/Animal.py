class Animal:
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor

    def mover(self):
        print(f"{self.nome} moveu-se")

    def comer(self):
        print(f"{self.nome} comeu")    

class Cachorro(Animal):
    def __init__(self, nome, cor,peso):
        super().__init__(nome, cor)
        self.peso = peso

    def mijarNoPoste(self):
        print(f"{self.nome} batizou o poste")                


class Peixe(Animal):
    def __init__(self, nome, cor, especie):
        super().__init__(nome, cor)
        self.especie = especie


peixe1 = Peixe("NEMO","LARANJA","PALHAÇO")

print(peixe1.nome)

peixe1.mover()

c1 = Cachorro("TOTO","CARAMELO",5)
c1.mover()
c1.comer()

dog1 = Cachorro("AUAUA", "PRETO E BRANCO", 10)
dog1.mijarNoPoste()

a1 = Animal("BILU","AZUL")
print(a1.nome)
print(a1.cor)

a1.cor = "MARROM"
print(a1.cor)

a1.mover()