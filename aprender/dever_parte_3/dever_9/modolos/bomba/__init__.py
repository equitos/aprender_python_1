class bombaDeCombustivel:
    def __init__(self):
        self._combustivel = {}

    def abastecimento_por_valor(self, tipo_combostivel, pagar):
        valor_litro = self._combustivel[tipo_combostivel]["valor_litro"]
        litros = pagar // valor_litro
        self._combustivel[tipo_combostivel]["litros_de_combustivel"] -= litros
        return litros

    def abastecimento_por_litro(self, tipo_combostivel, litro):
        valor_litro = self._combustivel[tipo_combostivel]["valor_litro"]
        self._combustivel[tipo_combostivel]["litros_de_combustivel"] -= litro
        return litro * valor_litro

    def add_combustivel(self, tipo_combostivel, valor_litro, litros_combustivel):
        self._combustivel[tipo_combostivel] = {"valor_litro": valor_litro, "litros_de_combustivel": litros_combustivel}

    def altera_valor(self, combustivel, novo_valor):
        self._combustivel[combustivel]["valor_litro"] = novo_valor

    def lista_combustivel(self):
        for i in self._combustivel.items():
            for j in i:
                print(f"{j} ", end="")
            print()

