from random import shuffle

n1 = input("nome um")
n2 = input("nome dos")
n3 = input("nome tres")
n4 = input("nome quatro")

lista = [n1,n2,n3,n4]
shuffle(lista)
print(lista)