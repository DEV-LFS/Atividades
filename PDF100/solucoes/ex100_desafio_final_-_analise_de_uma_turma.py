# Exercício 100 - Desafio final — análise de uma turma
# Solução em Python 3

def mediaNotas(notas):
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


def quantidadeAprovados(notas):
    quantidade = 0
    for nota in notas:
        if nota >= 7:
            quantidade += 1
    return quantidade


def indiceMaisVelho(idades):
    indice = 0
    for i in range(1, len(idades)):
        if idades[i] > idades[indice]:
            indice = i
    return indice


def nomesAcimaDaMedia(nomes, notas):
    media = mediaNotas(notas)
    resultado = []
    for i in range(len(nomes)):
        if notas[i] > media:
            resultado.append(nomes[i])
    return resultado


nomes = []
idades = []
notas = []

for i in range(10):
    nomes.append(input(f"Nome do aluno {i + 1}: "))
    idades.append(int(input("Idade: ")))
    notas.append(float(input("Nota: ")))

media = mediaNotas(notas)
i_maior = indiceMaiorNota(notas)
i_menor = indiceMenorNota(notas)
i_velho = indiceMaisVelho(idades)

print(f"Média das notas: {media:.2f}")
print(f"Maior nota: {nomes[i_maior]} — {notas[i_maior]}")
print(f"Menor nota: {nomes[i_menor]} — {notas[i_menor]}")
print(f"Aprovados: {quantidadeAprovados(notas)}")
print(f"Mais velho: {nomes[i_velho]} — {idades[i_velho]} anos")
print("Acima da média:", ", ".join(nomesAcimaDaMedia(nomes, notas)) or "nenhum")
