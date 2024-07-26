lista = []
mulheres = []
dic = {}
tudo = 0

print("-"*60)
while True:
    dic["nome"] = input("Nome: ")
    dic["sexo"] = input("Sexo: ")
    dic["idade"] = int(input("Idade: "))
    lista.append(dic.copy())
    dic.clear()

    pergunta = input("Quer continuar? [S/N] ")

    if pergunta in "Nn":
        break
print("-"*60)

for i in lista:
    for n, k in i.items():
        print(f"{n} : {k}")
    tudo += i["idade"]
    if i["sexo"] in "Ff":
        mulheres.append(i["nome"])
    print("-"*60)

media = tudo/len(lista)

print(f"o grupo tem {len(lista)} pessoas")
print(f"a media de idade do grupo é {media:.2f}")
print("as mulhers do grupo foram a ", end="")
for i in mulheres:
    print(i, end=" ")
print()
print("as pessoas que estao na media de idade do grupo são ", end="")
for i in lista:
    if i["idade"] >= media:
        print(i["nome"], end=" ")
print()
print("-"*60)