
produtos = {}

for i in range(5):
    nome = input(f"Digite o nome do produto {i+1}: ")
    preco = float(input(f"Digite o preço de {nome}: R$ "))
    produtos[nome] = preco

total = sum(produtos.values())


print("\nResumo da compra:")
for nome, preco in produtos.items():
    print(f"{nome}: R$ {preco:.2f}")

print(f"\nValor total da compra: R$ {total:.2f}")