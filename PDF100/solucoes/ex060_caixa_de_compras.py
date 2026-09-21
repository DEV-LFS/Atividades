# Exercício 060 - Caixa de compras
# Solução em Python 3

quantidade = 0
total = 0.0
maior_preco = None

while True:
    preco = float(input("Preço: R$ "))
    if preco == 0:
        break

    quantidade += 1
    total += preco

    if maior_preco is None or preco > maior_preco:
        maior_preco = preco

if quantidade == 0:
    print("NENHUM PRODUTO INFORMADO")
else:
    print(f"Produtos: {quantidade}")
    print(f"Total: R$ {total:.2f}")
    print(f"Maior preço: R$ {maior_preco:.2f}")
