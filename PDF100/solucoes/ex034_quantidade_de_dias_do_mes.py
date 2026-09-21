# Exercício 034 - Quantidade de dias do mês
# Solução em Python 3

mes = int(input("Mês (1-12): "))
ano = int(input("Ano: "))

bissexto = ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)

if mes < 1 or mes > 12:
    print("MÊS INVÁLIDO")
elif mes == 2:
    print("29 dias" if bissexto else "28 dias")
elif mes in (4, 6, 9, 11):
    print("30 dias")
else:
    print("31 dias")
