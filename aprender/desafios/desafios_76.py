tupla = ()

while True:
    tupla += ((input("produto ")),)
    tupla += ((float(input("preso "))),)
    continuar = input("Deseja continuar? [S/N] ").upper().strip()
    if continuar == 'N':
        break

print("-"*60)

for i in range(0, len(tupla)):
    if i % 2 == 0:
        print(f"produto: {tupla[i]:-<20}", end = "")
    else:
        print(f" R$ {tupla[i]:>5.2f}")

print("-"*60)