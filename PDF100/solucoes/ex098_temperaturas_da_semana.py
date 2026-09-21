# Exercício 098 - Temperaturas da semana
# Solução em Python 3

def mediaTemperaturas(temperaturas):
    return sum(temperaturas) / len(temperaturas)


def maiorTemperatura(temperaturas):
    maior = temperaturas[0]
    for valor in temperaturas[1:]:
        if valor > maior:
            maior = valor
    return maior


def menorTemperatura(temperaturas):
    menor = temperaturas[0]
    for valor in temperaturas[1:]:
        if valor < menor:
            menor = valor
    return menor


def diasAcimaDaMedia(temperaturas):
    media = mediaTemperaturas(temperaturas)
    quantidade = 0
    for valor in temperaturas:
        if valor > media:
            quantidade += 1
    return quantidade


temperaturas = []

for i in range(7):
    temperaturas.append(float(input(f"Temperatura do dia {i + 1}: ")))

print(f"Média: {mediaTemperaturas(temperaturas):.2f}")
print(f"Maior: {maiorTemperatura(temperaturas)}")
print(f"Menor: {menorTemperatura(temperaturas)}")
print(f"Dias acima da média: {diasAcimaDaMedia(temperaturas)}")
