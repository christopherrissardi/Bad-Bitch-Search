import time
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

mensagem1 = "╔════════════════════════════════════════════════════════════════╗"
mensagem = "                    Bem-vindo ao meu programa!"
mensagem2 = "╚════════════════════════════════════════════════════════════════╝"

while True:
    limpar_tela()

    print("\033[1m" + mensagem1 + "\033[0m")
    print("\033[1m" + mensagem + "\033[0m")
    print("\033[1m" + mensagem2 + "\033[0m")

    time.sleep(0.5)

    limpar_tela()

    time.sleep(0.5)
