from random import randint

n = 1
lista = []
print("-"*60)
print(f"{"PALPITES DA MEGA":^60}")
print(f"{"Quantos palpites você quer?":^60}")
n_sorte = int(input(f"{"":<29}"))
print("-"*60)
for c in range(0,6):
    for x in range(0,10):
        print(f"{n:^4}", end=" ")
        n += 1
    print()
print("-"*60)

for i in range(0,n_sorte):
    for c in range(0,6):
        while True:
            n1 = randint(1,60)
            if n1 not in lista:
                lista.append(n1)
                break
        lista.sort()
    for i in range(0,6):
        print(f"{lista[i]:^4}", end=" ")
    lista.clear()
    print()
    print("-=-"*10)


