n1 = int(input("numero entre 0 e 9999 "))

u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10

print("analisando o numero {}".format(n1))
print("unidade {}".format(u))
print("dezena {}".format(d))
print("centena {}".format(c))
print("milhara {}".format(m))
