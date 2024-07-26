dicionario = {}
lista = []

print("-"*60)
while True:
    dicionario["nome"] = input("name ")
    dicionario["nota_1"] = float(input("nota 1 "))
    dicionario["nota_2"] = float(input("nota 2 "))
    dicionario["media"] = (dicionario["nota_1"] + dicionario["nota_2"])/2

    lista.append(dicionario.copy())

    pergunta = input("Quer continuar? [S/N] ")
    print("-"*60)

    if pergunta in "Nn":
        break

for i in lista:
    for v, m in i.items():
        print(f"{v} = {m}")
    print("-"*60)