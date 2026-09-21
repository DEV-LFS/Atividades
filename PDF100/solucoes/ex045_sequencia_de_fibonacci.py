# Exercício 045 - Sequência de Fibonacci
# Solução em Python 3

quantidade = int(input("Quantidade de termos: "))

if quantidade < 2:
    raise ValueError("A quantidade deve ser maior ou igual a 2.")

a, b = 0, 1

for i in range(quantidade):
    print(a, end=" " if i < quantidade - 1 else "\n")
    a, b = b, a + b
