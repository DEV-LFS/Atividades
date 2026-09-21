# Exercício 053 - Pesquisa de alturas
# Solução em Python 3

primeira = float(input("Altura 1: "))
soma = primeira
maior = primeira
menor = primeira

for i in range(2, 9):
    altura = float(input(f"Altura {i}: "))
    soma += altura
    if altura > maior:
        maior = altura
    if altura < menor:
        menor = altura

media = soma / 8

print(f"Média: {media:.2f} m")
print(f"Maior: {maior:.2f} m")
print(f"Menor: {menor:.2f} m")
