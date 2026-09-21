# Exercício 074 - Nomes acima da média
# Solução em Python 3

nomes = []
notas = []

for i in range(5):
    nomes.append(input(f"Nome do aluno {i + 1}: "))
    notas.append(float(input("Nota: ")))

media = sum(notas) / len(notas)
acima = []

for i in range(len(nomes)):
    if notas[i] > media:
        acima.append(nomes[i])

print(f"Média: {media:.1f}")
print("Acima da média:", ", ".join(acima) if acima else "nenhum")
