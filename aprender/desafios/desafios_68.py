from random import randint
vitorias = 0

print("-=-"*20)
print("VAMOS JOGAR PAR OU INPAR ")
print("-=-"*20)

while True:
    n_pc = randint(0, 20)
    n_player = int(input("digite um valor "))
    lado_player = input("""[P] par
[I] impar
""").upper().strip()
    print("-"*60)
    soma = n_pc + n_player
    if soma % 2 == 0:
        lado_g = "par"
    else:
        lado_g = "impar"

    print(f"você jogo {n_player} e o computador jogou {n_pc}, total é {soma} que é {lado_g}")

    if (lado_player == "P" and lado_g == "par") or (lado_player == "I" and lado_g == "impar"):
        print("você venceu!!")
        print("vamos jogar novamente")
        vitorias += 1
    else:
        print(f"você perdeu com {vitorias} vitorias consecutivas")
        break
    print("-"*60)
