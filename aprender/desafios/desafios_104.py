def input_numero(msg):
    while True:
        a = input(msg).strip()

        if a.isnumeric():
            a = int(a)

        if type(a) != int:
            print("\033[31mERRO! esse valor nao é um numero intero!\033[m ")
        else:
            return a
            break


a = input_numero("digite um numero ")
print(a)
