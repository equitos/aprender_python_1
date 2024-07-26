
palavra = input('Digite uma palavra: ')

palavra = palavra.strip().lower()
palavra1 = palavra.split()
palavra1 = "".join(palavra1)

n1 = len(palavra1)-1
n = 0

for c in range(0, n1):
    if palavra1[c] == palavra1[n1-c]:
        n += 1

if n == n1:
    print("a palavra \033[34m{}\033[m é um \033[32mpalimedromo".format(palavra))
else:
    print("a palavra \033[34m{}\033[m nao é um \033[31mpalimedromo".format(palavra))