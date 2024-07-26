from random import randint

tumpa = ()
maior = 0
menor = float("inf")

for c in range(0,5):
    tumpa = tumpa + (randint(0,10),)
    if tumpa[c] > maior :
        maior = tumpa[c]
    if tumpa[c] < menor:
        menor = tumpa[c]
print(tumpa)
print(maior)
print(menor)