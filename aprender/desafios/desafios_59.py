
n1 = ""
n2 = ""
r = ""
while r != 5:
    n1 = int(input('valor 1: '))
    n2 = int(input('valor 2: '))

    print("""
    [1] soma
    [2] mutiplicar
    [3] maior numero
    [4] novos numeros
    [5] sair do progama
    """)
    r = int(input(''))
    if r == 1:
        soma = n1 + n2
        print("a soma entre {} e {} vale {}".format(n1, n2, soma))
    elif r == 2:
        mult = n1 * n2
        print("a mutiplicação entre {} e {} vale {}".format(n1, n2, mult))
    elif r == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("o maio é {}".format(maior))



