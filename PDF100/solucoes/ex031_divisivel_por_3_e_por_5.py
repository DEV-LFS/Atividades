# Exercício 031 - Divisível por 3 e por 5
# Solução em Python 3

numero = int(input("Número: "))

por3 = numero % 3 == 0
por5 = numero % 5 == 0

if por3 and por5:
    print("DIVISÍVEL POR 3 E 5")
elif por3:
    print("DIVISÍVEL APENAS POR 3")
elif por5:
    print("DIVISÍVEL APENAS POR 5")
else:
    print("NÃO DIVISÍVEL POR 3 NEM 5")
