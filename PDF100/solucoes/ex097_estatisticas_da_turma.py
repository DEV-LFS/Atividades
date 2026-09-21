# Exercício 097 - Estatísticas da turma
# Solução em Python 3

def calcularMedia(notas):
    return sum(notas) / len(notas)


def indiceMaiorNota(notas):
    indice = 0
    for i in range(1, len(notas)):
        if notas[i] > notas[indice]:
            indice = i
    return indice


def indiceMenorNota(notas):
    indice = 0
    for i in range(1, len(notas)):
        if notas[i] < notas[indice]:
            indice = i
    return indice


def nomesAcimaDaMedia(nomes, notas):
    media = calcularMedia(notas)
    resultado = []
    for i in range(len(nomes)):
        if notas[i] > media:
            resultado.append(nomes[i])
    return resultado


nomes = []
notas = []

for i in range(8):
    nomes.append(input(f"Nome do aluno {i + 1}: "))
    notas.append(float(input("Nota: ")))

media = calcularMedia(notas)
i_maior = indiceMaiorNota(notas)
i_menor = indiceMenorNota(notas)

print(f"Média: {media:.2f}")
print(f"Maior nota: {notas[i_maior]} — {nomes[i_maior]}")
print(f"Menor nota: {notas[i_menor]} — {nomes[i_menor]}")
print("Acima da média:", ", ".join(nomesAcimaDaMedia(nomes, notas)) or "nenhum")
