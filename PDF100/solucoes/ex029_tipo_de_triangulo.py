# Exercício 029 - Tipo de triângulo
# Solução em Python 3

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

forma = (
    a > 0 and b > 0 and c > 0 and
    a < b + c and b < a + c and c < a + b
)

if not forma:
    print("NÃO FORMA TRIÂNGULO")
elif a == b == c:
    print("EQUILÁTERO")
elif a == b or a == c or b == c:
    print("ISÓSCELES")
else:
    print("ESCALENO")
