dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

preso = 60 * dias + 0.15 * km

print("o valor a pagar por {} dias com {} km rodados é de ${} reais".format(dias, km, preso))