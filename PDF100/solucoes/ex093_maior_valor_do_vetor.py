# Exercício 093 - Maior valor do vetor
# Solução em Python 3

def maiorVetor(vetor):
    if not vetor:
        raise ValueError("O vetor não pode ser vazio.")

    maior = vetor[0]

    for valor in vetor[1:]:
        if valor > maior:
            maior = valor

    return maior


print(maiorVetor([4, 7, 2, 9, 5]))
print(maiorVetor([-8, -2, -5]))
print(maiorVetor([3, 3, 3]))
