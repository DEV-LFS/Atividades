# Exercício 059 - Senha até acertar
# Solução em Python 3

SENHA_CORRETA = "1234"
tentativas = 0

while True:
    senha = input("Senha: ")
    tentativas += 1

    if senha == SENHA_CORRETA:
        break

    print("Senha incorreta.")

print("ACESSO LIBERADO")
print(f"Tentativas: {tentativas}")
