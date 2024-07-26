limpa = "\033[m"
sublinha = "\033[4m"
cores = {"verde": "\033[32m", "vermelho": "\033[31m"}

n1 = int(input("numero intero "))
n2 = int(input("numero intero "))
n3 = int(input("numero intero "))

nt = n1,n2,n3

maior = n1
menor = n1

if n2 >= n1 and n2 >= n3:
    maior = n2
if n3 >= n1 and n3 >= n2:
    maior = n3

if n2 <= n1 and n2 <= n3:
    menor = n2
if n3 <= n1 and n3 <= n2:
    menor = n3

print("entre {}{}{}".format(sublinha, nt, limpa))
print("o maior é {}{}{}".format(cores["verde"], maior, limpa))
print("o menor é {}{}{}".format(cores["vermelho"], menor, limpa))