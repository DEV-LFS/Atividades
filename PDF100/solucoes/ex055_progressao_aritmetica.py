# Exercício 055 - Progressão aritmética
# Solução em Python 3

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
quantidade = int(input("Quantidade: "))

if quantidade <= 0:
    raise ValueError("A quantidade deve ser positiva.")

soma = 0
sequencia = []

for i in range(quantidade):
    termo = primeiro + i * razao
    sequencia.append(termo)
    soma += termo

print("Sequência:", *sequencia)
print(f"Soma: {soma}")
