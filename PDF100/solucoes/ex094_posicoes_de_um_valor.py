# Exercício 094 - Posições de um valor
# Solução em Python 3

def buscarPosicoes(vetor, procurado):
    posicoes = []

    for i, valor in enumerate(vetor):
        if valor == procurado:
            posicoes.append(i)

    return posicoes


print(buscarPosicoes([4, 7, 2, 7, 9], 7))
print(buscarPosicoes([5, 5, 5], 5))
print(buscarPosicoes([1, 3, 5], 2))
