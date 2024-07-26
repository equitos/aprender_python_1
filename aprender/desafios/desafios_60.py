n1 = int(input("digite um numero que deseja fazer fatorial: "))
n2 = 1

for c in range(1,n1):
    n2 += n2 * (n1-c)
print(n2)
print("/////////////////")
n2 = 1
c = (
    n1)
while c != 1:
    c -= 1
    n2 += n2 * (n1-c)
print("{}! = {}".format(n1, n2))