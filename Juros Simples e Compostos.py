import sys

opcao = int(input('''Por favor, informe a opção desejada:
1 - Juros simples
2 - Juros compostos

Opção selecionada: '''))
print("")

if opcao == 1:
    capital = float(input("Informe o valor do capital inicial (em R$): "))
    perc = float(input("Informe o valor percentual da taxa mensal (sem o %): "))
    taxa = perc / 100
    periodo = float(input("Informe o período (em meses): "))
    print("")

    juros = capital * taxa * periodo
    print(f"Juros: R$ {juros:.2f}")

elif opcao == 2:
    capital = float(input("Informe o valor do capital inicial (em R$): "))
    perc = float(input("Informe o valor percentual da taxa mensal (sem o %): "))
    taxa = perc / 100
    periodo = float(input("Informe o período (em meses): "))
    print("")

    montante = capital * (1 + taxa)**periodo
    print(f"Juros: R$ {montante:.2f}")

else:
    print("Opção inválida. Por favor, reinicie o programa e tente novamente.")
    sys.exit()