class contaCorrent:
    def __init__(self, numero_conta, nome_corretista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_corretista = nome_corretista
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        self.saldo -= valor


