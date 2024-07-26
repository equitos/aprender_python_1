colocados = (
"Palmeiras", "Cruzeiro", "Grêmio", "santos", "Atlético Mineiro", "Corinthians",
"Flamengo", "Botafogo", "Atlético Paranaense", "Internacional", "São Paulo",
"Fluminense", "Vasco da Gama", "Chapecoense", "Sport", "Ponte Preta", "Coritiba",
"Vitória", "Figueirense", "Atlético Goianiense")

print("-"*60)

for c in range(0,5):
    print(colocados[c])
print("-"*60)

for c in range(1,5):
    print(colocados[-c])
print("-"*60)

alva_colocados = sorted(colocados)

for c in range(len(colocados)-1):
    print(alva_colocados[c])

print("-"*60)
for c, a in enumerate(colocados):
    if a == "Chapecoense":
        print(f"Chapecoense esta na posição {c+1}")
print("-"*60)