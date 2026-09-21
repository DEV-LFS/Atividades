# Exercício 080 - Maior elemento da matriz
# Solução em Python 3

matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input(f"Valor [{i}][{j}]: ")))
    matriz.append(linha)

maior = matriz[0][0]
linha_maior = 0
coluna_maior = 0

for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha_maior = i
            coluna_maior = j

print(f"Maior valor: {maior}")
print(f"Primeira posição: linha {linha_maior}, coluna {coluna_maior}")
