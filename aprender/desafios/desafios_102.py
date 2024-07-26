def fatorial(numero, show=False):
    """
    --> essa função faz o vatorial da variavel (numero)
    numero = numero a ser fatorado

    --> show é uma variavel que diz se é ou não pra mostrar como esse (numero) foi fatorado
    show = True ou False

    exemplo do show = True e False
    --> fatorial(5, show=True)
    5 x 4 x 3 x 2 x 1 = 120
    --> fatorial(5, show=False)
    120

    --> show = True
    return = str

    --> show = False
    return = int
    """

    f = 1
    proceso = ""

    for i in range(numero, 0, -1):
        f *= i
        if show == True:
            if i > 1:
                print(f"{i} x", end=" ")
            else:
                print(f"{i} = {f}")

    return f


print(fatorial(5, True))
