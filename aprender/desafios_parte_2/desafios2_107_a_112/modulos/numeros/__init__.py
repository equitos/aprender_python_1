def linha(n=40,sinbolo="-"):
    print(f'{sinbolo}'*n)

def metade(n,redondo=True):
    """

    :param n: numero a ser dividido
    :param redondo: se é ou nao para redondar esse numero
    :return: n dividido pela metade
    """
    if redondo == True:
        n = n//2
    else:
        n = n/2
    return n


def dobro(n):
    """

    :param n: dobra n
    :return: n dobrado
    """
    return n*2


def aumento(n,aumento_porcentagem):
    """

    :param n: numero a ser aumentado
    :param aumento_porcentagem: aumento em porcentagem
    :return: n aumentado em porcentagem
    """
    return n + (n*(aumento_porcentagem/100))


def diminuir(n,diminuir_porcentagem):
    """

    :param n: numero a ser diminuido
    :param diminuir_porcentagem: diminui uma porcentagem
    :return: n diminado em porcentagem
    """
    return n - (n*(diminuir_porcentagem/100))


def moeda(n,formatado = True, moeda='R$'):
    if formatado == True:
        return f'{moeda}{n:.2f}'.replace('.', ',')
    else:
        return f'{n:.2f}'.replace(".", ",")

def moeda_resumo(n,taxa1, taxa2):
    linha(50)
    print(f"metade de {moeda(n)} é {moeda(metade(n, False))}")
    print(f"o dobro de {moeda(n)} é {moeda(dobro(n))}")
    print(f"um aumento de {taxa1}% em {moeda(n)} é {moeda(aumento(n, taxa1))}")
    print(f"um diminuição de {taxa2}% em {moeda(n)} é {moeda(diminuir(n, taxa2))}")
    linha(50)
