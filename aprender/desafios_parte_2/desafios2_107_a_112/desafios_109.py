from modulos.numeros import *

linha()
n = float(input("numero "))
taxa = float(input("taxa "))
form = input("formatado [S/N]")

if form in "nN":
    form = False
else:
    form = True

linha()
print(f"metade de {moeda(n, form)} é {moeda(metade(n, False), form)}")
print(f"o dobro de {moeda(n, form)} é {moeda(dobro(n), form)}")
print(f"um aumento de {taxa}% em {moeda(n, form)} é {moeda(aumento(n, taxa), form)}")
print(f"um diminuição de {taxa}% em {moeda(n, form)} é {moeda(diminuir(n, taxa), form)}")
linha()