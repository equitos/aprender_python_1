from datetime import date

("\033[36msua clasificação na natação")

ano = int(input("Digite o ano de nascimento: "))
idade = date.today().year - ano

if idade <= 9:
    resposta = "mirim"
elif idade < 19:
    resposta = "infantil"
elif idade < 20:
    resposta = "junior"
elif idade == 20:
    resposta = "senior"
else:
    resposta = "master"

print("\033[34msua clasificação é {}\033[m".format(resposta))