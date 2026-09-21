# Exercício 025 - Preço conforme a forma de pagamento
# Solução em Python 3

preco = float(input("Preço: R$ "))
opcao = int(input("Opção de pagamento (1-4): "))

if opcao == 1:
    final = preco * 0.90
elif opcao == 2:
    final = preco * 0.95
elif opcao == 3:
    final = preco
elif opcao == 4:
    final = preco * 1.08
else:
    raise ValueError("Opção inválida.")

print(f"Valor final: R$ {final:.2f}")
