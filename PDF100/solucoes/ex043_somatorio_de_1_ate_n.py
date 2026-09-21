# Exercício 043 - Somatório de 1 até N
# Solução em Python 3

n = int(input("N: "))

if n < 1:
    raise ValueError("N deve ser positivo.")

soma = 0
for numero in range(1, n + 1):
    soma += numero

print(f"Soma: {soma}")
