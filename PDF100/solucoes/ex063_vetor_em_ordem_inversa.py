# Exercício 063 - Vetor em ordem inversa
# Solução em Python 3

vetor = []

for i in range(8):
    vetor.append(int(input(f"Valor {i + 1}: ")))

print("Saída:", end=" ")
for i in range(len(vetor) - 1, -1, -1):
    print(vetor[i], end=" ")
print()
