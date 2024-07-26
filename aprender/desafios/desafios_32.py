ano = int(input("escreva um ano "))

if ano % 4 == 0:
    print("o ano {} é um ano bissexto".format(ano))
else:
    print("o ano {} não é um ano bissexto".format(ano))