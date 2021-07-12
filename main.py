# Modulos da Biblioteca Padrao
import sys

# Modulos secundarios
from input_output import le_entrada, escreve_grafo

def menu():
    """ 
        Apresenta o menu de opcoes. O usuario pode escolher entre tres
        valores de 0 a 2. Sendo:

        (0) Terminar o programa

        (1) Lista de adjacência

        (2) Matriz de adjacência 

        :return: True se a representacao a utilizar eh lista, 
        False caso for matriz.
    """

    # Apresenta mensagem de escolha
    print("Digite o valor da representação você deseja utilizar.")
    print("(0) Terminar o programa")
    print("(1) Lista de adjacência")
    print("(2) Matriz de adjacência")
    
    # Roda enquanto não for um valor válido
    while(True):
        # Tratando caso em que a entrada seja um char
        try:
            escolha = int(input())
        except:
            escolha = ""
            print("Isso não é um número!")
            
        if escolha == 1:
            return True
        elif escolha == 2:
            return False
        elif escolha == 0:
            print("Programa finalizado")
            sys.exit()
        else:
            print("Essa escolha não é valida! Por favor digite um valor válido.")


if __name__ == "__main__":
    # Guarda em args os argumentos recebidos na 
    # linha de comando ao executar o programa
    args = sys.argv    
    representa_lista = menu()
    
    grafo = le_entrada(args[1], representa_lista)
    escreve_grafo(grafo)
    
    

