mulher_menos_20 = homen = pessoas_maior_18 = 0

print("-"*60)
print("cadrasta pessoas")

while True:
    print("-"*60)
    idade = int(input('idade: '))
    sexo = input('sexo [M/F]: ').strip().upper()
    print('-'*60)

    if sexo == "M":
        homen += 1
    if idade > 18:
        pessoas_maior_18 += 1
    if sexo == "F":
        if idade < 20:
            mulher_menos_20 += 1
    pergunta = input('Quer continuar? [S/N] ').strip().upper()
    if pergunta == "N":
        print("-"*60)
        break

print(f"tem {pessoas_maior_18} pessoa maiores de idade")
print(f"tem {homen} homens")
print(f"tem {mulher_menos_20} mulheres menor de 20 anos")
print("-"*60)

