class conta_Invertidor:
    def __init__(self, saldo=0, juros_compostos=10):
        self._saldo = saldo
        self._juros_compostos = juros_compostos/100

    def ver_conta(self):
        print(f'saldo: {self._saldo}')
        print(f'juros compostos: {self._juros_compostos}')

    def tempo_passado(self, tempo_anos):
        montante = self._saldo * (1 + self._juros_compostos) ** tempo_anos
        montante = float(f"{montante:.2f}")
        self._saldo = montante
        return montante

    def ver_tempo(self, tempo_anos):
        montante = self._saldo * (1 + self._juros_compostos) ** tempo_anos
        print(f'saldo em {tempo_anos} anos: {montante:.2f}')

