class funcionario:
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    def get_funcionario(self):
        print(f'Nome: {self._nome}')
        print(f'Salario: {self._salario}')
    def porcentagemDeaumento(self, taxa):
        self._salario = self._salario + (self._salario * (taxa/100))

