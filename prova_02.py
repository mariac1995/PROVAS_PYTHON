# Coletando dados do usuário
nome = input("Digite o nome do contato: ")
telefone = input("Digite o número de telefone: ")
email = input("Digite o endereço de email: ")

contato = {
    "Nome": nome,
    "Telefone": telefone,
    "Email": email
}

print("\nInformações do contato:")
for chave, valor in contato.items():
    print(f"{chave}: {valor}")