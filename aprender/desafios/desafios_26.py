frase = input('Digite uma frase: ')

frase = frase.strip()

print("sua frase tem (a), {}".format(frase.count('a')))
print("o lugar da primeira letra (a) é {} e a utima é {} ".format(frase.find('a')+1,frase.rfind('a')+1))