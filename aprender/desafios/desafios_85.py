
lista = [[],[],[]]
p_t = 7

print("-"*60)
for c in range(0,p_t):
    n = (int(input('Digite um valor: ')))
    lista[0].append(n)

    if n % 2 == 0:
        lista[1].append(n)
    else:
        lista[2].append(n)
print("-"*60)

print("lista")
for c in range(0,p_t):
    print(f"{lista[0][c]}", end = ", ")

if lista[1] != []:
    print("\n"+"lista dos pares")
    for c in range(0,len(lista[1])):
        print(f"{lista[1][c]}", end = ", ")

if lista[2] != []:
    print("\n"+"lista dos inpares")
    for c in range(0,len(lista[2])):
        print(f"{lista[2][c]}", end = ", ")

print("\n"+"-"*60)
