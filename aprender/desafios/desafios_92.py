import datetime

dic = {}

ano_atual = datetime.date.today().year

print("-"*60)

dic["nome"] = input('Nome: ')
dic["data_nacimento"] = int(input('Data de nascimento: '))
dic["anos"] = ano_atual - dic["data_nacimento"]
dic["ctps"] = int(input("carteira de trabalho (0 não tenho) "))
if dic["ctps"] != 0:
    dic["contratação"] = int(input("ano de contratação "))
    dic["salario"] = float(input("salarios "))
    dic["aposentar"] = (dic["contratação"] - dic["data_nacimento"]) + 35

print("-"*60)

for k, v in dic.items():
    print(f"{k}: {v}")
print("-"*60)