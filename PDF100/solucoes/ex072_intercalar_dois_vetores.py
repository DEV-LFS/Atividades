# Exercício 072 - Intercalar dois vetores
# Solução em Python 3

a = []
b = []

for i in range(5):
    a.append(int(input(f"A[{i}]: ")))

for i in range(5):
    b.append(int(input(f"B[{i}]: ")))

c = []

for i in range(5):
    c.append(a[i])
    c.append(b[i])

print("C:", c)
