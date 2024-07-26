import datetime

ano_atual = datetime.date.today().year
menor = 0
maior = 0

for c in range(0,7):
    ano1 = int(input('Digite o ano de nascimento: '))
    if (ano_atual - ano1) <= 21:
        menor += 1
    else:
        maior +=1

print("entre essas pessoas a {} de maior e {} de menor".format(maior,menor))