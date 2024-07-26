def ficha(nome='<desconhecido>', gols=0):
    if nome == "":
        nome = "<desconhecido>"
    if gols != int or gols == "" or gols < 0:
        gols = 0
    return f'O jogador {nome} fez {gols} no campeonato.'


print("-"*40)
a = input('nome do jogador: ')
b = input('quantos gols ele fez: ')
print("-"*40)
print(ficha(a,b))
print("-"*40)