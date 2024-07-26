from random import randint

print("pedra, papel, tisoura")
jogos_posives = "pedra", "papel", "tisoura"
mao_j = input("escolha a sua mão")
mao_pc = randint(0, 2)
mao_pc = jogos_posives[mao_pc]

if mao_j == mao_pc:
    resutado = "empate"
else:
    if mao_j == "pedra" and mao_pc == "tisoura":
        resutado = "jogador ganhou"
    else:
        resutado = "perdeu"
    if mao_j == "papel" and mao_pc == "pedra":
        resutado = "jogador ganhou"
    else:
        resutado = "perdeu"
    if mao_j == "tisoura" and mao_pc == "papel":
        resutado = "jogador ganhou"
    else:
        resutado = "perdeu"

if resutado == "jogador ganhou":
    set_cor = "\033[32m"
elif resutado == "perdeu":
    set_cor = "\033[31m"
else:
    set_cor = "\033[34m"
print("contra")
print("\033[32m",mao_pc)
print(set_cor,resutado)