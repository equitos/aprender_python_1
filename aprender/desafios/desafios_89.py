lista = []

n = 0

print('-'*30)
while True:
    lista.append([input('Nome: ')])
    lista[n].append(int(input("primeira nota ")))
    lista[n].append(int(input("segunda nota ")))
    lista[n].append((lista[n][1]+lista[n][2])/2)

    pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()
    n += 1

    if pergunta == "N":
        break
print('-'*30)
print(f"nome    / media")
for i in lista:
    print(f'{i[0]:^7} : {i[3]}')
print('-'*30)
while True:
    ver = int(input("coloque o njumero do aluno  pra ver as notas, se não quiser digite 999 "))
    if ver <= len(lista):
        print(f'Notas de {lista[ver][0]}')
        print(f"n1 = {lista[ver][1]}")
        print(f"n2 = {lista[ver][2]}")
        print('-'*30)
    elif ver == 999:
        break