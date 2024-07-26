lista = []
while True:
    n = int(input("digite um valor "))
    while True:
        if n not in lista:
            lista.append(n)
            break
        else:
            n = int(input("ja tem esse numero, tente novemente "))
    pergunta = input("quer continuar? [S/N] ").strip().upper()

    if pergunta == "N":
        break
lista.sort()
print(lista)