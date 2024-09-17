class Veiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo =  modelo

    def mover(self):
        print(f"{self.marca} moveu-se")

    def ligar(self):
        print(f"{self.modelo} ligou")     


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas, ano, motor):
        super().__init__(marca, modelo)
        self.portas = portas
        self.ano = ano
        self.motor = motor

    def mover(self):
        print(f"{self.modelo} andou")


class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, capacete=False):
        super().__init__(marca, modelo)
        self.placa = placa
        self.capacete = capacete

    def mover(self):
        print(f"{self.modelo} empinou")                 


car1 = Carro("VOLKS","GOL",2,1999,1.0)
car1.mover()                   


moto1 = Moto("HONDA","BIZ","HSX-9999",True)
moto1.mover()
