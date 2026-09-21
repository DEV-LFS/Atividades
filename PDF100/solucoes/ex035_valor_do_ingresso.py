# Exercício 035 - Valor do ingresso
# Solução em Python 3

idade = int(input("Idade: "))
estudante = input("Estudante? (S/N): ").strip().upper() == "S"

preco = 30.0
tem_meia = idade < 12 or estudante or idade >= 60

if tem_meia:
    preco *= 0.5

print(f"Valor do ingresso: R$ {preco:.2f}")
