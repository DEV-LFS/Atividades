# Exercício 020 - Três valores em ordem crescente
# Solução em Python 3

a = int(input("Valor 1: "))
b = int(input("Valor 2: "))
c = int(input("Valor 3: "))

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print(f"Ordem crescente: {a}, {b}, {c}")
