# Exercício 038 - Contagem até um limite
# Solução em Python 3

n = int(input("N: "))

if n < 1:
    raise ValueError("N deve ser maior ou igual a 1.")

for numero in range(1, n + 1):
    print(numero, end=" ")
print()
