class Filme:
    def __init__(self,nome,duracao):
        self.nome = nome
        self.duracao = duracao

    def play(self):
        print(f"O filme {self.nome} começou!")


class Acao(Filme):
    def __init__(self, nome, duracao, estudio):
        super().__init__(nome, duracao) 
        self.estudio = estudio

    def explodir(self, explosivo):
        print(f"Ativar explosivos {explosivo}")    

   
class Comedia(Filme):
    def __init__(self, nome, duracao, atrizes):
        super().__init__(nome, duracao) 
        self.atrizes = atrizes  

    def rir(self, risadas):
        print(f"Muitas {risadas} durante a exibição")


class Suspense(Filme):
    def __init__(self, nome, duracao, roteiro):
        super().__init__(nome, duracao)
        self.roteiro = roteiro         

    def susto(self, sustos):
        print(f"Muitos {sustos} devido as cenas do Suspense") 



filme_acao = Acao("Correr ou Morrer", 120,"Warner Bros")
filme_acao.play()
filme_acao.explodir("TNT")

filme_comedia = Comedia("De Pernas pro Ar", 135, "Ingrid Guimaraes")
filme_comedia.play()
filme_comedia.rir("RISADAS BARULHENTAS")

filme_suspense = Suspense("Silencio dos Inocentes", 180, "AAABBB")
filme_suspense.play()
filme_suspense.susto("GRITOS")