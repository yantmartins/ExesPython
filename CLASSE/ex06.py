class Circulo:
    def __init__(self,raio):
        self.raio = raio

    def imprimir_raio(self):
        print(f"O valor do raio equivale a: {self.raio}")

    def calcularArea(self):
        area = 3.18 * (self.raio * self.raio)
        print (f"A área do círculo equivale a {area}")

    def circunferencia(self):
        circ = 2 * 3.14 * self.raio
        print(f"A circunferência do círculo equivale a {circ:.2f}")

circ1 = Circulo(5)

circ1.imprimir_raio()

circ1.calcularArea()

circ1.circunferencia()