# Exercício 073 - Comparar dois vetores
# Solução em Python 3

a = []
b = []

for i in range(5):
    a.append(int(input(f"A[{i}]: ")))

for i in range(5):
    b.append(int(input(f"B[{i}]: ")))

iguais = []

for i in range(5):
    if a[i] == b[i]:
        iguais.append(i)

if iguais:
    print("Posições iguais:", *iguais)
else:
    print("NENHUMA POSIÇÃO")
