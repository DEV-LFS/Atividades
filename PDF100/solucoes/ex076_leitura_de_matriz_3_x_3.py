# Exercício 076 - Leitura de matriz 3 x 3
# Solução em Python 3

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Valor [{i}][{j}]: ")))
    matriz.append(linha)

for linha in matriz:
    print(*linha)
