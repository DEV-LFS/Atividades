# Exercício 077 - Soma dos elementos da matriz
# Solução em Python 3

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Valor [{i}][{j}]: ")))
    matriz.append(linha)

soma = 0
for linha in matriz:
    for valor in linha:
        soma += valor

print(f"Soma: {soma}")
