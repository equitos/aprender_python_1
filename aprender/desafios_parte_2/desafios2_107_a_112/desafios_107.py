import modulos.numeros as numeros

print("-"*40)
n = int(input("coloque um numero inteiro: "))
p = int(input("coloque um porcentagem inteira: "))

print("-"*40)

print(f"o dobrado de {n} é {numeros.dobro(n)}")
print(f"a metade redonda de {n} é {numeros.metade(n)}")
print(f"a metade não redonda de {n} é {numeros.metade(n, False)}")
print(f"um aumento de {p}% em {n} é {numeros.aumento(n, p)}")
print(f"um diminuição de {p}% em {n} é {numeros.diminuir(n, p)}")
print("-"*40)