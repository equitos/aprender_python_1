class retangulo:
    def __init__(self, largura, autura):
        """
        *0-1-2-3-4-5-6-7-8*9
        |1                |
        |2                |
        |3                |
        |4                |
        *5----------------*


        plano carteziano com o y invertido
        """
        self.largura = largura
        self.autura = autura
        self.pontos = []

        for i in range(0, 2):
            for j in range(0, 2):
                self.pontos.append(ponto(i * self.largura, j * self.autura))

    def mostrar_vertices(self):
        """
        *0-----------------*1
        |                  |
        |                  |
        |                  |
        |                  |
        *2-----------------*3
        """
        for i in range(4):
            print(f"ponto {i} = ({self.pontos[i].x} {self.pontos[i].y})")

    def achar_ponto(self, numero_do_ponto):
        return (self.pontos[numero_do_ponto].x, self.pontos[numero_do_ponto].y)

    def achar_ponto_cental(self):
        return (self.largura / 2, self.autura / 2)

class ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
