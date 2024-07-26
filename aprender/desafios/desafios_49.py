print("TABUADA")
n1 = int(input('numero base '))
n2 = int(input('maximo de numeros mutiplicadores '))
a = 0

for c in range(0,n2+1):
    a = n1 * c
    print("\033[35m{}\033[m x \033[35m{}\033[m = \033[35m{}".format(n1, c, a))