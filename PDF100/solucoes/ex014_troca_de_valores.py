# Exercício 014 - Troca de valores
# Solução em Python 3

a = int(input("A: "))
b = int(input("B: "))

aux = a
a = b
b = aux

print("Depois da troca:")
print(f"A: {a}")
print(f"B: {b}")
