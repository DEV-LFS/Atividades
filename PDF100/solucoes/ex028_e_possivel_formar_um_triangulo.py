# Exercício 028 - É possível formar um triângulo?
# Solução em Python 3

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

forma = (
    a > 0 and b > 0 and c > 0 and
    a < b + c and
    b < a + c and
    c < a + b
)

print("FORMAM UM TRIÂNGULO" if forma else "NÃO FORMAM")
