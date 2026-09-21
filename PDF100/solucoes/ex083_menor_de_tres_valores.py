# Exercício 083 - Menor de três valores
# Solução em Python 3

def menor3(a, b, c):
    menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c
    return menor


print(menor3(8, 3, 5))
print(menor3(-1, -7, -2))
print(menor3(4, 4, 9))
