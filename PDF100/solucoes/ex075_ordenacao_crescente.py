# Exercício 075 - Ordenação crescente
# Solução em Python 3

vetor = []

for i in range(10):
    vetor.append(int(input(f"Valor {i + 1}: ")))

for fim in range(len(vetor) - 1, 0, -1):
    trocou = False
    for i in range(fim):
        if vetor[i] > vetor[i + 1]:
            vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
            trocou = True
    if not trocou:
        break

print("Ordenado:", *vetor)
