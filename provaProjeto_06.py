import os

# Lista de produtos (exemplo inicial)
produtos = [
    {
        'nome': 'arroz',
        'preco': 40.00,
        'quantidade': 1
    },
    {
        'nome': 'cafe',
        'preco': 35.00,
        'quantidade': 6
    }
]

# Função: Exibir o menu
def menu():
    print("=" * 30)
    print("Gerenciamento de Produtos".center(30))
    print("=" * 30)
    print("[1] - Listar Produtos")
    print("[2] - Cadastrar Produto")
    print("[3] - Editar Produto")
    print("[4] - Excluir Produto")
    print("[5] - Sair")
    print("=" * 30)
    opcao = input("--> Selecione uma Opção: ")
    return opcao

# Função: Listar produtos
def listar_produtos():
    if len(produtos) == 0:
        print("Não há produtos cadastrados")
        return False
    print(" Produtos ".center(30, "="))
    for index, produto in enumerate(produtos, start=1):
        print(f"[{index}] - {produto['nome']}")
        print(f"Preço: R${produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")
        if index != len(produtos):
            print("-" * 30)
    return True

# Função: Cadastrar produto
def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    while True:
        try:
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade: "))
            if preco <= 0 or quantidade <= 0:
                print("Preço e quantidade devem ser maiores que zero!")
                continue
            break
        except ValueError:
            print("Por favor, digite valores numéricos válidos!")
    
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    produtos.append(produto)
    print("Produto cadastrado com sucesso.")

# Função: Editar produto
def editar_produto():
    tem_produtos = listar_produtos()
    if not tem_produtos:
        return
    
    while True:
        try:
            print("=" * 30)
            produto_index = int(input("Selecione o produto a ser editado: "))
            if produto_index < 1 or produto_index > len(produtos):
                print("Número de produto inválido!")
                continue
            break
        except ValueError:
            print("Por favor, digite um número válido!")
    
    # Passagem de valor por referência
    produto = produtos[produto_index - 1]
    
    while True:
        try:
            nome = input("Digite o novo nome do produto: ")
            preco = float(input("Digite o novo preço do produto: "))
            quantidade = int(input("Digite a nova quantidade do produto: "))
            if preco <= 0 or quantidade <= 0:
                print("Preço e quantidade devem ser maiores que zero!")
                continue
            break
        except ValueError:
            print("Por favor, digite valores numéricos válidos!")
    
    produto["nome"] = nome
    produto["preco"] = preco
    produto["quantidade"] = quantidade
    print("Produto editado com sucesso.")

# Função: Excluir produto
def excluir_produto():
    tem_produtos = listar_produtos()
    if not tem_produtos:
        return
    
    while True:
        try:
            print("=" * 30)
            produto_index = int(input("Selecione o produto a ser excluido: "))
            if produto_index < 1 or produto_index > len(produtos):
                print("Número de produto inválido!")
                continue
            break
        except ValueError:
            print("Por favor, digite um número válido!")
    
    produtos.pop(produto_index - 1)
    print("Produto excluido com sucesso.")

# Código principal
while True:
    os.system("cls" if os.name == "nt" else "clear")
    opcao = menu()
    match opcao:
        case "1":
            listar_produtos()
        case "2":
            cadastrar_produto()
        case "3":
            editar_produto()
        case "4":
            excluir_produto()
        case "5":
            break
        case _:
            print("Opção Inválida.")
    input("\nPressione Enter para continuar...")