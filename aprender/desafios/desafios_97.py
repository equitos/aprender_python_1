def escreva(texto):
    texto = str(texto)
    n = len(texto)+2
    print('-' * n)
    print(f"{texto:^{n}}")
    print('-' * n)


escreva(input(''))