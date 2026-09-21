# Exercício 058 - Idades até valor negativo
# Solução em Python 3

quantidade = 0
soma = 0
maiores = 0

while True:
    idade = int(input("Idade: "))
    if idade < 0:
        break
    quantidade += 1
    soma += idade
    if idade >= 18:
        maiores += 1

if quantidade == 0:
    print("NENHUMA IDADE INFORMADA")
else:
    print(f"Quantidade: {quantidade}")
    print(f"Média: {soma / quantidade:.1f}")
    print(f"Maiores de idade: {maiores}")
