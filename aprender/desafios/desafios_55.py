pesos = []
maior = 0
menor = 10000

for c in range(0, 5):
    peso = float(input("qual é seu pesso em kg "))
    pesos.append([peso , "kg"])

    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print("entre esses {} pesos".format(pesos))
print("o maior peso foi {} kg".format(maior))
print("o menor peso foi {} kg".format(menor))
