n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite o segundo termo: '))
diferenca = abs(n1 - n2)
c = r = 10
while r != 1:
    print(diferenca*c)
    c += 1
    if c % 5 == 0:
        print("""
        [1] parar
        [2] continuar
        """)
        r = int(input(''))
print('FIM')