from modulos.conta_corrente import contaCorrent

def linha():
    print('-'*40)


while True:
    try:
        linha()
        n_conta = int(input("numero da conta "))
        nome_corretista = input("nome do corretista ")
        saldo = float(input("saldo da conta "))
    except ValueError:
        print("\033[31mERRO, tente novamente!\033[m")
        linha()
    else:
        break

conta = contaCorrent(n_conta, nome_corretista, saldo)

while True:
    try:
        linha()
        if input("deseja deposita na sua conta? [S/N] ") in "Ss":
            conta.depositar(int(input("valor a ser depositado ")))
        elif input("desaja sacar da sua conta? [S/N] ") in "Ss":
            conta.sacar(int(input("valor a ser sacado ")))
        else:
            break
    except:
        print("\033[31mERRO, tente novamente!\033[m")

linha()
print(f"conta numero = {conta.numero_conta}")
print(f"nome do coretista = {conta.nome_corretista}")
print(f"saldo = {conta.saldo}")
linha()