# Exercício 079 - Soma de cada linha e coluna
# Solução em Python 3

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Valor [{i}][{j}]: ")))
    matriz.append(linha)

somas_linhas = []
for linha in matriz:
    somas_linhas.append(sum(linha))

somas_colunas = []
for j in range(3):
    soma = 0
    for i in range(3):
        soma += matriz[i][j]
    somas_colunas.append(soma)

print("Somas das linhas:", *somas_linhas)
print("Somas das colunas:", *somas_colunas)
