# Exercício 066 - Pares e suas posições
# Solução em Python 3

vetor = []

for i in range(10):
    vetor.append(int(input(f"Valor {i + 1}: ")))

encontrou = False

for posicao, valor in enumerate(vetor):
    if valor % 2 == 0:
        print(f"Valor {valor} — posição {posicao}")
        encontrou = True

if not encontrou:
    print("NENHUM VALOR PAR")
