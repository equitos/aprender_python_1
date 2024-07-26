sexo = " "

while sexo != "M" and sexo != "F":
    sexo = input("Informe seu sexo [M/F]: ")
    sexo = sexo.strip().upper()
    if sexo != "M" and sexo != "F":
        print("repita o questionario")

print("Fim do programa")
