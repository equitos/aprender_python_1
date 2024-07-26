def linha():
    print("-"*60)


while True:
    try:
        linha()
        n_int = int(input("digite um numero intero "))
    except KeyboardInterrupt:
        n_int = 0
        print("\n"+"ERRO, você saiu do progama")
        break
    except (ValueError, TypeError):
        print("você é burro? escreve certo carai")
    except Exception as erro:
        print(f"\033[31mERRO {erro.__class__}\033[m")
    else:
        break

while True:
    try:
        linha()
        n_real = float(input("coloque um valor real "))
    except KeyboardInterrupt:
        n_real = 0
        print("\n"+"ERRO, você saiu do progama")
        break
    except (ValueError, TypeError):
        print("você é burro? escreve certo carai")
    except Exception as erro:
        print(f"\033[31mERRO {erro.__class__}\033[m")
    else:
        print("ai esta os resutados")
        break

linha()
print(f"valor intero {n_int}")
print(f"valor real {n_real}")
linha()