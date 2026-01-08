# Criar um dicionário para armazenar informações de contato

# Solicitar os dados ao usuário
nome = input("Digite o nome do contato: ")
telefone = input("Digite o número de telefone: ")
email = input("Digite o endereço de email: ")

# Armazenar os dados em um dicionário
contato = {"Nome": nome, "Telefone": telefone, "Email": email}

# Exibir o conteúdo do dicionário
print("\nInformações do contato:")
for chave, valor in contato.items():
    print(f"{chave}: {valor}")
