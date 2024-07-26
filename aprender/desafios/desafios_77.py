tupla = vogal_usada = ()
vogais = ["A","E", "I", "O", "U"]
print("-"*60)
while True:
    tupla += ((input('Digite um nome: ').strip().upper()),)
    resposta = input('Deseja continuar? [S/N] ').upper().strip()
    if resposta == "N":
        break
print("-"*60)

for c in range(0, len(tupla)):
    for i in range(0, len(tupla[c])):
        if tupla[c][i] in vogais:
            vogal_usada += ((tupla[c][i]),)
    print(f"{tupla[c]}: {vogal_usada}")
    vogal_usada = ()
print("-"*60)
print("/"*60)
print("-"*60)
for p in tupla:
    print(f"\nna palavra {p} temos ", end = "")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end = " ")

print("\n")
print("-"*60)