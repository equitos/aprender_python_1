class tv:
    def __init__(self, nome, volume, canais):
        self.nome = nome
        self.volume = volume
        self.canais = canais

    def aumenta_volume(self, aumento=0):
        self.volume += aumento
        if self.volume > 100:
            self.volume = 100
    def diminuir_volume(self, diminuir=0):
        self.volume -= diminuir
        if self.volume < 0:
            self.volume = 0

    def trocar_usuario(self, usuario):
        self.nome = usuario
