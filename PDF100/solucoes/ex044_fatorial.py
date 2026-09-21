# Exercício 044 - Fatorial
# Solução em Python 3

n = int(input("Número (0 a 12): "))

if not 0 <= n <= 12:
    raise ValueError("O número deve estar entre 0 e 12.")

fatorial = 1
for valor in range(2, n + 1):
    fatorial *= valor

print(f"{n}! = {fatorial}")
