import math

angulo = float(input("angulo "))

seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print("seno = {:.2f} / coseno = {:.2f} / tangente = {:.2f} ".format(seno, coseno, tangente))
