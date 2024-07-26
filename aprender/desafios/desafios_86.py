
lista = []
c = 3
l = 3

#c colunas
#l linhas

print("-"*60)
for i in range(0, c):
    lista.append([])

for i in range(0, c):
    for j in range(0, l):
        lista[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))

print("-"*60)
for i in range(0, c):
    for j in range(0, l):
        if j != l-1:
            print(f"[ {lista[i][j]:^3} ]", end=' ')
        else:
            print(f"[ {lista[i][j]:^3} ]")
print("-"*60)