lista = []

for i in range(0, 5):
    n = int(input('Digite um valor: '))

    if len(lista) == 0:
            lista.append(n)
    else:
        for c, a in enumerate(lista):
            if n < a:
                lista.insert(c, n)
                break
            elif c == len(lista)-1:
                lista.append(n)
                break

print(lista)