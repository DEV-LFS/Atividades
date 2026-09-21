# Exercício 095 - Contar ocorrências em função
# Solução em Python 3

def contarOcorrencias(vetor, procurado):
    quantidade = 0

    for valor in vetor:
        if valor == procurado:
            quantidade += 1

    return quantidade


print(contarOcorrencias([3, 5, 3, 8, 3], 3))
print(contarOcorrencias([1, 2, 3], 4))
print(contarOcorrencias([7, 7, 7, 7], 7))
