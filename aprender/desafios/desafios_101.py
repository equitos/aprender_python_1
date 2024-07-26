def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f"com {idade} anos o voto é proibido"
    elif idade < 18 and idade >= 16 or idade > 65:
        return f"com {idade} anos o voto é opicional"
    else:
        return f"com {idade} anos o voto é obrigatorio"

print("-"*60)
n = int(input("Digite o ano de nascimento: "))
print(voto(n))
print("-"*60)