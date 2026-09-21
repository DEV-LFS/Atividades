# Exercício 023 - Categoria de votação
# Solução em Python 3

idade = int(input("Idade: "))

if idade < 16:
    categoria = "NÃO PODE VOTAR"
elif idade < 18:
    categoria = "VOTO OPCIONAL"
elif idade < 70:
    categoria = "VOTO OBRIGATÓRIO"
else:
    categoria = "VOTO OPCIONAL"

print(categoria)
