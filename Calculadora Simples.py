import sys

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
print("")

opcao = int(input('''Por favor, informe o número correspondente à operação desejada:
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão

Opção selecionada: '''))

if opcao == 1:
    resultado = num1 + num2
    nome_opcao = "soma"
elif opcao == 2:
    resultado = num1 - num2
    nome_opcao = "subtração"
elif opcao == 3:
    resultado = num1 * num2
    nome_opcao = "multiplicação"
elif opcao == 4:
    resultado = num1 / num2
    nome_opcao = "divisão"
else:
    print("Opção inválida. Por favor, reinicie o programa e tente novamente")
    sys.exit()
print("")

print(f"O resultado da {nome_opcao} é: {resultado}")
