# Exercício 087 - Função fatorial
# Solução em Python 3

def fatorial(n):
    if not 0 <= n <= 12:
        raise ValueError("n deve estar entre 0 e 12.")

    resultado = 1
    for valor in range(2, n + 1):
        resultado *= valor
    return resultado


print(fatorial(0))
print(fatorial(1))
print(fatorial(5))
print(fatorial(6))
