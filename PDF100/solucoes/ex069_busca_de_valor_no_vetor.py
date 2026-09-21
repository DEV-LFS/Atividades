# Exercício 069 - Busca de valor no vetor
# Solução em Python 3

vetor = []

for i in range(10):
    vetor.append(int(input(f"Valor {i + 1}: ")))

busca = int(input("Valor procurado: "))
posicoes = []

for i, valor in enumerate(vetor):
    if valor == busca:
        posicoes.append(i)

if posicoes:
    print("Posições:", *posicoes)
else:
    print("VALOR NÃO ENCONTRADO")
