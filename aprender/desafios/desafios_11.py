print("saber a quantidade de tinta para pintar uma parede sabendo que um balde pinta 2m²")

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura * altura
tinta = area/2

print("para pintar uma parede de {} m² serao nessesarios {} latas de tinta".format(area, tinta))