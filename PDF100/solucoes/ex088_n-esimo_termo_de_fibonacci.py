# Exercício 088 - N-ésimo termo de Fibonacci
# Solução em Python 3

def fibonacci(n):
    if n < 0:
        raise ValueError("n deve ser não negativo.")

    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(6))
print(fibonacci(10))
