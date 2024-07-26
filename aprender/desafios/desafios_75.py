
tupla = tupla_pares = ()
valor_nove = casa = 0

for i in range(0,4):

    tupla = tupla + ((int(input('Digite um valor: '))),)

    if tupla[i] == 9:
        valor_nove += 1
for i in range(0,4):
    if tupla[i] == 3:
        casa = i
        break
for i in range(0,4):
    if tupla[i] % 2 == 0:
        tupla_pares = tupla_pares + ((tupla[i]),)

print(tupla)
print(f"tem {valor_nove} nove")
print(f"primeiro 3 é na casa {casa+1}")
print(f"os pares foram {tupla_pares}")


