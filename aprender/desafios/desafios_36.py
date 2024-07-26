cores = {'limpa': '\033[m', "vermelho": "\033[31m", "verde": "\033[32m", "amarelo": "\033[33m"}

print("emprestimo do mec love")

val_casa = float(input("Digite o valor da casa: R$"))
salario = float(input("seu salario: R$"))
anos = int(input("Quantos anos de financiamento? "))

prestacao = val_casa / (anos * 12)

if prestacao > (salario * 0.3):
    resposta = "negado, vai mora na rua, pobre"
    set_cor = cores["vermelho"]
else:
    resposta = "aprovado"
    set_cor = cores["verde"]

print("valor mensal vai ser de R${}{:.2f}{} ".format(cores["amarelo"], prestacao, cores["limpa"]))
print("seu emprestimo foi {}{}{}".format(set_cor, resposta, cores["limpa"]))
