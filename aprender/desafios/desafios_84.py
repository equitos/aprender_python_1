lista = []
dado = []

print('-'*60)
while True:
    dado.append(input('Nome: '))
    dado.append(float(input('peso: ')))
    lista.append(dado[:])
    dado.clear()

    pergunta = input('Quer continuar? [S/N] ')

    if pergunta in 'Nn':
        break
print('-'*60)

p_maior = max(sub_lista[1] for sub_lista in lista)
p_menor = min(sub_lista[1] for sub_lista in lista)

print(f"a(s) pessoas(s) com o(s) \033[31mmaior peso(s) de {p_maior} kg\033[m é de ", end = "")
for i, p in enumerate(lista):
    if p[1] == p_maior:
        print(f"{p[0]}", end = ", ")

print("\n" + f"a(s) pessoas(s) com o(s) \033[34mmenor peso(s) de {p_menor} kg\033[m é de ", end = "")
for i, p in enumerate(lista):
    if p[1] == p_menor:
        print(f"{p[0]}", end = ", ")
print("\n" + '-'*60)