# Exercício 026 - Reajuste por faixa salarial
# Solução em Python 3

salario = float(input("Salário atual: R$ "))

if salario <= 1500:
    percentual = 0.15
elif salario <= 3000:
    percentual = 0.10
else:
    percentual = 0.05

aumento = salario * percentual
novo_salario = salario + aumento

print(f"Percentual: {percentual * 100:.0f}%")
print(f"Aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
