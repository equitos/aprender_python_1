print("digite 999 para finalisar o progama")
resutado = 0
n = 0

while n != 999:
    n = int(input("digite um valor"))
    if n != 999:
        resutado += n

print(resutado)