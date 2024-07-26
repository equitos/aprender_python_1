n = 0

soma = maior = menor = media = 0

repetisoes = 0
continuar = 0

while continuar != 1:
    repetisoes += 1
    n = int(input("digite um valor "))

    if n > maior:
        maior = n
    if n < menor:
        menor = n

    if repetisoes % 5 == 0:
        print("""você quer continuar?
[1] não
[2] sim""")
        continuar = int(input(""))

    soma += n


media = soma // repetisoes

print("a media é {}, o maior é {}, o menor é {}".format(media, maior, menor))