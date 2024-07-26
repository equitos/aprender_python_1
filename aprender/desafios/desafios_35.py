cores = {"limpa": "\033[m", "amarelo": "\033[33m", "vermelho": "\033[31m", "verde": "\033[32m"}

r1 = float(input("tamanho da primeira reta "))
r2 = float(input("tamanho da segunda reta "))
r3 = float(input("tamanho da terceira reta "))

rmaior = r1

if r2 > rmaior and r2 > r3:
    rmaior = r2
if r3 > rmaior and r3 > r2:
    rmaior = r3

posivel = r1 + r2 + r3 - rmaior * 2

if posivel >= 0:
    posivel = "posivel"
    set_cores = cores["verde"]
else:
    posivel = "inposivel"
    set_cores = cores["vermelho"]

print('um triangulo entre as retas {}{}{} / {}{}{} / {}{}{} é {}{}{}'.format(cores["amarelo"], r1, cores["limpa"],
                                                                             cores["amarelo"], r2, cores["limpa"],
                                                                             cores["amarelo"], r1, cores["limpa"],
                                                                             set_cores, posivel, cores["limpa"]))
