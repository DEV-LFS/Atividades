# Exercício 042 - Tabuada com início e fim
# Solução em Python 3

numero = int(input("Número: "))
inicio = int(input("Início: "))
fim = int(input("Fim: "))

passo = 1 if inicio <= fim else -1

for multiplicador in range(inicio, fim + passo, passo):
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")
