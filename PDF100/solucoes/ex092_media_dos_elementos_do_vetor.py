# Exercício 092 - Média dos elementos do vetor
# Solução em Python 3

def mediaVetor(vetor):
    if not vetor:
        raise ValueError("O vetor não pode ser vazio.")
    return sum(vetor) / len(vetor)


print(mediaVetor([2, 4, 6, 8]))
print(mediaVetor([10, 10, 10]))
print(mediaVetor([-5, 5]))
