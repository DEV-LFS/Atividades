# Exercício 062 - Leitura e exibição de vetor
# Solução em Python 3

vetor = []

for i in range(8):
    vetor.append(int(input(f"Valor {i + 1}: ")))

print("Saída:", *vetor)
