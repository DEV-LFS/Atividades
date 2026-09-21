# Exercício 048 - Positivos, negativos e zeros
# Solução em Python 3

positivos = 0
negativos = 0
zeros = 0

for i in range(1, 9):
    valor = int(input(f"Valor {i}: "))
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1
    else:
        zeros += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Zeros: {zeros}")
