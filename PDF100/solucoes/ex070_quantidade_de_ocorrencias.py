# Exercício 070 - Quantidade de ocorrências
# Solução em Python 3

vetor = []

for i in range(10):
    vetor.append(int(input(f"Valor {i + 1}: ")))

busca = int(input("Valor procurado: "))
ocorrencias = 0

for valor in vetor:
    if valor == busca:
        ocorrencias += 1

print(f"Ocorrências: {ocorrencias}")
