# Exercício 047 - Média de dez notas
# Solução em Python 3

soma = 0.0

for i in range(1, 11):
    nota = float(input(f"Nota {i}: "))
    if not 0 <= nota <= 10:
        raise ValueError("As notas devem estar entre 0 e 10.")
    soma += nota

media = soma / 10
print(f"Média: {media:.1f}")
