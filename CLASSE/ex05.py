class Conta:
    def __init__(self,nome,cpf,numero,saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def depositar(self, dinheiro):
        self.saldo += dinheiro
        print(f"Foi depositado R${dinheiro:.2f} em sua conta")

    def saque(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque no valor R${valor:.2f} realizado.")
        else:
            print(f"Saldo insuficiente para saque.")

    def extrato(self):
        print(f"Saldo atual de R${self.saldo:.2f}") 

conta1 = Conta("Yan Torres Martins",42368571620,999698168,1000)

conta1.extrato()

conta1.depositar(500)

conta1.extrato()

conta1.saque(200)

conta1.extrato()