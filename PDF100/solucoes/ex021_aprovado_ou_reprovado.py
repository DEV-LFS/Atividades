# Exercício 021 - Aprovado ou reprovado
# Solução em Python 3

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2
situacao = "APROVADO" if media >= 7 else "REPROVADO"

print(f"Média: {media:.1f}")
print(f"Situação: {situacao}")
