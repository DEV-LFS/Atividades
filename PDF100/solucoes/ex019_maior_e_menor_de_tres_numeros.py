# Exercício 019 - Maior e menor de três números
# Solução em Python 3

a = float(input("Valor 1: "))
b = float(input("Valor 2: "))
c = float(input("Valor 3: "))

maior = a
menor = a

for valor in (b, c):
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f"Maior: {maior}")
print(f"Menor: {menor}")
