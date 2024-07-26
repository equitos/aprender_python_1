from math import sqrt

cateto_opo = float(input('Digite o valor do cateto oposto: '))
cateto_adj = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = sqrt(cateto_opo**2 + cateto_adj**2)

print("hipotenusa é de {}".format(hipotenusa))