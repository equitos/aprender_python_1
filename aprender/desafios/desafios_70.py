total_gasto = produto_mais_mil = produto_mais_barato = preso_do_produto_mais_barato = 0

print('-'*60)
print("loja do Hiago")

while True:
    print('-'*60)
    produto = input('Qual o nome do produto: ').strip().upper()
    preso_produto = float(input("valor do produto: "))
    print('-'*60)

    total_gasto += preso_produto

    if preso_produto > 1000:
        produto_mais_mil += 1
    if preso_produto > preso_do_produto_mais_barato:
        produto_mais_barato = produto

    pergunta = input('você quer continuar? [S/N] ').strip().upper()

    if pergunta == 'N':
        print('-'*60)
        break

print(f"tem {produto_mais_mil} produtos mais de mil")
print(f"o produto mai barato é {produto_mais_barato}")
print(f"o total gasto é de {total_gasto}")
print('-'*60)