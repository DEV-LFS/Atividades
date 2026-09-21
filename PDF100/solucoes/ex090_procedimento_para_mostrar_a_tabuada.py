# Exercício 090 - Procedimento para mostrar a tabuada
# Solução em Python 3

def mostrarTabuada(numero):
    for multiplicador in range(1, 11):
        print(f"{numero} x {multiplicador} = {numero * multiplicador}")


mostrarTabuada(4)
