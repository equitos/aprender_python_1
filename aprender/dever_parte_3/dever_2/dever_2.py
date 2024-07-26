from modulos.retangulo import *

def linha():
    print("-"*60)


while True:
    try:
        linha()
        altura = float(input("digite a altura "))
        largura = float(input("digite a largura "))
    except:
        print("\033[31mERRO, tente novamente\033[m")
    else:
        if input("errou? [S/N] ") in "Nn":
            break

linha()
retangulo = retangulo(altura, largura)
retangulo.mudar_lados(100,False)
retangulo.valor_lados()
print(f"area = {retangulo.area()}")
print(f"perimetro = {retangulo.perimetro()}")
linha()




