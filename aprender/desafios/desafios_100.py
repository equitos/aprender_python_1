def sorteio(tamanho,lista):
    from random import randint

    for i in range(tamanho):
        lista.append(randint(1, 100))

def soma_par(lista):
    soma = 0

    print("-"*60)
    for i in lista:
        if i%2 == 0:
            print(i, end = " ")
            soma += i
    print()
    print(f"soma dos pares é {soma}")
    print("-"*60)


lista = []
sorteio(10, lista)

print(lista)
soma_par(lista)

