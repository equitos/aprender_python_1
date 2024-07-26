a = []

print("-"*60)
for i in range(0, 5):
    a.append(int(input("Digite um valor: ")))

maior = max(a)
menor = min(a)

print("-"*60)

print(f"O maior valor digitado foi {maior} nas posiçoes ", end= "")

for c, v in enumerate(a):
    if maior == v:
        print(f"{c+1}...", end = "")

print("\n" + "-"*60)

print(f"O menor valor digitado foi {menor} nas posiçoes ", end = "")

for c, v in enumerate(a):
    if menor == v:
        print(f"{c+1}...", end = "")

print("\n" + "-"*60)

