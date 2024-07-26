import modulos.numeros as modulo_numeros

print("-"*40)
n = int(input("coloque um valor monetario: "))
p = int(input("coloque um porcentagem inteira: "))

print("-"*40)

print(f"o dobrado de {modulo_numeros.moeda(n)} é {modulo_numeros.moeda(modulo_numeros.dobro(n))}")
print(f"a metade redonda de {modulo_numeros.moeda(n)} é {modulo_numeros.moeda(modulo_numeros.metade(n))}")
print(f"um aumento de {p}% em {modulo_numeros.moeda(n)} é {modulo_numeros.moeda(modulo_numeros.aumento(n, p))}")
print(f"um diminuição de {p}% em {modulo_numeros.moeda(n)} é {modulo_numeros.moeda(modulo_numeros.diminuir(n, p))}")
print("-"*40)