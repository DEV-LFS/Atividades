# Exercício 049 - Pares e ímpares
# Solução em Python 3

pares = 0
impares = 0

for i in range(1, 7):
    valor = int(input(f"Valor {i}: "))
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
