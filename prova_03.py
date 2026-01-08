produtos = {}

for i in range(1, 6):
    nome = input(f"Digite o nome do {i}º produto: ")

    while True:  
        try:
            preco = float(input(f"Digite o preço do {i}º produto: "))
            break  
        except ValueError:
            print("Por favor, digite um número válido para o preço.")

    produtos[nome] = preco

total = sum(produtos.values())
print("\nValor total da compra:", total)
