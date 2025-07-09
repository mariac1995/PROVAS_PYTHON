'''Crie uma função chamada lancar_dados que utilizará o módulo random para simular o lançamento de dois dados. 
Cada dado deve gerar um número aleatório entre 1 e 6. 
A função deve somar os resultados desses dois lançamentos e retornar o valor total.
type: ignore'''

import random

def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print(f"Dado 1: {dado1}, Dado 2: {dado2}")
    
    return dado1 + dado2


print("Lançando os dados...")
resultado = lancar_dados()      
print(f"O resultado do lançamento dos dados é: {resultado}")
print("A soma dos dados é:", resultado)

print("Fim do programa")