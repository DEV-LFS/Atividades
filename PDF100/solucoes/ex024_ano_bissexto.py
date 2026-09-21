# Exercício 024 - Ano bissexto
# Solução em Python 3

ano = int(input("Ano: "))

bissexto = ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)

if bissexto:
    print("Resultado: ANO BISSEXTO")
else:
    print("Resultado: NÃO BISSEXTO")
