# Exercício 022 - Situação do aluno por faixa
# Solução em Python 3

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

if media < 5:
    situacao = "REPROVADO"
elif media < 7:
    situacao = "RECUPERAÇÃO"
else:
    situacao = "APROVADO"

print(f"Média: {media:.1f}")
print(f"Situação: {situacao}")
