# Exercício 051 - Maior e menor valor
# Solução em Python 3

primeiro = float(input("Valor 1: "))
maior = primeiro
menor = primeiro

for i in range(2, 11):
    valor = float(input(f"Valor {i}: "))
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f"Maior: {maior}")
print(f"Menor: {menor}")
