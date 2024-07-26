def maior(lista):
    print(max(i for i in lista))


from random import randint

lista = []

for i in range(0,10):
    lista.append(randint(1,100))

print(lista)
maior(lista)