salario = float(input("qual é seu salario? "))

if salario > 1250:
    salario = salario*1.1
else:
    salario = salario*1.15

print("seu novo salario é {}{:.2f}{} reais".format("\033[4;33m", salario, "\033[m"))