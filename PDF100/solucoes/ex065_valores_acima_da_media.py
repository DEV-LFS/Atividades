# Exercício 065 - Valores acima da média
# Solução em Python 3

notas = []

for i in range(8):
    notas.append(float(input(f"Nota {i + 1}: ")))

media = sum(notas) / len(notas)
acima = []

for nota in notas:
    if nota > media:
        acima.append(nota)

print(f"Média: {media:.2f}")
print("Acima da média:", *acima if acima else ["nenhum valor"])
print(f"Quantidade: {len(acima)}")
