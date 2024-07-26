class bichinho:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0.5
        self.saude = 0.5
        self._humor = 1

    @property
    def get_humor(self):
        if self._humor == 0:
            humor = "triste"
        elif self._humor == 1:
            humor = "normal"
        elif self._humor == 2:
            humor = "feliz"
        return humor

    @property
    def get_lista(self):
        print(f"nome: {self.nome}")
        print(f"saude = {self.saude}")
        print(f"fome = {self.fome}")
        print(f"humor = {self.get_humor}")
    def alimentar(self, n_comidas):
        self.fome -= n_comidas * 0.1
        self.saude += n_comidas * 0.1

    def brincrar(self, tempo):
        taxa = tempo * 0.2
        if taxa > 1:
            taxa = 1
        self.fome += taxa
        self.saude += taxa

    @property
    def _humor(self):
        return self.__humor

    @_humor.setter
    def _humor(self, value):
        self.__humor = value
        if self.__humor > 2:
            self.__humor = 2
        elif self.__humor < 0:
            self.__humor = 0

    @property
    def saude(self):
        return self._saude

    @saude.setter
    def saude(self, valor):
        self._saude = valor
        if self._saude >= 1:
            self._saude = 1
            self._humor = 1
        elif self._saude < 0:
            self._saude = 0

    @property
    def fome(self):
        return self._fome

    @fome.setter
    def fome(self, valor):
        self._fome = valor
        if self._fome >= 1:
            self._fome = 1
            self._saude = 0
        elif self._fome < 0:
            self._fome = 0


a = bichinho('arthur')
a.alimentar(1)
a.brincrar(8)
a.get_lista
