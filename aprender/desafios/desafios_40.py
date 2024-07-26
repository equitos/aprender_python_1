print("escreva duas notas de um aluno")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media < 5:
    resposta = "\033[31mreprovado burro\033[m"
elif media >= 5 and media < 6.9:
    resposta = "\033[34mrecuperação\033[m"
else:
    resposta = "\033[32maprovado\033[m"

print(resposta)