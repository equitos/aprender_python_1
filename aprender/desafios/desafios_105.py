def avaliar_notas(*n, sit=False):
    """
    --> função que recebe uma variavel composta n e faz as sequintes operações
    total de notas dadas
    menor nota
    maior nota
    media das notas

    --> sit é uma variavel que se estiver True vai dizer se a situação esta boa ou ruim
    --> sit é uma variavel que se estiver False faz nada
    """
    dic = {"total de notas passadas é": len(n),}
    dic["maior"] = max(n)
    dic["menor"] = min(n)
    dic["media"] = sum(n)/len(n)
    if sit == True:
        if dic["media"] >= 6:
            dic["situação"] = "tranquilo"
        else:
            dic["situação"] = "ruim"

    return dic

a = avaliar_notas(100.5, 4.5, 3.5, 2.5, 1.5,sit=True)
print(a)
help(avaliar_notas)
