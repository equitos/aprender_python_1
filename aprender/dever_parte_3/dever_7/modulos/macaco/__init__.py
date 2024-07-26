class macaco:
    def __init__(self, nome, estomago):
        self.estomago = estomago
        self.nome = nome

    def digirir(self):
        self.estomago -= 1

    def comer(self, obj):
        if isinstance(obj, macaco):
            self.estomago += obj.estomago
        else:
            from ..comidas import comida
            self.estomago += obj.caloria
