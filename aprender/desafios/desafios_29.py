vel = int(input("Qual a velocidade do carro em km/h? "))

if vel <= 80:
    print("sua velocidade é {} km/h e o limete é de 80 km/h, entao esta tranquilo".format(vel))
else:
    m = (vel - 80) * 7.00
    print("sua velocidade utrapasou o limite de 80 km/h e levara uma muta de {} reais".format(m))
