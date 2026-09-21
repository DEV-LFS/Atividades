# Exercício 008 - Desconto no produto
# Solução em Python 3

preco = float(input("Preço: R$ "))

desconto = preco * 0.10
preco_final = preco - desconto

print(f"Desconto: R$ {desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
