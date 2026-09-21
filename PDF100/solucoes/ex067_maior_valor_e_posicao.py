# Exercício 067 - Maior valor e posição
# Solução em Python 3

vetor = []

for i in range(8):
    vetor.append(int(input(f"Valor {i + 1}: ")))

maior = vetor[0]
posicao = 0

for i in range(1, len(vetor)):
    if vetor[i] > maior:
        maior = vetor[i]
        posicao = i

print(f"Maior valor: {maior}")
print(f"Primeira posição: {posicao}")
