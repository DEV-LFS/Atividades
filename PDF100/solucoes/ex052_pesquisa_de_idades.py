# Exercício 052 - Pesquisa de idades
# Solução em Python 3

soma = 0
menores = 0
idosos = 0

for i in range(1, 11):
    idade = int(input(f"Idade {i}: "))
    soma += idade
    if idade < 18:
        menores += 1
    if idade >= 60:
        idosos += 1

media = soma / 10

print(f"Média: {media:.1f}")
print(f"Menores de 18: {menores}")
print(f"Com 60 anos ou mais: {idosos}")
