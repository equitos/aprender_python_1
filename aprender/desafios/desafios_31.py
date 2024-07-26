
km = int(input("qual é a kilometragem da viagem? "))

if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
print(" o preço da viagem é de {} reais".format(preco))