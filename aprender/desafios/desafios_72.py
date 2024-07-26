nome_numeros = (
"zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito",
"nove", "dez", "onze", "doze", "treze", "quatorze", "quinze",'dezesseis',
"dezessete", "dezoito",'dezenove', "vinte"
)

pergunta = int(input("digite um valor enrtre 0 e 20 "))
while True:
    if pergunta < 0 or pergunta > 20:
        pergunta = int(input("tente novamente, digite um valor entre 0 e 20 "))
    else:
        break
print(nome_numeros[pergunta])

