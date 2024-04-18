from math import ceil

lista = []
cont = 1

print('''
Este programa realizará o cálculo da mediana com base nos números informados, exceto 0.
Para sair, digite 0.
''')

while True:
    num = float(input(f"Informe o {cont}º número: "))
    if num == 0:
        break
    lista.append(num)
    cont += 1

print("")
qtde_itens = len(lista)
lista.sort()
print(f"Números informados: {lista}")
print("")

if qtde_itens % 2 == 0:
    media_itens = int(qtde_itens / 2)
    med1 = lista[media_itens - 1]
    med2 = lista[media_itens]
    mediana = (med1 + med2) / 2
    print(f"A lista de números informados possui dois valores modais, a saber: {med1} e {med2}\nA mediana é: {mediana}")

else:
    media_itens = ceil(qtde_itens / 2)
    mediana = lista[media_itens - 1]
    print(f"A mediana dos valores informados é: {mediana}")
