lista = []
dic = {}

print("-"*60)

dic["nome do jogador"] = input("Nome do jogador: ")
dic["partidas_jogadas"] = int(input("quantas partidas jogadas "))
for i in range(dic["partidas_jogadas"]):
    lista.append(int(input(f"quantos gols na partida {i+1} ")))
dic["gols"] = lista
dic["total"] = sum(dic["gols"])

print("-"*60)
print(f"o jogadoer {dic["nome do jogador"]} jogou {dic['partidas_jogadas']} partidas.")
for i, n in enumerate(dic["gols"]):
    print(f"{"->":>5} Na partida {i+1} fez {n} gols.")
print(f"no total ele fez {dic['total']} gols.")

print("-"*60)
