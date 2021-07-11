import sys

def menu():
    print("Digite o valor da representação você deseja utilizar.")
    print("(1) Lista de adjacência")
    print("(2) Matriz de adjacência")
    
    while(True):
        escolha = int(input())
        
        if escolha == 1:
            return True
        elif escolha == 2:
            return False
        else:
            print("Essa escolha não é valida! Por favor digite um valor válido.")

# def ler_arquivo(caminho):

    
#     [[],[],[],[],[]]    


#     return grafo
    


if __name__ == "__main__":
    args = sys.argv
    
    representa_lista = menu()

