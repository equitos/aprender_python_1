dic = {}
lista = []
lista_g = []
print("-"*60)
while True:
    dic['nome_jogador'] = input('Nome do jogadore ')
    dic["partidas"] = int(input('Quantas partidas o jogador jogou? '))
    for i in range(dic["partidas"]):
        lista_g.append(int(input(f'Quantos gols na partida {i+1} ')))
    dic["gols"] = lista_g[:]
    dic["total"] = sum(lista_g)
    print("-"*60)
    lista.append([dic.copy()])
    dic.clear()
    lista_g.clear()
    pergunta = input('Quer continuar? [S/N] ')
    if pergunta in 'Nn':
        break
print("-"*60)
print("cod   jogador   gols        total")
print("-="*30)

for i in range(len(lista)):
    for n  in lista[i]:
        print(f"{i+1:<6}{n["nome_jogador"]:<10}", end = "")
        print(f"{n["gols"]}",end=" ")
        print(f"{n['total']}")
print("-"*60)

while pergunta != 999:
    print("coloque 999 para finalizar o progama")
    pergunta = int(input('qual jgadoer você quer ver? cod '))
    if pergunta > len(lista) and pergunta != 999:
        print("erro")
        print("tente novemente")
        print("-"*60)
    elif pergunta == 999:
        print("fim do programa")
        print("-"*60)
    else:
        print("-"*60)
        for i in lista[pergunta-1]:
            print(f"nome do jogadoer é {i['nome_jogador']}")
            for m, n  in enumerate(i["gols"]):
                print(f"partida {m+1} fez {n} gols")
            print(f"total de gols nas partidas é {i['total']}")
            print("-"*60)
