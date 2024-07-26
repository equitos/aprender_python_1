from modulos.macaco import macaco
from modulos.comidas import comida

def linha():
    print("-"*60)


lista_macaco = []

while True:
    for i in range(0, 2):
        try:
            linha()
            nome = input(f"Nome do macaco {i+1}: ")
            bucho = int(input(f"Bucho do macaco {i+1}: "))

            lista_macaco.append(macaco(nome, bucho))
        except:
            print("\033[31mERRO, tente novamente!\033[m")
            exit()
    break

linha()

for i in range(0, len(lista_macaco)):
    print(f"nome do macaco {i+1} = {lista_macaco[i].nome}")
    print(f"bucho do macaco {i+1} = {lista_macaco[i].estomago}")
    linha()

print(f"se o macaco {1} comer o macaco {2}")
lista_macaco[0].comer(lista_macaco[1])
print(f"o estomago do macaco {1} = {lista_macaco[0].estomago}")
banana = comida(100)
lista_macaco[1].comer(banana)
print(f"o macaco {2} comendo banana = {lista_macaco[1].estomago}")