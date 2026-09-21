# Exercício 089 - Validação de nota
# Solução em Python 3

def notaValida(nota):
    return 0 <= nota <= 10


print(notaValida(7.5))
print(notaValida(0))
print(notaValida(10))
print(notaValida(-1))
print(notaValida(10.1))
