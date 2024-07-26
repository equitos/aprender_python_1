def contador(inicial, final, passos):
    from time import sleep

    i = inicial
    f = final

    if i > f:
        if passos > 0:
            i = final
            f = inicial
        if passos == 0:
            passos = -1

    else:
        if passos < 0:
            passos = -passos
        if passos == 0:
            passos = 1


    if passos > 0:
        while i <= f:
            print(i, end=' ')
            i += passos
            #sleep(0.5)
        if f != i-passos:
            print(f, end=" ")
    else:
        while i >= f:
            print(i, end=' ')
            i += passos
            #sleep(0.5)
        if f != i-passos:
            print(f, end=" ")

    print('FIM')


print("-"*60)
contador(1, 10, 1)
print("-"*60)
contador(10, 0, -2)
print("-"*60)
contador(10,-10,-10)
print("-"*60)
contador(10, 0, 0)
print("-"*60)
i = int(input('Inicial: '))
f = int(input('Final: '))
p = int(input('Passos: '))
print('-'*60)
contador(i,f,p)
print("-"*60)