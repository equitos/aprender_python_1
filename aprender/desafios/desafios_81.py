
lista = []

print("-"*60)
while True:
    lista.append(int(input("digite um numero: ")))
    perguta = input("quer continuar? [S/N] ").strip().upper()

    if perguta == "N":
        break
print("-"*60)

print(lista)
print(f"a lista tem {len(lista)} elementos")
lista.sort(reverse=True)
print(lista)
print(f"se a lista tem numero 5 em seus elemento?, {5 in lista}")
print("-"*60)