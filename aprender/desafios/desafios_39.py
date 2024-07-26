import datetime

print("\033[7malistamento militar\033[m")

ano_atual = datetime.date.today().year
ano = int(input('seu ano de nacimento '))
idade = ano_atual - ano

if idade < 18:
    resposta = "\033[36mcalma que ainda não chegou a hora"
elif idade == 18:
    resposta = "\033[31mé hoge que você se fode"
elif idade > 18:
    resposta = "\033[32mfinalmente acabou"

print(resposta)




