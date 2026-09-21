# Exercício 064 - Soma dos elementos do vetor
# Solução em Python 3

vetor = []

for i in range(10):
    vetor.append(float(input(f"Valor {i + 1}: ")))

soma = 0.0
for valor in vetor:
    soma += valor

print(f"Soma: {soma}")
