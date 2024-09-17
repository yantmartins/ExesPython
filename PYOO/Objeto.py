class Objeto:
    def __init__(self, forma):
        self.__forma = forma

    def mostrarForma(self):
        print(f"{self.__forma}")


          
obj2 = Objeto("TRIANGULO")           
obj3 = Objeto("CIRCULO")           
obj4 = Objeto("QUADRADO") 


obj4.mostrarForma()
obj4.__forma = "RETANGULO"

obj3.__forma = "LUA"
print(obj3.__forma)
