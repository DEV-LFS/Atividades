# Exercício 099 - Controle de estoque
# Solução em Python 3

def valorEmEstoque(quantidade, preco):
    return quantidade * preco


def valorTotalEstoque(quantidades, precos):
    total = 0.0
    for i in range(len(quantidades)):
        total += valorEmEstoque(quantidades[i], precos[i])
    return total


def contarEstoqueBaixo(quantidades):
    quantidade = 0
    for valor in quantidades:
        if valor < 5:
            quantidade += 1
    return quantidade


def indiceMaiorValorEstoque(quantidades, precos):
    indice = 0
    maior_valor = valorEmEstoque(quantidades[0], precos[0])

    for i in range(1, len(quantidades)):
        atual = valorEmEstoque(quantidades[i], precos[i])
        if atual > maior_valor:
            maior_valor = atual
            indice = i

    return indice


nomes = []
quantidades = []
precos = []

for i in range(8):
    nomes.append(input(f"Produto {i + 1}: "))
    quantidades.append(int(input("Quantidade: ")))
    precos.append(float(input("Preço unitário: R$ ")))

indice = indiceMaiorValorEstoque(quantidades, precos)

print(f"Valor total do estoque: R$ {valorTotalEstoque(quantidades, precos):.2f}")
print(f"Produtos com estoque menor que 5: {contarEstoqueBaixo(quantidades)}")
print(
    f"Maior valor em estoque: {nomes[indice]} — "
    f"R$ {valorEmEstoque(quantidades[indice], precos[indice]):.2f}"
)
