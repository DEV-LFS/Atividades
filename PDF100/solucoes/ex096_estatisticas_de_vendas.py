# Exercício 096 - Estatísticas de vendas
# Solução em Python 3

def totalVendas(vetor):
    return sum(vetor)


def mediaVendas(vetor):
    return totalVendas(vetor) / len(vetor)


def maiorVenda(vetor):
    maior = vetor[0]
    for valor in vetor[1:]:
        if valor > maior:
            maior = valor
    return maior


def contarAcimaDaMedia(vetor):
    media = mediaVendas(vetor)
    quantidade = 0
    for valor in vetor:
        if valor > media:
            quantidade += 1
    return quantidade


vendas = []

for i in range(10):
    vendas.append(float(input(f"Venda {i + 1}: R$ ")))

print(f"Total: R$ {totalVendas(vendas):.2f}")
print(f"Média: R$ {mediaVendas(vendas):.2f}")
print(f"Maior venda: R$ {maiorVenda(vendas):.2f}")
print(f"Acima da média: {contarAcimaDaMedia(vendas)}")
