print("caucolo de IMC")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    resutado = "Abaixo do peso"
elif imc >= 18.5 and imc < 25:
    resutado = "peso ideal"
elif imc >= 25 and imc < 30:
    resutado = "sobre peso"
elif imc >= 30 and imc < 40:
    resutado = "obesidade"
else:
    resutado = "obesidade mórbida"

if resutado == "Abaixo do peso" or resutado == "sobre peso":
    set_cor = "\033[34m"
elif resutado == "peso ideal":
    set_cor = "\033[32m"
else:
    set_cor = "\033[31m"

print("seu IMC esta {}{}".format(set_cor, resutado))