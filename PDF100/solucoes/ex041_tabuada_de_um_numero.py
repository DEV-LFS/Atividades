# Exercício 041 - Tabuada de um número
# Solução em Python 3

numero = int(input("Número: "))

for multiplicador in range(1, 11):
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")
