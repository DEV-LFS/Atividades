# Exercício 033 - Dia da semana
# Solução em Python 3

numero = int(input("Número do dia (1-7): "))

dias = {
    1: "SEGUNDA-FEIRA",
    2: "TERÇA-FEIRA",
    3: "QUARTA-FEIRA",
    4: "QUINTA-FEIRA",
    5: "SEXTA-FEIRA",
    6: "SÁBADO",
    7: "DOMINGO",
}

print(dias.get(numero, "OPÇÃO INVÁLIDA"))
