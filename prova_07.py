import random

def lancar_dado():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    return soma


soma_dados = lancar_dado()
print(f"Soma dos dados: {soma_dados}")
