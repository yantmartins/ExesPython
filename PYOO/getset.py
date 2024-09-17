class Quadrado:
    def __init__(self,lado_a,lado_b):
        self.__ladoA = lado_a
        self.__ladoB = lado_b

    def getLadoA(self):
        return self.__ladoA

    def setLadoA(self,novo_lado):
        self.__ladoA = novo_lado

    def getLadoB(self):
        return self.__ladoB

    def setLadoB(self,novo_lado):
        self.__ladoB = novo_lado

q1 = Quadrado(89,55)
print( q1.getLadoA() )
print( q1.getLadoB() )
q1.setLadoB(65)
print()
print( q1.getLadoA() )
print( q1.getLadoB() )
  


##GETTERS E SETTERS
#GET PEGA O VALOR E SET DEFINE O VALOR   
