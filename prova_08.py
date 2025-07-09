import os

diretorio_atual = os.getcwd()

itens = os.listdir(diretorio_atual)

print("Conteúdo do diretório atual:")
for item in itens:
    print(item)