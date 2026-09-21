# Exercício 056 - Validação de nota
# Solução em Python 3

invalidas = 0

while True:
    nota = float(input("Nota: "))
    if 0 <= nota <= 10:
        break
    print("Valor inválido.")
    invalidas += 1

print(f"Nota aceita: {nota}")
print(f"Tentativas inválidas: {invalidas}")
