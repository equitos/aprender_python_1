nome = []
idade = []
sexo = []

h_mais_idade = 0
nome_mais_idade = 0

mulher_menor_20 = 0

for c in range(0,4):
    nome.append(input('Digite o seu nome: '))
    idade.append(int(input('Digite sua idade: ')))
    sexo.append(input('Digit o seu sexo [m/f]: '))

for c in range(0,4):

    if idade[c] > h_mais_idade and sexo[c] == 'm':
            h_mais_idade = idade[c]
            nome_mais_idade = nome[c]
    if sexo[c] == 'f' and idade[c] < 20:
        mulher_menor_20 += 1
media_idade = sum(idade)/len(nome)

print("o homen mais velho é {} com {} anos".format(nome_mais_idade,h_mais_idade))
print("tem {} meninas menor de idade".format(mulher_menor_20))
print("a media de idade do grupo é {}".format(media_idade//1))
