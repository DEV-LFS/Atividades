# Exercício 091 - Contar positivos no vetor
# Solução em Python 3

def contarPositivos(vetor):
    quantidade = 0
    for valor in vetor:
        if valor > 0:
            quantidade += 1
    return quantidade


print(contarPositivos([5, -2, 0, 8, -1]))
print(contarPositivos([1, 2, 3]))
print(contarPositivos([-1, -2, 0]))
