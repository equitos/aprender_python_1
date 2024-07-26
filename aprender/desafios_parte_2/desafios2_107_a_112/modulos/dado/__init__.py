def dado_é_numero(numero):
    numero = str(numero)
    n = numero.replace(",", "").replace(".", "").strip()
    a = True

    for i in n:
        try:
            int(i)
        except ValueError:
            a = False
            break
    return a


def dado_monetario(msg):
    #from desafios_parte_2.desafios2_107_a_112.modulos.numeros import linha, moeda_resumo

    linha(50)
    while True:
        n = input(f"{msg} ").replace(',', '.').strip()
        taxa1 = input("coloque a taxa de aumento ").replace(',', '.').strip()
        taxa2 = input("coloque a taxa de diminuição ").replace(',', '.').strip()
        tudo = taxa1 + taxa2 + n

        if dado_é_numero(tudo):
            n = float(n)
            taxa1 = float(taxa1)
            taxa2 = float(taxa2)

            moeda_resumo(n, taxa1, taxa2)
            break
        else:
            print("\033[31mERRO, tente novemente!\033[m")


