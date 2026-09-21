# Exercício 071 - Copiar apenas valores positivos
# Solução em Python 3

vetor_a = []

for i in range(10):
    vetor_a.append(float(input(f"A[{i}]: ")))

vetor_b = []

for valor in vetor_a:
    if valor > 0:
        vetor_b.append(valor)

print("Vetor A:", vetor_a)
if vetor_b:
    print("Vetor B:", vetor_b)
else:
    print("VETOR VAZIO")
