lista = []
pares_mais = soma_coluna_3 = 0
for c in range(0,3):
    lista.append([])

for l in range(0,3):
    for c in range(0,3):
        lista[l].append(int(input(f"valor da [{c}][{l}]")))

print("-"*60)
print(lista)
print("-"*60)

for l in range(0,3):
    print(" coluna    ", end="")
print()
for l in range(0,3):
    for c in range(0,3):
        print(f" [ {lista[l][c]:^5} ]", end = " ")
    print(" linha")

print("-"*60)

for c in range(0,3):
    for l in range(0,3):
        if lista[c][l] % 2 == 0:
            pares_mais += lista[c][l]
    soma_coluna_3 += lista[c][2]
maior = max(v for v in lista[1])
print(f"todos os pares somados é {pares_mais}")
print(f"soma da coluna tres é {soma_coluna_3}")
print(f"maior valor da segunda linha é {maior}")
print("-"*60)