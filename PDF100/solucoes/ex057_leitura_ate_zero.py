# Exercício 057 - Leitura até zero
# Solução em Python 3

quantidade = 0
soma = 0.0

while True:
    valor = float(input("Valor: "))
    if valor == 0:
        break
    quantidade += 1
    soma += valor

if quantidade == 0:
    print("NENHUM VALOR VÁLIDO")
else:
    media = soma / quantidade
    print(f"Quantidade: {quantidade}")
    print(f"Soma: {soma}")
    print(f"Média: {media}")
