# Exercício 030 - Aprovação de empréstimo
# Solução em Python 3

valor_imovel = float(input("Valor do imóvel: R$ "))
salario = float(input("Salário mensal: R$ "))
anos = int(input("Prazo (anos): "))

prestacao = valor_imovel / (anos * 12)
limite = salario * 0.30

print(f"Prestação: R$ {prestacao:.2f}")
print(f"Limite: R$ {limite:.2f}")
print("APROVADO" if prestacao <= limite else "NEGADO")
