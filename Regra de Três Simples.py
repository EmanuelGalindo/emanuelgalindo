total = float(input("Informe o número que representa 100%: "))
num = float(input("Informe o número do qual deseja saber a porcentagem do todo: "))

porcentagem = (num*100) / total
print("")

print(f"O número {num:.0f} representa {porcentagem:.0f}% de {total:.0f}")