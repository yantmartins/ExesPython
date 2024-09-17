class Livro:
    def __init__(self, nome,autor,editora,paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def alterar_editora(self,nova_editora):
        self.editora = nova_editora
        print(f"A editora foi atualizada para: {nova_editora}")

    def listar_qtde_paginas(self):
        print(f"A quantidade de páginas é: {self.paginas} ")

livro1 = Livro("Harry Potter","J.K.Rowlings","Abril",500)

print(livro1.nome)
print(livro1.autor)
print(livro1.editora)


livro1.alterar_editora("Panini")


livro1.listar_qtde_paginas()