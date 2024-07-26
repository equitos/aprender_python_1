class humano():
    def __init__(self, nome, idade, pesso, altura):
        self.nome = nome
        self.idade = idade
        self.pesso = pesso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.idade += 1
            self.altura += 0.5
        else:
            self.idade += 1


