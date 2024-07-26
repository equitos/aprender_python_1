from random import randint

n1 = randint(0,10)
print("o pc pensou em um numero entre 0 e 10")
print("tente adivinhar")
r = ""
palpite = 0

while n1 != r:
    r = int(input("de um palpite de qual numero é "))
    palpite += 1
    if n1 != r:
        print("errou")
        print("tente novamente")

print("você presisou de {} palpites para acerta o numero {}".format(palpite,n1))