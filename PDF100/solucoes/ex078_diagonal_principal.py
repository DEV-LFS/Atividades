# Exercício 078 - Diagonal principal
# Solução em Python 3

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Valor [{i}][{j}]: ")))
    matriz.append(linha)

diagonal = []
for i in range(3):
    diagonal.append(matriz[i][i])

print("Diagonal principal:", *diagonal)
print(f"Soma: {sum(diagonal)}")
