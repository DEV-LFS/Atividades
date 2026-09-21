# Exercício 015 - Custo final da compra
# Solução em Python 3

preco_unitario = float(input("Preço unitário: R$ "))
quantidade = int(input("Quantidade: "))
frete = float(input("Frete: R$ "))

subtotal = preco_unitario * quantidade
total = subtotal + frete

print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Total: R$ {total:.2f}")
