n1 = int(input("digite um valor "))
n = 0

for c in range(1,abs(n1)+1):
    if abs(n1) % c == 0:
        n += 1
if n >= 3 and n != 1:
    print("{} não é um valor primo e pode ser dividido por {} numeros diferentes".format(n1, n))
else:
    print("{} é um valor primo".format(n1))
