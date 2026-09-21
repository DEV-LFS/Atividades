# Exercício 050 - Maior valor informado
# Solução em Python 3

maior = float(input("Valor 1: "))

for i in range(2, 11):
    valor = float(input(f"Valor {i}: "))
    if valor > maior:
        maior = valor

print(f"Maior valor: {maior}")
