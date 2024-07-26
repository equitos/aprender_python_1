n1 = int(input('Digite um valor maximo de fibonat: '))
n = [1]
for c in range(0, n1):
    n.append(n[c] + n[c-1])
print(n)