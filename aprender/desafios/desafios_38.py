
amarelo = '\033[1;33m'
limpar = '\033[m'
n1 = int(input("primeiro numero: "))
n2 = int(input("segundo numero: "))

if n1 > n2:
    resposta = "{}{}{} é maior que {}{}{}".format(amarelo, n1, limpar, amarelo, n2, limpar)
elif n2 > n1:
    resposta = "{}{}{} é maior que {}{}{}".format(amarelo, n2, limpar, amarelo, n1, limpar)
else:
    resposta = "{}{}{} e {}{}{} sao iguais".format(amarelo, n1, limpar, amarelo, n2, limpar)

print(resposta)