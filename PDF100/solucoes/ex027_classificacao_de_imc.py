# Exercício 027 - Classificação de IMC
# Solução em Python 3

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura * altura)

if imc < 18.5:
    classificacao = "ABAIXO DA FAIXA"
elif imc < 25:
    classificacao = "FAIXA NORMAL"
elif imc < 30:
    classificacao = "ACIMA DA FAIXA"
else:
    classificacao = "FAIXA ELEVADA"

print(f"IMC: {imc:.1f}")
print(f"Classificação: {classificacao}")
