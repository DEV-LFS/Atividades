import math

def calcular_area_circulo(raio):
    area = math.pi * raio ** 2
    return area

raio = float(input("Digite o raio do círculo: "))

resultado = calcular_area_circulo(raio)

print(f"Área do círculo: {resultado:.2f}")