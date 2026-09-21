# Exercício 068 - Menor valor e posição
# Solução em Python 3

vetor = []

for i in range(8):
    vetor.append(int(input(f"Valor {i + 1}: ")))

menor = vetor[0]
posicao = 0

for i in range(1, len(vetor)):
    if vetor[i] < menor:
        menor = vetor[i]
        posicao = i

print(f"Menor valor: {menor}")
print(f"Primeira posição: {posicao}")
