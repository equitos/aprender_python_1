
n1 = int(input('Digite um valor intero: '))

print(''' Escolha uma das basses para comversã0:
[ 1 ] binario
[ 2 ] octal
[ 3 ] hexadecimal''')

pedido = int(input('Digite o que você que: '))

if pedido == 1:
    print(" {} para binario é {}".format(n1, bin(n1)))
elif pedido == 2:
    print(" {} para octal é {}".format(n1, oct(n1)))
elif pedido == 3:
    print(" {} para hexadecimal {}".format(n1, hex(n1)))
else:
    print("você é retardado?")