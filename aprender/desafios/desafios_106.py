def l__(msg,cor_fundo):
    t = len(msg)+4
    print(f'{cor_fundo}~'*t)
    print(f"  {msg}")
    print('~'*t)
    print("\033[m")
def pyhelp():
    pergunta = " "
    while pergunta not in "fim,FIM,Fim":
        l__("pyhelp",cores["verde"])
        pergunta = input("").strip()

        l__(pergunta,cores["azul"])
        if pergunta not in "fim,FIM,Fim":
            print(cores["branco"])
            help(pergunta)
            print(cores["limpa"])


cores = {"limpa":"\033[m","vermelho":"\033[41m", "azul":"\033[44m", "verde":"\033[42m", "branco":"\033[7;40m"}
pyhelp()

