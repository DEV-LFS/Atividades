# Exercício 046 - Soma de cinco valores
# Solução em Python 3

soma = 0.0

for i in range(1, 6):
    valor = float(input(f"Valor {i}: "))
    soma += valor

print(f"Soma: {soma}")
