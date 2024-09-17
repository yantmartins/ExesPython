class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def nome_completo(self):
        return f"O funcionário se chama {self.nome} {self.sobrenome}"

    def calcular_salario(self):
        salario = self.horas_trabalhadas * self.valor_hora
        return salario

    def incrementar_horas(self, horas):
        self.horas_trabalhadas += horas
        return self.horas_trabalhadas


func1 = Funcionario("Yan", "Torres", 80, 60)


imprimir = func1.nome_completo()
print(imprimir)

old_salario = func1.calcular_salario()
print(f"O salário dele é de R${old_salario:.2f}")


incremento = func1.incrementar_horas(10)


novo_salario = func1.calcular_salario()
print(f"Salário após incremento: R${novo_salario:.2f}")
