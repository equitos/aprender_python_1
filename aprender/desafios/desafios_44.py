
preso = float(input("preso do produto"))
print("metodos de compra : à vista, à vista no cartão, 2x no cartão, 3x no cartão")
met = input("metodo de compra ")
met = met.strip()

if met == "à vista":
    preso2 = preso * 0.9
    desconto = "teve 10% de desconto"
    set_cor = "\033[32m"
elif met == "à vista no cartão":
    preso2 = preso * 0.95
    desconto = "teve 5% de desconto"
    set_cor = "\033[32m"
elif met == "2x no cartão":
    preso2 = preso
    desconto = "sem desconto"
    set_cor = "\033[34m"
else:
    preso2 = preso * 1.2
    desconto = "teve 20% de juros"
    set_cor = "\033[31m"

print("o produto de R$\033[34m{}\033[m {}{}\033[m, com o metado de pagamento {}{}\033[m, o produto custara R${}{}\033[m"
      .format(preso, set_cor, desconto,set_cor, met,set_cor,preso2))