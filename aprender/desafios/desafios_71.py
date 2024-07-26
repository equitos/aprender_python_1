notas_50 = notas_20 = notas_10 = notas_1 = 0

while True:
    print("-"*60)
    saque = int(input('Digite o valor aser sacado em reais: '))
    saque1 = saque
    while True:
        if saque >= 50:
            saque -= 50
            notas_50 += 1
        else:
            break
    while True:
        if saque >= 20:
            saque -= 20
            notas_20 += 1
        else:
            break
    while True:
        if saque >= 10:
            saque -= 10
            notas_10 += 1
        else:
            break
    while True:
        if saque >= 1:
            saque -= 1
            notas_1 += 1
        else:
            break
    print("-"*60)

    print(f"Valor a ser sacado: {saque1}")
    print(f"notas de R$ 50 : {notas_50}")
    print(f"notas de R$ 20 : {notas_20}")
    print(f"notas de R$ 10 : {notas_10}")
    print(f"notas de R$ 1 : {notas_1}")
    print("-"*60)

    pergunta = input('Quer continuar? [S/N] ').upper().strip()[0]

    if pergunta == 'N':
        print("-"*60)
        break
