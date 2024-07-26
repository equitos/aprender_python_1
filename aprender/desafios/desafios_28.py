from random import randint

print("o mano pc pensou em um numero entre 1 e 10, qual vc acha que é?")

r = randint(1, 10)
n1 = int(input("Digite o numero que voce acha que é o certo "))

print("vamos ver se voce acertou")

if n1 == r :
    print("o numero do pc é {} e o seu é {}, parabem".format(r,r))
else :
    print("o numero do pc é {} e o seu é {}, errou macaco".format(r,n1))
