
class retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def mudar_lados(self, lado, altura=True):
        """
        troca o valor do lado
        :param lado = o valor a ser mudado
        :param altura = se tiver True ele vai trocar o valor da autura,
         caso contrario ele vai colocar o valor de lado em largura
        """
        if altura == True:
            self.altura = lado
        else:
            self.largura = lado

    def valor_lados(self):
        print(f"o obj tem {self.altura} de altura")
        print(f"o obj tem {self.largura} de largura")

    def area(self):
        area = self.altura * self.largura
        return area

    def perimetro(self):
        perimetro = self.altura*2 + self.largura*2
        return perimetro




