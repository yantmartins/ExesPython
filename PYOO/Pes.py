class Pessoa:
    def __init__(self,nome,fone,email):
        self.__nome = nome ##Atributo PRIVADO
        self.fone = fone
        self.email = email

    def hello(self):
        print(f"Olá {self.__nome}")


class PessoaFisica(Pessoa):
    def __init__(self, nome, fone, email, rg, cpf):
        super().__init__(nome, fone, email)
        self.rg = rg
        self.cpf = cpf


class PessoaJuridica(Pessoa):
    def __init__(self, nome, fone, email, cnpj, cidade):
        super().__init__(nome, fone, email)
        self.cnpj = cnpj
        self.cidade = cidade



pes1 = PessoaFisica("Yan", 67999698168, "yantmartins@live.com", 1812183, 42368571620)
pes1.hello()

pes2 = PessoaJuridica("Zaine", 67981400243, "lojazaine13@gmail.com", 42019494000119, "CAMPOGRANDE")
pes2.hello()

    