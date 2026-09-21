# Exercício 010 - Salário com comissão
# Solução em Python 3

salario_fixo = float(input("Salário fixo: R$ "))
vendas = float(input("Total vendido: R$ "))

comissao = vendas * 0.04
salario_total = salario_fixo + comissao

print(f"Comissão: R$ {comissao:.2f}")
print(f"Salário total: R$ {salario_total:.2f}")
