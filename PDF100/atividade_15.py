from re import sub


preco_unitario = float(input("Digite o preço unitário: "))
quantidade = int(input("Digite a quantidade: "))
frete = float(input("Digite o valor do frete: "))
subtotal = preco_unitario * quantidade
total = subtotal + frete
print(f"O subtotal dos produtos é {subtotal} e o total da compra é {total}")