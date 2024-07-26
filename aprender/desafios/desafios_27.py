
nome = input('Qual o seu nome completo? ')

nome = nome.split()

print(nome)
print("primeiro nome é ({}) e o utimo é ({})".format(nome[0],nome[len(nome)-1]))
