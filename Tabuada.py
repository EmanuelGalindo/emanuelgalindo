import sys

num = int(input("Informe um número maior que zero: "))
if num <= 0:
    print("")
    print("ERRO: Um número igual ou maior que zero foi inserido. Por favor, reinicie o programa e tente novamente.")
    sys.exit()
print("")

letra = input('''Informe a letra correspondente à operação desejada:
A - Adição
S - Subtração
M - Multiplicação
D - Divisão

Operação desejada: ''')
operacao = letra.upper()
cont = 1
print("")

if operacao == "A":
    print("> Operação selecionada: Adição")
    print("")
    while cont <= 10:
        print(f"{num} + {cont} = {num + cont}")
        cont += 1

elif operacao == "S":
    print("> Operação selecionada: Subtração")
    print("")
    while cont <= 10:
        print(f"{num} - {cont} = {num - cont}")
        cont += 1

elif operacao == "M":
    print("> Operação selecionada: Multiplicação")
    print("")
    while cont <= 10:
        print(f"{num} x {cont} = {num * cont}")
        cont += 1

elif operacao == "D":
    print("> Operação selecionada: Divisão")
    print("")
    while cont <= 10:
        print(f"{num} / {cont} = {(num / cont):.1f}")
        cont += 1

else:
    print("ERRO: Operação inválida. Por favor, reinicie o programa e tente novamente.")
    sys.exit()