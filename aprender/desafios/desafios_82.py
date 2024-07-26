lista = []
lista_p = []
lista_i = []

print("-"*60)
while True:
    lista.append(int(input('Digite um valor: ')))
    pergunta = input('Deseja continuar? [S/N] ').strip().upper()

    if pergunta == 'N':
        break
for i, c in enumerate(lista):
    if c % 2 == 0:
        lista_p.append(c)
    else:
        lista_i.append(c)
print("-"*60)

print(lista)
print(lista_i)
print(lista_p)

print("-"*60)