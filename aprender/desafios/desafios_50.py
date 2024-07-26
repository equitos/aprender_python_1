ns = []

for i in range(0,6):
    n1 = int(input('Digite um valor de n{}: '.format(i+1)))
    ns.append(n1)

soma = 0

for c in range(0,6):
    if ns[c] % 2 == 0:
        soma += ns[c]
        print("valores pares {}".format(ns[c]))

print("a soma deles vai dar \033[31m{}".format(soma))