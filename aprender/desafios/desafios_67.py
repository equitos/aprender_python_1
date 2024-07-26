
while True:
    n = int(input("quer ver a tabuada de qual valor "))
    print("-"*50)
    if n < 0:
        break
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
    print("-"*50)