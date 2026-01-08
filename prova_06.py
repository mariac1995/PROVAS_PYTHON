# Lista que armazenará os produtos
produtos = []


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


def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("\nLista de Produtos:")
        for i, produto in enumerate(produtos, start=1):
            print(
                f"{i}. Nome: {produto['nome']} | Preço: R$ {produto['preco']:.2f} | Quantidade: {produto['quantidade']}"
            )


def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))

    produto = {"nome": nome, "preco": preco, "quantidade": quantidade}

    produtos.append(produto)
    print("Produto cadastrado com sucesso!")


def editar_produto():
    listar_produtos()
    if not produtos:
        return

    indice = int(input("Digite o número do produto que deseja editar: ")) - 1

    if 0 <= indice < len(produtos):
        print("Digite os novos dados do produto:")
        produtos[indice]["nome"] = input("Novo nome: ")
        produtos[indice]["preco"] = float(input("Novo preço: "))
        produtos[indice]["quantidade"] = int(input("Nova quantidade: "))
        print("Produto atualizado com sucesso!")
    else:
        print("Produto inválido.")


def excluir_produto():
    listar_produtos()
    if not produtos:
        return

    indice = int(input("Digite o número do produto que deseja excluir: ")) - 1

    if 0 <= indice < len(produtos):
        removido = produtos.pop(indice)
        print(f"Produto '{removido['nome']}' excluído com sucesso!")
    else:
        print("Produto inválido.")


# Código Principal
while True:
    opcao = menu()

    if opcao == "1":
        listar_produtos()
    elif opcao == "2":
        cadastrar_produto()
    elif opcao == "3":
        editar_produto()
    elif opcao == "4":
        excluir_produto()
    elif opcao == "5":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção Inválida.")

    input("\nPressione <ENTER> para continuar...")
