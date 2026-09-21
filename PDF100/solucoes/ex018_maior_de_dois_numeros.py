# Exercício 018 - Maior de dois números
# Solução em Python 3

a = float(input("Primeiro valor: "))
b = float(input("Segundo valor: "))

if a > b:
    print(f"Maior valor: {a}")
elif b > a:
    print(f"Maior valor: {b}")
else:
    print("VALORES IGUAIS")
