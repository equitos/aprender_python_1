
print('-'*60)
print("teste de parênteses ")
equacao = str(input(""))
teste = 0

for i in range(0,len(equacao)):
   if equacao[i] == "(":
       teste += 1
   elif equacao[i] == ")":
       teste -= 1

if teste != 0:
    print("parênteses estao errados")
else:
    print("parênteses estao ok")
print('-'*60)