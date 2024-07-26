from modulos.tv import tv
def linha():
    print('-'*40)

linha()
nome = input('Nome: ')

while True:
    try:
        volume = int(input('Volume: '))
        canais = int(input('Canais: '))
    except:
        linha()
        print("\033[31mERRO, tente novamente!\033[m")
        linha()
    else:
        break

tv = tv(nome, volume, canais)

while True:
    try:
        linha()

        if input('Quer aumentar o volume? [S/N] ') in 'Ss':
            aumento = int(input('aumentar volume: '))
            tv.aumenta_volume(aumento)
        elif input("quer diminuir o volume? [S/N] ") in 'Ss':
            diminuir = int(input('diminuir volume: '))
            tv.diminuir_volume(diminuir)
        else:
            break
    except:
        print("\033[31mERRO, tente novamente!\033[m")

linha()
print(f'usuario da tv é {tv.nome}')
print(f"volume é {tv.volume}")
print(f"quantidade de canais é de {tv.canais}")
linha()

