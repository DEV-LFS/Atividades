salario_fixo = float(input("Digite o salário fixo: "))
total_vendas = float(input("Digite o total vendido: "))
comissao = total_vendas * 0.04
salario_total = salario_fixo + comissao
print(f"A comissao foi de {comissao} e o salario é {salario_total}")