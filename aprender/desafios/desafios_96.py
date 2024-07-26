def area(largura, altura):
    print(largura * altura,"m²")

def l():
    print("-"*40)


l()
largura = float(input("Largura da parede (m): "))
altura = float(input("Altura da parede (m): "))
l()
area(largura, altura)
l()