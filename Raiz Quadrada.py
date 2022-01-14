final = int(input("Informe o número final da contagem: "))
final += 1
lista = []
num = 0

for x in range(final):
    lista.append(num)
    print("Valor:",lista[num], "    Raiz:",lista[num]**2)
    num += 1